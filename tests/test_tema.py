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
