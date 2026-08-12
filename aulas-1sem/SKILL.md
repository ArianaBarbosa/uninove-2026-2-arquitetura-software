---
name: arquitetura-course-design
description: Metodologia e padrão de construção das aulas de Arquitetura de Software da Uninove 2026.2. Inclui a espiral de conteúdo, o case Rota Sul, a estrutura do encontro de 150 minutos em quatro ciclos, o padrão dos decks Reveal.js com tema Uninove e o padrão dos kits de laboratório.
---

# Arquitetura Course Design Skill: Metodologia e Construção das Aulas de Arquitetura de Software

Este guia consolida a metodologia pedagógica e os padrões técnicos de construção
do acervo da disciplina **Arquitetura de Software**, Uninove, 2026.2, Prof. José
Romualdo. Uma turma, 20 encontros de 150 minutos cada.

Este documento é a fonte da verdade de metodologia e padrão de construção. Para
títulos, escopo e conteúdo de cada encontro, a fonte é
`PLANEJAMENTO_AULA_A_AULA.md`; para ementa, cronograma e avaliação,
`PLANO_DE_ENSINO.md`. Quem escreve um deck ou um kit lê primeiro a seção
correspondente do planejamento e depois este documento para saber como
transformar aquele conteúdo em HTML.

---

## 1. Pilares metodológicos

A construção das aulas se apoia em dois pilares integrados.

### 1.1 Aprendizagem em espiral

Nenhum tópico técnico se esgota em uma única aula. Toda aula a partir da Aula
02 **abre retomando explicitamente a aula anterior** e acrescenta uma camada
nova sobre o que já existe. Ao montar a aula N, cite pelo nome o entregável da
aula N-1: o aluno precisa reconhecer o que construiu antes de avançar.

```
Aula 02  inventário de frameworks e padrões da Rota Sul, em docs/decisoes.md
   └─ Aula 03  o inventário ganha o mapeamento das interações no modelo 3C
        └─ Aula 04  as interações viram diagrama de componentes e de implantação
             └─ Aula 05  os diagramas ganham a notação UML formal e o de classes
```

A Aula 01 é a única sem retomada, porque é o primeiro encontro do semestre. Em
seu lugar entra a abertura: apresentação do professor, metodologia, avaliação
e o case.

### 1.2 Aprendizagem por case: Rota Sul

Todo exemplo, laboratório e quiz do semestre orbita um único case, a **Rota
Sul**. Não há exercícios de tema genérico soltos ao longo do curso. A seção 5
deste documento detalha o mini mundo, os atores, as entidades e o contrato
técnico. Aqui fica registrado apenas o essencial do pilar: o case nasce
conceitual, sem código de aplicação, nas Aulas 01 a 05, ganha as três camadas
com o primeiro código na Aula 06, avança por integração e padrões nas Aulas 07
a 18 e termina distribuído em quatro processos na Aula 19, apresentado na Aula
20.

- **Repositório único:** diferente de um laboratório por aula, existe um único
  repositório-esqueleto, `josercf/uninove-2026-2-rota-sul`, que o aluno forka
  na Aula 01 e evolui semana a semana. Os diretórios em `aulas-1sem/labs/` são
  a referência e o gabarito do professor para cada etapa, não repositórios
  independentes.

---

## 2. Sem sala de aula invertida

A disciplina **não usa sala de aula invertida**. Não há atividade pré-aula,
não há leitura antecipada e nenhum conteúdo é cobrado antes de ter sido
apresentado em sala. Cada encontro é **autossuficiente**: tudo o que o aluno
precisa para acompanhar a aula chega dentro dela mesma.

Consequência para quem escreve o planejamento e o deck: nenhuma seção de aula
pode conter a frase "o aluno deve ter lido" nem equivalente. O capítulo do AVA
correspondente é indicado como leitura complementar nas referências, nunca
como pré-requisito.

---

## 3. Estrutura do encontro de 150 minutos

Cada encontro tem 150 minutos corridos, sem intervalo formal, organizados em
quatro ciclos de 35, 35, 35 e 25 minutos, mais quiz e fechamento de 10 minutos
cada:

| Bloco | Horário | Duração | Natureza |
|---|---|---|---|
| Ciclo 1 | 19h30 às 20h05 | 35 min | Conceito, demonstração, exercício curto |
| Ciclo 2 | 20h05 às 20h40 | 35 min | Conceito, demonstração, exercício curto |
| Quiz | 20h40 às 20h50 | 10 min | Fixação, uma pergunta com quatro alternativas |
| Ciclo 3 | 20h50 às 21h25 | 35 min | Laboratório guiado, parte 1 |
| Ciclo 4 | 21h25 às 21h50 | 25 min | Laboratório, parte 2, e o entregável |
| Fechamento | 21h50 às 22h00 | 10 min | Commit, push e prévia da próxima aula |

- **A retomada ocupa os cinco primeiros minutos do Ciclo 1**, que por isso
  entra no conceito por volta de 19h35.
- **Ciclos 1 e 2** seguem sempre o mesmo ritmo interno: o professor apresenta
  o conceito, demonstra ao vivo no projetor e o aluno reproduz num exercício
  curto, ainda dentro do ciclo.
