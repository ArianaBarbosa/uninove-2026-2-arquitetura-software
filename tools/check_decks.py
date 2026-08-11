#!/usr/bin/env python3
"""
Valida a estrutura de cada deck aulaXX.html, de forma estática.

POR QUE ESTE SCRIPT EXISTE
--------------------------
`check_slides.py` mede geometria e `check_canto_coral.py` mede pixel: os dois
abrem o navegador e olham como o slide ficou. Nenhum dos dois olha o CONTEÚDO
do arquivo. Com as Aulas 02 a 20 sendo produzidas a partir de cópias da Aula
01, os defeitos mais caros são justamente os que passam ilesos por geometria e
por pixel:

  - um `<div class="decor-coral">` esquecido não gera erro nenhum: o triângulo
    simplesmente não aparece, e o `check_canto_coral.py` pula o slide porque
    só confere slides que TÊM o elemento;
  - `class="quiz-slide"` sem `content-slide` perde a top-bar, a logo e o
    rodapé, porque o CSS só define essas barras para `content-slide`;
  - dois `data-correct="true"` no mesmo quiz fazem o script pintar duas
    respostas de verde;
  - `href="#/ref-slide"` sem o `id="ref-slide"` correspondente é um link morto;
  - rodapé fora de sequência depois de inserir ou remover um slide;
  - `src` ou `href` relativo apontando para arquivo que não existe dá 404 no
    GitHub Pages, que não faz listagem de diretório;
  - `<code>` solto dentro de uma alternativa de quiz parte a frase na
    projeção, porque a `li` é um contexto de flex (ADR-007). Este defeito
    escapou três vezes, em três decks diferentes, antes de virar checagem;
  - uma data escrita à mão, copiada por hábito de um deck anterior, envelhece
    o material sem que ninguém perceba, porque este acervo não tem calendário
    definido (ADR-002). O acervo de Desenvolvimento Web resolve turma por
    código e exige uma data correta no deck; aqui não existe resolução de
    turma, então a regra correspondente é a oposta, reprovar qualquer data
    escrita à mão;
  - o caminho mais provável de uma data entrar num deck deste acervo não é
    escrita à mão: é copiar um deck do acervo de Desenvolvimento Web trazendo
    junto o atributo `data-data-da-aula` e a referência a
    `assets/js/turmas.js` (SKILL.md seção 6 chama isso de "diferença número
    um" entre os dois acervos). Nesse caso a data é injetada em tempo de
    execução, não aparece como texto no HTML estático, e escaparia da
    checagem de data escrita à mão se não houvesse uma checagem própria para
    o atributo e para a referência ao script (ADR-002).

AS ONZE CHECAGENS
------------------
1. Toda `section` com classe `content-slide`, `quiz-slide` ou `exercise-slide`
   tem um `<div class="decor-coral">`.
2. Toda `quiz-slide` e `exercise-slide` também tem `content-slide` na lista de
   classes.
3. Todo `.quiz-container` tem exatamente um `data-correct="true"`.
4. Nenhuma alternativa de quiz tem elemento inline solto como filho direto da
   `<li>`: só `.option-letter` e `.option-text` são permitidos. A `li` é
   `display: flex` com `gap: 12px`, então um `<code>` solto vira item de flex
   próprio e a frase se parte com 12px de buraco de cada lado (ADR-007).
5. Toda âncora interna `href="#/..."` aponta para um `id` que existe no
   documento (índice numérico de slide, `#/7`, é aceito se estiver dentro da
   faixa de slides do deck).
6. Os `footer-page` formam sequência crescente, sem pular nem repetir.
7. Todo `src` e `href` relativo a arquivo local existe no disco. Diretório só
   conta como existente se tiver `index.html` dentro, porque é assim que o
   GitHub Pages se comporta.
8. Nenhuma data escrita à mão, no formato `DD/MM/AAAA` (dia e mês com um ou
   dois dígitos) ou por extenso, aparece no texto do deck (ADR-002).
9. Nenhum elemento carrega o atributo `data-data-da-aula` (ADR-002).
10. Nenhuma referência, em `src` ou em `import`, a `assets/js/turmas.js`
    (ADR-002).
11. Dentro de `aulas-1sem/aulas/`, o nome do arquivo segue `aulaXX.html`.
    Fora dessa pasta, a checagem não se aplica.

NUMERAÇÃO DOS SLIDES
--------------------
Os slides são reportados em BASE 0, a mesma base de `check_slides.py`,
`check_canto_coral.py` e `Reveal.slide(i)`. O primeiro slide do deck é o
slide 0.

Sai com código 1 e imprime aula, slide e problema se qualquer checagem falhar.

Uso:
    python3 tools/check_decks.py                       # todos os decks
    python3 tools/check_decks.py aulas-1sem/aulas/aula01.html

Não requer Playwright: lê o HTML direto do disco.
"""
import glob
import io
import os
import re
import sys
from html.parser import HTMLParser
from urllib.parse import unquote, urlparse

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PASTA_DECKS = os.path.join(RAIZ, "aulas-1sem", "aulas")

