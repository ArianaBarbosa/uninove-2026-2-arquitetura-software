#!/usr/bin/env python3
"""
Mede a folga de altura de cada slide dos decks Reveal.js.

Folga é a distância entre o elemento mais baixo do slide (excluídos rodapé,
`top-bar` e logo, o mesmo critério do `check_slides.py`) e o limite inferior
da área útil da section, que é 720px **menos o `padding-bottom` de 60px**
que `.reveal .slides section` define no tema
(`aulas-1sem/assets/css/uninove-theme.css`).

Esta ferramenta existe porque scripts de medição escritos por conta própria,
sem descontar esse padding, vinham inflando a folga real em cerca de 60px.
Foi o que aconteceu no relatório da Aula 07: o slide de quiz depois do
clique na alternativa correta foi registrado com 84px de folga quando o
valor real é 24px (`task-20-report.md`, seção 4). A revisão validou o
método certo contra o precedente documentado no `task-13-report.md`: o
slide de metodologia da Aula 01 só bate com os 57px lá registrados quando o
padding é subtraído.

A geometria usada aqui é literalmente a do `check_slides.py`: mesmo
`JS_MEDIR`, mesmo cálculo de `padBottom`, mesma exclusão de
rodapé/barra/logo. Este script não recalcula nada por conta própria; só lê
o campo `folgaAltura` que o `JS_MEDIR` já devolve para cada slide.

Diferente do `check_slides.py`, esta não é uma ferramenta de validação: ela
mede e imprime, sem reprovar nada e sem exit code de erro. Quem decide o que
fazer com o número é quem lê o relatório.

Uso:
    python3 tools/medir_folga.py                        # todos os decks
    python3 tools/medir_folga.py aulas-1sem/aulas/aula07.html
    python3 tools/medir_folga.py --quiz-respondido aulas-1sem/aulas/aula07.html

A opção `--quiz-respondido` clica na alternativa `data-correct="true"` de
cada slide de quiz antes de medir, revelando o `.quiz-feedback` que fica
`display:none` até o clique. Sem a opção, o quiz é medido no estado inicial,
como o `check_slides.py` mede. Esse é exatamente o ponto cego registrado na
ADR-007: o feedback consome espaço que só aparece depois do clique, e o
`check_slides.py` nunca dispara esse clique sozinho.

Requer: pip install playwright && python3 -m playwright install chromium
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from check_slides import (  # noqa: E402
    ALTURA,
    JS_MEDIR,
    LARGURA,
    RAIZ,
    porta_livre,
    servir,
)
from playwright.sync_api import sync_playwright  # noqa: E402


def medir(page, url, nome, quiz_respondido):
    """Mede um deck e imprime a folga de cada slide; devolve a lista medida."""
    page.goto(url, wait_until="networkidle")
    page.wait_for_timeout(900)
    slides = page.evaluate(JS_MEDIR, quiz_respondido)

    sufixo = " (quiz respondido, feedback visível)" if quiz_respondido else ""
    print("\n%s%s  (%d slides)" % (nome, sufixo, len(slides)))
    for s in slides:
        tema = s["tema"] or "(sem footer-bar)"
        print("  slide %-2d  %-48s  folga: %4dpx" % (s["indice"], tema, s["folgaAltura"]))

    return slides


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    quiz_respondido = "--quiz-respondido" in sys.argv

    if args:
        decks = args
    else:
        pasta = os.path.join(RAIZ, "aulas-1sem", "aulas")
        if os.path.isdir(pasta):
            decks = [
                os.path.join("aulas-1sem", "aulas", f)
                for f in sorted(os.listdir(pasta))
                if f.endswith(".html")
            ]
        else:
            decks = []

    if not decks:
        print("Nenhum deck encontrado em %s" % os.path.relpath(
            os.path.join(RAIZ, "aulas-1sem", "aulas"), RAIZ
        ))
        return 0

    porta = porta_livre()
    httpd = servir(porta)

    try:
        with sync_playwright() as p:
            navegador = p.chromium.launch()
            page = navegador.new_page(viewport={"width": LARGURA, "height": ALTURA})
            for deck in decks:
                # Aceita caminho absoluto ou relativo: o servidor serve a partir da RAIZ
                rel = os.path.relpath(os.path.abspath(deck), RAIZ).replace(os.sep, "/")
                url = "http://127.0.0.1:%d/%s" % (porta, rel)
                medir(page, url, os.path.basename(deck), quiz_respondido)
            navegador.close()
    finally:
        httpd.shutdown()

    print()
    # Ferramenta de medição, não validador: nunca reprova nada.
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