- **O quiz de fixação**, às 20h40, quebra o ritmo entre a teoria dos dois
  primeiros ciclos e o laboratório dos dois últimos.
- **Ciclos 3 e 4** são laboratório: o aluno constrói uma etapa concreta do
  case com o professor circulando pela sala. O entregável nasce dentro do
  Ciclo 4, não fora da aula.
- **O fechamento** inclui o commit e o push do trabalho do dia no fork do
  aluno, mais a prévia da aula seguinte.

Não há intervalo: a própria troca de ciclo, a cada 35 minutos aproximadamente,
funciona como o respiro da aula.

---

## 4. Eixos de conteúdo da disciplina

Toda aula se encaixa em um destes cinco módulos, que avançam em espiral ao
longo do semestre, mapeados 1 para 1 com a ordem dos 18 capítulos do AVA:

1. **M1, Fundamentos e sistemas colaborativos** (Aulas 01 a 06): o problema da
   arquitetura, padrões de projeto e frameworks, sistemas colaborativos e o
   modelo 3C, arquitetura de sistemas colaborativos, arquitetura de software e
   representação em UML, arquitetura em três camadas e a evolução do MVC.
2. **M2, Integração e serviços distribuídos** (Aulas 07 a 10): arquitetura
   orientada a serviços, servidores de aplicação e a plataforma Java EE,
   metadados para troca de dados em XML e JSON, objetos remotos com RMI, SOAP
   e REST.
3. **M3, Padrões e frameworks** (Aulas 11 a 14): design patterns, anatomia de
   frameworks e inversão de controle, frameworks para aplicativos web,
   frameworks para gerenciamento de dados.
4. **M4, Persistência e componentes** (Aulas 15 a 18): a API de persistência
   Java (JPA), Enterprise Java Beans, frameworks para software em três
   camadas, Hibernate e JavaServer Faces.
5. **M5, Projeto final** (Aulas 19 e 20): montagem da aplicação distribuída,
   apresentação do projeto final.

**Duas consequências assumidas** nessa ordem, herdadas do AVA e não corrigidas
por conveniência didática:

- A ordem trata de padrões e frameworks (Aula 02) antes de definir
  arquitetura de software (Aula 05). A Aula 02 apresenta o vocabulário em
  nível de panorama e a Aula 05 formaliza o conceito; é a espiral resolvendo a
  lacuna, não um erro de sequência.
- As Aulas 16 e 18 tratam de EJB, JSF e Hibernate, e a stack do laboratório é
  Spring Boot. Nessas duas aulas, EJB e JSF são conteúdo conceitual e
  histórico, apresentado com código de leitura e comparação lado a lado com o
  equivalente Spring; os ciclos 3 e 4 constroem o equivalente Spring, não
  escrevem EJB nem JSF. Hibernate não tem esse problema: é o provedor JPA por
  baixo do Spring Data e roda de verdade no laboratório.

---

## 5. O case Rota Sul

### 5.1 Mini mundo

Uma transportadora de médio porte opera com pedidos vindos de lojistas, um
armazém que monta remessas, frota própria na rota principal e transportadoras
parceiras na última milha. Cada peça tem hoje seu próprio sistema, e a
integração é feita por planilha e telefone. O resultado é pedido duplicado,
remessa sem rastreio, parceiro que não recebe a carga e cliente que liga para
o atendimento porque ninguém sabe onde está o volume.

### 5.2 Por que este case

Ele sustenta os três eixos da disciplina sem forçar nenhum:

- **Colaborativo**, para as Aulas 03 e 04. Expedidor, motorista, atendente e
  parceiro coordenam a mesma entrega. O painel de ocorrências compartilhado é
  cooperação síncrona; a fila de eventos entre serviços é coordenação
  assíncrona. O modelo 3C tem onde aterrissar. O 3C entra pela bibliografia do
  próprio capítulo 02, que cita Pimentel e Fucks, referência canônica de
  sistemas colaborativos no Brasil: o aluno não encontra o modelo lendo o
  capítulo do AVA, e o material precisa dizer isso.
- **Distribuído e integrado**, para as Aulas 07 a 10. Serviços separados
  conversando por REST, um parceiro legado que só aceita SOAP com XML, e
  contratos de dados explícitos.
- **Em camadas com framework**, para as Aulas 11 a 19. Apresentação, negócio e
  persistência, com inversão de controle e ORM reais.

### 5.3 Atores e entidades

**Atores:** lojista, expedidor, motorista, atendente e transportadora
parceira.

**Entidades:** `Cliente`, `Pedido`, `Remessa`, `Volume`, `Rota`, `Veiculo`,
`Motorista`, `Ocorrencia`, `Parceiro`.

Esses nomes valem o semestre inteiro e não mudam. Quem escreve uma aula nova
não inventa entidade nem ator fora desta lista.

### 5.4 Contrato técnico

Vale do começo ao fim do semestre. O aluno forka o repositório-esqueleto na
Aula 01 e o primeiro código de aplicação entra na Aula 06, mas os nomes abaixo
já estão fixados desde o fork. Quem escrever uma aula nova herda daqui e não
inventa nome.

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
- **Convenção de pacotes, fixada na Aula 05 e válida o semestre inteiro:**
  `br.uni9.rotasul.<contexto>.<camada>`, com os contextos `pedido`,
  `expedicao` e `rastreamento`, e as camadas `web`, `service`, `repository` e
  `domain`.

