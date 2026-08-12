# ADR-007: Defeitos de tema invisíveis aos validadores

**Data:** 11/08/2026
**Status:** Aceita
**Decisores:** Prof. José Romualdo

## Contexto

O acervo tem quatro validadores automáticos, descritos na seção 10 do
`aulas-1sem/SKILL.md`: `check_decks.py` lê a estrutura estática do HTML,
`check_slides.py` mede geometria no navegador e procura estouro dos 1280x720 e
sobreposição de blocos, `check_canto_coral.py` confere o triângulo coral pixel
a pixel e `check_portal.py` faz um GET real em cada botão habilitado do portal.

Existe uma classe de defeito que **passa nos quatro e só aparece na tela**:
o slide não estoura, nenhum bloco cobre outro, a decoração está inteira e todo
link responde, mas o texto chega errado ao projetor. O caso concreto que deu
origem a esta ADR é a alternativa de quiz com elemento inline solto.

**O mecanismo.** A regra `.quiz-slide .quiz-options li`
(`aulas-1sem/assets/css/uninove-theme.css`, linha 382) é `display: flex` com
`gap: 12px`. O `gap` existe para separar o círculo da letra, o
`<span class="option-letter">`, do texto da alternativa. Mas o contexto de flex
não distingue "o círculo e o texto" de "os pedaços do texto": num elemento
flex, **cada trecho de texto solto e cada elemento inline vira um item de flex
separado**. Uma alternativa escrita assim,

```html
<li data-correct="false"><span class="option-letter">D</span> Anota a interface
num campo <code>@Autowired</code> e deixa o Spring resolver.</li>
```

tem quatro itens de flex, não dois: a letra, o texto antes do `<code>`, o
`<code>` e o texto depois. O navegador põe 12px entre cada par, no lugar exato
onde deveria haver um espaço de palavra, e a frase se parte na projeção.
Alternativa longa piora o quadro, porque item de flex não quebra linha sem
`flex-wrap`.

Nada disso estoura os 1280x720 nem sobrepõe bloco algum, então o
`check_slides.py` aprovava. O defeito **escapou três vezes, em três decks
diferentes, por três autores diferentes**, e nas três foi encontrado por alguém
que abriu o slide no navegador e olhou.

O mesmo mecanismo reapareceu em outro lugar do tema: o `h3` do
`exercise-container` também era `display: flex`, com `gap: 8px`, e um `<code>`
no meio do título ganhava 8px de buraco. Medido na Aula 09: o texto "Em"
terminava em x=121 e o `<code>` começava em x=129.

E há uma terceira variante, sem flex nenhum: o `reveal.css` traz
`pre code { max-height: 400px; overflow: auto }`. Num deck que rola isso é um
recurso; aqui a `section` tem altura travada e ninguém rola nada em sala, então
o bloco de código simplesmente chegava cortado ao projetor e ao PDF. O
`check_slides.py` também não via, porque quem transbordava era o `code`, dentro
de uma caixa `pre` que continuava dentro dos 720px. Medido: um bloco de 433px
aparecia com 410px, com as últimas linhas fora da tela.

**A quarta variante, achada na revisão da Aula 04:** uma linha de código longa
demais para a largura do slide (a URL do proxy do PlantUML dentro de um bloco
`language-markdown`) não quebra, mesmo com o `<pre>` e o `<code>` ocupando os
1160px de área útil. O sintoma parecia contradizer a própria folha de estilo
do Reveal.js: `reveal.css` traz `.reveal .hljs { white-space: pre-wrap }`, e a
classe `hljs` é adicionada por `RevealHighlight` a todo `<code>` já na
inicialização, antes de qualquer medição. O relatório da Task 17 registrou o
sintoma mas deixou a causa como "possivelmente uma condição de corrida entre o
plugin de destaque e o momento da medição".

Não é condição de corrida. Apurado nesta revisão com o Chrome DevTools
Protocol (`CSS.getMatchedStylesForNode` sobre o `<code>`, numa página mínima
com as mesmas três folhas de estilo do deck): a regra
`.reveal .hljs { white-space: pre-wrap }` do `reveal.css` está dentro de um
bloco `@media print` inteiro (a mesma seção que trata `page-break-after` e
outras regras exclusivas de paginação). Ela **só vale na exportação do PDF**,
nunca na tela. Na tela, quem vence é `.reveal .code-wrapper code
{ white-space: pre }`, do `white.css`, o tema padrão do próprio Reveal.js: o
plugin `RevealHighlight` adiciona a classe `code-wrapper` ao `<pre>` na
inicialização, e essa regra, sem restrição de mídia, é a única que sobra para
decidir a quebra de linha durante a projeção. O comportamento pretendido pelo
Reveal.js para código longo na tela é rolagem horizontal (`.reveal pre code
{ overflow: auto }`, do próprio `white.css`, e `.hljs { overflow-x: auto }`,
do `monokai.css`), não quebra de linha; este acervo não pode usar rolagem
porque a `section` tem altura e largura travadas e ninguém rola nada em sala,
então a saída é forçar a quebra.

