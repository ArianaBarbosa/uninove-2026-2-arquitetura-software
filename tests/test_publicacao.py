"""O workflow de publicação não pode vazar fonte de trabalho para o site."""
import pathlib

RAIZ = pathlib.Path(__file__).resolve().parents[1]
WORKFLOW = RAIZ / ".github" / "workflows" / "static.yml"

# Precisa ser a lista completa do Step 7. Uma exclusão que está no workflow mas
# não está aqui pode ser removida do workflow sem o teste reclamar, e material
# de trabalho vaza para o site publicado.
EXCLUSOES_OBRIGATORIAS = [
    ".git", ".github", ".claude", "tools", "tests", "docs", "pdf",
    "node_modules", ".superpowers", "shots", "CLAUDE.md", "_site",
]


def test_workflow_existe():
    assert WORKFLOW.is_file(), "static.yml não existe"


def test_todas_as_exclusoes_estao_no_rsync():
    texto = WORKFLOW.read_text(encoding="utf-8")
    faltando = [e for e in EXCLUSOES_OBRIGATORIAS
                if f"--exclude={e}" not in texto and f"--exclude='{e}'" not in texto]
    assert not faltando, f"exclusões ausentes no rsync: {faltando}"


def test_existe_passo_anti_symlink():
    texto = WORKFLOW.read_text(encoding="utf-8")
    assert "find _site -type l" in texto, (
        "falta o passo que falha o build quando sobra symlink no _site"
    )