### 5.5 Diagramas: PlantUML

A ferramenta de diagrama do case é o **PlantUML**, decisão do professor, com a
imagem embutida no `.md` pelo proxy do `plantuml.com`. A regra vale da Aula 04
em diante. O motivo é a notação: esta é uma disciplina cuja Aula 05 se chama
"Arquitetura de software e representação em UML", e o PlantUML tem as
notações nativas de que os capítulos falam, `component` para componentes,
`node` em diagrama de implantação, `package` para pacotes e `class` para
classes. Ferramenta sem essas notações obriga a aproximar componente de
fluxograma, e aí o aluno confunde ferramenta com notação.

Cada diagrama entregue pelo aluno são **dois arquivos** em
`docs/arquitetura/` do fork: o `.puml` com a fonte, que é a fonte de verdade
versionada, e um `.md` irmão que embute a imagem pelo proxy oficial,
apontando para o `raw` do fork do próprio aluno:

```markdown
![Diagrama de componentes da Rota Sul](https://www.plantuml.com/plantuml/proxy?cache=no&src=https://raw.githubusercontent.com/SEU_USUARIO/uninove-2026-2-rota-sul/main/docs/arquitetura/componentes.puml)
```

**Duas limitações desse mecanismo, que o roteiro manda declarar em sala nas
Aulas 04 e 05:**

- A imagem depende de um serviço externo, o `plantuml.com`. Se ele cair, a
  imagem some do `.md`, mas o `.puml` versionado continua sendo a fonte de
  verdade.
- O proxy só consegue ler a fonte se o repositório do aluno for **público**.
  Fork privado quebra a imagem, mesmo com o `.puml` correto.

**Duas armadilhas de sintaxe já custaram tempo de aula e precisam ser
evitadas por quem escreve o material:**

- `device` não aceita bloco com chaves. Escrever `device "Nome" { ... }` falha
  de sintaxe. A forma correta é `node "Nome" as apelido <<device>> { ... }`,
  com o estereótipo `<<device>>` sobre um `node` comum:

  ```
  node "Estação do atendente e do expedidor" as estacao <<device>> {
    artifact "Navegador" as navegador
  }
  ```

- `package` vazio ao lado de `class` no mesmo diagrama falha com a mensagem
  "Use 'allowmixing'". Um pacote sem nenhuma classe dentro dele, escrito lado
  a lado com declarações de classe soltas, mistura dois modos de diagrama que
  o PlantUML não combina por padrão. A correção é sempre colocar as classes
  dentro do `package` a que pertencem, nunca deixar `package` decorativo vazio
  ao lado de `class`.

**Uma armadilha de renderização, não de sintaxe:** a linha do Markdown que
embute a imagem (o bloco acima, com a URL do proxy) é longa demais para caber
na tela dentro de um bloco de código, em qualquer tamanho de fonte legível.
Não precisa tratar isso no deck: `uninove-theme.css` já força
`white-space: pre-wrap` e `overflow-wrap: anywhere` em todo `<pre>`/`<code>`
do acervo, então a linha quebra sozinha na projeção. Se um slide novo mostrar
essa linha sem quebrar, o defeito é no tema, não no deck; ver ADR-007.

**Uma quinta armadilha, achada na Aula 09 e da mesma família da anterior:**
um `<code>` **inline**, fora de qualquer `<pre>` (um trecho de XML ou JSON
citado dentro de um parágrafo ou item de lista, por exemplo), não herdava a
quebra acima, porque a regra do tema era escopada a `<pre>` e ao `<code>` que
vive dentro dele. Sem espaço para quebrar, o elemento inline esticava a
`section` além de 1280px, e nenhum dos quatro validadores via isso. Fechada
na origem: `.reveal code` recebe `overflow-wrap: anywhere` para todo código
inline do acervo, sem depender de alguém lembrar de mover o próximo trecho
longo para dentro de um `<pre>`. Ver ADR-007, quinta variante.

### 5.6 A forma distribuída, Aula 19

A Aula 19 monta a versão distribuída do case, com quatro processos subindo
por um único `compose.yaml`:

| Serviço | Papel |
|---|---|
| `pedidos-service` | Recebe e valida pedidos dos lojistas |
| `expedicao-service` | Monta remessas e volumes a partir dos pedidos |
| `rastreamento-service` | Registra eventos de rastreio e ocorrências |
| `portal-web` | Interface em Thymeleaf, consome os três por REST |

A limitação do GitHub Codespaces é dita em voz alta no deck e no kit: a URL
existe enquanto o codespace está rodando, ele hiberna por inatividade, e o
aluno precisa iniciar o codespace antes da apresentação da Aula 20. O
checklist de publicação inclui "a porta está marcada como pública, e não
privada".

### 5.7 Aulas 01 a 05, laboratório sem código de aplicação

O Módulo 1 é conceitual: nenhuma das cinco primeiras aulas rende laboratório
de código de aplicação. Os ciclos 3 e 4 delas são de **ambiente e
modelagem**, e todo entregável é versionado no fork, para que a espiral
funcione desde o primeiro encontro.

