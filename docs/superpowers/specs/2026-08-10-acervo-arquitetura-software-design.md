# Acervo didático de Arquitetura de Software, Uninove 2026.2

**Data:** 10/08/2026
**Status:** Aprovado
**Autor:** Prof. José Romualdo, com apoio do Claude Code

---

## 1. Objetivo

Construir o acervo didático completo da disciplina **Arquitetura de Software**,
Uninove, 2026.2, seguindo o padrão já estabelecido no acervo de
**Desenvolvimento Web** (`uninove-2026-2-desenvolvimento-web`): site estático
publicado no GitHub Pages, sem build e sem bundler, com decks Reveal.js
autocontidos, kits de laboratório e um portal que lista as aulas.

O conteúdo vem de 18 capítulos em PDF, extraídos do AVA da Uninove, de autoria do
Prof. Paulo Ricardo Batista Mesquita, hoje versionados em `pdf/001.pdf` a
`pdf/018.pdf`.

**Repositório:** `git@github.com:josercf/uninove-2026-2-arquitetura-software.git`,
branch `main`.

### O que está fora de escopo

- O repositório-esqueleto do case, `josercf/uninove-2026-2-rota-sul`. É outro
  repositório, com ciclo próprio, e não é criado por este trabalho.
- Exportação dos decks em PDF. Continua sendo `?print-pdf` no navegador, sob
  demanda, como no acervo de Desenvolvimento Web.
- Publicação dos PDFs do AVA no site. O diretório `pdf/` é fonte de trabalho e
  fica fora do artefato do GitHub Pages.

---

## 2. Parâmetros da disciplina

| Campo | Valor |
|---|---|
| Disciplina | Arquitetura de Software |
| Instituição | Uninove, Universidade Nove de Julho |
| Semestre | 2026.2 |
| Professor | José Romualdo |
| Turmas | Uma turma |
| Encontros | 20 encontros de 150 minutos |
| Estrutura do encontro | Quatro ciclos de 35, 35, 35 e 25 minutos, mais quiz de 10 e fechamento de 10 |
| Sala de aula invertida | Não. Cada encontro é autossuficiente |
| Case integrador | Rota Sul, plataforma de operações de uma transportadora |
| Stack do laboratório | Java 21, Spring Boot 3.x, Spring Data JPA sobre Hibernate, MySQL |

**Não há calendário.** A disciplina tem uma turma só e as datas dos encontros
não foram definidas. Consequência de projeto, detalhada na seção 6.2: o acervo
não tem módulo de resolução de turma, o portal não tem seletor de turma e
nenhum deck exibe data.

---

## 3. Mapa do semestre

Mapeamento **1 para 1 com a ordem do AVA**. A Aula 01 abre o semestre, as Aulas
02 a 19 cobrem os capítulos 01 a 18 na ordem em que foram escritos, e a Aula 20
é a apresentação do projeto final. A escolha preserva a rastreabilidade entre
cada aula e o capítulo correspondente do AVA, que o aluno acessa em paralelo.

| Módulo | Aula | Título | Capítulo |
|---|---|---|---|
| **M1** Fundamentos e sistemas colaborativos | 01 | Abertura do semestre e o problema da arquitetura | sem capítulo |
| | 02 | Padrões de projeto e frameworks: origem e distinção | 01 |
| | 03 | Sistemas colaborativos | 02 |
| | 04 | Arquitetura de sistemas colaborativos | 03 |
| | 05 | Arquitetura de software e representação em UML | 04 |
| | 06 | Arquitetura em 3 camadas e a evolução do MVC | 05 |
| **M2** Integração e serviços distribuídos | 07 | Arquitetura orientada a serviços, SOA | 06 |
| | 08 | Servidores de aplicação e a plataforma Java EE | 07 |
| | 09 | Metadados para troca de dados: XML e JSON | 08 |
| | 10 | Objetos remotos: RMI, SOAP e REST | 09 |
| **M3** Padrões e frameworks | 11 | Design Patterns | 10 |
| | 12 | Frameworks: anatomia e inversão de controle | 11 |
| | 13 | Frameworks para aplicativos web | 12 |
| | 14 | Frameworks para gerenciamento de dados | 13 |
| **M4** Persistência e componentes | 15 | API de persistência Java, JPA | 14 |
| | 16 | Enterprise Java Beans | 15 |
| | 17 | Frameworks para software em 3 camadas | 16 |
| | 18 | Hibernate e JavaServer Faces | 17 |
| **M5** Projeto final | 19 | Montagem da aplicação distribuída | 18 |
| | 20 | Apresentação do projeto final | sem capítulo |

