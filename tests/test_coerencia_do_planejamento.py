"""Os 20 titulos precisam ser identicos nos lugares onde aparecem.

O plano de ensino (Task 3) e o planejamento aula a aula (Task 4) ja existem
neste ponto do acervo e sao comparados de verdade, sem pular. O portal
(aulas-1sem/index.html) e a Task 12 e ainda nao existe: os testes que
dependem dele pulam ate la, com motivo explicito, para nao deixar a suite
vermelha por um artefato que ainda nao foi produzido. Assim que o portal
aparecer, esses testes passam a valer sozinhos, sem precisar editar nada
aqui.
"""
import re

import pytest

from helpers import RAIZ

PLANO = RAIZ / "PLANO_DE_ENSINO.md"
PLANEJAMENTO = RAIZ / "PLANEJAMENTO_AULA_A_AULA.md"
PORTAL = RAIZ / "aulas-1sem" / "index.html"

MOTIVO_DO_SKIP = (
    "aulas-1sem/index.html ainda nao existe: o portal e a Task 12 do plano "
    "de execucao. Este teste passa a valer sozinho assim que o arquivo "
    "aparecer, sem edicao nenhuma neste arquivo."
)


def titulos_do_plano():
    linhas = PLANO.read_text(encoding="utf-8").splitlines()
    achados = {}
    for linha in linhas:
        m = re.match(r"^\|\s*(\d{2})\s*\|[^|]*\|\s*([^|]+?)\s*\|", linha)
        if m:
            achados[m.group(1)] = m.group(2).strip()
    return achados


def titulos_do_planejamento():
    texto = PLANEJAMENTO.read_text(encoding="utf-8")
    return {m.group(1): m.group(2).strip()
            for m in re.finditer(r"^## Aula (\d{2}), (.+)$", texto, re.MULTILINE)}


def titulos_do_portal():
    texto = PORTAL.read_text(encoding="utf-8")
    numeros = re.findall(r'<span class="card-numero">Aula (\d{2})</span>', texto)
    titulos = re.findall(r'<h3 class="card-titulo">(.+?)</h3>', texto)
    assert len(numeros) == len(titulos), "cada card precisa ter numero e titulo"
    return dict(zip(numeros, [t.strip() for t in titulos]))


# -- comparacoes que rodam ja, entre plano de ensino e planejamento ---------

def test_plano_tem_vinte_aulas():
    assert len(titulos_do_plano()) == 20


def test_planejamento_tem_vinte_aulas():
    assert len(titulos_do_planejamento()) == 20


def test_titulos_batem_entre_plano_e_planejamento():
    plano, planejamento = titulos_do_plano(), titulos_do_planejamento()
    divergentes = [
        (n, plano[n], planejamento.get(n))
        for n in sorted(plano)
        if plano[n] != planejamento.get(n)
    ]
    assert not divergentes, (
        "titulos divergentes (aula, plano, planejamento):\n"
        + "\n".join(map(str, divergentes))
    )


# -- comparacoes que dependem do portal, Task 12 -----------------------------

def test_portal_tem_vinte_aulas():
    if not PORTAL.is_file():
        pytest.skip(MOTIVO_DO_SKIP)
    assert len(titulos_do_portal()) == 20


def test_titulos_batem_entre_os_tres():
    if not PORTAL.is_file():
        pytest.skip(MOTIVO_DO_SKIP)
    plano, planejamento, portal = (
        titulos_do_plano(), titulos_do_planejamento(), titulos_do_portal()
    )
    divergentes = [
        (n, plano[n], planejamento.get(n), portal.get(n))
        for n in sorted(plano)
        if not (plano[n] == planejamento.get(n) == portal.get(n))
    ]
    assert not divergentes, (
        "titulos divergentes (aula, plano, planejamento, portal):\n"
        + "\n".join(map(str, divergentes))
    )
