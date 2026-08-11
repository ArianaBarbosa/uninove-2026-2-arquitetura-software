"""Fumaça dos dois validadores que dependem de navegador.

`check_slides.py` e `check_canto_coral.py` medem geometria e pixel no
navegador headless: nenhuma checagem estática do `check_decks.py` enxerga
conteúdo que estoura os 720px fixos da `section` do tema, porque estourar
não muda o `scrollHeight`, não lança erro no console e não aparece em
nenhuma inspeção de HTML. Só a medição real no navegador pega isso. Por
dependerem de Playwright e de um navegador Chromium instalado, estes dois
validadores não entram na suíte de fixtures estáticas da Task 8; aqui o
teste é apenas de fumaça, garantindo que o script roda no ambiente, aprova
um deck válido e reprova um deck que estoura.
"""
import re

import pytest

from helpers import FIXTURES_DECKS, rodar_validador

# Casa com a mensagem real de estouro do check_slides.py, por exemplo
# "ESTOURO: 5407px abaixo do limite". Casar com o nome do arquivo da fixture
# faria a asserção passar mesmo que o validador reprovasse por outro motivo
# qualquer; ver o comentário equivalente em tests/test_check_decks.py.
PADRAO_MENSAGEM_DE_ESTOURO = re.compile(r"ESTOURO: \d+px")


def test_check_slides_aprova_deck_valido():
    codigo, saida = rodar_validador("check_slides.py", FIXTURES_DECKS / "deck_ok.html")
    assert codigo == 0, f"o deck válido foi reprovado:\n{saida}"


def test_check_slides_reprova_deck_que_estoura():
    codigo, saida = rodar_validador(
        "check_slides.py", FIXTURES_DECKS / "deck_estoura_altura.html"
    )
    assert codigo != 0, "o deck que estoura 720px passou"
    assert PADRAO_MENSAGEM_DE_ESTOURO.search(saida), (
        f"a saída não contém uma mensagem de ESTOURO em pixels:\n{saida}"
    )


def test_check_canto_coral_aprova_deck_valido():
    codigo, saida = rodar_validador(
        "check_canto_coral.py", FIXTURES_DECKS / "deck_ok.html"
    )
    assert codigo == 0, f"o deck válido foi reprovado:\n{saida}"