CLASSES_QUE_EXIGEM_DECOR = ("content-slide", "quiz-slide", "exercise-slide")
CLASSES_QUE_EXIGEM_CONTENT = ("quiz-slide", "exercise-slide")

# Atributos que carregam caminho de arquivo e precisam existir no disco.
ATRIBUTOS_DE_CAMINHO = ("src", "href")

# Esquemas que não apontam para arquivo local.
ESQUEMAS_EXTERNOS = ("http", "https", "mailto", "tel", "data", "javascript")

# Elementos sem tag de fechamento: não abrem nível de aninhamento.
TAGS_VAZIAS = (
    "area", "base", "br", "col", "embed", "hr", "img", "input",
    "link", "meta", "param", "source", "track", "wbr",
)

# Os únicos filhos diretos que uma alternativa de quiz pode ter. Qualquer
# outro elemento inline solto vira item de flex próprio (ADR-007).
FILHOS_PERMITIDOS_NA_ALTERNATIVA = ("option-letter", "option-text")


def classes_de(attrs):
    return (attrs.get("class") or "").split()


class LeitorDeDeck(HTMLParser):
    """Percorre o deck uma vez e recolhe tudo o que as checagens usam.

    As `section` dos decks nunca são aninhadas (o Reveal usa slides verticais
    aninhados, que este acervo não usa), então 'a seção atual' é sempre a
    última aberta.
    """

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.secoes = []          # uma entrada por slide, em ordem de documento
        self.ids = set()
        self.textos = []          # (texto, linha); usado pelas checagens de data
        self.quizzes = []         # {'secao', 'linha', 'corretas'}
        self.ancoras = []         # (alvo, linha, secao)
        self.caminhos = []        # (atributo, valor, linha, secao)
        self.rodapes = []         # (valor_texto, linha, secao)
        self.alternativas = []    # {'secao', 'linha', 'soltos'}
        self.atributos_data_da_aula = []  # linha de cada data-data-da-aula
        self._quiz_aberto = None
        self._capturando_rodape = None
        self._quiz_options_aberto = False
        self._li_aberta = None
        self._profundidade_na_li = 0

    # -- utilidades ------------------------------------------------------
    @property
    def secao_atual(self):
        return len(self.secoes) - 1 if self.secoes else None

    # -- eventos do parser -----------------------------------------------
    def handle_starttag(self, tag, attrs):
        self._processar_tag(tag, attrs)

    def handle_startendtag(self, tag, attrs):
        # <path ... /> dentro de SVG: conta como abertura, nunca abre bloco.
        self._processar_tag(tag, attrs, autofechada=True)

    def _processar_tag(self, tag, attrs, autofechada=False):
        attrs = {k: (v if v is not None else "") for k, v in attrs}
        linha = self.getpos()[0]
        classes = classes_de(attrs)

        if "id" in attrs and attrs["id"]:
            self.ids.add(attrs["id"])

        if tag == "section":
            self.secoes.append(
                {"linha": linha, "classes": classes, "decor": False}
            )
            self._quiz_aberto = None

        if "decor-coral" in classes and self.secao_atual is not None:
            self.secoes[self.secao_atual]["decor"] = True

        # -- alternativas de quiz (checagem 4) -----------------------------
        # Precisamos saber se um elemento inline é filho DIRETO da <li>: o que
        # está dentro do `.option-text` já é um item de flex só, e não quebra.
        if "quiz-options" in classes:
            self._quiz_options_aberto = True

        if self._quiz_options_aberto and tag == "li" and self._li_aberta is None:
            self._li_aberta = {
                "secao": self.secao_atual,
                "linha": linha,
                "soltos": [],
            }
            self._profundidade_na_li = 0
        elif self._li_aberta is not None:
            if self._profundidade_na_li == 0:
                permitido = any(
                    c in classes for c in FILHOS_PERMITIDOS_NA_ALTERNATIVA
                )
                if not permitido:
                    self._li_aberta["soltos"].append(tag)
            if not autofechada and tag not in TAGS_VAZIAS:
                self._profundidade_na_li += 1

        if "quiz-container" in classes:
            self._quiz_aberto = {
                "secao": self.secao_atual,
                "linha": linha,
                "corretas": 0,
            }
            self.quizzes.append(self._quiz_aberto)

        if attrs.get("data-correct") == "true" and self._quiz_aberto is not None:
            self._quiz_aberto["corretas"] += 1

        # -- resolução de turma reintroduzida (checagem 9) ------------------
        # Este acervo não tem resolução de turma (ADR-002). Se o atributo
        # aparece em qualquer elemento, é sinal de deck copiado do acervo de
        # Desenvolvimento Web sem remover o mecanismo.
        if "data-data-da-aula" in attrs:
            self.atributos_data_da_aula.append(linha)

        if "footer-page" in classes and not autofechada:
            self._capturando_rodape = {
                "texto": [],
                "linha": linha,
                "secao": self.secao_atual,
            }

        for atributo in ATRIBUTOS_DE_CAMINHO:
            valor = attrs.get(atributo)
            if not valor:
                continue
            if valor.startswith("#"):
                if atributo == "href":
                    self.ancoras.append((valor, linha, self.secao_atual))
                continue
            self.caminhos.append((atributo, valor, linha, self.secao_atual))

    def handle_data(self, data):
        if self._capturando_rodape is not None:
            self._capturando_rodape["texto"].append(data)
        # Texto colhido para as checagens 8 e 10 (data escrita à mão e
        # referência a turmas.js): guarda a linha de cada trecho não vazio,
        # para a mensagem de erro citar a linha. `<script>` também cai aqui,
        # porque o HTMLParser trata o conteúdo de `<script>` como dado, não
        # como marcação, e é lá que um `import ... from ".../turmas.js"`
        # apareceria.
        limpo = data.strip()
        if limpo:
            self.textos.append((limpo, self.getpos()[0]))

    def handle_endtag(self, tag):
        if self._li_aberta is not None:
            if self._profundidade_na_li > 0:
                if tag not in TAGS_VAZIAS:
                    self._profundidade_na_li -= 1
            elif tag == "li":
                self.alternativas.append(self._li_aberta)
                self._li_aberta = None
        if tag == "ul":
            self._quiz_options_aberto = False

        if self._capturando_rodape is not None and tag == "div":
            rodape = self._capturando_rodape
            self._capturando_rodape = None
            self.rodapes.append(
                ("".join(rodape["texto"]).strip(), rodape["linha"], rodape["secao"])
            )


