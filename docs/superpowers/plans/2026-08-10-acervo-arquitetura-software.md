# Acervo de Arquitetura de Software, plano de implementação

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Construir o acervo didático completo da disciplina Arquitetura de Software, Uninove 2026.2, com 20 decks Reveal.js, 20 kits de laboratório, portal, planejamento e validação automática, publicado no GitHub Pages.

**Architecture:** Site estático sem build e sem bundler. Reveal.js 5.1.0 vem do jsDelivr por CDN, o tema é CSS puro copiado do acervo de Desenvolvimento Web, e não há JavaScript de aplicação além do script de quiz. A qualidade dos decks é garantida por quatro validadores em Python, e os próprios validadores são cobertos por uma suíte pytest sobre decks-fixture propositalmente quebrados. Os validadores são construídos antes de qualquer deck existir.

**Tech Stack:** HTML5, CSS3, Reveal.js 5.1.0 por CDN, Python 3 com Playwright para os validadores de geometria, pytest, GitHub Actions e GitHub Pages.

**Spec:** `docs/superpowers/specs/2026-08-10-acervo-arquitetura-software-design.md`

---

## Global Constraints

Estas regras valem em toda tarefa deste plano. Elas não são repetidas em cada uma.

- **Idioma:** português do Brasil, com acentuação completa, em todo texto de slide, kit, documento e comentário de código.
- **Nunca usar o caractere travessão em dash (`—`)** em nenhum arquivo produzido por este plano. Usar vírgula, dois pontos ou reescrever a frase.
- **Sem emojis** em slides, títulos, textos, kits ou nomes de arquivo.
- **Sem tom exagerado.** Nada de frases de efeito, punchlines, metáforas amplificadoras ou títulos de slogan. Títulos descritivos do conteúdo, afirmações diretas.
- **Nenhuma data escrita à mão em nenhum deck.** Não há calendário nesta disciplina. Data em deck é reprovada pelo `check_decks.py`.
- **Não existe `assets/js/turmas.js`** neste acervo, nem seletor de turma no portal, nem atributo `data-data-da-aula` em deck nenhum.
- **Toda `section` de deck mede 1280x720 com altura travada.** Um conceito por slide. Conteúdo que não couber vira dois slides, nunca fonte menor.
- **Reveal.js versão `5.1.0`**, sempre pelo jsDelivr, nunca outra versão e nunca local.
- **Cores da marca:** `--uninove-azul: #00274D` e `--uninove-coral: #C84B31`. Não inventar cor nova.
- **Case:** Rota Sul, transportadora. Entidades `Cliente`, `Pedido`, `Remessa`, `Volume`, `Rota`, `Veiculo`, `Motorista`, `Ocorrencia`, `Parceiro`. Atores lojista, expedidor, motorista, atendente e transportadora parceira.
- **Stack do laboratório:** Java 21 LTS, Maven, Spring Boot 3.x, pacote raiz `br.uni9.rotasul`, Spring Data JPA sobre Hibernate, MySQL 8.4 schema `rotasul`, Flyway, Thymeleaf, springdoc-openapi, JUnit 5, Testcontainers.
- **Repositório-esqueleto do case:** `josercf/uninove-2026-2-rota-sul`. Este plano não o cria; apenas o referencia.
- **Pesos de avaliação aparecem nos slides.**
- **Commits em Conventional Commits com escopo pela aula:** `feat(aula03): ...`, `fix(portal): ...`, `test(validadores): ...`, `docs(plano): ...`.
- **Push:** o remote usa o host `github.com`, que autentica como `canaldoovidio`. Para publicar como `josercf`, usar sempre:
  ```bash
  GIT_SSH_COMMAND='ssh -i /Users/joseromualdocostafilho/.ssh/id_ed25519_josercf -o IdentitiesOnly=yes -F /dev/null' git push
  ```
- **Acervo de referência:** `/Users/joseromualdocostafilho/Projects/Uninove/2026/uninove-2026-2-desenvolvimento-web`. Referido daqui em diante como **ACERVO_DW**. Copiar de lá, nunca criar symlink para lá.

---

## File Structure

| Arquivo | Responsabilidade | Tarefa |
|---|---|---|
| `.gitignore` | Ignorar `__pycache__`, `.pytest_cache`, `shots/`, `node_modules`, `.DS_Store` | 1 |
| `README.md` | Apresentação curta do acervo e link do portal publicado | 1 |
| `index.html` | Redirecionar a raiz para `aulas-1sem/index.html` | 1 |
| `docs/ANDAMENTO.md` | Estado do trabalho entre sessões | 1 |
| `.github/workflows/static.yml` | Montar `_site` e publicar no GitHub Pages | 1 |
| `aulas-1sem/assets/css/uninove-theme.css` | Tema visual dos decks | 2 |
| `aulas-1sem/assets/css/uninove-print.css` | Ajustes de impressão para `?print-pdf` | 2 |
| `aulas-1sem/assets/js/uninove-quiz.js` | Interação do quiz de fixação | 2 |
| `aulas-1sem/assets/img/uninove-logo.png`, `code-bg.png` | Imagens do tema | 2 |
| `PLANO_DE_ENSINO.md` | Ementa, objetivos, avaliação, bibliografia | 3 |
| `PLANEJAMENTO_AULA_A_AULA.md` | Roteiro minuto a minuto das 20 aulas. Fonte da verdade do conteúdo de cada deck | 4 |
| `aulas-1sem/SKILL.md` | Metodologia e padrão de construção de deck e kit | 5 |
| `docs/adrs/ADR-001..005` | As cinco decisões arquiteturais da spec | 6 |
| `CLAUDE.md` | Instruções do repositório para sessões futuras | 7 |
| `tools/check_decks.py` | Validação estática de estrutura do deck | 8 |
| `tests/conftest.py` | Localização da raiz e helper de execução de validador | 8 |
| `tests/fixtures/decks/*.html` | Decks propositalmente quebrados, um defeito por arquivo | 8 |
| `tests/test_check_decks.py` | Cobertura das nove regras do `check_decks.py` | 8 |
| `tools/check_slides.py` | Geometria no navegador, estouro e sobreposição | 9 |
| `tools/check_canto_coral.py` | Triângulo coral pixel a pixel | 9 |
| `tools/check_portal.py` | Portal, 20 cards e GET real nos botões | 10 |
| `tests/test_check_portal.py` | Cobertura do `check_portal.py` | 10 |
| `tests/test_coerencia_do_planejamento.py` | Os 20 títulos batem entre plano de ensino, planejamento e portal | 10 |
| `.github/workflows/ci.yml` | pytest e os quatro validadores a cada push | 11 |
| `aulas-1sem/index.html` | Portal com 20 cards em 5 módulos | 12 |
| `aulas-1sem/aulas/aula01.html` | Deck padrão-ouro | 13 |
| `aulas-1sem/labs/aula01-lab/README.md`, `index.html` | Kit padrão-ouro | 14 |
| `aulas-1sem/aulas/aula02.html` a `aula20.html` | Os 19 decks restantes | 15 a 33 |
| `aulas-1sem/labs/aula02-lab/` a `aula20-lab/` | Os 19 kits restantes | 15 a 33 |

---

## Task 1: Bootstrap do repositório e publicação vazia

**Files:**
- Create: `.gitignore`
- Create: `README.md`
- Create: `index.html`
- Create: `docs/ANDAMENTO.md`
- Create: `.github/workflows/static.yml`
- Test: `tests/test_publicacao.py`

**Interfaces:**
- Consumes: nada.
- Produces: o workflow `static.yml`, cujo passo de montagem do `_site` a Task 11 replica no CI. A lista de exclusões do `rsync` é consumida por `tests/test_publicacao.py` e por nenhum outro lugar.

- [ ] **Step 1: Escrever o teste que falha**

Criar `tests/test_publicacao.py`. Ele lê o workflow e afirma que os diretórios sensíveis estão excluídos e que existe o passo anti-symlink.

```python
"""O workflow de publicacao nao pode vazar fonte de trabalho para o site."""
import pathlib

RAIZ = pathlib.Path(__file__).resolve().parents[1]
WORKFLOW = RAIZ / ".github" / "workflows" / "static.yml"

EXCLUSOES_OBRIGATORIAS = [
    ".git", ".github", ".claude", "tools", "tests", "docs", "pdf",
    "node_modules", "CLAUDE.md",
]


def test_workflow_existe():
    assert WORKFLOW.is_file(), "static.yml nao existe"


def test_todas_as_exclusoes_estao_no_rsync():
    texto = WORKFLOW.read_text(encoding="utf-8")
    faltando = [e for e in EXCLUSOES_OBRIGATORIAS
                if f"--exclude={e}" not in texto and f"--exclude='{e}'" not in texto]
    assert not faltando, f"exclusoes ausentes no rsync: {faltando}"


def test_existe_passo_anti_symlink():
    texto = WORKFLOW.read_text(encoding="utf-8")
    assert "find _site -type l" in texto, (
        "falta o passo que falha o build quando sobra symlink no _site"
    )
```

- [ ] **Step 2: Rodar o teste e confirmar que falha**

```bash
cd /Users/joseromualdocostafilho/Projects/Uninove/2026/uninove-2026-2-arquitetura-software
python3 -m pytest tests/test_publicacao.py -v
```

Esperado: FAIL em `test_workflow_existe`, porque `static.yml` ainda não existe.

- [ ] **Step 3: Criar o `.gitignore`**

```gitignore
__pycache__/
*.pyc
.pytest_cache/
.DS_Store
node_modules/
shots/
_site/
```

- [ ] **Step 4: Criar o `index.html` da raiz**

```html
<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="refresh" content="0; url=aulas-1sem/index.html">
  <title>Arquitetura de Software, Uninove 2026.2</title>
  <script>window.location.href = "aulas-1sem/index.html";</script>
</head>
<body style="font-family: sans-serif; text-align: center; padding-top: 50px; background-color: #00274D; color: #fff;">
  <h2>Redirecionando para o portal da disciplina</h2>
  <p>Caso o redirecionamento não ocorra, <a href="aulas-1sem/index.html" style="color: #C84B31;">clique aqui</a>.</p>
</body>
</html>
```