| Aula | Entregável dos ciclos 3 e 4 |
|---|---|
| 01 | Ambiente pronto: JDK 21 e Maven instalados, fork do repositório-esqueleto clonado e o projeto Spring Boot vazio subindo |
| 02 | Inventário dos frameworks e padrões que a Rota Sul vai usar, com a justificativa de cada escolha, em `docs/decisoes.md` do fork |
| 03 | Mapeamento da Rota Sul no modelo 3C: que interação é comunicação, qual é coordenação e qual é cooperação, e quais são síncronas ou assíncronas |
| 04 | Diagrama UML de componentes e de implantação da arquitetura colaborativa da Rota Sul |
| 05 | Diagramas UML estruturais formalizados: classes do domínio e pacotes, revisando o que a Aula 04 esboçou |

O primeiro código de aplicação entra na Aula 06, quando as três camadas
aparecem e o Spring Boot deixa de estar vazio.

---

## 6. Anatomia do deck

Cada `aulas-1sem/aulas/aulaXX.html` é autocontido, publicado por CDN, sem
build e sem bundler, mede exatamente 1280x720 e é inicializado com
`center: false, margin: 0`. A `section` tem altura travada: o conteúdo não
rola, e o que não couber quebra o slide visualmente sem lançar erro no
console. Consequência prática: **um conceito por slide**; quando não couber,
dividir em dois slides, nunca encolher a fonte.

> **Este acervo não tem resolução de turma.** Não existe
> `assets/js/turmas.js`, não existe o atributo `data-data-da-aula` e **nenhum
> deck exibe data**. O slide de título traz apenas `AULA XX | Módulo N, Nome
> do módulo` e o nome do professor. Data escrita à mão, no formato
> `DD/MM/AAAA` ou por extenso, é reprovada por `tools/check_decks.py`. Esta é
> a diferença número um em relação ao acervo de Desenvolvimento Web: aquele
> acervo tem duas turmas e resolve a data de cada encontro por código,
> injetando o `<span data-data-da-aula="XX">` no slide de título via módulo
> ES. Quem copiar um deck de lá sem perceber isso reintroduz o mecanismo
> inteiro, um `assets/js/turmas.js` e um `<script type="module">` que este
> acervo não usa e não deve usar.

### 6.1 Ordem canônica dos slides

```
capa
título com AULA XX e o módulo
agenda com os horários dos quatro ciclos
ciclo 1                                                 19h30 às 20h05
ciclo 2                                                 20h05 às 20h40
quiz de fixação                                         20h40 às 20h50
ciclo 3 de laboratório                                  20h50 às 21h25
ciclo 4 de laboratório e entregável                     21h25 às 21h50
fechamento                                               21h50 às 22h00
referências da aula, com id="ref-slide"
encerramento com copyright
```

O slide de referências é canônico, entre o fechamento e o encerramento: é o
alvo das citações `[N]` dos títulos, e por isso leva `id="ref-slide"`. Os 18
capítulos do AVA entram nas referências de cada aula, junto com a
bibliografia externa. A **agenda com horários também é canônica de todas as
aulas**: todo deck abre mostrando os quatro ciclos do encontro. O que a Aula
01 tem a mais são os slides de abertura de semestre (apresentação do
professor, metodologia, avaliação com os pesos e apresentação do case Rota
Sul). As demais aulas não repetem esses.

### 6.2 Esqueleto do arquivo

O `<head>` carrega, nesta ordem: `reveal.css`, tema `white.css`,
`monokai.css` do plugin de destaque, `uninove-theme.css` e
`uninove-print.css`, mais o Google Fonts com Montserrat e JetBrains Mono. O
tema da Uninove precisa vir depois do `white.css` para sobrescrevê-lo, e sem
o Google Fonts o deck cai na fonte do sistema.

```html
<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Aula XX, Título da aula | Uninove</title>
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/reveal.js@5.1.0/dist/reveal.css">
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/reveal.js@5.1.0/dist/theme/white.css">
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/reveal.js@5.1.0/plugin/highlight/monokai.css">
  <link rel="stylesheet" href="../assets/css/uninove-theme.css">
  <link rel="stylesheet" href="../assets/css/uninove-print.css">
  <link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;500;700&display=swap" rel="stylesheet">
</head>
<body>
  <div class="reveal">
    <div class="slides">
      <!-- Capa -->
      <section class="cover-slide">...</section>
      <!-- Título da aula, com AULA XX e o módulo, sem data -->
      <section class="title-slide">...</section>
      <!-- Agenda com os horários dos quatro ciclos -->
      <section class="content-slide">...</section>
      <!-- Ciclo 1: conceito, demonstração, exercício curto -->
      <section class="content-slide">...</section>
      <!-- Ciclo 2: conceito, demonstração, exercício curto -->
      <section class="content-slide">...</section>
      <!-- Quiz de fixação -->
      <section class="quiz-slide content-slide">...</section>
      <!-- Ciclo 3: laboratório guiado, um slide por passo -->
      <section class="exercise-slide content-slide">...</section>
      <!-- Ciclo 4: laboratório final e entregável -->
      <section class="exercise-slide content-slide">...</section>
      <!-- Fechamento: entregável, commit, push e prévia da próxima aula -->
      <section class="content-slide">...</section>
      <!-- Referências da aula, alvo das citações [N] -->
      <section id="ref-slide" class="content-slide">...</section>
      <!-- Encerramento com copyright -->
      <section class="end-slide">...</section>
    </div>
  </div>

  <script src="https://cdn.jsdelivr.net/npm/reveal.js@5.1.0/dist/reveal.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/reveal.js@5.1.0/plugin/highlight/highlight.js"></script>
  <script src="../assets/js/uninove-quiz.js"></script>
  <script>
    Reveal.initialize({
      width: 1280, height: 720, center: false, margin: 0,
      hash: true, slideNumber: false,
      controls: false, progress: false,
      pdfMaxPagesPerSlide: 1,
      plugins: [RevealHighlight],
    });
  </script>
</body>
</html>
```

