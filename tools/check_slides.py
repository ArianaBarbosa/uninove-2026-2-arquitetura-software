#!/usr/bin/env python3
"""
Valida os decks Reveal.js procurando conteúdo que estoura o slide.

Três checagens, porque são três defeitos diferentes:

1. ESTOURO. O tema fixa cada <section> em 1280x720. Qualquer elemento que
   ultrapasse essa caixa aparece cortado na projeção. Medir `scrollHeight` da
   section NÃO detecta isso de forma confiável, então percorremos os
   descendentes e comparamos o retângulo de cada um com a área útil do slide
   (já descontado o padding).

2. SOBREPOSIÇÃO. Um bloco posicionado em absoluto cabe dentro dos 720px e ainda
   assim cobre o bloco de cima, deixando texto ilegível. Isso passa inteiro pela
   checagem de estouro. Aqui comparamos os filhos diretos da section entre si:
   como o layout deles é empilhado, qualquer interseção real é defeito.

3. TÍTULO NO LOGO. O logo da Uninove fica fora da checagem 2 de propósito, senão
   todo slide daria falso positivo. O efeito colateral era um ponto cego: um
   título longo quebra a segunda linha por baixo do logo sem estourar os 720px
   e sem sobrepor filho direto da section. Apareceu nas Aulas 10 e 11 em
   31/07/2026, e só foi visto porque alguém abriu o slide no navegador.
   Comparamos as caixas de LINHA do título (não a caixa do h2, que costuma ser
   larga e vazia à direita) com o retângulo do logo.

Uso:
    python3 tools/check_slides.py                      # todos os decks
    python3 tools/check_slides.py aulas-1sem/aulas/aula01.html
    python3 tools/check_slides.py --shots out/         # salva PNG dos slides com problema

Requer: pip install playwright && python3 -m playwright install chromium
"""
import http.server
import os
import socket
import socketserver
import sys
import threading

from playwright.sync_api import sync_playwright

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LARGURA, ALTURA = 1280, 720
TOLERANCIA = 2  # px, para arredondamento de layout


def porta_livre():
    s = socket.socket()
    s.bind(("127.0.0.1", 0))
    p = s.getsockname()[1]
    s.close()
    return p


def servir(porta):
    handler = lambda *a, **k: http.server.SimpleHTTPRequestHandler(  # noqa: E731
        *a, directory=RAIZ, **k
    )
    socketserver.TCPServer.allow_reuse_address = True
    httpd = socketserver.TCPServer(("127.0.0.1", porta), handler)
    threading.Thread(target=httpd.serve_forever, daemon=True).start()
    return httpd