## Decisão

Quando um defeito de tema é invisível aos quatro validadores, a resposta é
**mudar o tema, ou o validador, para que o defeito passe a ser detectável**,
em vez de confiar na disciplina de quem escreve o deck.

## Motivações

- **Confiar na disciplina do autor já falhou, e o número é conhecido.** O
  defeito da alternativa de quiz escapou três vezes, em três decks diferentes,
  por três autores diferentes. Nenhum deles foi descuidado: o markup parecia
  correto na leitura do HTML, e o defeito só existia depois do layout. Uma
  convenção que precisa ser lembrada a cada alternativa escrita não é uma
  garantia, é uma estatística.
- **O momento da descoberta é o pior possível.** Material didático é projetado
  uma vez por semestre, na frente de uma turma. Defeito que só aparece na
  projeção é descoberto com a sala cheia, sem chance de corrigir, e com o
  professor lendo em voz alta uma frase partida.
- **Falha ruidosa é preferível a falha silenciosa.** O comentário da linha 635
  do tema já registrava a postura antes de ela virar ADR: zerando o
  `max-height` do `pre code`, o bloco cresce até a altura real e, quando não
  couber, estoura a `section` e o validador acusa. "Trocamos uma falha
  silenciosa por uma falha ruidosa, que é o que se quer de um validador."
  Esta ADR generaliza essa frase para os demais casos.
- **Corrigir na origem é mais barato que corrigir por convenção.** Quando o
  contexto de flex não servia a nada, como no `h3` do `exercise-container`, a
  correção foi devolver a regra a `display: block`: a armadilha some na origem
  e não sobra convenção para ninguém lembrar. Só onde o flex é necessário, como
  na `li` da alternativa, é que restou uma convenção (`.option-text`), e nesse
  caso ela ganhou uma checagem no `check_decks.py` para não depender de memória.

## Onde a decisão está materializada no código

| Arquivo e linha | O que está lá |
|---|---|
| `tools/check_decks.py`, linhas 25, 52, 109, 308 e 318 | Checagem 4, `checar_alternativas_sem_inline_solto`: reprova qualquer filho direto de `<li>` de quiz que não seja `.option-letter` ou `.option-text` |
| `aulas-1sem/assets/css/uninove-theme.css`, linha 382 | `.quiz-slide .quiz-options li`, o `display: flex` com `gap: 12px` que origina o defeito e que é necessário para alinhar a letra |
| `aulas-1sem/assets/css/uninove-theme.css`, linha 406 | `.quiz-slide .quiz-options .option-text`, com `flex: 1` e `min-width: 0`, que devolve o texto inteiro a um único item de flex |
| `aulas-1sem/assets/css/uninove-theme.css`, linha 541 | `.exercise-slide .exercise-container h3` de volta a `display: block`, tirando a armadilha da origem |
| `aulas-1sem/assets/css/uninove-theme.css`, linha 636 | `.reveal pre code` com `max-height: none`, que troca o corte silencioso do código por um estouro que o `check_slides.py` enxerga |
| `aulas-1sem/assets/css/uninove-theme.css`, linha 655 | `.reveal pre, .reveal pre code` com `white-space: pre-wrap !important` e `overflow-wrap: anywhere !important`, movida da Aula 04 para o tema: a regra equivalente do `reveal.css` só vale dentro de `@media print`, então na tela nada quebrava linha comprida de código sem esta regra |
| `aulas-1sem/SKILL.md`, seções 6.3, 7 e 10 | A convenção do `.option-text` e a tabela do que cada validador cobre |
| `tools/check_slides.py`, campo `folgaAltura` do `JS_MEDIR`, e parâmetro `clicarQuiz` | A geometria (limite inferior menos `padding-bottom`) e o clique programático na alternativa certa, reaproveitados por `tools/medir_folga.py` em vez de duplicados |
| `tools/medir_folga.py`, opção `--quiz-respondido` | Mede o slide de quiz com o `.quiz-feedback` visível, o ponto cego desta ADR; ver seção "Riscos conhecidos" |

## Riscos conhecidos

- **A classe de defeito não acabou; só os quatro casos conhecidos foram
  fechados.** Qualquer regra nova de tema pode reabrir a categoria, e nenhum
  validador procura "defeito que só aparece na tela" de forma genérica, porque
  isso não é procurável.
  - **Mitigação:** a seção 6.9 do `task-13-report.md` e a seção 10 do
    `aulas-1sem/SKILL.md` mandam abrir o deck no navegador depois dos quatro
    validadores, e listam o que olhar: fonte carregada, alternativa de quiz
    inteira e bloco de código não cortado. Toda vez que um caso novo aparecer,
    esta ADR ganha uma linha na tabela acima e, se der, uma checagem nova.