# -- as onze checagens -----------------------------------------------------
def checar_decor_coral(leitor, erros, rotulo):
    for i, secao in enumerate(leitor.secoes):
        if not any(c in secao["classes"] for c in CLASSES_QUE_EXIGEM_DECOR):
            continue
        if not secao["decor"]:
            erros.append(
                "%s  slide %d (linha %d, class=%r): sem <div class=\"decor-coral\">; "
                "o triângulo coral não aparece e nenhum outro validador acusa"
                % (rotulo, i, secao["linha"], " ".join(secao["classes"]))
            )


def checar_content_slide_em_quiz_e_exercicio(leitor, erros, rotulo):
    for i, secao in enumerate(leitor.secoes):
        for classe in CLASSES_QUE_EXIGEM_CONTENT:
            if classe in secao["classes"] and "content-slide" not in secao["classes"]:
                erros.append(
                    "%s  slide %d (linha %d): class=%r sem 'content-slide'; sem "
                    "ela o slide perde top-bar, logo e rodapé, que só existem "
                    "no CSS de .content-slide"
                    % (rotulo, i, secao["linha"], " ".join(secao["classes"]))
                )


def checar_quiz_com_uma_resposta(leitor, erros, rotulo):
    for quiz in leitor.quizzes:
        if quiz["corretas"] != 1:
            erros.append(
                "%s  slide %s (linha %d): .quiz-container com %d "
                "data-correct=\"true\", esperado exatamente 1"
                % (rotulo, quiz["secao"], quiz["linha"], quiz["corretas"])
            )


