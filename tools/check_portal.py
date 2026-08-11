#!/usr/bin/env python3
"""
Valida o portal da disciplina, aulas-1sem/index.html.

Duas checagens, na ordem em que o aluno realmente encontra o portal:

1. Existem exatamente 20 cards, um por aula.
2. Todo href de botão habilitado ("Slides" ou "Lab") responde HTTP 200 numa
   requisição real. Botão desabilitado (classe "disabled") é ignorado, porque
   a aula ainda não foi produzida. O servidor deste validador não faz
   listagem de diretório, de propósito: é assim que o GitHub Pages se
   comporta, e listagem de diretório mascarava link quebrado (diretório sem
   index.html "funcionava" aqui e dava 404 lá).

Esta disciplina tem um único horário (ver PLANO_DE_ENSINO.md, seção 1) e
nenhuma resolução de calendário no portal: sem seletor, sem modal de escolha
e sem leitura de estado salvo no navegador. As checagens correspondentes do
acervo de Desenvolvimento Web, de onde este validador nasceu, não se
aplicam aqui e foram removidas.

Sai com código 1 e imprime o que falhou se qualquer checagem não passar.

Uso:
    python3 tools/check_portal.py                      # confere aulas-1sem/index.html
    python3 tools/check_portal.py caminho/para/index.html   # confere o portal indicado

Sem argumento, confere `aulas-1sem/index.html`, servindo a partir da raiz do
repositório. Com um caminho, confere o portal indicado, servindo a partir do
diretório que o contém, o que torna o validador testável contra fixture.

Requer: pip install playwright && python3 -m playwright install chromium
"""
import http.server
import os
import socket
import socketserver
import sys
import threading
import urllib.parse

from playwright.sync_api import sync_playwright

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PORTAL_PADRAO = os.path.join(RAIZ, "aulas-1sem", "index.html")


def porta_livre():
    s = socket.socket()
    s.bind(("127.0.0.1", 0))
    p = s.getsockname()[1]
    s.close()
    return p


class SemListagemHandler(http.server.SimpleHTTPRequestHandler):
    """SimpleHTTPRequestHandler comum serve a listagem de arquivos quando o
    caminho é um diretório sem index.html dentro. O GitHub Pages não faz
    isso: devolve 404. Sem essa diferença, um botão "Lab" apontando para um
    diretório que só tem README.md pareceria funcionar aqui e quebraria em
    produção."""

    def list_directory(self, path):
        self.send_error(404, "File not found")
        return None


def servir(porta, diretorio):
    handler = lambda *a, **k: SemListagemHandler(  # noqa: E731
        *a, directory=diretorio, **k
    )
    socketserver.TCPServer.allow_reuse_address = True
    httpd = socketserver.TCPServer(("127.0.0.1", porta), handler)
    threading.Thread(target=httpd.serve_forever, daemon=True).start()
    return httpd


def abrir_pagina(navegador, porta, nome_do_arquivo):
    """Cria um contexto isolado e navega até o portal servido pelo diretório
    passado a `servir`."""
    contexto = navegador.new_context()
    page = contexto.new_page()
    page.goto(
        "http://127.0.0.1:%d/%s" % (porta, nome_do_arquivo), wait_until="networkidle"
    )
    page.wait_for_timeout(300)
    return contexto, page


def checar_total_de_cards(navegador, porta, nome_do_arquivo, erros):
    contexto, page = abrir_pagina(navegador, porta, nome_do_arquivo)
    try:
        total = page.eval_on_selector_all("[data-aula]", "els => els.length")
        if total != 20:
            erros.append("checagem 1: existem %d cards com data-aula, esperado 20" % total)

        container = page.query_selector("[data-total-cards]")
        if container is None:
            erros.append("checagem 1: nenhum elemento com o atributo data-total-cards")
        else:
            declarado = container.get_attribute("data-total-cards")
            if declarado != "20":
                erros.append(
                    "checagem 1: data-total-cards vale %r, esperado '20'" % declarado
                )
    finally:
        contexto.close()


def checar_links_dos_botoes_habilitados(navegador, porta, nome_do_arquivo, erros):
    contexto, page = abrir_pagina(navegador, porta, nome_do_arquivo)
    try:
        botoes = page.eval_on_selector_all(
            "a.btn:not(.disabled)",
            "els => els.map(el => ({ href: el.getAttribute('href'), texto: el.textContent.trim() }))",
        )
        # Nenhum botão habilitado é o estado legítimo de um acervo em
        # produção: o portal nasce com os 20 cards desabilitados e cada um
        # é habilitado conforme a aula fica pronta (SKILL.md, seção 9).
        # Ausência de link para conferir não é erro, é nada para conferir;
        # só informamos a contagem, sem afetar o código de saída.
        print("checagem 2: %d botão(ões) habilitado(s) encontrado(s) no portal" % len(botoes))

        for botao in botoes:
            href = botao["href"]
            if not href:
                erros.append(
                    "checagem 2: botão habilitado '%s' não tem href" % botao["texto"]
                )
                continue
            url = urllib.parse.urljoin(page.url, href)
            resposta = contexto.request.get(url)
            if resposta.status != 200:
                erros.append(
                    "checagem 2: GET %s (botão '%s') devolveu %d, esperado 200"
                    % (url, botao["texto"], resposta.status)
                )
    finally:
        contexto.close()


def main():
    argumentos = [a for a in sys.argv[1:] if not a.startswith("--")]
    caminho_portal = os.path.abspath(argumentos[0]) if argumentos else PORTAL_PADRAO

    if not os.path.isfile(caminho_portal):
        print("Portal não encontrado: %s" % caminho_portal)
        return 1

    diretorio_base = os.path.dirname(caminho_portal)
    nome_do_arquivo = os.path.basename(caminho_portal)

    porta = porta_livre()
    httpd = servir(porta, diretorio_base)
    erros = []

    try:
        with sync_playwright() as p:
            navegador = p.chromium.launch()
            try:
                checar_total_de_cards(navegador, porta, nome_do_arquivo, erros)
                checar_links_dos_botoes_habilitados(navegador, porta, nome_do_arquivo, erros)
            finally:
                navegador.close()
    finally:
        httpd.shutdown()

    print("=" * 62)
    if erros:
        print("%d checagem(ns) falhou(aram):\n" % len(erros))
        for erro in erros:
            print("  - %s" % erro)
        return 1

    print("Todas as checagens do portal passaram.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