### 3.1 Duas consequências assumidas

**A ordem do AVA trata de padrões e frameworks (Aula 02) antes de definir
arquitetura de software (Aula 05).** A alternativa seria puxar o capítulo 04
para a Aula 02, ganhando coerência conceitual e perdendo o casamento direto com
o AVA. A decisão é manter o AVA e resolver a lacuna com a espiral: a Aula 02
apresenta o vocabulário em nível de panorama e a Aula 05 formaliza o conceito.

**As Aulas 16 e 18 tratam de EJB, JSF e Hibernate, e a stack do laboratório é
Spring Boot.** Nessas duas aulas, EJB e JSF são conteúdo conceitual e histórico,
apresentados com código de leitura e comparação lado a lado com o equivalente
Spring; os ciclos 3 e 4 constroem o equivalente Spring, não escrevem EJB nem
JSF. Hibernate não tem esse problema: é o provedor JPA por baixo do Spring Data
e roda de verdade no laboratório.

---

## 4. O case Rota Sul

### 4.1 Mini mundo

Uma transportadora de médio porte opera com pedidos vindos de lojistas, um
armazém que monta remessas, frota própria na rota principal e transportadoras
parceiras na última milha. Cada peça tem hoje seu próprio sistema, e a
integração é feita por planilha e telefone. O resultado é pedido duplicado,
remessa sem rastreio, parceiro que não recebe a carga e cliente que liga para o
atendimento porque ninguém sabe onde está o volume.

### 4.2 Por que este case

Ele sustenta os três eixos da disciplina sem forçar nenhum:

- **Colaborativo**, para as Aulas 03 e 04. Expedidor, motorista, atendente e
  parceiro coordenam a mesma entrega. O painel de ocorrências compartilhado é
  cooperação síncrona; a fila de eventos entre serviços é coordenação
  assíncrona. O modelo 3C tem onde aterrissar.

  **Correção de 10/08/2026:** esta seção afirmava que o modelo 3C vinha "dos
  capítulos 02 e 03". Não vem. Os dois capítulos foram lidos por inteiro durante
  a Task 4 e nenhum deles apresenta o modelo. O 3C entra pela bibliografia do
  próprio capítulo 02, que cita Pimentel e Fucks, referência canônica de sistemas
  colaborativos no Brasil. A ancoragem é legítima e rastreável, mas o aluno não
  encontrará o 3C lendo o capítulo do AVA, e o material precisa dizer isso.
- **Distribuído e integrado**, para as Aulas 07 a 10. Serviços separados
  conversando por REST, um parceiro legado que só aceita SOAP com XML, e
  contratos de dados explícitos.
- **Em camadas com framework**, para as Aulas 11 a 19. Apresentação, negócio e
  persistência, com inversão de controle e ORM reais.

### 4.3 Atores e entidades

**Atores:** lojista, expedidor, motorista, atendente e transportadora parceira.

**Entidades:** `Cliente`, `Pedido`, `Remessa`, `Volume`, `Rota`, `Veiculo`,
`Motorista`, `Ocorrencia`, `Parceiro`.

### 4.4 Contrato técnico

Vale do começo ao fim do semestre. O aluno forka o repositório-esqueleto na Aula
01 e o primeiro código de aplicação entra na Aula 06, mas os nomes abaixo já
estão fixados desde o fork. Quem escrever uma aula nova herda daqui e não inventa
nome.