def checar_alternativas_sem_inline_solto(leitor, erros, rotulo):
    """Checagem 4: alternativa de quiz não pode ter elemento inline solto.

    `.quiz-slide .quiz-options li` é `display: flex` com `gap: 12px`. Cada
    trecho de texto solto e cada elemento inline vira um item de flex
    separado, então um `<code>` no meio da alternativa ganha 12px de buraco de
    cada lado, no lugar onde deveria haver um espaço normal, e a frase se parte
    na projeção. A saída é envolver o texto em `<span class="option-text">`.

    Nada disso estoura os 1280x720 nem sobrepõe bloco, então `check_slides.py`
    aprova. O defeito apareceu três vezes, em três decks diferentes, antes de
    virar esta checagem. Ver ADR-007.
    """
    for alt in leitor.alternativas:
        if not alt["soltos"]:
            continue
        tags = ", ".join("<%s>" % t for t in sorted(set(alt["soltos"])))
        erros.append(
            "%s  slide %s (linha %d): alternativa de quiz com %s solto fora de "
            "<span class=\"option-text\">; a li é display:flex com gap:12px, "
            "então o trecho vira item próprio e a frase se parte na projeção "
            "(ADR-007)" % (rotulo, alt["secao"], alt["linha"], tags)
        )


def checar_ancoras_internas(leitor, erros, rotulo):
    total_de_slides = len(leitor.secoes)
    for alvo, linha, secao in leitor.ancoras:
        if not alvo.startswith("#/"):
            continue
        destino = alvo[2:].strip("/")
        if not destino:
            continue
        if destino.isdigit():
            if int(destino) >= total_de_slides:
                erros.append(
                    "%s  slide %s (linha %d): href=%r aponta para o slide %s, "
                    "mas o deck tem %d slides"
                    % (rotulo, secao, linha, alvo, destino, total_de_slides)
                )
            continue
        if destino not in leitor.ids:
            erros.append(
                "%s  slide %s (linha %d): href=%r não encontra nenhum id=%r no "
                "documento"
                % (rotulo, secao, linha, alvo, destino)
            )


def checar_sequencia_dos_rodapes(leitor, erros, rotulo):
    anterior = None
    for texto, linha, secao in leitor.rodapes:
        if not texto.isdigit():
            erros.append(
                "%s  slide %s (linha %d): footer-page com %r, que não é um número"
                % (rotulo, secao, linha, texto)
            )
            continue
        numero = int(texto)
        if anterior is not None and numero != anterior + 1:
            erros.append(
                "%s  slide %s (linha %d): footer-page %d vem depois de %d; a "
                "sequência %s"
                % (
                    rotulo,
                    secao,
                    linha,
                    numero,
                    anterior,
                    "repete" if numero == anterior
                    else ("retrocede" if numero < anterior else "pula"),
                )
            )
        anterior = numero


