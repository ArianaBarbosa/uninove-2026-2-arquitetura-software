# ADR-008: Convenções de molde do deck padrão-ouro

**Data:** 11/08/2026
**Status:** Aceita
**Decisores:** Prof. José Romualdo

## Contexto

`aulas-1sem/aulas/aula01.html` é o deck padrão-ouro do acervo: as Tasks 15 a 33
o copiam e trocam o conteúdo, então cada convenção de markup decidida nele se
propaga por 19 decks e cada defeito custa 20.

A revisão do deck levantou três pontos que não são erro de conteúdo e sim
ausência de padrão, e que oscilariam de deck em deck se ficassem sem decisão:

1. O parágrafo de abertura de cada slide carregava `style="font-size:0.76em"`,
   `0.74em` ou `0.72em` conforme o slide. São cerca de 15 declarações inline
   por deck, 300 no acervo, sem classe que permita ajustar o corpo do texto de
   todos os decks de uma vez.
2. O planejamento prevê **exercício curto** ao fim dos Ciclos 1 e 2 de toda
   aula, e o slide de metodologia promete isso na tela, mas o deck não
   entregava nenhum. Faltava decidir se o enunciado é um bloco no pé do slide
   de conceito ou um slide próprio.
3. O slide de entregável era `content-slide` puro, enquanto os três slides de
   passo de laboratório eram `exercise-slide content-slide`, embora os quatro
   pertençam aos Ciclos 3 e 4. Nenhum validador reclama, então a divergência
   se replicaria em silêncio.

## Decisão

Três convenções passam a valer para os 20 decks: o parágrafo de abertura usa a
classe `.lead` do tema, o exercício curto dos Ciclos 1 e 2 é um slide próprio,
e todo slide dos Ciclos 3 e 4, inclusive o do entregável, é
`exercise-slide content-slide`.

## Motivações

- **`.lead` em vez de `style` inline.** Corpo de texto de material projetado é
  parâmetro de legibilidade da última fileira da sala, não escolha por slide.
  Com a classe, ajustar os 20 decks é uma edição em `uninove-theme.css`; sem
  ela, é uma varredura de 300 declarações. O valor padrão é `0.74em`, que
  equivale a 20,7px com a base de 28px do tema. Desvio continua permitido
  quando a altura obrigar, com `style` inline e comentário HTML dizendo por
  quê.
- **Exercício curto como slide próprio.** O enunciado precisa ficar projetado
  durante os minutos em que a sala trabalha. Como bloco no pé do slide de
  conceito, ele obrigaria o professor a manter na tela um slide já explicado, e
  disputaria altura com o conteúdo do conceito num deck em que a `section` tem
  altura travada. Um slide a mais custa menos que um exercício que não existe.
- **`exercise-slide content-slide` em todo slide de laboratório.** A regra fica
  sem exceção e sem julgamento caso a caso. O slide de entregável é o último
  passo do laboratório e nasce dentro do Ciclo 4, como os demais.

## Riscos conhecidos

- **Nenhum validador confere as três convenções.** Um deck copiado pode voltar
  ao `style` inline, esquecer o exercício curto ou marcar o slide de entregável
  como `content-slide` puro, e os quatro validadores continuam com exit 0.
  - **Mitigação parcial:** `lead` entrou em `CLASSES_OBRIGATORIAS` de
    `tests/test_tema.py`, o que protege a classe de sumir do tema, mas não
    obriga o deck a usá-la. As três convenções estão escritas na seção 6 do
    `task-13-report.md`, que é o documento que as Tasks 15 a 33 leem, e a
    decisão do slide de entregável está repetida como comentário HTML dentro do
    próprio slide.
- **Um slide a mais por exercício curto aperta o orçamento de tempo do deck**,
  que já tem 21 slides na Aula 01 e ganharia mais um quando a Task 14
  acrescentar o exercício do Ciclo 1.
  - **Mitigação:** o slide de exercício não acrescenta conteúdo novo, apenas
    projeta o enunciado durante uma atividade que já estava no planejamento e
    já consumia os mesmos três minutos de aula.

## Consequências

### Positivas

- O corpo do parágrafo de abertura dos 20 decks passa a ser um número em um
  lugar só.
- O exercício curto deixa de ser promessa não cumprida do slide de metodologia,
  e ganha um molde reutilizável, medido com 77px de folga.
- A classe da `section` deixa de depender de interpretação: Ciclos 3 e 4 são
  `exercise-slide content-slide`, ponto.

### Negativas

- Cada deck ganha um ou dois slides a mais em relação ao desenho original de 20
  slides, e a renumeração dos `footer-page` fica maior.
- O `exercise-container`, moldura escura da lista de passos, continua sendo
  decisão de conteúdo e não de classe da `section`: o slide de entregável leva
  `exercise-slide` sem levar `exercise-container`, o que exige a explicação
  registrada no comentário HTML do slide.

## ADRs relacionadas

- ADR-002: sem resolução de turma e sem data no deck
- ADR-004: case Rota Sul e repositório-esqueleto único
- ADR-007: defeitos de tema invisíveis aos validadores, que é a mesma situação
  vista do outro lado, quando o defeito existe e nenhum validador o vê; aqui a
  convenção existe e nenhum validador a cobra