| O quê | Valor |
|---|---|
| JDK | Java 21 LTS |
| Build | Maven |
| Framework | Spring Boot 3.x |
| Pacote raiz | `br.uni9.rotasul` |
| Persistência | Spring Data JPA sobre Hibernate |
| Banco | MySQL 8.4, schema `rotasul` |
| Migrations | Flyway |
| Apresentação server-side | Thymeleaf |
| Contrato de API | springdoc-openapi |
| Integração legada | Spring Web Services, para o parceiro SOAP da Aula 10 |
| Testes | JUnit 5 e Testcontainers |
| Deploy | Docker Compose em GitHub Codespaces, com a porta encaminhada em modo público |
| Repositório-esqueleto | `josercf/uninove-2026-2-rota-sul`, forkado na Aula 01 e evoluído semana a semana |

Convenções de código que valem em todas as aulas:

- Textos, comentários e mensagens em português. Nomes de classe, método e
  pacote em inglês quando forem convenção do framework (`findById`,
  `PedidoRepository`), em português quando forem do domínio (`Remessa`,
  `Ocorrencia`).
- **Nunca fixar porta de `localhost` como se fosse universal.** Usar `8080`
  apenas como exemplo e escrever "a porta que o seu terminal imprimiu".
- Segredos e senha de banco vão para variável de ambiente, nunca para o
  repositório. O `.env` entra no `.gitignore` desde a Aula 01.

### 4.5 A forma distribuída, Aula 19

A Aula 19 monta a versão distribuída do case, com quatro processos subindo por
um único `compose.yaml`:

| Serviço | Papel |
|---|---|
| `pedidos-service` | Recebe e valida pedidos dos lojistas |
| `expedicao-service` | Monta remessas e volumes a partir dos pedidos |
| `rastreamento-service` | Registra eventos de rastreio e ocorrências |
| `portal-web` | Interface em Thymeleaf, consome os três por REST |

A limitação do GitHub Codespaces é dita em voz alta no deck e no kit: a URL
existe enquanto o codespace está rodando, ele hiberna por inatividade, e o aluno
precisa iniciar o codespace antes da apresentação da Aula 20. O checklist de
publicação inclui "a porta está marcada como pública, e não privada".

### 4.6 Aulas 01 a 05, laboratório sem código de aplicação

O Módulo 1 é conceitual: nenhuma das cinco primeiras aulas rende laboratório de
código de aplicação. Os ciclos 3 e 4 delas são de **ambiente e modelagem**, e
todo entregável é versionado no fork, para que a espiral funcione desde o
primeiro encontro.

| Aula | Entregável dos ciclos 3 e 4 |
|---|---|
| 01 | Ambiente pronto: JDK 21 e Maven instalados, fork do repositório-esqueleto clonado e o projeto Spring Boot vazio subindo |
| 02 | Inventário dos frameworks e padrões que a Rota Sul vai usar, com a justificativa de cada escolha, em `docs/decisoes.md` do fork |
| 03 | Mapeamento da Rota Sul no modelo 3C: que interação é comunicação, qual é coordenação e qual é cooperação, e quais são síncronas ou assíncronas |
| 04 | Diagrama UML de componentes e de implantação da arquitetura colaborativa da Rota Sul |
| 05 | Diagramas UML estruturais formalizados: classes do domínio e pacotes, revisando o que a Aula 04 esboçou |

O primeiro código de aplicação entra na Aula 06, quando as três camadas aparecem
e o Spring Boot deixa de estar vazio.

---

## 5. Estrutura do repositório

```
uninove-2026-2-arquitetura-software/
  CLAUDE.md                          instruções do repositório
  PLANO_DE_ENSINO.md                 ementa, objetivos, avaliação
  PLANEJAMENTO_AULA_A_AULA.md        roteiro minuto a minuto das 20 aulas
  README.md
  index.html                         redireciona para aulas-1sem/index.html
  .gitignore
  pdf/                               os 18 capítulos do AVA, fonte de trabalho
  docs/
    ANDAMENTO.md                     estado do trabalho entre sessões
    adrs/                            ADR-001 a ADR-005
    superpowers/specs/               esta spec
  aulas-1sem/
    SKILL.md                         metodologia e padrão de construção
    index.html                       portal com 20 cards
    aulas/aula01.html .. aula20.html
    labs/aula01-lab/ .. aula20-lab/  README.md, index.html e gabarito
    assets/css/uninove-theme.css
    assets/css/uninove-print.css
    assets/js/uninove-quiz.js
    assets/img/uninove-logo.png
    assets/img/code-bg.png
  tools/
    check_slides.py                  geometria, 1280x720 e sobreposição
    check_decks.py                   estrutura estática do HTML
    check_canto_coral.py             triângulo coral, pixel a pixel
    check_portal.py                  portal, cards e links
  tests/
    conftest.py
    fixtures/                        decks propositalmente quebrados
    test_check_decks.py
    test_check_portal.py
  .github/workflows/
    ci.yml                           pytest e os quatro validadores
    static.yml                       publicação no GitHub Pages
```