def checar_caminhos_locais(leitor, caminho_do_deck, erros, rotulo):
    base = os.path.dirname(os.path.abspath(caminho_do_deck))
    for atributo, valor, linha, secao in leitor.caminhos:
        if valor.startswith("//"):
            continue
        esquema = urlparse(valor).scheme.lower()
        if esquema in ESQUEMAS_EXTERNOS:
            continue
        if esquema:
            continue
        relativo = unquote(valor.split("#")[0].split("?")[0])
        if not relativo:
            continue
        if os.path.isabs(relativo):
            alvo = os.path.join(RAIZ, relativo.lstrip("/"))
        else:
            alvo = os.path.normpath(os.path.join(base, relativo))
        if os.path.isdir(alvo):
            if os.path.isfile(os.path.join(alvo, "index.html")):
                continue
            erros.append(
                "%s  slide %s (linha %d): %s=%r aponta para um diretório sem "
                "index.html; o GitHub Pages devolve 404, porque não faz "
                "listagem de diretório"
                % (rotulo, secao, linha, atributo, valor)
            )
            continue
        if not os.path.isfile(alvo):
            erros.append(
                "%s  slide %s (linha %d): %s=%r não existe no disco (%s)"
                % (rotulo, secao, linha, atributo, valor,
                   os.path.relpath(alvo, RAIZ))
            )


# Datas em deck envelhecem o material sem que ninguém perceba, e esta
# disciplina não tem calendário definido. Ver ADR-002.
#
# `\d{1,2}` nos dois primeiros campos, não `\d{2}`: dia e mês de um dígito são
# escrita brasileira comum ("2/8/2026", "12/8/2026"), e a versão anterior com
# `\d{2}` fixo deixava passar exatamente esses formatos, que é o defeito mais
# provável de aparecer. O sufixo obrigatório `/\d{4}` evita falso positivo em
# proporção ("16/9"), fração ("2/3 dos casos") ou faixa numérica ("404/500",
# "8080/8090", "50/50"): nenhum desses tem um segundo "/" seguido de quatro
# dígitos.
PADRAO_DATA_NUMERICA = re.compile(r"\b\d{1,2}/\d{1,2}/\d{4}\b")
MESES = (
    "janeiro|fevereiro|marco|março|abril|maio|junho|julho|agosto|setembro|"
    "outubro|novembro|dezembro"
)
PADRAO_DATA_POR_EXTENSO = re.compile(
    rf"\b\d{{1,2}}\s+de\s+({MESES})\b", re.IGNORECASE
)

# O módulo do acervo de Desenvolvimento Web que injeta data-data-da-aula em
# tempo de execução. Ver ADR-002 e SKILL.md seção 6 ("diferença número um").
REFERENCIA_A_TURMAS_JS = "assets/js/turmas.js"


def checar_sem_data_manual(leitor, erros, rotulo):
    """Checagem 8: nenhuma data escrita à mão no texto do deck. Ver ADR-002."""
    for texto, linha in leitor.textos:
        for padrao in (PADRAO_DATA_NUMERICA, PADRAO_DATA_POR_EXTENSO):
            achado = padrao.search(texto)
            if achado:
                erros.append(
                    "%s  linha %d: data escrita à mão, %r; apague a data, "
                    "este acervo não tem calendário definido e nenhum deck "
                    "exibe data. Ver ADR-002."
                    % (rotulo, linha, achado.group(0))
                )


def checar_sem_atributo_data_da_aula(leitor, erros, rotulo):
    """Checagem 9: nenhum elemento carrega data-data-da-aula. Ver ADR-002.

    Esse atributo não aparece como texto: é o próprio mecanismo de resolução
    de turma do acervo de Desenvolvimento Web, que injeta a data em tempo de
    execução via `assets/js/turmas.js`. Um deck copiado de lá sem remover o
    mecanismo escaparia da checagem 8, que só lê texto.
    """
    for linha in leitor.atributos_data_da_aula:
        erros.append(
            "%s  linha %d: atributo data-data-da-aula presente; remova-o, "
            "este acervo não resolve turma e a data que ele carregaria nunca "
            "apareceria como texto no HTML. Ver ADR-002."
            % (rotulo, linha)
        )