# Executado no navegador: mede cada slide e devolve os elementos que vazam.
#
# O parâmetro `clicarQuiz` não é usado por este script (checar() sempre chama
# `page.evaluate(JS_MEDIR)`, sem argumento, e o padrão `false` preserva o
# comportamento de sempre). Ele existe para que `tools/medir_folga.py`
# reaproveite esta mesma função em vez de reescrever a geometria: com
# `clicarQuiz = true`, cada slide de quiz é respondido (clique na alternativa
# `data-correct="true"`) antes da medição, revelando o `.quiz-feedback` que
# fica `display:none` até o clique (ADR-007).
JS_MEDIR = """
(clicarQuiz = false) => {
  const secoes = [...document.querySelectorAll('.reveal .slides > section')];
  return secoes.map((sec, i) => {
    // Torna o slide mensurável mesmo sem estar ativo
    const estiloAnterior = sec.getAttribute('style') || '';
    sec.style.display = 'block';
    sec.style.visibility = 'visible';
    sec.style.opacity = '1';

    if (clicarQuiz && sec.classList.contains('quiz-slide')) {
      const correta = sec.querySelector('.quiz-options li[data-correct="true"]');
      if (correta) correta.click();
    }

    const cs = getComputedStyle(sec);
    const padTop = parseFloat(cs.paddingTop);
    const padBottom = parseFloat(cs.paddingBottom);
    const padLeft = parseFloat(cs.paddingLeft);
    const padRight = parseFloat(cs.paddingRight);

    const base = sec.getBoundingClientRect();
    const limiteBaixo = base.top + 720 - padBottom;
    const limiteDireita = base.left + 1280 - padRight;

    const vazamentos = [];
    // Elemento mais baixo do slide, com a mesma exclusão de rodapé/barra/logo
    // usada para achar vazamento: é o dado bruto de que a folga de altura
    // (limiteBaixo menos este valor) precisa, reaproveitado por
    // tools/medir_folga.py.
    let maxBottom = base.top;
    for (const el of sec.querySelectorAll('*')) {
      const ecs = getComputedStyle(el);
      if (ecs.display === 'none' || ecs.visibility === 'hidden') continue;
      // Rodapé e barras são posicionados de propósito na borda
      if (el.closest('.slide-footer, .top-bar, [class*="logo-header"]')) continue;
      const r = el.getBoundingClientRect();
      if (r.width === 0 && r.height === 0) continue;

      if (r.bottom > maxBottom) maxBottom = r.bottom;

      const excessoBaixo = r.bottom - limiteBaixo;
      const excessoDireita = r.right - limiteDireita;
      if (excessoBaixo > 2 || excessoDireita > 2) {
        vazamentos.push({
          tag: el.tagName.toLowerCase(),
          classe: (el.className && el.className.baseVal !== undefined
                    ? el.className.baseVal : el.className || '').toString().slice(0, 40),
          texto: (el.textContent || '').trim().replace(/\\s+/g, ' ').slice(0, 60),
          abaixo: Math.round(excessoBaixo),
          direita: Math.round(excessoDireita),
        });
      }
    }

    // --- Sobreposição entre os blocos empilhados do slide --------------
    // Só os filhos diretos: comparar descendentes daria falso positivo, já
    // que todo filho intersecta o próprio pai.
    const rotulo = (el) => {
      const c = (el.className && el.className.baseVal !== undefined
                  ? el.className.baseVal : el.className || '').toString().trim();
      return el.tagName.toLowerCase() + (c ? '.' + c.split(/\\s+/).join('.') : '');
    };

    const blocos = [...sec.children].filter((el) => {
      const ecs = getComputedStyle(el);
      if (ecs.display === 'none' || ecs.visibility === 'hidden') return false;
      // Decoração de borda: sobrepõe de propósito
      if (el.matches('.slide-footer, .top-bar, [class*="logo-header"]')) return false;
      const r = el.getBoundingClientRect();
      return r.width > 0 && r.height > 0;
    });

    const sobreposicoes = [];
    for (let a = 0; a < blocos.length; a++) {
      for (let b = a + 1; b < blocos.length; b++) {
        const ra = blocos[a].getBoundingClientRect();
        const rb = blocos[b].getBoundingClientRect();
        const vertical = Math.min(ra.bottom, rb.bottom) - Math.max(ra.top, rb.top);
        const horizontal = Math.min(ra.right, rb.right) - Math.max(ra.left, rb.left);
        if (vertical > 2 && horizontal > 2) {
          sobreposicoes.push({
            a: rotulo(blocos[a]),
            b: rotulo(blocos[b]),
            px: Math.round(vertical),
            texto: (blocos[b].textContent || '').trim().replace(/\\s+/g, ' ').slice(0, 60),
          });
        }
      }
    }

    // COLISÃO COM O LOGO. O logo fica de propósito fora da checagem acima, senão
    // todo slide daria falso positivo. O efeito colateral é um ponto cego: um
    // título longo quebra a segunda linha por baixo do logo sem estourar os
    // 720px e sem sobrepor filho direto da section. Aconteceu nas Aulas 10 e 11,
    // e só apareceu porque alguém olhou o slide no navegador.
    //
    // Medimos as caixas de LINHA do título, não a caixa do h2: o h2 costuma ser
    // largo e vazio à direita, então a caixa dele encosta no logo em todo slide.
    const MARGEM_LOGO = 15;
    const colisoes = [];
    const logo = sec.querySelector('[class*="logo-header"]');
    if (logo) {
      const rl = logo.getBoundingClientRect();
      if (rl.width > 0 && rl.height > 0) {
        for (const alvo of sec.querySelectorAll('h1, h2, h3')) {
          const faixa = document.createRange();
          faixa.selectNodeContents(alvo);
          for (const rt of faixa.getClientRects()) {
            if (rt.width < 1 || rt.height < 1) continue;
            const dx = Math.max(rl.left - rt.right, rt.left - rl.right);
            const dy = Math.max(rl.top - rt.bottom, rt.top - rl.bottom);
            // Só interessa quando as caixas se cruzam em uma das direções.
            if (dx >= MARGEM_LOGO || dy >= MARGEM_LOGO) continue;
            const folga = Math.round(Math.max(dx, dy));
            colisoes.push({
              alvo: rotulo(alvo),
              folga: folga,
              texto: (alvo.textContent || '').trim().replace(/\\s+/g, ' ').slice(0, 60),
            });
            break;
          }
        }
      }
    }

    sec.setAttribute('style', estiloAnterior);

    const titulo = sec.querySelector('h2');
    const footer = sec.querySelector('.footer-bar');
    return {
      indice: i,
      titulo: titulo ? titulo.textContent.trim().slice(0, 55) : '(' + sec.className + ')',
      tema: footer ? footer.textContent.trim() : null,
      // só o vazamento mais grave por slide, para o relatório não explodir
      pior: vazamentos.sort((a, b) =>
        (b.abaixo + b.direita) - (a.abaixo + a.direita))[0] || null,
      total: vazamentos.length,
      sobreposicoes: sobreposicoes.sort((x, y) => y.px - x.px).slice(0, 3),
      colisoes: colisoes.sort((x, y) => x.folga - y.folga).slice(0, 2),
      // Folga de altura: limiteBaixo já descontou o padding-bottom de 60px da
      // section (linha ~90). tools/medir_folga.py usa este campo em vez de
      // recalcular a geometria por conta própria.
      folgaAltura: Math.round(limiteBaixo - maxBottom),
    };
  });
}
"""


