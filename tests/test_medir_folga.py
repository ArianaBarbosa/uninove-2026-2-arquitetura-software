"""Fumaça de tools/medir_folga.py.

`medir_folga.py` não é um validador (não reprova nada, sempre sai com 0):
é a ferramenta que substitui os scripts de medição que cada implementador
vinha escrevendo por conta própria, inflando a folga real em cerca de 60px
por não descontar o `padding-bottom` da section (ver docstring do próprio
script e a seção 4 do `task-20-report.md`).

Os dois testes de valor seguem o mesmo par de fixtures que
`test_validadores_de_navegador.py` usa para `check_slides.py`: `deck_ok.html`
prova que o número bate com o valor esperado num deck conhecido,
`deck_estoura_altura.html` prova que um slide que estoura os 720px vira
folga **negativa**, não um valor positivo qualquer.
"""
import re

from helpers import FIXTURES_DECKS, rodar_validador


def _folga_do_slide(saida, indice):
    """Extrai o valor de folga (em px) impresso para o slide de índice dado."""
    padrao = re.compile(r"slide %d(?!\d)\s+.*folga:\s*(-?\d+)px" % indice)
    encontrado = padrao.search(saida)
    assert encontrado, f"o slide {indice} não apareceu na saída:\n{saida}"
    return int(encontrado.group(1))


def test_medir_folga_bate_com_valor_conhecido_do_deck_ok():
    codigo, saida = rodar_validador("medir_folga.py", FIXTURES_DECKS / "deck_ok.html")
    assert codigo == 0, f"ferramenta de medição não deve reprovar nada:\n{saida}"
    # Slide 2 é "99 Conceito", um content-slide simples: título e um
    # parágrafo curto, sem quiz e sem estouro. 527px é o valor medido para
    # esta fixture com a geometria do check_slides.py (720 menos os 60px de
    # padding-bottom, menos o texto).
    assert _folga_do_slide(saida, 2) == 527


def test_medir_folga_devolve_folga_negativa_no_deck_que_estoura():
    codigo, saida = rodar_validador(
        "medir_folga.py", FIXTURES_DECKS / "deck_estoura_altura.html"
    )
    assert codigo == 0, (
        f"ferramenta de medição não deve reprovar nada, nem quando um slide estoura:\n{saida}"
    )
    # Slide 4 é "99 Texto demais", a fixture com 60 parágrafos de
    # preenchimento que estoura de propósito os 720px fixos.
    assert _folga_do_slide(saida, 4) < 0


def test_medir_folga_aceita_varios_decks_num_unico_comando():
    codigo, saida = rodar_validador(
        "medir_folga.py",
        FIXTURES_DECKS / "deck_ok.html",
        FIXTURES_DECKS / "deck_estoura_altura.html",
    )
    assert codigo == 0
    assert "deck_ok.html" in saida
    assert "deck_estoura_altura.html" in saida


def test_medir_folga_aceita_a_opcao_de_quiz_respondido_sem_reprovar():
    codigo, saida = rodar_validador(
        "medir_folga.py", "--quiz-respondido", FIXTURES_DECKS / "deck_ok.html"
    )
    assert codigo == 0, f"a opção --quiz-respondido não deve mudar o exit code:\n{saida}"
    assert "quiz respondido" in saida.lower()