def checar_sem_referencia_a_turmas_js(leitor, erros, rotulo):
    """Checagem 10: nenhuma referência a assets/js/turmas.js. Ver ADR-002.

    Cobre as duas formas de trazer o módulo para o deck: um `src`/`href`
    apontando para o arquivo (checado em `leitor.caminhos`, preenchido pela
    checagem 7) e um `import ... from ".../turmas.js"` dentro de
    `<script type="module">`, que é texto, não atributo (checado em
    `leitor.textos`).
    """
    for atributo, valor, linha, secao in leitor.caminhos:
        if REFERENCIA_A_TURMAS_JS in valor:
            erros.append(
                "%s  slide %s (linha %d): %s=%r referencia turmas.js; remova "
                "o script, este acervo não tem módulo de resolução de "
                "turma. Ver ADR-002."
                % (rotulo, secao, linha, atributo, valor)
            )
    for texto, linha in leitor.textos:
        if REFERENCIA_A_TURMAS_JS in texto:
            erros.append(
                "%s  linha %d: import referenciando turmas.js; remova a "
                "importação, este acervo não tem módulo de resolução de "
                "turma. Ver ADR-002."
                % (rotulo, linha)
            )


def checar_nome_do_arquivo(caminho, erros, rotulo):
    """Checagem 11: dentro de aulas-1sem/aulas/, o nome segue aulaXX.html.

    Não é gate: roda depois de todas as outras checagens e só se aplica a
    arquivo dentro da pasta de decks publicados. Fixture de teste, arquivo
    fora dessa pasta, fica isento, porque o padrão de nome é convenção de
    publicação (o portal monta o `href` a partir dele), não requisito
    estrutural do deck.
    """
    pasta_do_arquivo = os.path.dirname(os.path.abspath(caminho))
    if pasta_do_arquivo != os.path.abspath(PASTA_DECKS):
        return
    if not re.match(r"^aula\d+\.html$", os.path.basename(caminho)):
        erros.append(
            "%s: nome fora do padrão aulaXX.html; renomeie o arquivo, é dele "
            "que o card do portal e o glob de check_decks.py dependem"
            % rotulo
        )


def checar_deck(caminho, erros):
    rotulo = os.path.basename(caminho)

    leitor = LeitorDeDeck()
    leitor.feed(io.open(caminho, encoding="utf-8").read())
    leitor.close()

    antes = len(erros)
    checar_decor_coral(leitor, erros, rotulo)
    checar_content_slide_em_quiz_e_exercicio(leitor, erros, rotulo)
    checar_quiz_com_uma_resposta(leitor, erros, rotulo)
    checar_alternativas_sem_inline_solto(leitor, erros, rotulo)
    checar_ancoras_internas(leitor, erros, rotulo)
    checar_sequencia_dos_rodapes(leitor, erros, rotulo)
    checar_caminhos_locais(leitor, caminho, erros, rotulo)
    checar_sem_data_manual(leitor, erros, rotulo)
    checar_sem_atributo_data_da_aula(leitor, erros, rotulo)
    checar_sem_referencia_a_turmas_js(leitor, erros, rotulo)
    checar_nome_do_arquivo(caminho, erros, rotulo)

    novos = len(erros) - antes
    print(
        "\n%s  (%d slides, %d quiz, %d rodapés)"
        % (rotulo, len(leitor.secoes), len(leitor.quizzes), len(leitor.rodapes))
    )
    if novos:
        print("  %d problema(s):" % novos)
        for erro in erros[antes:]:
            print("  - %s" % erro)
    else:
        print("  OK: as onze checagens estruturais passaram")
    return novos


def main():
    alvos = [a for a in sys.argv[1:] if not a.startswith("--")]
    if not alvos:
        alvos = sorted(glob.glob(os.path.join(PASTA_DECKS, "aula*.html")))
    if not alvos:
        print("Nenhum deck encontrado em %s" % os.path.relpath(PASTA_DECKS, RAIZ))
        return 1

    erros = []
    for alvo in alvos:
        checar_deck(alvo, erros)

    print("\n" + "=" * 62)
    if erros:
        print("%d problema(s) estrutural(is) em %d deck(s)." % (len(erros), len(alvos)))
        return 1
    print("Estrutura correta nos %d deck(s) conferido(s)." % len(alvos))
    return 0


if __name__ == "__main__":
    sys.exit(main())