- [ ] **Step 5: Criar o `README.md`**

Conteúdo: nome da disciplina, instituição, semestre, professor, uma frase sobre o case Rota Sul, o link do portal publicado (`https://josercf.github.io/uninove-2026-2-arquitetura-software/`), e a instrução de preview local (`python3 -m http.server 8000`). Máximo de 40 linhas.

- [ ] **Step 6: Criar o `docs/ANDAMENTO.md`**

Conteúdo inicial: seção "Ordem de leitura ao abrir uma sessão" apontando para `CLAUDE.md`, `aulas-1sem/SKILL.md` e este arquivo; tabela "Onde está cada coisa" com o caminho local, o remote, o portal publicado e o ACERVO_DW; e as seções "Concluído" e "O que falta", esta última listando as 34 tarefas deste plano.

- [ ] **Step 7: Criar o `.github/workflows/static.yml`**

Copiar de `ACERVO_DW/.github/workflows/static.yml` e ajustar a lista de exclusões do `rsync` para exatamente: `.git`, `.github`, `.claude`, `tools`, `tests`, `docs`, `pdf`, `node_modules`, `.superpowers`, `shots`, `CLAUDE.md`. Manter o passo que roda `find _site -type l` e falha o build se houver saída.

- [ ] **Step 8: Rodar o teste e confirmar que passa**

```bash
python3 -m pytest tests/test_publicacao.py -v
```

Esperado: 3 passed.

- [ ] **Step 9: Commitar**

```bash
git add .gitignore README.md index.html docs/ANDAMENTO.md .github/workflows/static.yml tests/test_publicacao.py
git commit -m "feat(repo): bootstrap do acervo e workflow de publicacao"
```

- [ ] **Step 10: Habilitar o GitHub Pages e confirmar a publicação**

```bash
GIT_SSH_COMMAND='ssh -i /Users/joseromualdocostafilho/.ssh/id_ed25519_josercf -o IdentitiesOnly=yes -F /dev/null' git push
gh api -X POST repos/josercf/uninove-2026-2-arquitetura-software/pages -f build_type=workflow || true
gh run watch --exit-status
```

Esperado: o workflow conclui com sucesso. Acessar `https://josercf.github.io/uninove-2026-2-arquitetura-software/` deve redirecionar para `aulas-1sem/index.html` e dar 404, porque o portal ainda não existe. Esse 404 é o resultado correto nesta tarefa.

---

## Task 2: Tema visual e assets

**Files:**
- Create: `aulas-1sem/assets/css/uninove-theme.css`
- Create: `aulas-1sem/assets/css/uninove-print.css`
- Create: `aulas-1sem/assets/js/uninove-quiz.js`
- Create: `aulas-1sem/assets/img/uninove-logo.png`
- Create: `aulas-1sem/assets/img/code-bg.png`
- Test: `tests/test_tema.py`

**Interfaces:**
- Consumes: nada.
- Produces: as classes CSS que todo deck usa. Nomes exatos consumidos das Tasks 13 em diante: `cover-slide`, `title-slide`, `content-slide`, `section-slide`, `quiz-slide`, `exercise-slide`, `end-slide`, `slide-title-area`, `accent-bar`, `top-bar`, `uninove-logo-header`, `uninove-logo-full`, `title-card`, `lesson-bar`, `slide-footer`, `footer-bar`, `footer-page`, `concept-cards`, `concept-card`, `side-by-side`, `side`, `figure-split`, `slide-figure`, `timeline`, `tl-item`, `tl-dot`, `tl-year`, `tl-tool`, `tl-desc`, `is-past`, `takeaway`, `takeaway-label`, `callout`, `flow-diagram`, `flow-item`, `flow-arrow`, `exercise-container`, `exercise-steps`, `code-compact`, `ref-badge`, `decor-coral`, `quiz-container`, `quiz-question`, `quiz-options`, `option-letter`, `option-text`, `quiz-feedback`.

- [ ] **Step 1: Escrever o teste que falha**

Criar `tests/test_tema.py`.

```python
"""O tema copiado precisa trazer a paleta e todas as classes que os decks usam."""
import pathlib

RAIZ = pathlib.Path(__file__).resolve().parents[1]
ASSETS = RAIZ / "aulas-1sem" / "assets"
TEMA = ASSETS / "css" / "uninove-theme.css"

CLASSES_OBRIGATORIAS = [
    "cover-slide", "title-slide", "content-slide", "section-slide",
    "quiz-slide", "exercise-slide", "end-slide", "slide-title-area",
    "accent-bar", "top-bar", "uninove-logo-header", "uninove-logo-full",
    "title-card", "lesson-bar", "slide-footer", "footer-bar", "footer-page",
    "concept-cards", "concept-card", "side-by-side", "figure-split",
    "slide-figure", "timeline", "takeaway", "takeaway-label", "callout",
    "flow-diagram", "exercise-container", "exercise-steps", "code-compact",
    "ref-badge", "decor-coral", "quiz-container", "quiz-question",
    "quiz-options", "option-letter", "option-text", "quiz-feedback",
]

ARQUIVOS_OBRIGATORIOS = [
    "css/uninove-theme.css", "css/uninove-print.css",
    "js/uninove-quiz.js", "img/uninove-logo.png", "img/code-bg.png",
]


def test_todos_os_assets_existem():
    faltando = [a for a in ARQUIVOS_OBRIGATORIOS if not (ASSETS / a).is_file()]
    assert not faltando, f"assets ausentes: {faltando}"


def test_paleta_da_marca():
    css = TEMA.read_text(encoding="utf-8")
    assert "--uninove-azul: #00274D" in css
    assert "--uninove-coral: #C84B31" in css


def test_todas_as_classes_do_deck_existem_no_tema():
    css = TEMA.read_text(encoding="utf-8")
    faltando = [c for c in CLASSES_OBRIGATORIAS if f".{c}" not in css]
    assert not faltando, f"classes ausentes no tema: {faltando}"


def test_tema_nao_referencia_turmas():
    css = TEMA.read_text(encoding="utf-8")
    assert "turma" not in css.lower(), (
        "este acervo nao tem resolucao de turma; o tema nao deve mencionar turma"
    )
```

- [ ] **Step 2: Rodar o teste e confirmar que falha**

```bash
python3 -m pytest tests/test_tema.py -v
```

Esperado: FAIL em `test_todos_os_assets_existem`.

- [ ] **Step 3: Copiar os assets do ACERVO_DW**

```bash
DW=/Users/joseromualdocostafilho/Projects/Uninove/2026/uninove-2026-2-desenvolvimento-web
mkdir -p aulas-1sem/assets/css aulas-1sem/assets/js aulas-1sem/assets/img
cp "$DW/aulas-1sem/assets/css/uninove-theme.css"  aulas-1sem/assets/css/
cp "$DW/aulas-1sem/assets/css/uninove-print.css"  aulas-1sem/assets/css/
cp "$DW/aulas-1sem/assets/js/uninove-quiz.js"     aulas-1sem/assets/js/
cp "$DW/aulas-1sem/assets/img/uninove-logo.png"   aulas-1sem/assets/img/
cp "$DW/aulas-1sem/assets/img/code-bg.png"        aulas-1sem/assets/img/
```

Confirmar que são arquivos reais e não symlinks:

```bash
find aulas-1sem/assets -type l
```

Esperado: nenhuma saída.

- [ ] **Step 4: Rodar o teste e confirmar que passa**

```bash
python3 -m pytest tests/test_tema.py -v
```

Esperado: 4 passed. Se `test_todas_as_classes_do_deck_existem_no_tema` falhar, a classe ausente precisa ser acrescentada ao tema, não removida do teste: a lista veio da spec, seção 7.3.

- [ ] **Step 5: Commitar**

```bash
git add aulas-1sem/assets tests/test_tema.py
git commit -m "feat(tema): copia do tema visual Uninove do acervo de Desenvolvimento Web"
```

---

## Task 3: Plano de ensino

**Files:**
- Create: `PLANO_DE_ENSINO.md`

**Interfaces:**
- Consumes: o mapa do semestre da spec, seção 3.
- Produces: a tabela de cronograma com os 20 títulos, no formato `| 01 | Título |`, consumida por `tests/test_coerencia_do_planejamento.py` na Task 10.

- [ ] **Step 1: Escrever o documento**

Estrutura obrigatória, espelhando `ACERVO_DW/PLANO_DE_ENSINO.md`:

1. **Identificação**, em tabela: disciplina Arquitetura de Software, Uninove, graduação, semestre 2026.2, professor José Romualdo, contato `jose.romualdo@uni9.pro.br`, uma turma, 20 encontros de 150 minutos, 60 horas-aula, repositório do acervo e repositório-esqueleto do case. Explicar a conta das 60 horas-aula: a hora-aula da Uninove tem 50 minutos, 150 minutos equivalem a 3 horas-aula, 3 vezes 20 dão 60.
2. **Ementa**, em prosa corrida, cobrindo os 18 capítulos: evolução do desenvolvimento de software, padrões de projeto e frameworks, sistemas colaborativos e o modelo 3C, arquitetura de sistemas colaborativos, arquitetura de software e representação em UML, arquitetura em três camadas e MVC, arquitetura orientada a serviços, servidores de aplicação e a plataforma Java EE, metadados para troca de dados em XML e JSON, comunicação remota com RMI, SOAP e REST, catálogo de design patterns, anatomia de frameworks e inversão de controle, frameworks web, frameworks de persistência, JPA, Enterprise Java Beans, Hibernate, JavaServer Faces e montagem de uma aplicação distribuída.
3. **Objetivos gerais**, lista numerada de 9 itens, cada um começando com verbo no infinitivo.
4. **Metodologia**: sem sala de aula invertida, cada encontro autossuficiente, e o quadro dos quatro ciclos de 35, 35, 35 e 25 minutos mais quiz de 10 e fechamento de 10.
5. **O case Rota Sul**, resumindo a seção 4 da spec.
6. **Cronograma**, tabela com as colunas `Aula`, `Módulo`, `Título` e `Capítulo do AVA`, com as 20 linhas exatamente como a tabela da seção 3 da spec. A coluna `Aula` usa dois dígitos: `01`, não `1`.
7. **Avaliação**, com os pesos explícitos somando 100. Proposta: checkpoints de laboratório 40, prova 30, projeto final 30.
8. **Bibliografia**, separando os 18 capítulos do AVA de autoria do Prof. Paulo Ricardo Batista Mesquita da bibliografia complementar.