Não há módulo ES no fim do deck, porque não há resolução de turma. O único
script além do próprio Reveal é `uninove-quiz.js`.

Pontos do esqueleto que não são opcionais:

- **O formato do `<title>`:** `Aula XX, Título da aula | Uninove`, com
  vírgula depois do número e sem o nome da disciplina.
- **As cinco folhas de estilo, nesta ordem:** Reveal, tema `white`,
  `monokai` do plugin de destaque, `uninove-theme.css` e
  `uninove-print.css`.
- **`hash: true`** dá URL própria a cada slide e faz `href="#/ref-slide"`
  funcionar.
- **`controls: false, progress: false`** existem porque os controles do
  Reveal caem em cima do rodapé do tema.
- **`pdfMaxPagesPerSlide: 1`** garante uma página por slide no
  `?print-pdf`.

### 6.3 Classes do tema Uninove

Conferidas em `aulas-1sem/assets/css/uninove-theme.css`. Não confie neste
documento nem em nenhum outro: confira sempre no CSS. Cores da marca:
`--uninove-azul: #00274D` e `--uninove-coral: #C84B31`, definidas em `:root`
no próprio tema, sem alteração de paleta em relação ao acervo de origem.

**Classes de `section`:** `cover-slide`, `title-slide`, `content-slide`,
`section-slide`, `quiz-slide`, `exercise-slide`, `end-slide`.

`quiz-slide` e `exercise-slide` **não têm regras próprias** de `.top-bar`,
`.uninove-logo-header` nem `.slide-footer` no CSS. Essas barras só aparecem
se o slide também levar a classe `content-slide`, por isso o padrão é sempre
escrever `class="quiz-slide content-slide"` e `class="exercise-slide
content-slide"`.

**Blocos reutilizáveis:** `slide-title-area` com `accent-bar`, `top-bar`,
`uninove-logo-header`, `uninove-logo-full` (a logo grande da capa e do
encerramento), `title-card` e `lesson-bar` (exclusivos do `title-slide`),
`slide-footer` com `footer-bar` e `footer-page`, `concept-cards` com
`concept-card`, `side-by-side` com `side`, `figure-split`, `slide-figure`,
`timeline` com `tl-item`, `tl-dot`, `tl-year`, `tl-tool`, `tl-desc` e o
modificador `is-past` no `tl-item` já percorrido, `takeaway` com
`takeaway-label`, `callout`, `flow-diagram` com `flow-item` e `flow-arrow`,
`exercise-container` com `exercise-steps` (a lista numerada dos passos de
laboratório), `code-compact` (modificador de `<pre>` para bloco de código
curto), `ref-badge` e `decor-coral`.

`.decor-coral` é o triângulo coral do canto superior direito. É um `<div>`
real com caixa zerada no próprio elemento: quem desenha o triângulo é o
pseudo-elemento `::after`. Precisa ser escrito no HTML de cada slide de
conteúdo, quiz ou exercício; ele não aparece sozinho.

O `footer-bar` é o número da aula com dois dígitos, um espaço e o tema curto
do slide, sem hífen: `03 Modelo 3C`. O `footer-page` é a posição do slide no
deck, contada a partir de 1 com a capa como 1, crescente, sem pular nem
repetir.

### 6.4 O slide de título

O `title-slide` tem markup próprio, que não é o do `content-slide`. Sem
data, sem `<span>` de resolução de turma:

```html
<section class="title-slide">
  <div class="top-bar"></div>
  <img src="../assets/img/uninove-logo.png" alt="Uninove" class="uninove-logo-header">
  <div class="title-card">
    <div class="accent-bar"></div>
    <h1>Arquitetura de Software</h1>
    <h2>Título da aula</h2>
    <h3>Prof. José Romualdo</h3>
  </div>
  <div class="lesson-bar">AULA XX &nbsp;|&nbsp; Módulo N, Nome do módulo</div>
</section>
```

Nomes dos módulos, para o `lesson-bar`:

- M1: `Módulo 1, Fundamentos e sistemas colaborativos`
- M2: `Módulo 2, Integração e serviços distribuídos`
- M3: `Módulo 3, Padrões e frameworks`
- M4: `Módulo 4, Persistência e componentes`
- M5: `Módulo 5, Projeto final`

### 6.5 Esqueleto de um slide de conteúdo

