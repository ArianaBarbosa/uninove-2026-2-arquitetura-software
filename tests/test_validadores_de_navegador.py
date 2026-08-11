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
import pytest

from helpers import FIXTURES_DECKS, rodar_validador


def test_check_slides_aprova_deck_valido():
    codigo, saida = rodar_validador("check_slides.py", FIXTURES_DECKS / "deck_ok.html")
    assert codigo == 0, f"o deck válido foi reprovado:\n{saida}"


def test_check_slides_reprova_deck_que_estoura():
    codigo, saida = rodar_validador(
        "check_slides.py", FIXTURES_DECKS / "deck_estoura_altura.html"
    )
    assert codigo != 0, "o deck que estoura 720px passou"
    assert "720" in saida or "altura" in saida.lower()


def test_check_canto_coral_aprova_deck_valido():
    codigo, saida = rodar_validador(
        "check_canto_coral.py", FIXTURES_DECKS / "deck_ok.html"
    )
    assert codigo == 0, f"o deck válido foi reprovado:\n{saida}"