- **O `check_slides.py` mede o slide de quiz no estado inicial, com o
  `.quiz-feedback` oculto.** Achado da revisão da Task 13, medido na Aula 01:
  `.quiz-slide .quiz-feedback` é `display: none` por padrão
  (`uninove-theme.css`, linha 487) e o script `uninove-quiz.js` só o revela
  depois do clique na alternativa. Medido no slide de quiz da Aula 01: **193px
  de folga antes do clique e 56px depois, uma diferença de 137px**, dos quais
  123px são a caixa do feedback e 14px a margem dela. Um quiz com feedback mais
  longo, ou com um enunciado de uma linha a mais, **passa no validador e estoura
  em sala, depois do clique**. É exatamente a categoria de defeito que esta ADR
  trata, agora do lado do validador e não do tema.
  - **Mitigação, parcial desde a revisão da Task 20.** `tools/medir_folga.py
    --quiz-respondido` clica na alternativa `data-correct="true"` antes de
    medir, então o ponto cego agora tem uma ferramenta dedicada em vez de
    depender de abrir o navegador e olhar. A mesma revisão também achou que os
    scripts de medição que vinham sendo escritos por conta própria, inclusive
    o que gerou os números acima, infla(va)m a folga em cerca de 60px por não
    descontar o `padding-bottom` da `section`; medido de novo com a ferramenta,
    o quiz da Aula 01 dá **193px antes e 56px depois** (os mesmos números desta
    ADR, então o padding não estava errado aqui), mas o quiz da Aula 07 deu
    **153px antes e 24px depois**, bem abaixo dos 140px recomendados, achado
    só possível porque a medição agora está correta. Isto continua sendo uma
    medição, não uma checagem: `check_slides.py` não passou a reprovar quiz
    com pouca folga depois do clique, e nenhum limiar mínimo é imposto. A
    correção definitiva, integrar essa segunda medição ao próprio
    `check_slides.py` com um limiar que reprove automaticamente, continua em
    aberto.

- **Correção feita aqui não se propaga para os acervos irmãos.** Os validadores
  e o tema deste acervo são cópias, não symlinks (ADR-003). O mesmo defeito
  existe nos acervos de Desenvolvimento Web e da FIAP, e precisa ser corrigido
  lá manualmente.

## Consequências

### Positivas

- **O caso da alternativa de quiz deixou de ser invisível.** O
  `check_decks.py` reprova o elemento inline solto na leitura do HTML, antes de
  qualquer navegador, e a mensagem de erro explica o mecanismo do flex em vez
  de só apontar a linha.
- **Três armadilhas sumiram da origem**, sem depender de convenção: o `h3` do
  `exercise-container` voltou a `display: block`, o `max-height` do
  `pre code` foi zerado, o que transforma código cortado em estouro que o
  `check_slides.py` acusa, e a quebra de linha longa em bloco de código, achada
  na Aula 04, saiu do `style` inline daquele deck e foi para o tema: os 20
  decks ganham o comportamento de uma vez, e ninguém precisa redescobrir que a
  regra equivalente do `reveal.css` só vale na impressão.
- Quem lê os comentários do tema e do validador encontra o mecanismo explicado
  no ponto de uso, e não precisa reconstruí-lo a partir do sintoma.
- A postura fica registrada: diante de um defeito novo dessa categoria, a
  pergunta certa não é "como avisar o autor", é "como tornar isto detectável".

### Negativas

- **O tema fica com regras que existem para servir ao validador, não ao
  desenho.** `max-height: none` no `pre code` é a mais clara delas: ela piora
  deliberadamente o comportamento de um deck que rolasse, para melhorar o
  comportamento de um deck que é conferido por robô. Quem editar essas regras
  sem ler o comentário desfaz a rede de segurança sem perceber.
- A convenção do `.option-text` continua sendo uma convenção. O validador a
  cobra, mas o autor ainda precisa escrevê-la, e um caso que o parser do
  `check_decks.py` não reconheça passaria.
- Cada caso novo dessa categoria custa uma investigação manual no navegador
  antes de virar regra. Não existe atalho: o defeito, por definição, não é
  visível a quem lê o arquivo.

## ADRs relacionadas

- ADR-002: sem resolução de turma e sem data no deck, que é a outra família de
  defeito que o `check_decks.py` cobre e que também não aparece no HTML
  estático quando vem por script
- ADR-003: cópia em vez de symlink, que explica por que a correção não se
  propaga para os acervos irmãos
- ADR-008: convenções de molde do deck padrão-ouro, que registra três decisões
  de padrão que também não têm validador e dependem de documentação