### 5.1 As três camadas de conteúdo

Herdadas do acervo de Desenvolvimento Web:

1. **Planejamento, na raiz.** `PLANO_DE_ENSINO.md` e
   `PLANEJAMENTO_AULA_A_AULA.md` são a fonte da verdade de títulos, escopo e
   avaliação. Deck e portal seguem o que estiver aqui.
2. **Metodologia, em `aulas-1sem/SKILL.md`.** A espiral de conteúdo, o case Rota
   Sul, a estrutura do encontro de 150 minutos e o padrão de construção de decks
   e kits.
3. **Materiais, em `aulas-1sem/`.** Portal, decks, kits e tema.

---

## 6. Decisões de projeto

Cada uma vira um ADR em `docs/adrs/`.

### 6.1 ADR-001: Spring Boot no lugar de Jakarta EE clássico

O material do AVA é fortemente Java EE: servidor de aplicação, EJB, JPA, JSF,
RMI e SOAP. O laboratório usa **Java 21 com Spring Boot**.

**Motivação:** cobre a ementa inteira com código que roda em qualquer máquina da
sala, sem instalar servidor de aplicação. Três camadas, inversão de controle,
JPA e Hibernate, REST, XML e JSON são todos exercitados de verdade. O
vocabulário dos capítulos é preservado, porque Spring Data JPA usa Hibernate e
fala a mesma linguagem.

**Risco:** o aluno que ler o capítulo do AVA vai encontrar `@Stateless` e
`@ManagedBean` que não aparecem no laboratório. **Mitigação:** as Aulas 16 e 18
trazem slides de comparação lado a lado, EJB contra o componente Spring
equivalente, e JSF contra Thymeleaf, dizendo explicitamente por que a indústria
migrou.

### 6.2 ADR-002: Sem resolução de turma e sem data no deck

Com uma turma só e nenhum calendário definido, o acervo **não tem** o módulo
`assets/js/turmas.js` do acervo de Desenvolvimento Web, o portal não tem seletor
de turma e nenhum deck exibe data.

O slide de título traz:

```html
<div class="lesson-bar">AULA XX &nbsp;|&nbsp; Módulo N, Nome do módulo</div>
```

e o `<h3>` com o nome do professor e o semestre, sem data.

**Consequência para a validação:** o `check_decks.py` deste acervo **inverte** a
regra do acervo de Desenvolvimento Web. Lá ele confere se `data-data-da-aula`
bate com o número no nome do arquivo; aqui ele **reprova qualquer data escrita à
mão** no deck, no formato `DD/MM/AAAA` ou por extenso. Data escrita à mão é o
defeito equivalente neste acervo, porque envelhece o material sem que ninguém
perceba.

### 6.3 ADR-003: Cópia, não symlink

O acervo de Desenvolvimento Web compartilha seis arquivos com o acervo da FIAP
por symlink relativo, o que causou o incidente do `tar --dereference` registrado
na ADR-006 daquele repositório. Aqui os quatro validadores e o tema são
**cópias**, e este acervo é autônomo.

**Motivação:** os validadores precisam divergir de qualquer forma, porque não há
regra de data nem de turma, e a regra nova (reprovar data escrita à mão) é
específica deste acervo. Um symlink que precisa ser sobrescrito não é um
symlink útil.

**Consequência negativa aceita:** correção de bug em validador não se propaga
sozinha entre os três acervos e precisa ser aplicada em cada um.

