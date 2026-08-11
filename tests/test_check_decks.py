"""Cada regra do check_decks.py precisa reprovar a sua fixture, pelo motivo certo."""
import re

import pytest

# (fixture, trecho_esperado, linha_esperada, contagem_esperada)
#
# linha_esperada é a linha exata que a mensagem de erro deve citar, não só a
# palavra "linha" solta em algum lugar da saída: um validador que imprimisse
# "linha" fora de contexto passaria numa checagem frouxa.
#
# contagem_esperada é o número de trechos "linha N" na saída inteira, ou
# seja, quantas mensagens de erro a fixture produz. Quase sempre 1: uma
# fixture com dois defeitos não prova qual regra disparou. A exceção
# documentada é deck_footer_fora_de_sequencia.html, que produz DUAS
# mensagens a partir de um ÚNICO defeito (trocar um footer-page só): a
# checagem de sequência compara pares adjacentes, então a troca cria uma
# "pula" no par (slide alterado, slide anterior) e um "retrocede" no par
# seguinte (próximo slide, slide alterado). Não é um segundo defeito nem uma
# segunda regra; linha_esperada aponta para o slide onde o defeito foi de
# fato introduzido.
CASOS_QUE_DEVEM_REPROVAR = [
    ("deck_sem_decor_coral.html", "decor-coral", 27, 1),
    ("deck_quiz_sem_content_slide.html", "content-slide", 41, 1),
    ("deck_quiz_duas_corretas.html", "correct", 48, 1),
    ("deck_quiz_sem_correta.html", "correct", 48, 1),
    ("deck_footer_fora_de_sequencia.html", "footer-page", 60, 2),
    ("deck_ancora_orfa.html", "ref-slide", 32, 1),
    ("deck_caminho_quebrado.html", "inexistente.png", 12, 1),
    ("deck_com_data_manual.html", "data", 22, 1),
    ("deck_alternativa_inline_solto.html", "option-text", 54, 1),
    ("deck_com_atributo_data_da_aula.html", "data-data-da-aula", 23, 1),
    ("deck_com_referencia_a_turmas_js.html", "turmas.js", 80, 1),
]


def test_deck_valido_e_aprovado(checar_deck):
    codigo, saida = checar_deck("deck_ok.html")
    assert codigo == 0, f"o deck válido foi reprovado:\n{saida}"


@pytest.mark.parametrize(
    "fixture,trecho_esperado,linha_esperada,contagem_esperada", CASOS_QUE_DEVEM_REPROVAR
)
def test_fixture_quebrada_e_reprovada(
    checar_deck, fixture, trecho_esperado, linha_esperada, contagem_esperada
):
    codigo, saida = checar_deck(fixture)
    assert codigo != 0, f"{fixture} passou, mas deveria ser reprovada"
    assert trecho_esperado.lower() in saida.lower(), (
        f"{fixture} foi reprovada, mas a mensagem não cita {trecho_esperado!r}.\n"
        f"Saída:\n{saida}"
    )


@pytest.mark.parametrize(
    "fixture,trecho_esperado,linha_esperada,contagem_esperada", CASOS_QUE_DEVEM_REPROVAR
)
def test_mensagem_de_erro_cita_a_linha_esperada(
    checar_deck, fixture, trecho_esperado, linha_esperada, contagem_esperada
):
    codigo, saida = checar_deck(fixture)
    assert codigo != 0
    padrao = rf"linha {linha_esperada}\b"
    assert re.search(padrao, saida), (
        f"{fixture}: a mensagem não cita a linha {linha_esperada}.\nSaída:\n{saida}"
    )


@pytest.mark.parametrize(
    "fixture,trecho_esperado,linha_esperada,contagem_esperada", CASOS_QUE_DEVEM_REPROVAR
)
def test_apenas_a_regra_esperada_dispara(
    checar_deck, fixture, trecho_esperado, linha_esperada, contagem_esperada
):
    """Trava a contagem de mensagens: uma fixture com defeito extra, mesmo que
    ainda cite o trecho e a linha certos, precisa ser corrigida, não o teste.
    A exceção de deck_footer_fora_de_sequencia.html está documentada na
    tabela acima, junto de contagem_esperada.
    """
    codigo, saida = checar_deck(fixture)
    assert codigo != 0
    contagem = len(re.findall(r"linha \d+", saida))
    assert contagem == contagem_esperada, (
        f"{fixture}: esperava {contagem_esperada} mensagem(ns) citando linha, "
        f"encontrei {contagem}.\nSaída:\n{saida}"
    )
