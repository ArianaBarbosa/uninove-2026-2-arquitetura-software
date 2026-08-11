"""Helpers compartilhados pelos testes dos validadores."""
import pathlib
import subprocess
import sys

RAIZ = pathlib.Path(__file__).resolve().parents[1]
FIXTURES = pathlib.Path(__file__).resolve().parent / "fixtures"
FIXTURES_DECKS = FIXTURES / "decks"


def rodar_validador(script, *argumentos):
    """Roda um validador e devolve (exit_code, saída_combinada)."""
    processo = subprocess.run(
        [sys.executable, str(RAIZ / "tools" / script), *map(str, argumentos)],
        capture_output=True,
        text=True,
    )
    return processo.returncode, processo.stdout + processo.stderr