### 6.4 ADR-004: O case Rota Sul e o repositório-esqueleto único

Detalhado na seção 4. O ponto de decisão registrado no ADR é a escolha de um
único repositório-esqueleto evoluído semana a semana, em vez de um repositório
de laboratório por aula: o entregável de uma aula é o ponto de partida da
seguinte, e o aluno carrega um histórico só.

### 6.5 ADR-005: Mapeamento 1 para 1 com a ordem do AVA

Detalhado na seção 3, com as duas consequências assumidas em 3.1.

---

## 7. Anatomia do deck

Cada `aulas-1sem/aulas/aulaXX.html` é autocontido, mede exatamente 1280x720 e é
inicializado com `center: false, margin: 0`. A `section` tem altura travada: o
conteúdo não rola, e o que não couber quebra o slide visualmente sem lançar erro
no console. Consequência prática: **um conceito por slide**; quando não couber,
dividir em dois slides, nunca encolher a fonte.

### 7.1 Ordem canônica dos slides

```
capa
título com AULA XX e o módulo
agenda com os horários dos quatro ciclos
ciclo 1                                                 19h30 às 20h05
ciclo 2                                                 20h05 às 20h40
quiz de fixação                                         20h40 às 20h50
ciclo 3 de laboratório                                  20h50 às 21h25
ciclo 4 de laboratório e entregável                     21h25 às 21h50
fechamento                                              21h50 às 22h00
referências da aula, com id="ref-slide"
encerramento com copyright
```

O slide de referências é canônico, entre o fechamento e o encerramento: é o
alvo das citações `[N]` dos títulos, e por isso leva `id="ref-slide"`. Os 18
capítulos do AVA entram nas referências de cada aula, junto com a bibliografia
externa.

### 7.2 Esqueleto do arquivo

O `<head>` carrega, nesta ordem: `reveal.css`, tema `white.css`, `monokai.css`
do plugin de destaque, `uninove-theme.css` e `uninove-print.css`, mais o Google
Fonts com Montserrat e JetBrains Mono. O tema da Uninove precisa vir depois do
`white.css` para sobrescrevê-lo, e sem o Google Fonts o deck cai na fonte do
sistema.

```js
Reveal.initialize({
  width: 1280, height: 720, center: false, margin: 0,
  hash: true, slideNumber: false,
  controls: false, progress: false,
  pdfMaxPagesPerSlide: 1,
  plugins: [RevealHighlight],
});
```

`controls` e `progress` ficam desligados porque os controles do Reveal caem em
cima do rodapé do tema. `hash: true` dá URL própria a cada slide e faz
`href="#/ref-slide"` funcionar. `pdfMaxPagesPerSlide: 1` garante uma página por
slide no `?print-pdf`.

Não há módulo ES no fim do deck, porque não há resolução de turma. O único
script além do Reveal é `uninove-quiz.js`.

### 7.3 Classes e blocos

Tema copiado do acervo de Desenvolvimento Web, sem alteração de paleta:
`--uninove-azul: #00274D` e `--uninove-coral: #C84B31`.

**Classes de `section`:** `cover-slide`, `title-slide`, `content-slide`,
`section-slide`, `quiz-slide`, `exercise-slide`, `end-slide`.

`quiz-slide` e `exercise-slide` não têm regras próprias de `.top-bar`,
`.uninove-logo-header` nem `.slide-footer`. O padrão é sempre escrever
`class="quiz-slide content-slide"` e `class="exercise-slide content-slide"`.

**Blocos reutilizáveis:** `slide-title-area` com `accent-bar`, `top-bar`,
`uninove-logo-header`, `uninove-logo-full`, `title-card`, `lesson-bar`,
`slide-footer` com `footer-bar` e `footer-page`, `concept-cards` com
`concept-card`, `side-by-side` com `side`, `figure-split`, `slide-figure`,
`timeline`, `takeaway`, `callout`, `flow-diagram`, `exercise-container` com
`exercise-steps`, `code-compact`, `ref-badge` e `decor-coral`.

`.decor-coral` é o triângulo coral do canto superior direito. Precisa ser
escrito no HTML de cada slide de conteúdo, quiz ou exercício; ele não aparece
sozinho.