- [ ] **Step 2: Verificar que não há travessão em dash nem data inventada**

```bash
grep -n "—" PLANO_DE_ENSINO.md
grep -nE "[0-9]{2}/[0-9]{2}/[0-9]{4}" PLANO_DE_ENSINO.md
```

Esperado: nenhuma saída no primeiro. No segundo, apenas datas de confirmação de contato, se houver; nenhuma data de encontro.

- [ ] **Step 3: Verificar que as 20 linhas do cronograma existem**

```bash
grep -cE "^\| (0[1-9]|1[0-9]|20) \|" PLANO_DE_ENSINO.md
```

Esperado: `20`.

- [ ] **Step 4: Commitar**

```bash
git add PLANO_DE_ENSINO.md
git commit -m "docs(plano-de-ensino): ementa, cronograma das 20 aulas e avaliacao"
```

---

## Task 4: Planejamento aula a aula

**Files:**
- Create: `PLANEJAMENTO_AULA_A_AULA.md`

**Interfaces:**
- Consumes: os títulos da Task 3 e os PDFs em `pdf/001.pdf` a `pdf/018.pdf`.
- Produces: uma seção por aula, com cabeçalho no formato exato `## Aula NN, Título`, consumida por `tests/test_coerencia_do_planejamento.py` na Task 10 e pelas Tasks 13 a 33, que constroem cada deck a partir da sua seção.

Este é o documento mais longo do acervo e a fonte da verdade do conteúdo dos decks. Um deck construído sem a sua seção correspondente pronta vira improviso.

- [ ] **Step 1: Extrair o texto dos 18 PDFs para consulta**

```bash
mkdir -p /tmp/rota-sul-fontes
for f in pdf/*.pdf; do
  pdftotext -layout "$f" "/tmp/rota-sul-fontes/$(basename "${f%.pdf}").txt"
done
wc -l /tmp/rota-sul-fontes/*.txt
```

Esperado: 18 arquivos, cerca de 8000 linhas no total.

- [ ] **Step 2: Escrever o cabeçalho e a legenda do documento**

Abertura com: o propósito do arquivo, o quadro dos quatro ciclos, a convenção de que toda aula a partir da 02 abre retomando o entregável da aula anterior, e o aviso de que os títulos precisam bater com `PLANO_DE_ENSINO.md` e com o portal.

- [ ] **Step 3: Escrever as 20 seções**

Uma seção por aula, com esta estrutura fixa:

```markdown
## Aula NN, Título exatamente igual ao do plano de ensino

**Módulo:** M<N>, Nome do módulo
**Capítulo do AVA:** `pdf/0NN.pdf`, Título do capítulo
**Entregável:** frase única, com quantidade e critério

### Retomada, 5 minutos
O que a aula anterior entregou, citado pelo nome.

### Ciclo 1, 19h30 às 20h05
- Conceito: ...
- Demonstração no projetor: ...
- Exercício curto: ...

### Ciclo 2, 20h05 às 20h40
- Conceito: ...
- Demonstração no projetor: ...
- Exercício curto: ...

### Quiz, 20h40 às 20h50
Pergunta, quatro alternativas, alternativa correta e a justificativa.

### Ciclo 3, 20h50 às 21h25
Laboratório guiado, um passo numerado por bloco.

### Ciclo 4, 21h25 às 21h50
Laboratório final e o entregável.

### Fechamento, 21h50 às 22h00
Commit, push e prévia da próxima aula.

### Referências
Lista numerada. O capítulo do AVA é sempre a referência [1].
```

Os parâmetros de cada aula estão na tabela do **Procedimento P**, mais adiante neste plano. Use a coluna `Laboratório` e a coluna `Entregável` como âncora dos Ciclos 3 e 4.

- [ ] **Step 4: Verificar que as 20 seções existem e nenhuma tem travessão**

```bash
grep -cE "^## Aula (0[1-9]|1[0-9]|20), " PLANEJAMENTO_AULA_A_AULA.md
grep -n "—" PLANEJAMENTO_AULA_A_AULA.md
```

Esperado: `20` no primeiro, nenhuma saída no segundo.

- [ ] **Step 5: Commitar**

```bash
git add PLANEJAMENTO_AULA_A_AULA.md
git commit -m "docs(planejamento): roteiro minuto a minuto das 20 aulas"
```

---

## Task 5: Metodologia em SKILL.md

**Files:**
- Create: `aulas-1sem/SKILL.md`

**Interfaces:**
- Consumes: as seções 4, 7 e 8 da spec.
- Produces: o documento que as Tasks 13 a 33 leem antes de escrever qualquer deck.

- [ ] **Step 1: Escrever o documento**

Com frontmatter YAML no topo:

```yaml
---
name: arquitetura-course-design
description: Metodologia e padrão de construção das aulas de Arquitetura de Software da Uninove 2026.2. Inclui a espiral de conteúdo, o case Rota Sul, a estrutura do encontro de 150 minutos em quatro ciclos, o padrão dos decks Reveal.js com tema Uninove e o padrão dos kits de laboratório.
---
```

Seções obrigatórias, adaptadas de `ACERVO_DW/aulas-1sem/SKILL.md`:

1. **Pilares metodológicos:** aprendizagem em espiral e aprendizagem por case.
2. **Sem sala de aula invertida.**
3. **Estrutura do encontro de 150 minutos**, com o quadro dos quatro ciclos.
4. **Eixos de conteúdo**, os cinco módulos da seção 3 da spec.
5. **O case Rota Sul**, copiando a seção 4 da spec: mini mundo, atores, entidades, contrato técnico, forma distribuída da Aula 19 e a tabela das Aulas 01 a 05 sem código de aplicação.
6. **Anatomia do deck**, copiando a seção 7 da spec, incluindo o esqueleto HTML completo e o bloco `Reveal.initialize`.
7. **Quizzes**, com o markup completo e a regra do `option-text`.
8. **Padrão dos kits de laboratório**, copiando a seção 8 da spec.
9. **O ciclo do artefato**, os quatro passos.
10. **Validação**, a tabela dos quatro validadores da seção 9 da spec.

Duas diferenças em relação ao ACERVO_DW que precisam estar escritas com todas as letras, porque são o erro mais provável de quem copiar de lá:

> Este acervo **não tem** resolução de turma. Não existe `assets/js/turmas.js`, não existe o atributo `data-data-da-aula` e **nenhum deck exibe data**. O slide de título traz apenas `AULA XX | Módulo N, Nome do módulo` e o nome do professor. Data escrita à mão é reprovada por `tools/check_decks.py`.

> Os validadores deste acervo são **cópias**, não symlinks. Corrigir um bug aqui não corrige nos acervos de Desenvolvimento Web nem da FIAP.

- [ ] **Step 2: Verificar ausência de travessão e de menção a turma**

```bash
grep -n "—" aulas-1sem/SKILL.md
grep -niE "turmas\.js|data-data-da-aula" aulas-1sem/SKILL.md
```

Esperado: nenhuma saída no primeiro. No segundo, apenas as ocorrências dentro do parágrafo de aviso acima.

- [ ] **Step 3: Commitar**

```bash
git add aulas-1sem/SKILL.md
git commit -m "docs(metodologia): SKILL.md com o padrao de construcao das aulas"
```

---

## Task 6: Os cinco ADRs

**Files:**
- Create: `docs/adrs/ADR-001-stack-spring-boot-no-lugar-de-jakarta-ee.md`
- Create: `docs/adrs/ADR-002-sem-resolucao-de-turma-e-sem-data-no-deck.md`
- Create: `docs/adrs/ADR-003-copia-em-vez-de-symlink.md`
- Create: `docs/adrs/ADR-004-case-rota-sul-e-repositorio-esqueleto-unico.md`
- Create: `docs/adrs/ADR-005-mapeamento-um-para-um-com-a-ordem-do-ava.md`

**Interfaces:**
- Consumes: a seção 6 da spec, que já traz o conteúdo de cada um.
- Produces: nada consumido por código.

- [ ] **Step 1: Escrever os cinco arquivos**

Cada um com a estrutura mínima exigida pela diretiva global do professor:

```markdown
# ADR-00N: Título curto

**Data:** 10/08/2026
**Status:** Aceita
**Decisores:** Prof. José Romualdo

## Contexto
## Decisão
## Motivações
## Riscos conhecidos
## Consequências
### Positivas
### Negativas
## ADRs relacionadas
```

O conteúdo de cada um vem da seção 6 da spec: 6.1 vira ADR-001, 6.2 vira ADR-002, 6.3 vira ADR-003, 6.4 vira ADR-004 e 6.5 vira ADR-005. A seção **Decisão** é sempre uma frase única.

ADR-003 precisa citar nominalmente a ADR-006 do acervo de Desenvolvimento Web, que registra o incidente do `tar --dereference`, como a evidência que motiva a escolha por cópia.

- [ ] **Step 2: Verificar que os cinco existem, com as seções obrigatórias**

```bash
ls docs/adrs/ | wc -l
for f in docs/adrs/ADR-*.md; do
  for s in "## Contexto" "## Decisão" "## Motivações" "## Riscos conhecidos" "## Consequências"; do
    grep -q "$s" "$f" || echo "FALTA '$s' em $f"
  done
done
grep -l "—" docs/adrs/*.md
```

Esperado: `5`, nenhuma linha de "FALTA" e nenhum arquivo com travessão.

- [ ] **Step 3: Commitar**

```bash
git add docs/adrs
git commit -m "docs(adr): registra as cinco decisoes arquiteturais do acervo"
```

---

## Task 7: CLAUDE.md

**Files:**
- Create: `CLAUDE.md`

**Interfaces:**
- Consumes: tudo produzido nas Tasks 1 a 6.
- Produces: nada consumido por código.

- [ ] **Step 1: Escrever o documento**