```html
<section class="content-slide">
  <div class="top-bar"></div>
  <img src="../assets/img/uninove-logo.png" alt="Uninove" class="uninove-logo-header">
  <div class="decor-coral"></div>
  <div class="slide-title-area">
    <div class="accent-bar"></div>
    <h2>Título do conceito <a href="#/ref-slide" class="ref-badge">[3]</a></h2>
  </div>

  <p style="font-size:0.78em;">Uma frase que enquadra o problema.</p>

  <!-- figura, diagrama, cards ou tabela -->

  <div class="takeaway">
    <span class="takeaway-label">Takeaway</span>
    <p>O que o aluno leva se esquecer todo o resto.</p>
  </div>

  <div class="slide-footer">
    <div class="footer-bar">XX Tema curto</div>
    <div class="footer-page">3</div>
  </div>
</section>
```

---

## 7. Quizzes

Um quiz por aula, às 20h40, entre o Ciclo 2 e o Ciclo 3. O markup que
funciona com `assets/js/uninove-quiz.js` é o padrão de lista:

```html
<section class="quiz-slide content-slide">
  <div class="top-bar"></div>
  <img src="../assets/img/uninove-logo.png" alt="Uninove" class="uninove-logo-header">
  <div class="decor-coral"></div>
  <div class="slide-title-area">
    <div class="accent-bar"></div>
    <h2>Quiz de Fixação</h2>
  </div>

  <div class="quiz-container">
    <div class="quiz-question">Pergunta direta, sem rodeio.</div>
    <ul class="quiz-options">
      <li data-correct="false"><span class="option-letter">A</span> Opção A</li>
      <li data-correct="true"><span class="option-letter">B</span> Opção B</li>
      <li data-correct="false"><span class="option-letter">C</span> Opção C</li>
      <li data-correct="false"><span class="option-letter">D</span> Opção D</li>
    </ul>
    <div class="quiz-feedback"
         data-correct-msg="Correto. Explica por que."
         data-incorrect-msg="Incorreto. Aponta o que revisar."></div>
  </div>

  <div class="slide-footer">
    <div class="footer-bar">XX Quiz de fixação</div>
    <div class="footer-page">7</div>
  </div>
</section>
```

Regras de markup:

- `.quiz-container` envolve todo o quiz.
- `<div class="quiz-question">` traz o enunciado, direto, sem rodeio.
- `<ul class="quiz-options">` contém um `<li data-correct="true">` ou
  `<li data-correct="false">` por alternativa, cada um com
  `<span class="option-letter">` para a letra.
- Exatamente uma alternativa leva `data-correct="true"`.
- `<div class="quiz-feedback">` carrega os atributos `data-correct-msg` e
  `data-incorrect-msg`, com o texto completo exibido em cada caso. O script
  lê esses atributos: não é preciso registrar a resposta certa em nenhum
  outro lugar.

**Alternativa que contenha qualquer elemento inline, como `<code>` ou
`<strong>`, precisa ter o texto envolvido em `<span class="option-text">`.**
A `li` de `.quiz-options` é `display: flex` com `gap: 12px`, então cada
trecho de texto solto e cada elemento inline viram itens de flex separados: a
alternativa ganha 12px de buraco de cada lado do `<code>`, no lugar onde
deveria haver um espaço normal, e a frase se parte na projeção. Alternativa
de texto puro dispensa o `span`. **O `check_decks.py` cobre esse caso**
(`checar_alternativas_sem_inline_solto`): nada disso estoura nem se sobrepõe,
então `check_slides.py` e `check_canto_coral.py` não pegam, mas o
`check_decks.py` lê o HTML e reprova o elemento inline solto direto.

```html
<li data-correct="false"><span class="option-letter">D</span><span class="option-text">Anota a interface num campo <code>@Autowired</code> e deixa o Spring resolver a implementação.</span></li>
```

---

## 8. Padrão dos kits de laboratório

Cada aula tem um diretório de referência em `aulas-1sem/labs/aulaXX-lab/`,
contendo o roteiro e o gabarito daquela etapa do case, com:

1. **`README.md`:**
   - O passo do case Rota Sul que a aula resolve, ligado ao entregável da
     aula anterior.
   - Pré-requisitos e comandos, passo a passo.
   - O entregável esperado com quantidade e critério, nunca de forma vaga.
   - **Critérios de aceitação em tabela**, uma linha por critério com a
     evidência que o professor confere na correção. A tabela é obrigatória:
     o checkpoint vale nota, e uma lista em prosa deixa margem para o aluno e
     o professor lerem coisas diferentes.
   - A instrução de commit e push no fork do aluno.
2. **`index.html`**, uma página de redirecionamento para o `README.md`
   exibido pelo GitHub. Obrigatório: o GitHub Pages não faz listagem de
   diretório, e sem esse arquivo o botão "Lab" do portal devolve 404 em
   produção.
3. **Código de referência** que resolve o passo da aula, servindo de
   gabarito para o professor durante a correção.

Diferente de um acervo com um repositório de laboratório por aula, aqui
existe um único repositório-esqueleto do case,
`josercf/uninove-2026-2-rota-sul`, que o aluno forka na Aula 01 e evolui a
cada encontro. Os diretórios em `aulas-1sem/labs/` nunca substituem esse
repositório: são a referência do professor, não o material que o aluno clona
ou forka.

Os slides do laboratório, dentro do deck, seguem um slide por passo: o aluno
acompanha a tela enquanto executa, sem precisar dividir atenção entre o
slide e um roteiro à parte.