O `footer-bar` é o número da aula com dois dígitos, um espaço e o tema curto do
slide, sem hífen: `03 Modelo 3C`. O `footer-page` é a posição do slide no deck,
contada a partir de 1 com a capa como 1, crescente, sem pular nem repetir.

### 7.4 Quiz

Um quiz por aula, às 20h40. Markup de lista, com `data-correct` em cada `li` e
exatamente uma alternativa correta, e `quiz-feedback` carregando
`data-correct-msg` e `data-incorrect-msg`.

**Alternativa que contenha qualquer elemento inline, como `<code>` ou
`<strong>`, precisa ter o texto envolvido em `<span class="option-text">`.** A
`li` é `display: flex` com `gap: 12px`, então cada trecho solto vira um item de
flex e a frase se parte na projeção com 12px de buraco. Nenhum validador pega
isso; é disciplina do autor. Alternativa de texto puro dispensa o `span`.

---

## 8. O ciclo do artefato

Uma aula só está pronta quando os **quatro** artefatos existem:

1. **`aulas-1sem/aulas/aulaXX.html`**, o deck.
2. **`aulas-1sem/labs/aulaXX-lab/README.md`**, o kit, contendo: o passo do case
   que a aula resolve, ligado ao entregável da aula anterior; pré-requisitos e
   comandos; o entregável esperado com quantidade e critério; **critérios de
   aceitação em tabela**, uma linha por critério com a evidência que o professor
   confere; e a instrução de commit e push no fork do aluno.
3. **`aulas-1sem/labs/aulaXX-lab/index.html`**, redirecionamento para o
   `README.md` no GitHub. Obrigatório: o GitHub Pages não faz listagem de
   diretório, e sem esse arquivo o botão "Lab" do portal devolve 404 em
   produção.
4. **O card da aula habilitado em `aulas-1sem/index.html`**: tirar `disabled` da
   classe dos dois botões, tirar o `aria-disabled`, tirar o
   `<span class="badge-producao">` e pôr os dois `href`.

Sem os passos 3 e 4, a aula fica pronta em disco e invisível para a turma.

---

## 9. Validação e testes

Nenhuma aula é considerada pronta sem os quatro validadores passando. Eles
conferem coisas diferentes e nenhum substitui o outro.

| Validador | O que cobre |
|---|---|
| `check_slides.py` | Geometria no navegador: estouro de 1280x720 e sobreposição. Não olha o conteúdo do arquivo |
| `check_decks.py` | Estrutura estática do HTML: `decor-coral` faltando, `quiz-slide` sem `content-slide`, quiz com zero ou duas respostas certas, âncora `#/` sem `id` correspondente, `footer-page` fora de sequência, caminho relativo inexistente e **data escrita à mão** |
| `check_canto_coral.py` | O triângulo coral, pixel a pixel. Único que pega elemento opaco cobrindo a decoração |
| `check_portal.py` | Os 20 cards do portal e um GET real em cada botão habilitado |

Os três validadores de deck reportam o slide em **base 0**, a mesma base de
`Reveal.slide(i)`.

### 9.1 A suíte pytest

Os validadores são código, e código sem teste aprova o que não deveria. A suíte
em `tests/` valida os próprios validadores contra decks-fixture propositalmente
quebrados, um arquivo por defeito:

| Fixture | Defeito | Validador que precisa reprovar |
|---|---|---|
| `deck_ok.html` | Nenhum, deck mínimo válido | Todos aprovam |
| `deck_sem_decor_coral.html` | Slide de conteúdo sem `.decor-coral` | `check_decks` |
| `deck_quiz_sem_content_slide.html` | `quiz-slide` sem `content-slide` | `check_decks` |
| `deck_quiz_duas_corretas.html` | Duas alternativas com `data-correct="true"` | `check_decks` |
| `deck_quiz_sem_correta.html` | Nenhuma alternativa correta | `check_decks` |
| `deck_footer_fora_de_sequencia.html` | `footer-page` repetido ou pulado | `check_decks` |
| `deck_ancora_orfa.html` | `href="#/ref-slide"` sem o `id` correspondente | `check_decks` |
| `deck_caminho_quebrado.html` | `src` relativo que não existe no disco | `check_decks` |
| `deck_com_data_manual.html` | Data no formato `DD/MM/AAAA` no corpo do deck | `check_decks` |
| `portal_card_quebrado/` | Card habilitado apontando para arquivo inexistente | `check_portal` |