Espelhando `ACERVO_DW/CLAUDE.md`, com estas seções:

1. Instrução de abrir lendo `docs/ANDAMENTO.md`.
2. **O que é este repositório**, deixando claro que não há build nem bundler.
3. **Comandos**, em bloco bash: preview local, exportação em PDF por `?print-pdf`, `python3 -m pytest tests/ -v` e os quatro validadores.
4. **As três camadas de conteúdo**, apontando planejamento, metodologia e materiais.
5. **O case Rota Sul**, em parágrafo curto.
6. **Anatomia do deck**, com a ordem canônica dos slides.
7. **Armadilhas conhecidas**, contendo no mínimo:
   - Slide que estoura 720px não é detectável por `scrollHeight`, porque a `section` tem altura travada. Usar sempre `check_slides.py`.
   - A `li` do quiz é `display: flex` com `gap: 12px`: alternativa com elemento inline precisa de `<span class="option-text">`.
   - Este acervo não tem resolução de turma, e nenhum deck exibe data.
   - Os validadores são cópias, não symlinks; corrigir aqui não corrige nos outros acervos.
   - O remote usa o host `github.com`, que autentica como `canaldoovidio`; o push precisa do `GIT_SSH_COMMAND` com a chave `id_ed25519_josercf`.
   - O `pdf/` fica fora do artefato do GitHub Pages, de propósito.
8. **Convenções editoriais**, a lista de Global Constraints deste plano.

- [ ] **Step 2: Commitar**

```bash
git add CLAUDE.md
git commit -m "docs(claude): instrucoes do repositorio para sessoes futuras"
```

---

## Task 8: check_decks.py adaptado e a suíte pytest

**Files:**
- Create: `tools/check_decks.py`
- Create: `tests/conftest.py`
- Create: `tests/fixtures/decks/deck_ok.html`
- Create: `tests/fixtures/decks/deck_sem_decor_coral.html`
- Create: `tests/fixtures/decks/deck_quiz_sem_content_slide.html`
- Create: `tests/fixtures/decks/deck_quiz_duas_corretas.html`
- Create: `tests/fixtures/decks/deck_quiz_sem_correta.html`
- Create: `tests/fixtures/decks/deck_footer_fora_de_sequencia.html`
- Create: `tests/fixtures/decks/deck_ancora_orfa.html`
- Create: `tests/fixtures/decks/deck_caminho_quebrado.html`
- Create: `tests/fixtures/decks/deck_com_data_manual.html`
- Create: `tests/fixtures/decks/deck_alternativa_inline_solto.html`
- Create: `tests/test_check_decks.py`

**Interfaces:**
- Consumes: nada das tarefas anteriores.
- Produces: `tools/check_decks.py`, executável como `python3 tools/check_decks.py [caminho...]`, com **exit code 0 quando tudo passa e 1 quando há erro**, e mensagens de erro em stdout no formato `<rotulo>  linha <N>: <descricao>`. As Tasks 13 a 34 dependem desse contrato.

Esta é a tarefa central do plano. Os validadores são escritos **antes** de qualquer deck existir, de propósito: validador escrito depois de 20 decks tende a ser escrito para aprová-los.

- [ ] **Step 1: Copiar o validador de origem**

```bash
DW=/Users/joseromualdocostafilho/Projects/Uninove/2026/uninove-2026-2-desenvolvimento-web
mkdir -p tools
cp "$DW/tools/check_decks.py" tools/check_decks.py
find tools -type l
```

Esperado: nenhuma saída no `find`, confirmando que é cópia.

- [ ] **Step 2: Escrever o `tests/helpers.py` e o `tests/conftest.py`**

Os helpers ficam num módulo próprio, e não dentro do `conftest.py`, porque `from conftest import ...` só funciona por causa da inserção automática de `sys.path` do pytest e quebra assim que `tests/` ganhar um `__init__.py`. Um módulo comum é importável sem depender desse detalhe.

`tests/helpers.py`:

```python
"""Helpers compartilhados pelos testes dos validadores."""
import pathlib
import subprocess
import sys

RAIZ = pathlib.Path(__file__).resolve().parents[1]
FIXTURES = pathlib.Path(__file__).resolve().parent / "fixtures"
FIXTURES_DECKS = FIXTURES / "decks"


def rodar_validador(script, *argumentos):
    """Roda um validador e devolve (exit_code, saida_combinada)."""
    processo = subprocess.run(
        [sys.executable, str(RAIZ / "tools" / script), *map(str, argumentos)],
        capture_output=True,
        text=True,
    )
    return processo.returncode, processo.stdout + processo.stderr
```

`tests/conftest.py`:

```python
"""Fixtures do pytest. A logica de execucao vive em helpers.py."""
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
```

- [ ] **Step 3: Escrever a fixture válida `deck_ok.html`**

Deck mínimo de 5 slides que passa em todas as regras. Os caminhos relativos apontam para `../../../aulas-1sem/assets/...`, que existem desde a Task 2.

```html
<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8">
  <title>Aula 99, Fixture valida | Uninove</title>
  <link rel="stylesheet" href="../../../aulas-1sem/assets/css/uninove-theme.css">
</head>
<body>
  <div class="reveal"><div class="slides">

    <section class="cover-slide">
      <img src="../../../aulas-1sem/assets/img/uninove-logo.png" alt="Uninove" class="uninove-logo-full">
      <h1>Arquitetura de Software</h1>
    </section>

    <section class="title-slide">
      <div class="top-bar"></div>
      <div class="title-card">
        <div class="accent-bar"></div>
        <h1>Arquitetura de Software</h1>
        <h2>Fixture valida</h2>
        <h3>Prof. Jose Romualdo</h3>
      </div>
      <div class="lesson-bar">AULA 99 &nbsp;|&nbsp; Modulo 1, Fixtures</div>
    </section>

    <section class="content-slide">
      <div class="top-bar"></div>
      <div class="decor-coral"></div>
      <div class="slide-title-area">
        <div class="accent-bar"></div>
        <h2>Conceito <a href="#/ref-slide" class="ref-badge">[1]</a></h2>
      </div>
      <p>Uma frase.</p>
      <div class="slide-footer">
        <div class="footer-bar">99 Conceito</div>
        <div class="footer-page">3</div>
      </div>
    </section>

    <section class="quiz-slide content-slide">
      <div class="top-bar"></div>
      <div class="decor-coral"></div>
      <div class="slide-title-area">
        <div class="accent-bar"></div>
        <h2>Quiz de Fixacao</h2>
      </div>
      <div class="quiz-container">
        <div class="quiz-question">Pergunta direta?</div>
        <ul class="quiz-options">
          <li data-correct="false"><span class="option-letter">A</span> Opcao A</li>
          <li data-correct="true"><span class="option-letter">B</span> Opcao B</li>
          <li data-correct="false"><span class="option-letter">C</span> Opcao C</li>
          <li data-correct="false"><span class="option-letter">D</span> Opcao D</li>
        </ul>
        <div class="quiz-feedback" data-correct-msg="Correto." data-incorrect-msg="Incorreto."></div>
      </div>
      <div class="slide-footer">
        <div class="footer-bar">99 Quiz</div>
        <div class="footer-page">4</div>
      </div>
    </section>

    <section id="ref-slide" class="content-slide">
      <div class="top-bar"></div>
      <div class="decor-coral"></div>
      <div class="slide-title-area">
        <div class="accent-bar"></div>
        <h2>Referencias</h2>
      </div>
      <ol><li>MESQUITA, P. R. B. Capitulo do AVA.</li></ol>
      <div class="slide-footer">
        <div class="footer-bar">99 Referencias</div>
        <div class="footer-page">5</div>
      </div>
    </section>

  </div></div>
</body>
</html>
```

- [ ] **Step 4: Derivar as nove fixtures quebradas**

Cada uma é uma cópia de `deck_ok.html` com **exatamente um** defeito introduzido. Um arquivo com dois defeitos não prova qual regra disparou.

| Arquivo | Defeito introduzido |
|---|---|
| `deck_sem_decor_coral.html` | Remover a linha `<div class="decor-coral"></div>` do terceiro slide |
| `deck_quiz_sem_content_slide.html` | Trocar `class="quiz-slide content-slide"` por `class="quiz-slide"` |
| `deck_quiz_duas_corretas.html` | Pôr `data-correct="true"` também na alternativa C |
| `deck_quiz_sem_correta.html` | Pôr `data-correct="false"` na alternativa B |
| `deck_footer_fora_de_sequencia.html` | Trocar o `footer-page` do quiz de `4` para `6` |
| `deck_ancora_orfa.html` | Trocar `id="ref-slide"` por `id="referencias"`, deixando o `href="#/ref-slide"` órfão |
| `deck_caminho_quebrado.html` | Trocar o `src` da logo por `../../../aulas-1sem/assets/img/inexistente.png` |
| `deck_com_data_manual.html` | Acrescentar `<h3>Prof. Jose Romualdo<br>12/08/2026</h3>` no slide de título |
| `deck_alternativa_inline_solto.html` | Trocar a alternativa D por `<li data-correct="false"><span class="option-letter">D</span> Usa <code>@Service</code> na classe.</li>`, sem envolver o texto em `option-text` |

- [ ] **Step 5: Escrever o teste que falha**

```python
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
        f"{fixture} foi reprovada, mas a mensagem nao cita {trecho_esperado!r}.\n"
        f"Saida:\n{saida}"
    )


@pytest.mark.parametrize("fixture,_", CASOS_QUE_DEVEM_REPROVAR)
def test_mensagem_de_erro_cita_a_linha(checar_deck, fixture, _):
    codigo, saida = checar_deck(fixture)
    assert codigo != 0
    assert "linha" in saida.lower(), (
        f"{fixture}: a mensagem precisa nomear a linha do defeito.\nSaida:\n{saida}"
    )
```

- [ ] **Step 6: Rodar e observar quais falham**

```bash
python3 -m pytest tests/test_check_decks.py -v
```

Esperado: `deck_com_data_manual.html` **passa quando deveria reprovar**, porque a regra de data ainda não existe. Os demais casos devem reprovar corretamente, porque vieram do validador do ACERVO_DW. Se algum outro falhar, é bug de fixture, e a fixture é que precisa ser corrigida.

