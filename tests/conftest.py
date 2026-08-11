"""Fixtures do pytest. A lógica de execução vive em helpers.py."""
import pathlib
import sys

import pytest

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))

from helpers import FIXTURES_DECKS, rodar_validador  # noqa: E402


@pytest.fixture
def checar_deck():
    def _checar(nome_da_fixture):
        return rodar_validador("check_decks.py", FIXTURES_DECKS / nome_da_fixture)
    return _checar