**Armadilha recorrente: mudar assinatura, tipo ou construtor de algo já
entregue quebra o que uma aula anterior deixou pronto, e isso só aparece no
fork acumulado.** Já ocorreu três vezes neste acervo: a Aula 07 trocou
`PedidoService` de classe concreta para interface e quebrou o
`PedidoServiceTest` que a Aula 06 entregou; a Aula 11 acrescentou `regiao`
como terceiro parâmetro do construtor de `Pedido` e quebrou duas chamadas de
dois argumentos, uma da Aula 06 e outra da Aula 07; a Aula 10 acrescentou
`ParceiroClient` ao construtor de `RemessaController` e quebrou o
`RemessaControllerTest` que a Aula 09 entregou, porque o `@WebMvcTest` só
tinha `@MockBean` de `RemessaService`. As três correções seguem a mesma
regra:

- **Toda aula que muda assinatura, tipo ou construtor de algo já entregue
  precisa ajustar, no mesmo laboratório, os testes e as chamadas que a
  mudança quebra.** O ajuste é parte do passo que introduz a mudança, não um
  passo à parte nem um problema para a próxima aula herdar. Se o kit
  entregar arquivos prontos que dependem da assinatura antiga (uma classe de
  domínio, um teste, um cliente), o kit também entrega esses arquivos já
  corrigidos.
- **Verificar a aula em isolamento não pega esse defeito.** Montar só o
  código da aula em questão, num projeto Maven à parte, prova que o código
  novo compila e passa; não prova nada sobre o código que aulas anteriores
  já entregaram e que o aluno de verdade carrega no mesmo fork. As três
  quebras acima passaram batidas exatamente porque cada aula foi verificada
  assim.
- **A verificação correta monta o fork acumulado e roda a suíte inteira.**
  Empilhar, num único projeto Maven, o código de referência de cada aula na
  ordem em que o aluno o recebe, do primeiro laboratório até o mais recente,
  e rodar `./mvnw test` nesse projeto acumulado, a cada aula nova. `./mvnw
  test` precisa terminar verde contando **todos** os testes das aulas
  anteriores, não só os da aula que está sendo verificada.

Isso vale, sem exceção, para as Aulas 12 a 20, que ainda serão construídas.
Várias delas mudam assinatura de coisas já entregues: entidade JPA,
relacionamento `@ManyToOne`, transação, contêiner de teste de integração.
Quem escrever essas aulas verifica no fork acumulado, não isolado.

**Variante do mesmo defeito, achada na própria Aula 11 ao provar a cadeia
06 a 11 completa.** `CalculoDeFreteService` (`@Service`) recebia
`FreteRotaPropria` e `FreteTransportadoraParceira` pelo construtor, mas
nenhuma das duas classes tinha anotação de framework, de propósito, porque
são domínio. Isso nunca aparecia no laboratório isolado da Aula 11 (nem no
próprio kit de verificação da aula, que testava só `pedido` e
`rastreamento`, sem `expedicao` nem `parceiro`) porque
`CalculoDeFreteServiceTest` monta o serviço com `new`, sem Spring. Só
apareceu ao empilhar o fork completo, com `ParceiroClientTest`
(`@SpringBootTest`, da Aula 10) subindo o contexto inteiro:
`UnsatisfiedDependencyException`, por falta de bean para as duas
estratégias. Corrigido com `CalculoDeFreteConfig`, uma classe `@Configuration`
com um `@Bean` para cada estratégia, o mesmo padrão que `ParceiroClientConfig`
já usava desde a Aula 10: framework na configuração, nunca na classe de
domínio. A lição estende a de cima: não é só assinatura que muda e quebra
o que já existia; uma peça nova, sozinha correta, também pode faltar um elo
de fiação que só o contexto Spring inteiro exige, e só aparece testando o
fork acumulado.

---

## 9. O ciclo do artefato

Uma aula só está pronta quando os **quatro** artefatos existem. Sem os dois
últimos, a aula fica pronta em disco e invisível para a turma.

1. **`aulas-1sem/aulas/aulaXX.html`**, o deck.
2. **`aulas-1sem/labs/aulaXX-lab/README.md`**, o kit, conforme a seção 8.
3. **`aulas-1sem/labs/aulaXX-lab/index.html`**, redirecionamento para o
   `README.md` no GitHub.
4. **O card da aula habilitado em `aulas-1sem/index.html`**: tirar
   `disabled` da classe dos dois botões, tirar o `aria-disabled`, tirar o
   `<span class="badge-producao">` e pôr os dois `href`.

Antes, aula ainda em produção:

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

Depois, aula publicada:

```html
<article class="card" data-aula="3">
  <div class="card-header">
    <span class="card-numero">Aula 03</span>
  </div>
  <h3 class="card-titulo">Sistemas colaborativos</h3>
  <div class="card-acoes">
    <a class="btn" href="aulas/aula03.html">Slides</a>
    <a class="btn" href="labs/aula03-lab/">Lab</a>
  </div>
</article>
```

---

## 10. Validação

Nenhuma aula é considerada pronta sem os quatro validadores passando. Eles
conferem coisas diferentes e nenhum substitui o outro.