- [ ] **Step 7: Remover a regra de `data-data-da-aula`**

Em `tools/check_decks.py`, remover a função `checar_data_da_aula` (por volta da linha 232), a sua chamada dentro de `checar_deck`, a função `numero_da_aula_no_nome` se ficar sem uso, a coleta de `datas_da_aula` no parser (por volta da linha 188) e a menção à regra no docstring do topo do arquivo.

- [ ] **Step 8: Acrescentar a regra que reprova data escrita à mão**

```python
# Datas em deck envelhecem o material sem que ninguem perceba, e esta disciplina
# nao tem calendario definido. Ver ADR-002.
PADRAO_DATA_NUMERICA = re.compile(r"\b\d{2}/\d{2}/\d{4}\b")
MESES = (
    "janeiro|fevereiro|marco|março|abril|maio|junho|julho|agosto|setembro|"
    "outubro|novembro|dezembro"
)
PADRAO_DATA_POR_EXTENSO = re.compile(
    rf"\b\d{{1,2}}\s+de\s+({MESES})\b", re.IGNORECASE
)


def checar_sem_data_manual(leitor, erros, rotulo):
    """Nenhum deck deste acervo exibe data. Ver ADR-002."""
    for texto, linha in leitor.textos:
        for padrao in (PADRAO_DATA_NUMERICA, PADRAO_DATA_POR_EXTENSO):
            achado = padrao.search(texto)
            if achado:
                erros.append(
                    "%s  linha %d: data escrita a mao, %r. Este acervo nao tem "
                    "calendario e nenhum deck exibe data. Ver ADR-002."
                    % (rotulo, linha, achado.group(0))
                )
```

O parser precisa acumular `self.textos` como lista de `(texto, linha)` no `handle_data`. Se o `LeitorDeDeck` copiado já guardar os textos com a linha, reaproveitar; caso contrário, acrescentar no `handle_data` existente:

```python
def handle_data(self, data):
    limpo = data.strip()
    if limpo:
        self.textos.append((limpo, self.getpos()[0]))
```

Inicializar `self.textos = []` no `__init__` e chamar `checar_sem_data_manual(leitor, erros, rotulo)` dentro de `checar_deck`.

- [ ] **Step 9: Rodar a suíte e confirmar que fica verde**

```bash
python3 -m pytest tests/test_check_decks.py -v
```

Esperado: 19 passed (1 do deck válido, 9 de reprovação, 9 de mensagem com linha).

- [ ] **Step 10: Confirmar que a regra antiga sumiu**

```bash
grep -n "data-data-da-aula" tools/check_decks.py
```

Esperado: nenhuma saída.

- [ ] **Step 11: Commitar**

```bash
git add tools/check_decks.py tests/conftest.py tests/fixtures tests/test_check_decks.py
git commit -m "feat(validadores): check_decks.py sem regra de turma e reprovando data manual"
```

---

## Task 9: check_slides.py e check_canto_coral.py

**Files:**
- Create: `tools/check_slides.py`
- Create: `tools/check_canto_coral.py`
- Test: `tests/test_validadores_de_navegador.py`

**Interfaces:**
- Consumes: as fixtures da Task 8.
- Produces: dois executáveis com o mesmo contrato de exit code do `check_decks.py`.

Estes dois medem geometria num navegador headless e não entram na suíte de fixtures da Task 8. O teste aqui é de fumaça: garante que o script roda no ambiente e reprova um deck que estoura.

- [ ] **Step 1: Copiar os dois validadores**

```bash
DW=/Users/joseromualdocostafilho/Projects/Uninove/2026/uninove-2026-2-desenvolvimento-web
cp "$(readlink -f "$DW/tools/check_slides.py")" tools/check_slides.py
cp "$DW/tools/check_canto_coral.py" tools/check_canto_coral.py
find tools -type l
```

Esperado: nenhuma saída. O `readlink -f` é necessário porque no ACERVO_DW o `check_slides.py` é symlink para o acervo da FIAP; queremos o conteúdo, não o link.

- [ ] **Step 2: Instalar a dependência de navegador**

```bash
python3 -m pip install --quiet playwright
python3 -m playwright install chromium
```

- [ ] **Step 3: Criar a fixture que estoura a altura**

`tests/fixtures/decks/deck_estoura_altura.html`: cópia de `deck_ok.html` com um terceiro slide contendo 60 parágrafos de texto, o suficiente para ultrapassar 720px.

- [ ] **Step 4: Escrever o teste que falha**

```python
"""Fumaca dos dois validadores que dependem de navegador."""
import pytest

from helpers import FIXTURES_DECKS, rodar_validador


def test_check_slides_aprova_deck_valido():
    codigo, saida = rodar_validador("check_slides.py", FIXTURES_DECKS / "deck_ok.html")
    assert codigo == 0, f"o deck valido foi reprovado:\n{saida}"


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
    assert codigo == 0, f"o deck valido foi reprovado:\n{saida}"
```

- [ ] **Step 5: Rodar e ajustar**

```bash
python3 -m pytest tests/test_validadores_de_navegador.py -v
```

Esperado: 3 passed. Se um validador copiado esperar uma estrutura de diretório específica (por exemplo, procurar `aulas-1sem/aulas/*.html` por conta própria quando não recebe argumento), ajustar o script para aceitar caminho arbitrário via argumento, sem mudar o comportamento padrão.

- [ ] **Step 6: Commitar**

```bash
git add tools/check_slides.py tools/check_canto_coral.py tests/fixtures/decks/deck_estoura_altura.html tests/test_validadores_de_navegador.py
git commit -m "feat(validadores): copia dos validadores de geometria e teste de fumaca"
```

---

## Task 10: check_portal.py e a coerência do planejamento

**Files:**
- Create: `tools/check_portal.py`
- Create: `tests/fixtures/portal_quebrado/index.html`
- Create: `tests/test_check_portal.py`
- Create: `tests/test_coerencia_do_planejamento.py`

**Interfaces:**
- Consumes: `PLANO_DE_ENSINO.md` (Task 3) e `PLANEJAMENTO_AULA_A_AULA.md` (Task 4).
- Produces: `tools/check_portal.py`, com esta assinatura de linha de comando:
  - `python3 tools/check_portal.py` sem argumento confere `aulas-1sem/index.html`, o modo usado em sala e no CI.
  - `python3 tools/check_portal.py <caminho/para/index.html>` confere o portal indicado, servindo a partir do diretório que o contém. É esse argumento opcional que torna o validador testável contra fixture.
  - Exit code 0 quando tudo passa, 1 quando há erro, igual ao `check_decks.py`.

- [ ] **Step 1: Copiar e adaptar o validador do portal**

```bash
DW=/Users/joseromualdocostafilho/Projects/Uninove/2026/uninove-2026-2-desenvolvimento-web
cp "$DW/tools/check_portal.py" tools/check_portal.py
```

Três adaptações:

1. Remover toda verificação de seletor de turma e de `localStorage` da chave `uninove-turma`, que não existem neste acervo.
2. Aceitar o **argumento opcional de caminho** descrito no bloco Interfaces acima. Sem argumento, o comportamento é o atual.
3. Manter a contagem de 20 cards, a recusa de listagem de diretório pelo servidor de teste e o GET real em cada botão habilitado.

- [ ] **Step 2: Escrever o teste que falha**

```python
"""O check_portal precisa reprovar card habilitado apontando para arquivo ausente."""
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
```

- [ ] **Step 3: Criar a fixture `tests/fixtures/portal_quebrado/index.html`**

Portal mínimo com 20 cards, dos quais o card da Aula 07 está habilitado com `href="aulas/aula07.html"` apontando para um arquivo que não existe, e existe um diretório `tests/fixtures/portal_quebrado/labs/aula07-lab/` sem `index.html` dentro.

- [ ] **Step 4: Escrever o teste de coerência dos títulos**

```python
"""Os 20 titulos precisam ser identicos nos tres lugares onde aparecem."""
import re

from helpers import RAIZ

PLANO = RAIZ / "PLANO_DE_ENSINO.md"
PLANEJAMENTO = RAIZ / "PLANEJAMENTO_AULA_A_AULA.md"
PORTAL = RAIZ / "aulas-1sem" / "index.html"


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


def test_os_tres_lugares_tem_vinte_aulas():
    assert len(titulos_do_plano()) == 20
    assert len(titulos_do_planejamento()) == 20
    assert len(titulos_do_portal()) == 20


def test_os_titulos_batem_entre_os_tres():
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
```

- [ ] **Step 5: Rodar e confirmar o estado**

```bash
python3 -m pytest tests/test_check_portal.py tests/test_coerencia_do_planejamento.py -v
```

Esperado nesta tarefa: `test_check_portal.py` passa; `test_coerencia_do_planejamento.py` **falha**, porque `aulas-1sem/index.html` ainda não existe. Essa falha é o teste vermelho que a Task 12 fecha. Registrar isso no commit.

- [ ] **Step 6: Commitar**

```bash
git add tools/check_portal.py tests/fixtures/portal_quebrado tests/test_check_portal.py tests/test_coerencia_do_planejamento.py
git commit -m "feat(validadores): check_portal sem seletor de turma e teste de coerencia dos titulos"
```

---

## Task 11: CI

**Files:**
- Create: `.github/workflows/ci.yml`

**Interfaces:**
- Consumes: os quatro validadores e a suíte pytest.
- Produces: o gate que as Tasks 13 a 34 precisam ver verde.

- [ ] **Step 1: Escrever o workflow**

