"""O check_portal precisa reprovar card habilitado apontando para arquivo
ausente e diretorio sem index.html, cada um pelo motivo certo, e precisa
aprovar os dois estados legitimos de um portal: nenhum card habilitado
ainda (inicio de producao) e pelo menos um card habilitado com link que
resolve de verdade (caminho feliz completo)."""
from helpers import FIXTURES, rodar_validador

FIXTURE_PORTAL = FIXTURES / "portal_quebrado"
FIXTURE_TODOS_DESABILITADOS = FIXTURES / "portal_todos_desabilitados"
FIXTURE_VALIDO = FIXTURES / "portal_valido"


def test_reprova_card_com_link_quebrado():
    codigo, saida = rodar_validador("check_portal.py", FIXTURE_PORTAL / "index.html")
    assert codigo != 0, "o portal com link quebrado passou"
    assert "aula07" in saida.lower(), f"a mensagem nao nomeia o card quebrado:\n{saida}"


def test_reprova_diretorio_sem_index():
    """O GitHub Pages devolve 404 para diretorio sem index.html."""
    codigo, saida = rodar_validador("check_portal.py", FIXTURE_PORTAL / "index.html")
    assert codigo != 0
    assert "404" in saida or "index.html" in saida


def test_aprova_portal_com_todos_os_cards_desabilitados():
    """Nenhum botao habilitado e o estado legitimo do dia da publicacao do
    portal: os 20 cards existem e nenhuma aula foi produzida ainda
    (SKILL.md, secao 9). Nao e erro, e nada para conferir."""
    codigo, saida = rodar_validador(
        "check_portal.py", FIXTURE_TODOS_DESABILITADOS / "index.html"
    )
    assert codigo == 0, f"portal legitimo, sem nenhum card habilitado, foi reprovado:\n{saida}"


def test_aprova_portal_valido_com_card_habilitado():
    """Caminho feliz completo: card habilitado, arquivo de slide que existe
    e diretorio de lab com index.html dentro."""
    codigo, saida = rodar_validador("check_portal.py", FIXTURE_VALIDO / "index.html")
    assert codigo == 0, f"portal valido foi reprovado:\n{saida}"
