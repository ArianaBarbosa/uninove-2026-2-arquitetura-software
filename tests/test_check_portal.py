"""O check_portal precisa reprovar card habilitado apontando para arquivo
ausente e diretorio sem index.html, cada um pelo motivo certo."""
from helpers import FIXTURES, rodar_validador

FIXTURE_PORTAL = FIXTURES / "portal_quebrado"


def test_reprova_card_com_link_quebrado():
    codigo, saida = rodar_validador("check_portal.py", FIXTURE_PORTAL / "index.html")
    assert codigo != 0, "o portal com link quebrado passou"
    assert "aula07" in saida.lower(), f"a mensagem nao nomeia o card quebrado:\n{saida}"


def test_reprova_diretorio_sem_index():
    """O GitHub Pages devolve 404 para diretorio sem index.html."""
    codigo, saida = rodar_validador("check_portal.py", FIXTURE_PORTAL / "index.html")
    assert codigo != 0
    assert "404" in saida or "index.html" in saida