```yaml
name: CI

on:
  push:
  pull_request:

jobs:
  validar:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - uses: actions/setup-python@v5
        with:
          python-version: '3.12'

      - name: Instalar dependencias
        run: |
          python -m pip install --upgrade pip
          python -m pip install pytest playwright
          python -m playwright install --with-deps chromium

      - name: Suite de testes dos validadores
        run: python -m pytest tests/ -v

      - name: Estrutura dos decks
        run: |
          shopt -s nullglob
          decks=(aulas-1sem/aulas/aula*.html)
          if [ ${#decks[@]} -eq 0 ]; then echo "nenhum deck ainda"; exit 0; fi
          python tools/check_decks.py "${decks[@]}"

      - name: Geometria dos decks
        run: |
          shopt -s nullglob
          decks=(aulas-1sem/aulas/aula*.html)
          if [ ${#decks[@]} -eq 0 ]; then echo "nenhum deck ainda"; exit 0; fi
          python tools/check_slides.py "${decks[@]}"
          python tools/check_canto_coral.py "${decks[@]}"

      - name: Portal
        run: |
          if [ ! -f aulas-1sem/index.html ]; then echo "portal ainda nao existe"; exit 0; fi
          python tools/check_portal.py
```

As guardas `if` existem porque este workflow entra no ar antes dos decks e do portal. Elas saem na Task 34, quando os 20 decks existem e um acervo sem deck deixa de ser estado válido.

- [ ] **Step 2: Commitar e confirmar verde**

```bash
git add .github/workflows/ci.yml
git commit -m "ci: pytest e os quatro validadores a cada push"
GIT_SSH_COMMAND='ssh -i /Users/joseromualdocostafilho/.ssh/id_ed25519_josercf -o IdentitiesOnly=yes -F /dev/null' git push
gh run watch --exit-status
```

Esperado: o job conclui com sucesso, com o pytest verde e as três guardas informando que ainda não há deck nem portal.

---

## Task 12: Portal com os 20 cards

**Files:**
- Create: `aulas-1sem/index.html`

**Interfaces:**
- Consumes: os títulos de `PLANO_DE_ENSINO.md` e a estrutura de card do ACERVO_DW.
- Produces: 20 elementos `<article class="card" data-aula="N">`, cada um com `<span class="card-numero">Aula NN</span>` e `<h3 class="card-titulo">Título</h3>`, consumidos por `tests/test_coerencia_do_planejamento.py` e por `tools/check_portal.py`.

- [ ] **Step 1: Rodar o teste que já está vermelho**

```bash
python3 -m pytest tests/test_coerencia_do_planejamento.py -v
```

Esperado: FAIL, porque `aulas-1sem/index.html` não existe. Este é o vermelho que a tarefa fecha.

- [ ] **Step 2: Escrever o portal**

Partir de `ACERVO_DW/aulas-1sem/index.html` e aplicar quatro mudanças:

1. Trocar o nome da disciplina para Arquitetura de Software em título, cabeçalho e rodapé.
2. **Remover por completo o seletor de turma**, o bloco de script que lê `localStorage` da chave `uninove-turma` e qualquer texto que cite quarta ou quinta-feira.
3. Trocar os módulos pelos cinco deste acervo, com os títulos:
   - Módulo 1, Fundamentos e sistemas colaborativos, Aulas 01 a 06
   - Módulo 2, Integração e serviços distribuídos, Aulas 07 a 10
   - Módulo 3, Padrões e frameworks, Aulas 11 a 14
   - Módulo 4, Persistência e componentes, Aulas 15 a 18
   - Módulo 5, Projeto final, Aulas 19 e 20
4. Escrever os 20 cards com os títulos da tabela do **Procedimento P**, **todos desabilitados**:

```html
<article class="card" data-aula="3">
  <div class="card-header">
    <span class="card-numero">Aula 03</span>
  </div>
  <h3 class="card-titulo">Sistemas colaborativos</h3>
  <div class="card-acoes">
    <a class="btn disabled" aria-disabled="true">Slides</a>
    <a class="btn disabled" aria-disabled="true">Lab</a>
  </div>
  <span class="badge-producao">Em produção</span>
</article>
```

- [ ] **Step 3: Rodar os testes e o validador**

```bash
python3 -m pytest tests/test_coerencia_do_planejamento.py -v
python3 tools/check_portal.py
```

Esperado: pytest verde nos dois testes de coerência, e `check_portal.py` com exit 0, encontrando 20 cards e nenhum botão habilitado para conferir.

- [ ] **Step 4: Confirmar que não sobrou nada de turma**

```bash
grep -niE "turma|quarta-feira|quinta-feira|uninove-turma" aulas-1sem/index.html
```

Esperado: nenhuma saída.

- [ ] **Step 5: Commitar**

```bash
git add aulas-1sem/index.html
git commit -m "feat(portal): 20 cards em cinco modulos, todos em producao"
```

---

## Task 13: Aula 01, o deck padrão-ouro

**Files:**
- Create: `aulas-1sem/aulas/aula01.html`

**Interfaces:**
- Consumes: `PLANEJAMENTO_AULA_A_AULA.md` seção "Aula 01", o tema da Task 2 e os validadores das Tasks 8 e 9.
- Produces: o arquivo que as Tasks 15 a 33 copiam como ponto de partida. Toda decisão de markup tomada aqui se propaga por 19 decks.

Esta aula tem, além dos slides canônicos, os slides de abertura de semestre: apresentação do professor, metodologia, avaliação com os pesos e apresentação do case Rota Sul. As demais aulas não os repetem.

- [ ] **Step 1: Escrever o `<head>` e o `Reveal.initialize`**

Exatamente como a seção 7.2 da spec. Cinco folhas de estilo nesta ordem: `reveal.css`, `theme/white.css`, `plugin/highlight/monokai.css`, `../assets/css/uninove-theme.css`, `../assets/css/uninove-print.css`, mais o Google Fonts com Montserrat e JetBrains Mono. Título no formato `Aula 01, Abertura do semestre e o problema da arquitetura | Uninove`.

```js
Reveal.initialize({
  width: 1280, height: 720, center: false, margin: 0,
  hash: true, slideNumber: false,
  controls: false, progress: false,
  pdfMaxPagesPerSlide: 1,
  plugins: [RevealHighlight],
});
```

Scripts carregados: `reveal.js`, o plugin `highlight.js` e `../assets/js/uninove-quiz.js`. **Nenhum módulo ES**, porque não há resolução de turma.

- [ ] **Step 2: Escrever os slides na ordem canônica**

```
 1  capa
 2  título, com AULA 01 | Módulo 1, Fundamentos e sistemas colaborativos
 3  agenda com os horários dos quatro ciclos
 4  apresentação do professor
 5  metodologia do semestre, os quatro ciclos
 6  avaliação, com os pesos somando 100
 7  o case Rota Sul, mini mundo
 8  o case Rota Sul, atores e entidades
 9  ciclo 1, o que arquitetura de software resolve
10  ciclo 1, o custo de não decidir
11  ciclo 2, o contrato técnico do semestre
12  ciclo 2, Git e o fork do repositório-esqueleto
13  quiz de fixação
14  ciclo 3, laboratório, passo 1, instalar Java 21 e Maven
15  ciclo 3, laboratório, passo 2, forkar e clonar
16  ciclo 4, laboratório, passo 3, subir o Spring Boot vazio
17  ciclo 4, entregável e critérios de aceitação
18  fechamento, commit, push e prévia da Aula 02
19  referências, com id="ref-slide"
20  encerramento com copyright
```

Regras que o validador confere e que precisam estar certas desde aqui:

- Todo slide de conteúdo, quiz ou exercício leva `<div class="decor-coral"></div>`.
- `quiz-slide` e `exercise-slide` sempre acompanhados de `content-slide` na mesma `class`.
- `footer-bar` no formato `01 Tema curto`, sem hífen.
- `footer-page` crescente a partir de 3, sem pular nem repetir, terminando em 19 no slide de referências.
- O slide de referências leva `id="ref-slide"` e é o alvo dos `<a href="#/ref-slide" class="ref-badge">[N]</a>`.
- Nenhuma data em lugar nenhum.

- [ ] **Step 3: Rodar os três validadores de deck**

```bash
python3 tools/check_decks.py       aulas-1sem/aulas/aula01.html
python3 tools/check_slides.py      aulas-1sem/aulas/aula01.html
python3 tools/check_canto_coral.py aulas-1sem/aulas/aula01.html
```

Esperado: exit 0 nos três. Slide reportado em base 0: o slide 0 é a capa.

- [ ] **Step 4: Conferir na tela o que nenhum validador pega**

```bash
python3 -m http.server 8000 &
```

Abrir `http://localhost:8000/aulas-1sem/aulas/aula01.html` e verificar, slide a slide: as fontes Montserrat e JetBrains Mono carregaram, nenhuma alternativa de quiz está partida com buraco em volta de `<code>`, e nenhum bloco de código foi cortado na vertical.

- [ ] **Step 5: Commitar**

```bash
git add aulas-1sem/aulas/aula01.html
git commit -m "feat(aula01): deck de abertura do semestre, padrao-ouro do acervo"
```

---

## Task 14: Aula 01, kit de laboratório e habilitação do card

**Files:**
- Create: `aulas-1sem/labs/aula01-lab/README.md`
- Create: `aulas-1sem/labs/aula01-lab/index.html`
- Modify: `aulas-1sem/index.html`, o card `data-aula="1"`

**Interfaces:**
- Consumes: o deck da Task 13.
- Produces: o formato de kit que as Tasks 15 a 33 replicam, e o primeiro card habilitado do portal, que faz `check_portal.py` passar a executar GET real.

- [ ] **Step 1: Escrever o `README.md` do kit**

Seções obrigatórias:

1. **O passo do case que esta aula resolve**, ligado ao entregável da aula anterior. Na Aula 01 não há anterior: dizer que este é o ponto de partida.
2. **Pré-requisitos**: Java 21 LTS, Maven, Git e uma conta no GitHub.
3. **Passo a passo**, com os comandos exatos, incluindo o fork de `josercf/uninove-2026-2-rota-sul` e `./mvnw spring-boot:run`.
4. **Entregável**, com quantidade e critério, nunca vago.
5. **Critérios de aceitação em tabela**, obrigatória, uma linha por critério com a evidência que o professor confere:

```markdown
| Critério | Evidência conferida na correção |
|---|---|
| O fork existe na conta do aluno | URL `github.com/<usuario>/uninove-2026-2-rota-sul` responde |
| A aplicação sobe | `./mvnw spring-boot:run` imprime "Started RotaSulApplication" |
| O README do fork está preenchido | Nome completo e RA do aluno na primeira seção |
| O commit da aula existe | `git log` mostra um commit com a mensagem `chore: ambiente da aula 01` |
```