def checar(page, url, nome, shots_dir=None):
    page.goto(url, wait_until="networkidle")
    page.wait_for_timeout(900)
    slides = page.evaluate(JS_MEDIR)

    problemas = [s for s in slides
                 if s["pior"] or s.get("sobreposicoes") or s.get("colisoes")]
    print("\n%s  (%d slides)" % (nome, len(slides)))
    if not problemas:
        print("  OK: nada estourando 1280x720, sem bloco sobreposto nem título no logo")
        return 0

    for s in problemas:
        print("  slide %-2d  %-52s" % (s["indice"], s["titulo"]))

        p = s["pior"]
        if p:
            eixo = []
            if p["abaixo"] > TOLERANCIA:
                eixo.append("%dpx abaixo do limite" % p["abaixo"])
            if p["direita"] > TOLERANCIA:
                eixo.append("%dpx a direita" % p["direita"])
            print("           ESTOURO: %s  <%s class=%r>"
                  % (", ".join(eixo), p["tag"], p["classe"]))
            print("           texto: %s" % p["texto"])

        for sob in s.get("sobreposicoes", []):
            print("           SOBREPOSIÇÃO: %s cobre %s em %dpx"
                  % (sob["a"], sob["b"], sob["px"]))
            print("           texto coberto: %s" % sob["texto"])

        for col in s.get("colisoes", []):
            print("           TÍTULO NO LOGO: <%s> a %dpx do logo da Uninove"
                  % (col["alvo"], col["folga"]))
            print("           texto: %s" % col["texto"])

        if shots_dir:
            os.makedirs(shots_dir, exist_ok=True)
            page.evaluate("i => Reveal.slide(i, 0)", s["indice"])
            page.wait_for_timeout(500)
            destino = os.path.join(
                shots_dir, "%s-slide%02d.png" % (nome.replace(".html", ""), s["indice"])
            )
            page.screenshot(path=destino)
            print("           screenshot: %s" % destino)

    return len(problemas)


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    shots_dir = None
    if "--shots" in sys.argv:
        i = sys.argv.index("--shots")
        shots_dir = sys.argv[i + 1] if len(sys.argv) > i + 1 else "shots"

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
        return 1

    porta = porta_livre()
    httpd = servir(porta)
    total = 0

    try:
        with sync_playwright() as p:
            navegador = p.chromium.launch()
            page = navegador.new_page(viewport={"width": LARGURA, "height": ALTURA})
            for deck in decks:
                # Aceita caminho absoluto ou relativo: o servidor serve a partir da RAIZ
                rel = os.path.relpath(os.path.abspath(deck), RAIZ).replace(os.sep, "/")
                url = "http://127.0.0.1:%d/%s" % (porta, rel)
                total += checar(page, url, os.path.basename(deck), shots_dir)
            navegador.close()
    finally:
        httpd.shutdown()

    print("\n" + "=" * 62)
    if total:
        print("%d slide(s) com problema de layout, entre estouro e sobreposição." % total)
        return 1
    print("Todos os slides cabem em 1280x720, sem bloco sobreposto.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