| Validador | O que cobre |
|---|---|
| `check_slides.py` | Geometria no navegador: estouro de 1280x720 e sobreposição. Não olha o conteúdo do arquivo |
| `check_decks.py` | Estrutura estática do HTML: `decor-coral` faltando, `quiz-slide` sem `content-slide`, quiz com zero ou duas respostas certas, alternativa de quiz com elemento inline solto fora de `option-text`, âncora `#/` sem `id` correspondente, `footer-page` fora de sequência, caminho relativo inexistente, nome de arquivo fora do padrão `aulaXX.html` (só dentro de `aulas-1sem/aulas/`) e as três variantes de data: **data escrita à mão** no texto, atributo `data-data-da-aula` presente e referência a `assets/js/turmas.js` |
| `check_canto_coral.py` | O triângulo coral, pixel a pixel. Único que pega elemento opaco cobrindo a decoração |
| `check_portal.py` | Os 20 cards do portal e um GET real em cada botão habilitado |

Os três validadores de deck reportam o slide em **base 0**, a mesma base de
`Reveal.slide(i)`.

**Diferença deliberada em relação ao acervo de Desenvolvimento Web:** lá o
`check_decks.py` confere se `data-data-da-aula` bate com o número no nome do
arquivo. Aqui não existe resolução de turma, e o `check_decks.py` deste
acervo reprova as três formas pelas quais uma data pode entrar num deck: uma
**data escrita à mão** no texto (formato `DD/MM/AAAA` ou por extenso), o
próprio **atributo `data-data-da-aula`** presente em qualquer elemento e
qualquer **referência a `assets/js/turmas.js`**, em `src` ou em `import`. As
duas últimas existem porque copiar um deck do acervo de Desenvolvimento Web
sem remover o mecanismo de resolução de turma reintroduz uma data que é
injetada em tempo de execução: ela não aparece como texto no HTML estático, e
só a checagem de data escrita à mão não pegaria esse caso. Ver ADR-002.

> **Os validadores deste acervo são cópias, não symlinks.** `tools/` foi
> copiado do acervo de Desenvolvimento Web e depois adaptado: a regra de
> turma foi removida e a regra de data manuscrita foi acrescentada. Corrigir
> um bug num validador aqui **não corrige** o mesmo bug nos acervos de
> Desenvolvimento Web nem da FIAP, porque não há link entre os arquivos. Uma
> correção encontrada aqui precisa ser replicada manualmente nos outros dois
> acervos, se também se aplicar a eles.

### 10.1 A suíte pytest

Os validadores são código, e código sem teste aprova o que não deveria. A
suíte em `tests/` valida os próprios validadores contra decks-fixture
propositalmente quebrados, um arquivo por defeito, incluindo um defeito
específico deste acervo: um deck com data escrita à mão precisa ser
reprovado pelo `check_decks.py`, e o teste correspondente afirma isso.
`check_slides.py` e `check_canto_coral.py` dependem de navegador e não
entram na suíte pytest; são exercitados no CI contra os decks reais.

### 10.2 CI

`.github/workflows/ci.yml` roda, a cada push e pull request: `pytest tests/`,
`check_decks.py` sobre todos os decks existentes, `check_portal.py`, e
`check_slides.py` mais `check_canto_coral.py` sobre todos os decks, com o
navegador instalado no runner.

### 10.3 Medição de folga de altura, `tools/medir_folga.py`

`check_slides.py` só reprova **estouro**: um slide com 5px de folga passa
igual a um com 500px. Dimensionar um slide novo (decidir se cabe mais um
parágrafo, se o quiz precisa de texto mais curto) exige saber a folga de
verdade, não só se ela é positiva.

`tools/medir_folga.py` existe para que ninguém escreva esse script de
medição por conta própria de novo. Um implementador que mede a folga
"na unha" tende a esquecer que a `section` tem `padding-bottom: 60px`
(`aulas-1sem/assets/css/uninove-theme.css`) e a inflar o número em cerca de
60px, exatamente o tamanho do padding esquecido. Foi o que aconteceu no
relatório da Task 20 (Aula 07): o quiz depois do clique foi registrado com
84px de folga quando o valor real, descontado o padding, é 24px.

A ferramenta reaproveita literalmente a geometria do `check_slides.py`: usa
o mesmo `JS_MEDIR`, com o mesmo cálculo de `padBottom` e a mesma exclusão de
rodapé/`top-bar`/logo, e só lê o campo `folgaAltura` que o `JS_MEDIR` já
devolve por slide. Não é um quinto validador: nunca reprova nada e sempre
sai com 0, porque o número, sozinho, não diz se o slide está bom ou ruim
(isso depende do que ainda pode ser digitado ali).

```bash
python3 tools/medir_folga.py aulas-1sem/aulas/aula01.html
python3 tools/medir_folga.py --quiz-respondido aulas-1sem/aulas/aula01.html
```

A opção `--quiz-respondido` clica na alternativa `data-correct="true"` do
slide de quiz antes de medir, revelando o `.quiz-feedback` que fica
`display:none` até o clique. Sem essa opção, o quiz é medido no estado
inicial, como o `check_slides.py` mede, e o número não conta o espaço que o
feedback consome. Este é o ponto cego descrito na ADR-007: um quiz com folga
positiva no estado inicial pode ficar muito mais apertado depois do clique,
e só a medição com `--quiz-respondido` mostra isso.