6. **Commit e push esperados** no fork do aluno.

- [ ] **Step 2: Criar o `index.html` do kit**

O GitHub Pages não faz listagem de diretório: sem este arquivo, o botão "Lab" do portal devolve 404 em produção.

```html
<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="refresh" content="0; url=https://github.com/josercf/uninove-2026-2-arquitetura-software/blob/main/aulas-1sem/labs/aula01-lab/README.md">
  <title>Laboratório da Aula 01, Arquitetura de Software, Uninove</title>
  <script>window.location.href = "https://github.com/josercf/uninove-2026-2-arquitetura-software/blob/main/aulas-1sem/labs/aula01-lab/README.md";</script>
</head>
<body style="font-family: sans-serif; text-align: center; padding-top: 50px; background-color: #00274D; color: #fff;">
  <h2>Redirecionando para o roteiro do laboratório da Aula 01</h2>
  <p>O roteiro completo vive no <code>README.md</code> deste diretório, exibido pelo GitHub. Caso o redirecionamento não ocorra, <a href="https://github.com/josercf/uninove-2026-2-arquitetura-software/blob/main/aulas-1sem/labs/aula01-lab/README.md" style="color: #C84B31;">clique aqui</a>.</p>
</body>
</html>
```

- [ ] **Step 3: Habilitar o card da Aula 01 no portal**

Em `aulas-1sem/index.html`, no `<article class="card" data-aula="1">`: tirar `disabled` da classe dos dois botões, tirar os dois `aria-disabled`, remover o `<span class="badge-producao">Em produção</span>` e pôr os `href`:

```html
<div class="card-acoes">
  <a class="btn" href="aulas/aula01.html">Slides</a>
  <a class="btn" href="labs/aula01-lab/">Lab</a>
</div>
```

- [ ] **Step 4: Rodar a suíte completa**

```bash
python3 -m pytest tests/ -v
python3 tools/check_decks.py       aulas-1sem/aulas/aula01.html
python3 tools/check_slides.py      aulas-1sem/aulas/aula01.html
python3 tools/check_canto_coral.py aulas-1sem/aulas/aula01.html
python3 tools/check_portal.py
```

Esperado: tudo verde. O `check_portal.py` agora faz GET real em `aulas/aula01.html` e em `labs/aula01-lab/`, e o segundo só passa por causa do `index.html` do Step 2.

- [ ] **Step 5: Commitar e confirmar o CI**

```bash
git add aulas-1sem/labs/aula01-lab aulas-1sem/index.html
git commit -m "feat(aula01): kit de laboratorio e card habilitado no portal"
GIT_SSH_COMMAND='ssh -i /Users/joseromualdocostafilho/.ssh/id_ed25519_josercf -o IdentitiesOnly=yes -F /dev/null' git push
gh run watch --exit-status
```

Esperado: CI verde e a Aula 01 acessível no portal publicado.

---

## Procedimento P: construir uma aula, da 02 à 20

As Tasks 15 a 33 são a mesma sequência de passos, com parâmetros diferentes. O procedimento está escrito uma única vez aqui, na íntegra. Cada task diz qual linha da tabela usar.

### Tabela de parâmetros

| Task | Aula | Módulo | Título | Fonte | Laboratório, ciclos 3 e 4 | Entregável |
|---|---|---|---|---|---|---|
| 15 | 02 | M1 | Padrões de projeto e frameworks: origem e distinção | `pdf/001.pdf` | Inventariar os frameworks e padrões que a Rota Sul vai usar, com a justificativa de cada escolha | `docs/decisoes.md` no fork, com uma linha por escolha e o motivo |
| 16 | 03 | M1 | Sistemas colaborativos | `pdf/002.pdf` | Mapear as interações da Rota Sul no modelo 3C, marcando o que é síncrono e o que é assíncrono | `docs/colaboracao-3c.md` com a tabela das interações classificadas |
| 17 | 04 | M1 | Arquitetura de sistemas colaborativos | `pdf/003.pdf` | Desenhar a arquitetura colaborativa em diagrama de componentes e de implantação | `docs/arquitetura/componentes.md` com os dois diagramas em Mermaid |
| 18 | 05 | M1 | Arquitetura de software e representação em UML | `pdf/004.pdf` | Formalizar os diagramas estruturais: classes do domínio e pacotes | `docs/arquitetura/dominio.md` com as 9 entidades e os pacotes |
| 19 | 06 | M1 | Arquitetura em 3 camadas e a evolução do MVC | `pdf/005.pdf` | Primeiro código: `PedidoController`, `PedidoService` e `PedidoRepository` em memória, com view Thymeleaf | Tela que lista pedidos, servida pelas três camadas separadas |
| 20 | 07 | M2 | Arquitetura orientada a serviços, SOA | `pdf/006.pdf` | Separar contrato de implementação: interface `PedidoService` com duas implementações trocáveis por perfil | Teste JUnit que roda a mesma suíte contra as duas implementações |
| 21 | 08 | M2 | Servidores de aplicação e a plataforma Java EE | `pdf/007.pdf` | Empacotar em JAR executável e comparar com o modelo WAR em servidor de aplicação | JAR rodando com `java -jar` e `docs/empacotamento.md` com a comparação |
| 22 | 09 | M2 | Metadados para troca de dados: XML e JSON | `pdf/008.pdf` | Serializar `Remessa` em JSON e em XML com Jackson, por content negotiation | Endpoint que responde os dois formatos conforme o header `Accept` |
| 23 | 10 | M2 | Objetos remotos: RMI, SOAP e REST | `pdf/009.pdf` | Consumir o parceiro legado por SOAP e expor a API REST de remessas | Cliente SOAP funcionando e a API REST documentada por springdoc-openapi |
| 24 | 11 | M3 | Design Patterns | `pdf/010.pdf` | Aplicar Strategy no cálculo de frete e Factory Method na criação de `Ocorrencia` | Os dois padrões implementados, cada um com teste JUnit |
| 25 | 12 | M3 | Frameworks: anatomia e inversão de controle | `pdf/011.pdf` | Injeção de dependência explícita e configuração por perfil `dev` e `prod` | Os dois perfis subindo com beans distintos, comprovado por log |
| 26 | 13 | M3 | Frameworks para aplicativos web | `pdf/012.pdf` | Camada de apresentação em Thymeleaf: layout, fragments e formulário de pedido | Tela de cadastro de pedido com validação de campo obrigatório |
| 27 | 14 | M3 | Frameworks para gerenciamento de dados | `pdf/013.pdf` | Trocar o repositório em memória por JDBC puro e medir o custo em linhas de código | Repositório JDBC com o mesmo contrato e a contagem antes e depois |
| 28 | 15 | M4 | API de persistência Java, JPA | `pdf/014.pdf` | Mapear as entidades com JPA, criar a migration inicial no Flyway e migrar para Spring Data | CRUD de `Pedido` persistindo no MySQL, com a migration versionada |
| 29 | 16 | M4 | Enterprise Java Beans | `pdf/015.pdf` | Transações com `@Transactional` no serviço, mais o comparativo lado a lado com EJB | Baixa de remessa transacional, com teste que comprova o rollback |
| 30 | 17 | M4 | Frameworks para software em 3 camadas | `pdf/016.pdf` | Consolidar as três camadas e cobrir com teste de integração em Testcontainers | Suíte de integração verde subindo MySQL em contêiner |
| 31 | 18 | M4 | Hibernate e JavaServer Faces | `pdf/017.pdf` | Relacionamentos, lazy loading e o problema N+1, mais o comparativo com JSF | Consulta com `join fetch` e a evidência do N+1 antes e depois |
| 32 | 19 | M5 | Montagem da aplicação distribuída | `pdf/018.pdf` | Quebrar em `pedidos-service`, `expedicao-service`, `rastreamento-service` e `portal-web`, subir com `compose.yaml` no Codespaces | URL pública do Codespaces respondendo, com a porta marcada como pública |
| 33 | 20 | M5 | Apresentação do projeto final | sem capítulo | Apresentação de 10 minutos por equipe e avaliação por pares | Apresentação feita e o repositório final entregue |

Nomes dos módulos, para o `lesson-bar`:

- M1: `Módulo 1, Fundamentos e sistemas colaborativos`
- M2: `Módulo 2, Integração e serviços distribuídos`
- M3: `Módulo 3, Padrões e frameworks`
- M4: `Módulo 4, Persistência e componentes`
- M5: `Módulo 5, Projeto final`

### Os passos

- [ ] **P1: Ler a seção da aula em `PLANEJAMENTO_AULA_A_AULA.md`**

Localizar `## Aula NN, Título`. É a fonte do conteúdo dos ciclos, do quiz e do laboratório. Ler também o PDF de origem indicado na coluna `Fonte`, em `/tmp/rota-sul-fontes/0NN.txt`, gerado na Task 4.

- [ ] **P2: Copiar o deck da Aula 01 como esqueleto**

```bash
cp aulas-1sem/aulas/aula01.html aulas-1sem/aulas/aulaNN.html
```

**Primeira edição, antes de qualquer outra:** trocar o número da aula no `<title>`, no `lesson-bar` e em todos os `footer-bar`. Deck copiado sem essa troca projeta "AULA 01" na frente da turma.

Remover os slides 4 a 8, que são exclusivos da abertura de semestre: apresentação do professor, metodologia, avaliação e os dois do case. Aulas 02 a 20 não os repetem.

- [ ] **P3: Escrever os slides**

Ordem canônica, com a numeração de `footer-page` recomeçando em 3:

```
 1  capa
 2  título, com AULA NN | Nome do módulo
 3  agenda com os horários dos quatro ciclos
 4  retomada do entregável da aula anterior, citado pelo nome
 5  ciclo 1, conceito
 6  ciclo 1, aprofundamento ou demonstração
 7  ciclo 2, conceito
 8  ciclo 2, aprofundamento ou demonstração
 9  quiz de fixação
10  ciclo 3, laboratório, passo 1
11  ciclo 3, laboratório, passo 2
12  ciclo 4, laboratório, passo 3
13  ciclo 4, entregável e critérios de aceitação
14  fechamento, commit, push e prévia da próxima aula
15  referências, com id="ref-slide"
16  encerramento com copyright
```