Cada teste afirma duas coisas: que o validador **reprova** a fixture quebrada
com código de saída diferente de zero, e que a mensagem de erro **nomeia o slide
e a regra**. Um validador que reprova pelo motivo errado é tão ruim quanto um
que aprova.

`check_slides.py` e `check_canto_coral.py` dependem de navegador e não entram na
suíte pytest; são exercitados no CI contra os decks reais.

### 9.2 CI

`.github/workflows/ci.yml` roda, a cada push e pull request:

1. `pytest tests/`
2. `python3 tools/check_decks.py` sobre todos os decks existentes
3. `python3 tools/check_portal.py`
4. `python3 tools/check_slides.py` e `python3 tools/check_canto_coral.py` sobre
   todos os decks, com o navegador instalado no runner

---

## 10. Publicação

`.github/workflows/static.yml` monta um diretório `_site` com `rsync`,
excluindo `.git`, `.github`, `.claude`, `tools`, `tests`, `docs`, `pdf`,
`node_modules` e `CLAUDE.md`, e envia só o que sobra para o
`upload-pages-artifact`. O `pdf/` fica de fora porque é material do AVA e não é
nosso para redistribuir.

O workflow tem um passo que roda `find _site -type l` e falha o build se sobrar
symlink, herdado do incidente registrado na ADR-006 do acervo de
Desenvolvimento Web. Como aqui não há symlink nenhum (ADR-003), esse passo é
uma rede de segurança contra regressão.

**Push:** o remote deste repositório usa o host `github.com`, que no
`~/.ssh/config` do professor autentica como `canaldoovidio`. Para publicar como
`josercf`:

```bash
GIT_SSH_COMMAND='ssh -i /Users/joseromualdocostafilho/.ssh/id_ed25519_josercf -o IdentitiesOnly=yes -F /dev/null' git push
```

---

## 11. Convenções editoriais

- Sem emojis em slides, títulos ou textos. O tom é profissional.
- Português do Brasil com acentuação completa.
- **Nunca usar travessão em dash.**
- Sem tom exagerado: nada de frases de efeito, punchlines ou metáforas
  amplificadoras. Títulos descritivos do conteúdo, afirmações diretas.
- Pesos de avaliação aparecem nos slides.
- Preferir diagramas e imagens didáticas a paredes de texto.
- Referências numeradas ao longo dos slides e consolidadas no slide final.
- Todo deck termina com o slide de copyright do Prof. José Romualdo.
- Commits em Conventional Commits, com escopo pela aula: `feat(aula01): ...`,
  `fix(portal): ...`.

---

## 12. Fases de execução

| Fase | Entrega | Critério de pronto |
|---|---|---|
| 1 | Fundação: `PLANO_DE_ENSINO.md`, `PLANEJAMENTO_AULA_A_AULA.md`, `SKILL.md`, `CLAUDE.md`, os cinco ADRs, tema copiado, `.gitignore`, `README.md`, `index.html` da raiz, os dois workflows | Repositório publica no GitHub Pages, ainda sem aulas |
| 2 | Os quatro validadores adaptados e a suíte pytest | `pytest tests/` verde antes de existir qualquer deck |
| 3 | Portal com os 20 cards, todos desabilitados | `check_portal.py` passa |
| 4 | Aula 01 completa, como padrão-ouro: deck, kit, `index.html` do lab, card habilitado | Os quatro validadores passam sobre a Aula 01 |
| 5 | Aulas 02 a 20, em lotes | Os quatro validadores passam sobre cada aula |
| 6 | Revisão final e publicação | CI verde, portal publicado com os 20 cards habilitados |

A Fase 2 vem antes de qualquer deck de propósito: um validador escrito depois de
20 decks tende a ser escrito para aprová-los.
