"""Cada regra do check_decks.py precisa reprovar a sua fixture, pelo motivo certo."""
import pytest

CASOS_QUE_DEVEM_REPROVAR = [
    ("deck_sem_decor_coral.html", "decor-coral"),
    ("deck_quiz_sem_content_slide.html", "content-slide"),
    ("deck_quiz_duas_corretas.html", "correct"),
    ("deck_quiz_sem_correta.html", "correct"),
    ("deck_footer_fora_de_sequencia.html", "footer-page"),
    ("deck_ancora_orfa.html", "ref-slide"),
    ("deck_caminho_quebrado.html", "inexistente.png"),
    ("deck_com_data_manual.html", "data"),
    ("deck_alternativa_inline_solto.html", "option-text"),
]


def test_deck_valido_e_aprovado(checar_deck):
    codigo, saida = checar_deck("deck_ok.html")
    assert codigo == 0, f"o deck valido foi reprovado:\n{saida}"


@pytest.mark.parametrize("fixture,trecho_esperado", CASOS_QUE_DEVEM_REPROVAR)
def test_fixture_quebrada_e_reprovada(checar_deck, fixture, trecho_esperado):
    codigo, saida = checar_deck(fixture)
    assert codigo != 0, f"{fixture} passou, mas deveria ser reprovada"
    assert trecho_esperado.lower() in saida.lower(), (
        f"{fixture} foi reprovada, mas a mensagem não cita {trecho_esperado!r}.\n"
        f"Saída:\n{saida}"
    )


@pytest.mark.parametrize("fixture,_", CASOS_QUE_DEVEM_REPROVAR)
def test_mensagem_de_erro_cita_a_linha(checar_deck, fixture, _):
    codigo, saida = checar_deck(fixture)
    assert codigo != 0
    assert "linha" in saida.lower(), (
        f"{fixture}: a mensagem precisa nomear a linha do defeito.\nSaída:\n{saida}"
    )