O número de slides por ciclo varia conforme o conteúdo. A ordem dos blocos e a presença do quiz, do fechamento, das referências e do encerramento não variam.

Regras que os validadores conferem:

- `<div class="decor-coral"></div>` em todo slide de conteúdo, quiz ou exercício.
- `class="quiz-slide content-slide"` e `class="exercise-slide content-slide"`, nunca só a primeira.
- Exatamente uma alternativa do quiz com `data-correct="true"`.
- Alternativa de quiz com `<code>` ou `<strong>` precisa do `<span class="option-text">` em volta do texto.
- `footer-bar` no formato `NN Tema curto`, com dois dígitos e sem hífen.
- `footer-page` crescente a partir de 3, sem pular nem repetir.
- `id="ref-slide"` no slide de referências, alvo dos `ref-badge`.
- O capítulo do AVA é sempre a referência [1] da aula.
- Nenhuma data em lugar nenhum do arquivo.

- [ ] **P4: Rodar os três validadores de deck**

```bash
python3 tools/check_decks.py       aulas-1sem/aulas/aulaNN.html
python3 tools/check_slides.py      aulas-1sem/aulas/aulaNN.html
python3 tools/check_canto_coral.py aulas-1sem/aulas/aulaNN.html
```

Esperado: exit 0 nos três. Se `check_slides.py` acusar estouro, **dividir o slide em dois**, nunca reduzir a fonte.

- [ ] **P5: Escrever o kit em `aulas-1sem/labs/aulaNN-lab/README.md`**

Mesmas seis seções da Task 14, Step 1, com a tabela de critérios de aceitação obrigatória. O passo do case é o da coluna `Laboratório` e o entregável é o da coluna `Entregável`. A primeira seção liga explicitamente ao entregável da aula anterior, pelo nome.

- [ ] **P6: Criar `aulas-1sem/labs/aulaNN-lab/index.html`**

Copiar o arquivo da Task 14, Step 2, e trocar **os dois tokens**: o número da aula nos três caminhos e o número no título. Sem este arquivo o botão "Lab" devolve 404 em produção.

- [ ] **P7: Habilitar o card no portal**

Em `aulas-1sem/index.html`, no `<article class="card" data-aula="N">`: tirar `disabled` da classe dos dois botões, tirar os dois `aria-disabled`, remover o `<span class="badge-producao">` e pôr `href="aulas/aulaNN.html"` e `href="labs/aulaNN-lab/"`.

- [ ] **P8: Rodar a suíte completa**

```bash
python3 -m pytest tests/ -v
python3 tools/check_decks.py       aulas-1sem/aulas/aula*.html
python3 tools/check_slides.py      aulas-1sem/aulas/aula*.html
python3 tools/check_canto_coral.py aulas-1sem/aulas/aula*.html
python3 tools/check_portal.py
```

Esperado: tudo verde, incluindo os decks das aulas anteriores. Rodar sobre todos, não só sobre o novo: habilitar um card quebra o portal se o kit estiver incompleto.

- [ ] **P9: Conferir na tela**

Abrir `http://localhost:8000/aulas-1sem/aulas/aulaNN.html` e percorrer os slides. Procurar as duas coisas que nenhum validador pega: alternativa de quiz partida com buraco em volta de elemento inline, e bloco de código cortado na vertical.

- [ ] **P10: Commitar**

```bash
git add aulas-1sem/aulas/aulaNN.html aulas-1sem/labs/aulaNN-lab aulas-1sem/index.html
git commit -m "feat(aulaNN): deck, kit de laboratorio e card habilitado"
```

---

## Tasks 15 a 33: as aulas 02 a 20

Cada uma destas tarefas executa o **Procedimento P** inteiro, dos passos P1 a P10, com os parâmetros da sua linha na tabela.

**Files** (substituindo `NN` pelo número da aula da linha correspondente):
- Create: `aulas-1sem/aulas/aulaNN.html`
- Create: `aulas-1sem/labs/aulaNN-lab/README.md`
- Create: `aulas-1sem/labs/aulaNN-lab/index.html`
- Modify: `aulas-1sem/index.html`, o card `data-aula="N"`

**Interfaces:**
- Consumes: o deck da Task 13 como esqueleto, a seção correspondente de `PLANEJAMENTO_AULA_A_AULA.md`, e o entregável da aula anterior, citado pelo nome no slide de retomada.
- Produces: o entregável da coluna `Entregável`, que a aula seguinte retoma pelo nome.

- [ ] **Task 15:** Aula 02, Padrões de projeto e frameworks: origem e distinção
- [ ] **Task 16:** Aula 03, Sistemas colaborativos
- [ ] **Task 17:** Aula 04, Arquitetura de sistemas colaborativos
- [ ] **Task 18:** Aula 05, Arquitetura de software e representação em UML
- [ ] **Task 19:** Aula 06, Arquitetura em 3 camadas e a evolução do MVC
- [ ] **Task 20:** Aula 07, Arquitetura orientada a serviços, SOA
- [ ] **Task 21:** Aula 08, Servidores de aplicação e a plataforma Java EE
- [ ] **Task 22:** Aula 09, Metadados para troca de dados: XML e JSON
- [ ] **Task 23:** Aula 10, Objetos remotos: RMI, SOAP e REST
- [ ] **Task 24:** Aula 11, Design Patterns
- [ ] **Task 25:** Aula 12, Frameworks: anatomia e inversão de controle
- [ ] **Task 26:** Aula 13, Frameworks para aplicativos web
- [ ] **Task 27:** Aula 14, Frameworks para gerenciamento de dados
- [ ] **Task 28:** Aula 15, API de persistência Java, JPA
- [ ] **Task 29:** Aula 16, Enterprise Java Beans
- [ ] **Task 30:** Aula 17, Frameworks para software em 3 camadas
- [ ] **Task 31:** Aula 18, Hibernate e JavaServer Faces
- [ ] **Task 32:** Aula 19, Montagem da aplicação distribuída
- [ ] **Task 33:** Aula 20, Apresentação do projeto final

Duas observações que valem para tarefas específicas:

- **Tasks 29 e 31** (Aulas 16 e 18) precisam de um slide de comparação lado a lado, EJB contra o componente Spring equivalente e JSF contra Thymeleaf, usando o bloco `side-by-side` do tema. O código Java EE aparece como leitura, e o laboratório constrói o equivalente Spring. Ver ADR-001.
- **Task 32** (Aula 19) precisa dizer com todas as letras, no deck e no kit, que a URL do Codespaces existe enquanto o codespace está rodando, que ele hiberna por inatividade, e que o aluno precisa iniciar o codespace antes da apresentação da Aula 20. O checklist de publicação inclui a linha "a porta está marcada como pública, e não privada".

---

## Task 34: Revisão final e publicação

**Files:**
- Modify: `.github/workflows/ci.yml`, remover as três guardas de acervo vazio
- Modify: `docs/ANDAMENTO.md`

**Interfaces:**
- Consumes: tudo.
- Produces: o acervo publicado.

- [ ] **Step 1: Rodar tudo, sobre tudo**

```bash
python3 -m pytest tests/ -v
python3 tools/check_decks.py       aulas-1sem/aulas/aula*.html
python3 tools/check_slides.py      aulas-1sem/aulas/aula*.html
python3 tools/check_canto_coral.py aulas-1sem/aulas/aula*.html
python3 tools/check_portal.py
```

Esperado: tudo verde, com 20 decks conferidos.

- [ ] **Step 2: Verificar as invariantes do acervo inteiro**

```bash
echo "--- travessao em dash, esperado: nada ---"
# docs/superpowers fica de fora: a spec e este plano contem o caractere dentro
# dos proprios comandos que o procuram, e casariam sempre.
grep -rn "—" --include="*.html" --include="*.md" \
  --exclude-dir=superpowers aulas-1sem/ docs/ *.md

echo "--- data escrita a mao em deck, esperado: nada ---"
grep -rnE "[0-9]{2}/[0-9]{2}/[0-9]{4}" aulas-1sem/aulas/

echo "--- residuo de turma, esperado: nada ---"
grep -rniE "turmas\.js|data-data-da-aula|uninove-turma" aulas-1sem/

echo "--- symlink, esperado: nada ---"
find . -type l -not -path "./.git/*"

echo "--- contagem, esperado: 20, 20, 20 ---"
ls aulas-1sem/aulas/aula*.html | wc -l
ls -d aulas-1sem/labs/aula*-lab | wc -l
ls aulas-1sem/labs/aula*-lab/index.html | wc -l

echo "--- card ainda desabilitado, esperado: nada ---"
grep -n "badge-producao\|btn disabled" aulas-1sem/index.html
```

- [ ] **Step 3: Endurecer o CI**

Em `.github/workflows/ci.yml`, remover as três guardas `if` que permitiam acervo sem deck e sem portal. A partir daqui, acervo sem os 20 decks é build vermelho.

- [ ] **Step 4: Atualizar o `docs/ANDAMENTO.md`**

Mover as 34 tarefas de "O que falta" para "Concluído", registrar a data de conclusão e as decisões tomadas durante a execução que não estavam na spec.

- [ ] **Step 5: Commitar, publicar e confirmar**

```bash
git add .github/workflows/ci.yml docs/ANDAMENTO.md
git commit -m "chore(acervo): endurece o CI e fecha o andamento das 20 aulas"
GIT_SSH_COMMAND='ssh -i /Users/joseromualdocostafilho/.ssh/id_ed25519_josercf -o IdentitiesOnly=yes -F /dev/null' git push
gh run watch --exit-status
```

Esperado: CI verde e o portal publicado em `https://josercf.github.io/uninove-2026-2-arquitetura-software/` com os 20 cards habilitados.

- [ ] **Step 6: Conferir a publicação de ponta a ponta**

Abrir o portal publicado e, para cada um dos 20 cards, clicar em "Slides" e em "Lab". Nenhum dos 40 links pode dar 404. O `check_portal.py` já testa isso localmente; este passo confere contra o GitHub Pages real, que é onde o aluno entra.
