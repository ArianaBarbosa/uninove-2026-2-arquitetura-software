# Planejamento aula a aula

Roteiro minuto a minuto dos 20 encontros de **Arquitetura de Software**,
Uninove, 2026.2, Prof. José Romualdo.

Este arquivo é a fonte da verdade do **conteúdo** de cada aula. O
`PLANO_DE_ENSINO.md` é a fonte da verdade da ementa, do cronograma e da
avaliação; este documento detalha o que acontece dentro de cada encontro. Todo
deck em `aulas-1sem/aulas/aulaXX.html` e todo kit em
`aulas-1sem/labs/aulaXX-lab/` são construídos a partir da seção correspondente
daqui: os ciclos viram slides, o quiz vira o slide de quiz, os ciclos 3 e 4
viram o kit de laboratório e as referências viram o slide de referências. Deck
construído sem a sua seção pronta é improviso.

## Como cada seção está organizada

Toda aula tem a mesma estrutura, sem exceção. O cabeçalho da seção é
`## Aula NN, Título`, e logo abaixo dele vêm, nesta ordem:

```
**Módulo:**, **Capítulo do AVA:**, **Entregável:**
### Retomada, 5 minutos
### Ciclo 1, 19h30 às 20h05
### Ciclo 2, 20h05 às 20h40
### Quiz, 20h40 às 20h50
### Ciclo 3, 20h50 às 21h25
### Ciclo 4, 21h25 às 21h50
### Fechamento, 21h50 às 22h00
### Referências
```

O cabeçalho `## Aula NN, Título` é contratual: dois dígitos, vírgula, e o
título **idêntico caractere a caractere** ao da tabela de cronograma da seção 6
do `PLANO_DE_ENSINO.md`, que por sua vez é o mesmo texto que aparece no card do
portal. Um teste automatizado lê esse cabeçalho. Título parafraseado quebra a
cadeia planejamento, deck, portal.

## O quadro dos quatro ciclos

Os 150 minutos do encontro são sempre divididos assim, e nenhuma aula altera a
grade:

| Bloco | Horário | Duração | Natureza |
|---|---|---|---|
| Ciclo 1 | 19h30 às 20h05 | 35 min | Conceito, demonstração, exercício curto |
| Ciclo 2 | 20h05 às 20h40 | 35 min | Conceito, demonstração, exercício curto |
| Quiz | 20h40 às 20h50 | 10 min | Fixação, uma pergunta com quatro alternativas |
| Ciclo 3 | 20h50 às 21h25 | 35 min | Laboratório guiado, parte 1 |
| Ciclo 4 | 21h25 às 21h50 | 25 min | Laboratório, parte 2, e o entregável |
| Fechamento | 21h50 às 22h00 | 10 min | Commit, push e prévia da próxima aula |

Não há intervalo formal: a troca de ciclo é o respiro. **A retomada ocupa os
cinco primeiros minutos do Ciclo 1**, que por isso entra no conceito por volta
de 19h35. Os ciclos 1 e 2 seguem sempre o mesmo ritmo interno: o professor
apresenta o conceito, demonstra no projetor e o aluno reproduz num exercício
curto, ainda dentro do ciclo. Os ciclos 3 e 4 são laboratório, com o professor
circulando pela sala. O entregável nasce dentro do Ciclo 4, nunca fora da aula.

## A convenção da espiral

A disciplina **não usa sala de aula invertida**. Cada encontro é
autossuficiente: nenhum conteúdo é cobrado antes de ter sido apresentado em
sala, não há leitura prévia e não há atividade pré-aula. Nenhuma seção deste
documento pode conter a frase "o aluno deve ter lido" nem equivalente.

Em compensação, o conteúdo avança em espiral: **toda aula a partir da Aula 02
abre retomando, pelo nome, o entregável da aula anterior**. A Aula 02 retoma o
ambiente e o fork da Aula 01, a Aula 03 retoma o `docs/decisoes.md` da Aula 02,
e assim por diante. O bloco "Retomada" existe para isso e cita o arquivo, o
diagrama ou a classe pelo nome, não em termos genéricos. A Aula 01 é a única
sem retomada, porque é o primeiro encontro, e no lugar dela traz a abertura do
semestre.

## Sobre datas

**Não há calendário.** A disciplina tem uma turma só e as datas dos encontros
não estão definidas. Nenhuma seção deste documento escreve data, nem no formato
`DD/MM/AAAA`, nem por extenso, nem como "a definir". Os únicos horários que
aparecem são os horários de relógio dos ciclos, que são iguais em todas as
aulas.

## O case e a stack

Todo exemplo, quiz e laboratório orbita a **Rota Sul**, uma transportadora
fictícia de médio porte detalhada na seção 5 do `PLANO_DE_ENSINO.md` e na seção
4 da spec do acervo. Não se inventa domínio genérico e não se usa exemplo solto
de banco ou de loja virtual, exceto quando o próprio capítulo do AVA usa um
exemplo desses, e nesse caso o exemplo é citado como sendo do capítulo e em
seguida traduzido para a Rota Sul.

**Atores:** lojista, expedidor, motorista, atendente e transportadora parceira.
**Entidades:** `Cliente`, `Pedido`, `Remessa`, `Volume`, `Rota`, `Veiculo`,
`Motorista`, `Ocorrencia`, `Parceiro`.

**Contrato técnico**, fixado desde o fork da Aula 01 e válido até a Aula 20:
Java 21 LTS, Maven, Spring Boot 3.x, pacote raiz `br.uni9.rotasul`, Spring Data
JPA sobre Hibernate, MySQL 8.4 no schema `rotasul`, Flyway, Thymeleaf,
springdoc-openapi, Spring Web Services para o parceiro SOAP, JUnit 5 e
Testcontainers, e Docker Compose em GitHub Codespaces no fim do semestre. O
repositório-esqueleto é `josercf/uninove-2026-2-rota-sul`, forkado uma única
vez na Aula 01 e evoluído semana a semana. Nenhuma aula inventa nome fora desse
contrato.

Duas regras de código valem em todas as aulas: **nunca fixar porta de
`localhost` como se fosse universal**, sempre escrever "a porta que o seu
terminal imprimiu"; e senha e segredo vão para variável de ambiente, com `.env`
no `.gitignore` desde a Aula 01.

## O Módulo 1 é conceitual

Nenhuma das Aulas 01 a 05 tem laboratório de código de aplicação. Os ciclos 3 e
4 delas são de ambiente, inventário de decisões e modelagem, e todo entregável
é versionado no fork para que a espiral funcione desde o primeiro encontro. **O
primeiro código de aplicação entra na Aula 06**, quando as três camadas
aparecem e o projeto Spring Boot deixa de estar vazio.

## Referências e crédito

Cada seção termina com uma lista numerada de referências, e **o capítulo do AVA
é sempre a referência [1]**, creditada nominalmente ao **Prof. Paulo Ricardo
Batista Mesquita**, autor dos 18 capítulos publicados no Ambiente Virtual de
Aprendizagem da Uninove. As duas únicas aulas sem capítulo, a 01 e a 20, usam a
posição [1] para o documento que faz as vezes de fonte primária naquele
encontro, e dizem isso explicitamente na lista.

Onde o conhecimento geral sobre o tema divergir do capítulo, **o capítulo
manda**, porque é o texto que o aluno lê no AVA. Quando a aula precisar de um
conceito que o capítulo não traz, o conceito entra citando de onde veio, de
preferência da própria bibliografia do capítulo.

## Convenções editoriais deste documento

- Português do Brasil com acentuação completa.
- Nunca usar o caractere travessão em dash. Usar vírgula, dois pontos,
  parênteses ou reescrever a frase.
- Sem emojis.
- Sem tom exagerado: nada de frases de efeito, punchlines, metáforas
  amplificadoras ou títulos de slogan. Títulos descritivos do conteúdo e
  afirmações diretas.
- Nome de arquivo, classe, pacote, comando e endpoint sempre em `código`.

---

## Aula 01, Abertura do semestre e o problema da arquitetura

**Módulo:** M1, Fundamentos e sistemas colaborativos
**Capítulo do AVA:** sem capítulo, abertura de semestre
**Entregável:** um arquivo `docs/ambiente.md` no fork do aluno, com três
evidências coladas (saída de `java -version`, saída de `mvn -v` e a linha de
log em que a aplicação Spring Boot informa a porta em que subiu), commitado e
empurrado para o fork. Critério de aceitação: as três evidências presentes, o
JDK na versão 21 e o `.env` já listado no `.gitignore`.

### Retomada, 5 minutos

A Aula 01 não tem retomada: é o primeiro encontro do semestre. Os cinco
primeiros minutos são de abertura, com o professor se apresentando (formação,
atuação e o e-mail de contato do plano de ensino) e dizendo em uma frase o que
a turma vai construir ao longo dos 20 encontros: um sistema de operações de
transportadora, em camadas, distribuído em quatro processos ao final.

### Ciclo 1, 19h30 às 20h05

- **Conceito.** Como a disciplina funciona e o que se avalia. Três blocos:

  1. **A estrutura do encontro.** Quatro ciclos de 35, 35, 35 e 25 minutos,
     mais quiz de 10 e fechamento de 10, sem intervalo formal. Dizer em voz
     alta que a disciplina não usa sala de aula invertida: nada é cobrado antes
     de ter sido apresentado em sala e não há leitura antecipada. Em troca, o
     encontro é denso e o entregável nasce dentro da aula.
  2. **A avaliação, com os pesos.** Checkpoints de laboratório, peso 40, que
     são os entregáveis dos ciclos 3 e 4 de cada encontro. Prova, peso 30, que
     cobre o conteúdo teórico da ementa. Projeto final, peso 30, que é a Rota
     Sul na sua forma distribuída, apresentada na Aula 20. Nota final igual a
     `(checkpoints x 0,40) + (prova x 0,30) + (projeto x 0,30)`, aprovação com
     nota final maior ou igual a 6,0. Mostrar também os cinco critérios
     internos do projeto final, com destaque para os 15% de documentação do
     fork, que dependem de um arquivo que começa a ser escrito já na Aula 02.
  3. **A espiral e o fork único.** Não existe repositório de laboratório por
     aula. Existe um fork só, criado hoje, que cresce semana a semana. O
     entregável de uma aula é o ponto de partida da seguinte. Consequência
     prática, dita sem rodeio: quem não commita numa aula começa a seguinte
     atrás.

- **Demonstração no projetor.** Abrir o portal do acervo e percorrer os 20
  cards, mostrando que cada aula tem deck e kit. Abrir o `PLANO_DE_ENSINO.md`
  no repositório e mostrar a tabela de cronograma e a tabela de pesos, para que
  a turma veja que nada do que foi dito é informal. Abrir o
  `github.com/josercf/uninove-2026-2-rota-sul` e mostrar a estrutura do
  repositório-esqueleto: o `pom.xml`, o pacote `br.uni9.rotasul` com a classe
  de inicialização, o `docs/` vazio e o `.gitignore`.

- **Exercício curto.** Cada aluno abre o portal no próprio notebook, localiza o
  card da Aula 01 e abre o kit de laboratório. Quem não conseguir abrir o
  portal levanta a mão agora, não no Ciclo 3: problema de rede na sala é
  resolvido aqui, enquanto o custo é baixo.

### Ciclo 2, 20h05 às 20h40

- **Conceito.** O problema que a arquitetura resolve, apresentado pelo case.
  A Rota Sul é uma transportadora de médio porte que opera com quatro peças:
  pedidos vindos de lojistas, um armazém que monta remessas, frota própria na
  rota principal e transportadoras parceiras na última milha. Cada peça tem
  hoje o seu próprio sistema, e a integração entre elas é feita por planilha e
  telefone. Os sintomas são conhecidos: pedido duplicado, remessa sem rastreio,
  parceiro que não recebe a carga e cliente que liga para o atendimento porque
  ninguém sabe onde está o volume.

  A partir daí, três afirmações, que a disciplina inteira vai desdobrar:

  1. Nenhum desses sintomas é bug de programação. Todos vêm de decisões sobre
     **como as partes do sistema estão separadas e como conversam entre si**.
     Esse conjunto de decisões é o que se chama de arquitetura.
  2. Decisão de arquitetura é cara de mudar depois. Trocar o nome de uma
     variável custa minutos, trocar o modo como dois sistemas se integram custa
     meses. Por isso a decisão é registrada e justificada, não improvisada.
  3. Arquitetura não é diagrama bonito. Diagrama é a **representação** da
     arquitetura, e é o que a Aula 05 vai formalizar em UML.

  Apresentar os cinco atores (lojista, expedidor, motorista, atendente e
  transportadora parceira) e as nove entidades (`Cliente`, `Pedido`, `Remessa`,
  `Volume`, `Rota`, `Veiculo`, `Motorista`, `Ocorrencia`, `Parceiro`). Esses
  nomes valem o semestre inteiro e não mudam.

  Fechar com o mapa do semestre em cinco módulos, sem detalhar conteúdo: M1
  fundamentos e sistemas colaborativos, M2 integração e serviços distribuídos,
  M3 padrões e frameworks, M4 persistência e componentes, M5 projeto final. E
  com o contrato técnico: Java 21, Maven, Spring Boot 3.x, pacote raiz
  `br.uni9.rotasul`, MySQL mais adiante no semestre.

- **Demonstração no projetor.** Desenhar no quadro branco, em dois minutos, o
  fluxo atual da Rota Sul: lojista manda pedido por e-mail, alguém digita numa
  planilha, o armazém consulta a planilha, o motorista recebe uma lista
  impressa, o parceiro recebe uma ligação. Marcar com um círculo cada ponto em
  que a informação é redigitada por um humano. São esses os pontos em que o
  pedido duplica e o rastreio se perde.

- **Exercício curto.** Em duplas, três minutos: escolher um dos cinco atores e
  escrever uma frase respondendo "de que informação esse ator precisa e de quem
  ela vem hoje". Três duplas leem em voz alta. O objetivo não é acertar, é
  fixar os nomes dos atores, que vão reaparecer em todas as aulas do Módulo 1.

### Quiz, 20h40 às 20h50

**Pergunta.** Na Rota Sul, o mesmo pedido do lojista chega duas vezes ao
armazém porque a planilha foi preenchida por duas pessoas diferentes. Qual das
afirmações abaixo descreve corretamente a natureza desse problema?

- A) É um defeito de programação na planilha, e se resolve corrigindo a fórmula
  da célula.
- B) É uma decisão de arquitetura: não existe um único ponto responsável por
  receber e identificar o pedido, então a duplicação é possível por construção.
- C) É um problema de treinamento dos funcionários, sem relação com o software.
- D) É um problema de desempenho, e se resolve com um servidor mais rápido.

**Correta:** B.

**Justificativa.** O sintoma aparece na operação, mas a causa está em como o
sistema foi partido: nenhuma peça tem a responsabilidade exclusiva de receber o
pedido e decidir se ele já existe. Enquanto essa responsabilidade não estiver
atribuída a um componente único, qualquer correção pontual apenas adia o
problema. As alternativas A e D confundem sintoma com causa, e a C ignora que o
sistema permite a duplicação por construção, não por descuido.

### Ciclo 3, 20h50 às 21h25

Laboratório guiado de ambiente. Nenhuma linha de código de aplicação é escrita
hoje.

1. **Conferir o JDK.** Rodar `java -version` no terminal. A saída precisa
   indicar versão 21. Quem tiver outra versão instala o JDK 21 LTS agora,
   seguindo o roteiro do kit para o seu sistema operacional. Quem tiver mais de
   um JDK instalado confere qual está ativo no `PATH`, porque o Maven vai usar
   esse.
2. **Conferir o Maven.** Rodar `mvn -v`. A saída precisa mostrar o Maven e, na
   linha `Java version`, o mesmo 21 do passo anterior. Divergência entre os
   dois é a causa mais comum de erro de compilação nas próximas aulas, e é
   resolvida aqui.
3. **Conferir o Git e a identidade.** Rodar `git --version`, e em seguida
   `git config --global user.name` e `git config --global user.email`. Quem
   estiver com os dois vazios configura agora: os commits do semestre inteiro
   precisam sair com o nome do aluno, porque a entrega do projeto final é
   avaliada pelo histórico de commits do próprio aluno.
4. **Forkar o repositório-esqueleto.** Abrir
   `github.com/josercf/uninove-2026-2-rota-sul`, clicar em Fork e criar o fork
   na conta pessoal do aluno. Este é o único fork do semestre.
5. **Clonar o fork.** `git clone` do endereço do **fork**, não do original.
   Conferir com `git remote -v` que o `origin` aponta para a conta do aluno.
   Clonar o repositório original em vez do fork é o erro mais comum deste
   passo, e só aparece na hora do primeiro push, quando o GitHub nega a
   escrita.

### Ciclo 4, 21h25 às 21h50

6. **Subir o projeto vazio.** Dentro da pasta clonada, rodar
   `./mvnw spring-boot:run`. A primeira execução baixa dependências e demora.
   Ao final, o log imprime a linha com a porta em que a aplicação subiu. Abrir
   essa porta no navegador: a resposta esperada é a página de erro padrão do
   Spring Boot, e isso é sucesso, porque ainda não existe nenhuma rota
   mapeada. Usar sempre a porta que o terminal imprimiu, não uma porta
   decorada.
7. **Conferir o `.gitignore`.** Abrir o `.gitignore` do fork e confirmar que
   `.env` está listado. Se não estiver, acrescentar. A regra vale o semestre
   inteiro: senha de banco e qualquer segredo vão para variável de ambiente e
   nunca para o repositório.
8. **Escrever o entregável.** Criar `docs/ambiente.md` no fork, com três
   seções: `## JDK`, `## Maven` e `## Aplicação subindo`. Colar em cada uma a
   saída literal do comando correspondente e, na terceira, a linha de log com a
   porta. Acrescentar uma linha final informando o sistema operacional usado,
   que serve de referência para o professor ajudar em problemas de ambiente nas
   próximas aulas.

**Entregável do dia:** `docs/ambiente.md` com as três evidências, commitado e
empurrado. Critério de aceitação: JDK 21 nas duas primeiras evidências,
aplicação subindo na terceira, `.env` no `.gitignore`.

### Fechamento, 21h50 às 22h00

- `git add docs/ambiente.md .gitignore`
- `git commit -m "chore(ambiente): registra JDK 21, Maven e primeira execução"`
- `git push`
- Conferir no navegador que o commit apareceu no fork do aluno. Quem receber
  erro de permissão no push provavelmente clonou o repositório original em vez
  do fork, e corrige o `origin` agora.
- **Prévia da Aula 02.** O projeto que subiu hoje já vem com um framework
  dentro, o Spring Boot, e a turma ainda não sabe dizer o que exatamente isso
  significa. A próxima aula responde de onde vieram os frameworks e os padrões
  de projeto, e qual a diferença entre os dois, e o entregável será o
  inventário justificado das escolhas técnicas da Rota Sul.

### Referências

1. Esta aula não tem capítulo correspondente no AVA. A fonte primária do
   encontro é o `PLANO_DE_ENSINO.md` da disciplina, seções 4 (metodologia), 5
   (o case Rota Sul) e 7 (avaliação), Prof. José Romualdo, Uninove, 2026.2.
2. MESQUITA, Paulo Ricardo Batista. **Arquitetura de Software**, os 18
   capítulos do Ambiente Virtual de Aprendizagem da Uninove, apresentados nesta
   aula como o percurso teórico do semestre.
3. Spring. **Documentação do Spring Boot.**
   <https://docs.spring.io/spring-boot/index.html>
4. Oracle. **Java SE 21 Documentation.**
   <https://docs.oracle.com/en/java/javase/21/>

---

## Aula 02, Padrões de projeto e frameworks: origem e distinção

**Módulo:** M1, Fundamentos e sistemas colaborativos
**Capítulo do AVA:** `pdf/001.pdf`, Padrões de projeto e framework
**Entregável:** o arquivo `docs/decisoes.md` no fork, com uma tabela de no
mínimo oito linhas, sendo pelo menos cinco frameworks ou bibliotecas e pelo
menos três padrões de projeto, cada linha com quatro colunas preenchidas:
problema da Rota Sul, escolha, classificação (framework ou padrão de projeto) e
justificativa em uma frase. Critério de aceitação: nenhuma linha com
justificativa vazia e nenhuma escolha fora do contrato técnico da disciplina.

### Retomada, 5 minutos

Na Aula 01 cada aluno entregou `docs/ambiente.md` no seu fork, com JDK 21,
Maven e a aplicação Spring Boot subindo. Retomar duas coisas desse entregável:
o comando `./mvnw spring-boot:run`, que vai reaparecer em quase toda aula a
partir da 06, e o fato de o projeto ter subido sem uma linha de código escrita
pelo aluno. Alguém escreveu esse código por ele, e a aula de hoje é sobre
exatamente isso. Quem não conseguiu subir a aplicação na semana passada usa os
cinco minutos de agora com o professor ao lado.

### Ciclo 1, 19h30 às 20h05

- **Conceito.** A evolução do desenvolvimento de software até o reuso, na
  narrativa do capítulo [1].

  1. **1948, Universidade de Manchester.** Tom Kilburn, Frederic Williams e
     Geoff Tootill escrevem e executam um programa para calcular o maior fator
     do inteiro 262144, dividindo sucessivamente até o resto não ser mais
     divisível. O programa ficou conhecido como *Small Scale Experimental
     Machine*, e o que o torna marco é ser considerado o primeiro programa
     armazenado e executado na memória do computador.
  2. **A base teórica.** Os pesquisadores se apoiaram em *A Mathematical Theory
     of Communication*, de Claude Shannon, publicado no mesmo ano, que
     descrevia um método para escrever lógica binária em substituição aos
     métodos eletromecânicos, dos quais o cartão perfurado é o exemplo mais
     conhecido, usado em alguns lugares até a década de 1980.
  3. **Anos 1950, o software se separa do hardware.** Até então, só grandes
     fabricantes de equipamento, como a IBM, produziam software, cada um com
     seus próprios procedimentos. O trabalho de Kilburn, somado a novos tipos
     de computador, leva às primeiras empresas independentes de
     desenvolvimento, chamadas independentes justamente por não fabricarem o
     hardware em que suas aplicações rodavam.
  4. **A repetição vira mercado.** Com a popularização dos computadores,
     massifica-se o software de automação de processos de empresas. Como muitos
     processos eram parecidos, os programas saíam parecidos, e os
     desenvolvedores perceberam que entregariam mais rápido reaproveitando
     partes já prontas e já em uso.
  5. **O reuso e a divisão que ele criou.** O reuso se difundiu depressa, mas
     dividiu a categoria entre quem parte de soluções existentes e quem prefere
     começar do zero sempre. O capítulo descreve esse segundo modo como a
     "contínua reinvenção da roda" para problemas já conhecidos, e registra,
     com a difusão da orientação a objetos, que o reuso é mais do que desejável:
     é necessário quando se quer garantir um nível mínimo de qualidade no
     produto final. Frameworks e padrões de projeto são apontados como as
     principais ferramentas desse reuso.

- **Demonstração no projetor.** Abrir o `pom.xml` do fork e contar em voz alta
  quantas linhas de dependência existem. Rodar `./mvnw dependency:tree` e
  mostrar que aquelas poucas linhas puxam dezenas de artefatos. Perguntar à
  turma quantas linhas de código o aluno escreveu para ter tudo isso: nenhuma.
  Este é o reuso do capítulo, setenta anos depois, com outro nome e outra
  escala.

- **Exercício curto.** Cinco minutos, individual. Escrever no caderno três
  funcionalidades que a Rota Sul vai precisar e que certamente **já existem
  prontas** em algum lugar, e três que **ninguém no mundo tem pronta** porque
  são específicas da Rota Sul. Duas ou três respostas em voz alta. Respostas
  típicas do primeiro grupo: autenticação, geração de PDF, envio de e-mail,
  acesso a banco. Do segundo grupo: a regra que decide se um pedido vira uma ou
  duas remessas, o critério de escolha do parceiro na última milha.

### Ciclo 2, 20h05 às 20h40

- **Conceito.** Framework e padrão de projeto, e a distinção entre os dois,
  exatamente como o capítulo a define.

  **Framework.** Ferramenta que orienta o desenvolvedor a usar certos
  procedimentos para criar um software. Na orientação a objetos, o framework
  estrutura o código-fonte em classes funcionais, apoiado em abstração,
  polimorfismo e herança, e o que ele gera pode ser entendido como um
  *template* a ser customizado pelo desenvolvedor conforme a aplicação.
  Dependendo do caso, é possível reusar subsistemas inteiros. O capítulo
  registra que um dos primeiros frameworks amplamente difundidos na orientação
  a objetos foi o *SmallTalk Model-View-Controller*, o MVC, que volta na Aula
  06. As vantagens listadas no capítulo:

  - facilidade de reuso de partes prontas para implementar novos sistemas;
  - segmentar o processamento no máximo de classes possíveis, porque o
    framework fica mais flexível quanto mais específicas forem as classes: para
    coletar dados e gravar numa base, é melhor ter uma classe para a tela,
    outra para representar a tabela e outra para conectar as duas do que uma
    classe que faça tudo;
  - possibilidade de expandir o sistema, porque classes mais específicas
    facilitam acrescentar partes novas por meio de interfaces.

  O capítulo acrescenta um quarto ponto e o trata como controverso, não como
  vantagem: o framework **passa a controlar a execução** das classes e do
  software, tirando do desenvolvedor parte da responsabilidade de criar classes
  de controle. Uns veem vantagem, outros veem desvantagem, e cabe ao
  desenvolvedor analisar. Registrar esse ponto com cuidado, porque ele é o
  embrião da inversão de controle que a Aula 12 vai formalizar.

  **Padrão de projeto.** Também chamado de *design pattern*, é um modelo que
  orienta o desenvolvedor a implementar uma determinada solução para resolver
  **um problema específico**. À primeira vista parece o mesmo conceito de
  framework, e a diferença que o capítulo estabelece é uma só, e precisa ser
  dita nesses termos: **o framework orienta como estruturar o software que será
  desenvolvido; o padrão de projeto orienta como implementar a solução de um
  problema específico desse software.**

  **O exemplo do capítulo, e a sua tradução para a Rota Sul.** O capítulo usa
  um sistema de vendas on-line, que precisa de cadastro de produtos, cadastro
  de clientes, pagamento on-line, carrinho e pesquisa de produtos. Para separar
  as classes em funções específicas e organizar esses módulos, usa-se o
  framework. Mas ao olhar uma funcionalidade específica, a pesquisa de
  produtos, aparece outro tipo de problema: com volume muito grande de
  registros, carregar cada página de resultado direto do servidor conforme o
  usuário navega leva tempo demais. Esse é um problema pontual, e a resposta é
  um padrão de projeto, no caso um que mantém o resultado em memória já
  organizado em páginas, de modo que a navegação leia da memória em vez do
  servidor.

  Traduzindo: na Rota Sul, o atendente pesquisa ocorrências de rastreio de um
  período inteiro para responder ao cliente ao telefone. A estrutura em camadas
  do sistema é assunto de framework. Já o modo de paginar aquele resultado sem
  ir ao banco a cada clique é assunto de padrão de projeto. Mesma aplicação,
  duas perguntas diferentes.

- **Demonstração no projetor.** Abrir lado a lado duas telas. À esquerda, o
  site do Spring Boot mostrando o que o framework entrega pronto: estrutura de
  projeto, ciclo de vida da aplicação, servidor embutido. À direita, uma página
  de catálogo de padrões mostrando a ficha de um padrão só. Apontar a diferença
  de escopo: um decide a forma do projeto inteiro, o outro resolve um ponto.

- **Exercício curto.** Cinco minutos, em duplas. Classificar quatro
  necessidades da Rota Sul em "framework" ou "padrão de projeto":
  (a) organizar o sistema em camadas de apresentação, negócio e dados;
  (b) evitar que dois expedidores criem duas remessas para o mesmo pedido;
  (c) mapear as tabelas do banco para objetos Java;
  (d) trocar o cálculo de frete conforme o parceiro, sem espalhar `if` pelo
  código. Gabarito: (a) framework, (b) padrão, (c) framework, (d) padrão.

### Quiz, 20h40 às 20h50

**Pergunta.** Segundo o capítulo, qual é a diferença entre framework e padrão
de projeto?

- A) O framework orienta como implementar a solução de um problema específico
  do software, e o padrão de projeto orienta como estruturar o software como um
  todo.
- B) O framework orienta como o software a ser desenvolvido deve ser
  estruturado, e o padrão de projeto orienta como implementar a solução de um
  problema específico desse software.
- C) Framework e padrão de projeto são o mesmo conceito, e a escolha do termo
  depende da linguagem de programação usada.
- D) O framework serve para sistemas web e o padrão de projeto serve para
  sistemas desktop.

**Correta:** B.

**Justificativa.** É a definição literal do capítulo: o framework atua sobre a
**estrutura** do software que será desenvolvido, e o padrão de projeto atua
sobre a **solução de um problema específico** dentro dele. A alternativa A
inverte exatamente os dois papéis, que é o erro mais comum. A C nega a
distinção, que o capítulo faz questão de estabelecer. A D inventa um critério
de plataforma que não existe em nenhuma das duas definições.

### Ciclo 3, 20h50 às 21h25

Laboratório de inventário de decisões. Ainda não há código de aplicação. O
produto do dia é um documento que vale nota até o fim do semestre, porque a
documentação do fork responde por 15% do projeto final.

1. **Criar o arquivo.** No fork, criar `docs/decisoes.md` com o título
   `# Decisões técnicas da Rota Sul` e um parágrafo curto dizendo que o arquivo
   registra as escolhas de framework e de padrão de projeto do sistema, com a
   justificativa de cada uma, e que ele é atualizado ao longo do semestre.
2. **Criar a tabela.** Quatro colunas, exatamente nesta ordem: `Problema`,
   `Escolha`, `Tipo`, `Justificativa`. A coluna `Tipo` só aceita dois valores,
   `framework` ou `padrão de projeto`, e é essa coluna que exercita a distinção
   do Ciclo 2.
3. **Preencher as cinco linhas de framework**, todas dentro do contrato técnico
   da disciplina, que o professor projeta no quadro para consulta. Sugestão de
   problemas a cobrir, um por linha: estruturar a aplicação e gerenciar o ciclo
   de vida dos objetos; expor operações para outros sistemas por HTTP; gravar e
   ler dados relacionais sem escrever SQL na mão; gerar as telas do portal no
   servidor; escrever testes automatizados. A coluna `Escolha` recebe o nome do
   framework do contrato técnico, e a `Justificativa` responde em uma frase
   **por que esse e não escrever na mão**.
4. **Conferência cruzada.** Cada aluno troca de lugar com o colega ao lado e lê
   a tabela dele procurando uma coisa só: justificativa que apenas repete a
   escolha com outras palavras, do tipo "escolhi Spring Boot porque Spring Boot
   é bom". Justificativa assim volta para o autor reescrever.

### Ciclo 4, 21h25 às 21h50

5. **Preencher as três linhas de padrão de projeto.** Aqui não se exige o nome
   canônico do padrão, que só é catalogado na Aula 11. Exige-se a **descrição
   do problema específico** e a forma da solução. Três problemas sugeridos, dos
   quais o aluno escolhe pelo menos três: evitar remessa duplicada para o mesmo
   pedido; paginar em memória a consulta de ocorrências que o atendente faz ao
   telefone; variar o cálculo de frete conforme o parceiro sem espalhar
   condicionais; padronizar a criação de uma `Remessa` a partir de um `Pedido`.
   Na coluna `Escolha`, o aluno descreve a solução em uma frase, e, se souber o
   nome do padrão, escreve o nome entre parênteses.
6. **Escrever a nota de rastreabilidade.** Ao final do arquivo, um parágrafo
   dizendo quais linhas ainda são hipóteses e serão revisitadas quando a
   disciplina chegar aos capítulos correspondentes. Este parágrafo é o que
   torna o documento honesto: ele é um inventário de decisões, e decisão
   registrada com data de revisão é decisão, decisão sem revisão é palpite.

**Entregável do dia:** `docs/decisoes.md` com no mínimo oito linhas, sendo pelo
menos cinco de framework e pelo menos três de padrão de projeto, todas com as
quatro colunas preenchidas. Critério de aceitação: nenhuma justificativa que
apenas repita a escolha, e nenhuma escolha de framework fora do contrato
técnico da disciplina.

### Fechamento, 21h50 às 22h00

- `git add docs/decisoes.md`
- `git commit -m "docs(decisoes): inventário inicial de frameworks e padrões da Rota Sul"`
- `git push`
- **Prévia da Aula 03.** Hoje a Rota Sul foi tratada como um sistema só. Na
  próxima aula ela é tratada como aquilo que de fato é: várias pessoas
  diferentes, em lugares diferentes, trabalhando sobre a mesma entrega. Isso
  tem nome, tem literatura e muda os requisitos do sistema. O entregável será o
  mapeamento das interações da Rota Sul.

### Referências

1. MESQUITA, Paulo Ricardo Batista. **Capítulo 01: Padrões de projeto e
   framework.** Arquitetura de Software. AVA, Uninove. Fonte primária desta
   aula, `pdf/001.pdf`.
2. SHANNON, Claude E. **A Mathematical Theory of Communication.** The Bell
   System Technical Journal, v. 27, p. 379-423 e 623-656, 1948. Citado pelo
   capítulo como base teórica do programa de Manchester.
3. SIMON, Lavington. **A History of Manchester Computers.** 2. ed. Swindon: The
   British Computer Society, 1998. Citado pelo capítulo.
4. GAMMA, E.; HELM, R.; JOHNSON, R.; VLISSIDES, J. **Padrões de Projeto:
   Soluções Reutilizáveis de Software Orientado a Objetos.** Referência do
   catálogo que a Aula 11 vai abrir.
5. Spring. **Documentação do Spring Boot.**
   <https://docs.spring.io/spring-boot/index.html>

---

## Aula 03, Sistemas colaborativos

**Módulo:** M1, Fundamentos e sistemas colaborativos
**Capítulo do AVA:** `pdf/002.pdf`, Sistemas colaborativos
**Entregável:** o arquivo `docs/colaboracao.md` no fork, com uma tabela de no
mínimo nove interações reais da Rota Sul, cada uma classificada em comunicação,
coordenação ou cooperação, e em síncrona ou assíncrona, mais uma lista dos
requisitos não funcionais que a Rota Sul precisa e dos que ela não precisa, com
uma frase de justificativa por item descartado. Critério de aceitação: as três
categorias do modelo 3C presentes, com pelo menos duas interações em cada, e
pelo menos três requisitos não funcionais descartados com justificativa.

### Retomada, 5 minutos

Na Aula 02 cada aluno entregou `docs/decisoes.md`, com o inventário de
frameworks e padrões da Rota Sul. Retomar uma linha específica daquela tabela,
projetada no quadro: a que trata de expor operações para outros sistemas por
HTTP. Aquela linha pressupõe que existem **outros sistemas** e **outras
pessoas** do lado de fora. A aula de hoje é sobre quem são elas e o que a
presença delas muda nos requisitos do software.

### Ciclo 1, 19h30 às 20h05

- **Conceito.** *Groupware* e a diferença entre aplicação corporativa e sistema
  colaborativo, na definição do capítulo [1].

  O capítulo parte das redes sociais, que dependem de um tipo de software que
  também aparece em aplicações de grande porte, como a automação bancária, com
  a sua interação entre dispositivos móveis, sistemas web, terminais de
  autoatendimento e as aplicações usadas por gerentes e operadores de caixa.
  Esse segundo tipo é o que se chama de **aplicação corporativa**.

  **A diferença principal entre os dois está no objetivo final do software.** A
  aplicação corporativa existe para prover um serviço específico, e o exemplo
  do capítulo é o banco: o correntista acessa e atualiza a conta corrente a
  qualquer hora, de qualquer lugar. A rede social existe para que os usuários
  compartilhem informação uns com os outros, isoladamente ou em grupos, e o
  software que sustenta isso se baseia no conceito de **groupware**.

  **Groupware, ou sistema colaborativo**, é o software que apoia o trabalho em
  grupo, de modo que ele possa ser executado coletivamente. O exemplo do
  capítulo é direto: vários usuários editando simultaneamente um mesmo texto,
  situado num ponto central e acessível a todos que o estiverem editando. As
  tecnologias mais antigas de apoio a esse trabalho são o e-mail, as agendas
  corporativas e os bate-papos; hoje a maior parte da colaboração ocorre por
  aplicações web, cada vez mais dinâmicas e com mais dados.

  Os exemplos de sistema colaborativo que o capítulo lista, além das redes
  sociais, e que valem a pena percorrer um a um:

  - **Controle de versão de software.** Vários programadores acessam um
    servidor que centraliza o resultado do projeto, mas trabalham em cópias
    particulares. Ao terminar, cada um envia suas alterações, e o servidor cria
    uma versão. Como isso ocorre em paralelo entre vários programadores, sempre
    existe no servidor uma versão atualizada com o trabalho de todos,
    consultável a qualquer momento. Vale parar aqui: é exatamente o que a turma
    faz toda semana com o fork.
  - **Telemedicina.** Equipes médicas remotas atendendo o mesmo paciente. O
    exemplo do capítulo: um paciente em viagem é atendido por um médico no
    interior, e o médico que o acompanha, na capital, participa do exame e do
    diagnóstico à distância.
  - **Educação a distância.** O aluno acompanha remotamente o conteúdo e se
    reúne a outros para desenvolver atividades em conjunto.
  - **Teletrabalho.** Um grupo opera de vários locais remotos, em contato
    permanente para troca de informação e atualização do trabalho.

  A definição que o capítulo consolida, e que deve ir para o slide sem
  reescrita: **um sistema colaborativo é um sistema projetado para auxiliar um
  grupo de pessoas a realizar um trabalho, ou objetivo, comum a todas elas.**

  O capítulo fecha essa parte com uma observação que vale registrar: a
  interação entre pessoas sempre existiu, o que mudou foi a forma como ela
  ocorre, e mesmo com o uso maciço de ferramentas de tecnologia da informação
  ela continua dependendo de requisitos mínimos, que são armazenamento de
  dados, comunicação on-line, transferência de dados, operação on-line ou de
  preferência em tempo real, e sincronização das informações entre os usuários.

- **Demonstração no projetor.** Abrir a página de commits do fork de um aluno e
  a de outro, lado a lado, e depois a do repositório-esqueleto original. Mostrar
  que cada um trabalha na sua cópia e que o servidor guarda o histórico
  consolidado. É o exemplo de controle de versão do capítulo, rodando na sala,
  com a turma como grupo.

- **Exercício curto.** Cinco minutos, individual. Responder por escrito: a Rota
  Sul é uma aplicação corporativa ou um sistema colaborativo? Justificar pelo
  critério do capítulo, que é o objetivo final do software. A resposta esperada
  é "as duas coisas ao mesmo tempo": ela presta um serviço específico ao
  lojista, o que é corporativo, e ao mesmo tempo apoia expedidor, motorista,
  atendente e parceiro trabalhando sobre a mesma entrega, o que é colaborativo.
  Duas ou três leituras em voz alta, e a conclusão vai para o quadro, porque
  ela justifica por que o Módulo 1 inteiro trata dos dois assuntos juntos.

### Ciclo 2, 20h05 às 20h40

- **Conceito.** O que um sistema colaborativo exige, e uma ferramenta para ler
  a colaboração.

  **Parte 1, os requisitos, conforme o capítulo.** Um sistema colaborativo
  demanda, do lado funcional, ou seja, do que o aplicativo deve fazer:

  - alta disponibilidade dos recursos de comunicação, permitindo comunicação em
    tempo real, ou on-line;
  - acesso remoto de usuários;
  - evitar a sobrecarga de processamento nos servidores que executam as tarefas
    disponibilizadas pelo sistema;
  - gerenciamento das bases de dados que armazenam as informações do sistema,
    garantindo a integridade delas.

  E, do lado da infraestrutura, que o capítulo trata como requisitos não
  funcionais: balanceamento de carga, transparência a falhas, controle de
  transações de acesso, gerenciamento de clusters, reinstalação dinâmica,
  desligamento limpo, serviços de log e auditoria, gerenciamento de sistemas,
  uso de *threads*, pool de recursos e segurança de acesso.

  **A regra que o capítulo dá sobre essa lista é a parte mais importante do
  ciclo**, e costuma ser a que o aluno esquece: esses requisitos são uma regra
  geral, e isso **não** quer dizer que todos precisem ser considerados em toda
  aplicação nova. O correto é considerar apenas os que são essenciais ao
  aplicativo em questão e desconsiderar os demais. Um projeto que tenta atender
  os onze itens de infraestrutura sem precisar deles gasta o orçamento antes de
  entregar a primeira funcionalidade.

  **Parte 2, o modelo 3C.** Para classificar as interações da Rota Sul de forma
  disciplinada, o laboratório de hoje usa o modelo 3C, que vem de PIMENTEL e
  FUCKS [2], a obra que o próprio capítulo indica como referência. O modelo
  separa a colaboração em três dimensões:

  - **Comunicação.** Troca de mensagens e de informação entre as pessoas.
    Exemplo na Rota Sul: o atendente liga para o motorista perguntando onde
    está o volume.
  - **Coordenação.** Gestão de pessoas, tarefas e recursos ao longo do tempo,
    para que o trabalho de um não atropele o do outro. Exemplo: a ordem em que
    as remessas entram no caminhão e quem é responsável por cada trecho da
    rota.
  - **Cooperação.** Atuação conjunta sobre um mesmo artefato compartilhado.
    Exemplo: o painel de ocorrências que expedidor, motorista e atendente veem
    e alimentam ao mesmo tempo.

  As três se apoiam mutuamente e raramente aparecem puras: comunicação sem
  coordenação vira ruído, coordenação sem cooperação vira burocracia. O
  exercício do laboratório é justamente decidir qual dimensão **predomina** em
  cada interação.

- **Demonstração no projetor.** Retomar o desenho do fluxo atual da Rota Sul,
  feito na Aula 01, e etiquetar três interações ao vivo: a ligação do atendente
  para o motorista (comunicação), a planilha que define a ordem de carregamento
  (coordenação) e a lista de ocorrências que várias pessoas atualizam
  (cooperação). Em seguida, marcar cada uma como síncrona ou assíncrona pelo
  critério operacional: a resposta precisa vir agora ou pode esperar? A
  formalização de síncrono e assíncrono vem na Aula 04.

- **Exercício curto.** Cinco minutos, em duplas. Escolher três dos onze
  requisitos não funcionais listados pelo capítulo e decidir, para cada um, se
  a Rota Sul precisa dele. A regra é responder com uma frase de justificativa,
  não com sim ou não. O objetivo é treinar o descarte justificado, que é o que
  o entregável do dia vai exigir.

### Quiz, 20h40 às 20h50

**Pergunta.** Segundo o capítulo, qual afirmação está correta sobre os
requisitos não funcionais de um sistema colaborativo?

- A) Todo sistema colaborativo precisa atender aos onze requisitos de
  infraestrutura listados, sob pena de não ser considerado colaborativo.
- B) Requisitos não funcionais só se aplicam a redes sociais, porque só elas
  têm muitos usuários simultâneos.
- C) A lista é uma regra geral, e o desenvolvedor deve considerar apenas os
  requisitos essenciais ao seu aplicativo, desconsiderando os demais.
- D) Requisitos não funcionais são exclusivos dos sistemas colaborativos e não
  aparecem em aplicações corporativas.

**Correta:** C.

**Justificativa.** O capítulo enuncia a lista e imediatamente adverte que ela é
uma regra geral, e que o correto é considerar somente os requisitos essenciais
ao aplicativo em questão. A alternativa A transforma um catálogo de referência
em obrigação, que é o erro que encarece projeto. A B restringe o conceito às
redes sociais, contrariando os exemplos de telemedicina, controle de versão,
educação a distância e teletrabalho do próprio capítulo. A D contraria a
conclusão do capítulo, que aproxima o sistema colaborativo das aplicações
corporativas e afirma que eles compartilham requisitos.

### Ciclo 3, 20h50 às 21h25

Laboratório de mapeamento. Sem código.

1. **Criar o arquivo.** No fork, criar `docs/colaboracao.md` com o título
   `# A Rota Sul como sistema colaborativo` e um parágrafo aplicando a
   definição do capítulo ao case: qual é o trabalho comum a todos os atores. A
   resposta esperada, em uma frase, é entregar o volume certo no destino certo
   com rastreio íntegro.
2. **Levantar as interações.** Listar no mínimo nove interações reais entre os
   cinco atores, escritas no formato "quem faz o quê com quem". Exemplos para
   destravar quem ficar parado: o lojista envia o pedido; o expedidor confirma
   que a remessa foi montada; o motorista registra a saída do veículo; o
   atendente consulta o rastreio para responder ao cliente; o parceiro informa
   a entrega da última milha; o expedidor reserva o volume para uma rota; o
   motorista registra uma ocorrência de avaria; o atendente reabre um pedido; o
   parceiro devolve um volume não entregue. O aluno pode e deve trocar esses
   exemplos por outros que ele mesmo enxergar.
3. **Montar a tabela.** Quatro colunas: `Interação`, `Dimensão 3C`,
   `Síncrona ou assíncrona`, `Por quê`. A coluna `Dimensão 3C` só aceita
   `comunicação`, `coordenação` ou `cooperação`. A regra do exercício é que as
   três dimensões apareçam, com pelo menos duas interações em cada. Quem
   classificar tudo como comunicação não separou colaboração de conversa, e o
   professor devolve para revisão.
4. **Discussão dirigida, seis minutos.** Três alunos leem uma linha classificada
   como cooperação. Debater se é mesmo cooperação ou se é coordenação
   disfarçada. O critério de desempate é a pergunta: existe um artefato
   compartilhado que as duas pessoas alteram? Se existe, é cooperação; se o que
   existe é ordem de execução e responsabilidade, é coordenação.

### Ciclo 4, 21h25 às 21h50

5. **Escolher os requisitos.** No mesmo arquivo, criar a seção
   `## Requisitos não funcionais`, com duas listas. A primeira, `Necessários`,
   com os requisitos da lista do capítulo que a Rota Sul precisa, cada um com
   uma frase ligando o requisito a uma interação da tabela anterior. A segunda,
   `Descartados nesta etapa`, com no mínimo três requisitos e a justificativa do
   descarte. Justificativa aceitável é do tipo "gerenciamento de clusters fica
   fora porque o sistema roda em um processo só até a Aula 19"; justificativa
   inaceitável é "não precisa".
6. **Escrever a conclusão.** Um parágrafo final respondendo, com base no que
   foi mapeado, se a Rota Sul é uma aplicação corporativa, um sistema
   colaborativo, ou as duas coisas, e por quê, usando o critério do objetivo
   final do software.

**Entregável do dia:** `docs/colaboracao.md` com a tabela de no mínimo nove
interações, as três dimensões do 3C representadas com pelo menos duas
interações cada, e a seção de requisitos não funcionais com pelo menos três
descartes justificados. Critério de aceitação: nenhuma linha sem a coluna
`Por quê` preenchida, e a conclusão presente.

### Fechamento, 21h50 às 22h00

- `git add docs/colaboracao.md`
- `git commit -m "docs(colaboracao): mapeia as interações da Rota Sul no modelo 3C"`
- `git push`
- **Prévia da Aula 04.** Hoje a turma descreveu **o que** as pessoas fazem
  juntas. A próxima aula trata de **como o software se organiza** para
  sustentar isso: comunicação síncrona e assíncrona com definição formal,
  sistemas distribuídos e três modelos de arquitetura, centralizada,
  descentralizada e híbrida. O entregável será o primeiro esboço de diagrama da
  arquitetura da Rota Sul.

### Referências

1. MESQUITA, Paulo Ricardo Batista. **Capítulo 02: Sistemas colaborativos.**
   Arquitetura de Software. AVA, Uninove. Fonte primária desta aula,
   `pdf/002.pdf`.
2. PIMENTEL, Mariano; FUCKS, Hugo. **Sistemas Colaborativos.** Rio de Janeiro:
   Campus, 2011. Referência indicada pelo próprio capítulo, e origem do modelo
   3C usado no laboratório.
3. `PLANO_DE_ENSINO.md`, seção 5, o case Rota Sul, com os cinco atores e as
   nove entidades usados no mapeamento.

---

## Aula 04, Arquitetura de sistemas colaborativos

**Módulo:** M1, Fundamentos e sistemas colaborativos
**Capítulo do AVA:** `pdf/003.pdf`, Arquitetura de Sistemas Colaborativos
**Entregável:** o arquivo `docs/arquitetura-colaborativa.md` no fork, com a
escolha justificada de um dos três modelos de arquitetura para a Rota Sul, mais
dois diagramas em `docs/diagramas/`, um de componentes e um de implantação, com
o arquivo `.puml` e a imagem exportada de cada um. Critério de aceitação: o
diagrama de componentes com no mínimo quatro componentes e as interfaces entre
eles, o de implantação com no mínimo três nós, e a justificativa da escolha
citando pelo menos duas das seis características de sistemas distribuídos do
capítulo.

### Retomada, 5 minutos

Na Aula 03 cada aluno entregou `docs/colaboracao.md`, com a tabela das nove
interações classificadas no modelo 3C e marcadas como síncronas ou assíncronas.
Projetar a tabela de um aluno e apontar a coluna `Síncrona ou assíncrona`:
aquela coluna foi preenchida por intuição operacional, com a pergunta "a
resposta precisa vir agora?". Hoje o capítulo dá a definição formal dos dois
termos, e a turma vai conferir se a intuição da semana passada resistiu.

### Ciclo 1, 19h30 às 20h05

- **Conceito.** Comunicação síncrona e assíncrona, e o sistema distribuído que
  existe por baixo de todo sistema colaborativo.

  **Síncrono e assíncrono, na definição do capítulo [1].** A complexidade
  tecnológica de um sistema colaborativo depende de como os usuários precisam
  interagir entre si, e as aplicações permitem que essa comunicação ocorra em
  dois modos. No **modo síncrono**, um usuário envia um conteúdo aos demais, o
  conteúdo é transmitido imediatamente, e todos, incluindo quem enviou,
  visualizam exatamente o mesmo conteúdo, sempre em tempo real. No **modo
  assíncrono**, cada usuário pode receber o conteúdo em um momento diferente
  dos demais, e a consequência que o capítulo aponta é a que importa: um
  usuário pode estar vendo um conteúdo que outros já modificaram.

  Esse problema de sincronia dos dados não é exclusivo dos colaborativos:
  aparece também em automação comercial e industrial, onde componentes de
  hardware ou software recebem informação, processam e devolvem resultado, e
  quase sempre quem pediu o processamento depende do resultado para terminar o
  que estava fazendo. Isso exige que a troca de dados entre componentes seja
  eficiente.

  **Sistema distribuído.** O capítulo adota a definição mais comum: um conjunto
  de componentes de hardware e software localizados em computadores autônomos,
  que se comunicam pela troca de mensagens. A maior parte dos sistemas de
  grande porte é implementada assim, e os usuários interagem com eles por
  computadores pessoais ou dispositivos móveis. Distribuir componentes facilita
  compartilhar recursos, e é aí que nasce a concorrência: vários usuários podem
  tentar usar o mesmo recurso ao mesmo tempo.

  **Controle de concorrência**, com as duas abordagens do capítulo:

  - **Pessimista:** o componente controla, serializa e sincroniza todas as
    operações sobre os recursos compartilhados.
  - **Otimista:** em vez de evitar a inconsistência de antemão, o componente
    tenta detectar quando o problema está prestes a ocorrer e se propõe a
    evitá-lo.

  **As seis características de sistemas distribuídos**, que o capítulo lista e
  que voltam no Ciclo 2 como critério de comparação:

  1. **Transparência da distribuição dos componentes.** Do ponto de vista do
     usuário, seja ele humano ou outro sistema, é como se tudo estivesse
     instalado e rodando num único lugar. Se houver redistribuição dos
     componentes, o usuário não percebe.
  2. **Extensibilidade.** É possível acrescentar funcionalidades ou aumentar a
     capacidade de processamento de um componente sem duplicá-lo e sem
     interromper o uso dos demais.
  3. **Escalabilidade.** O sistema atende ao aumento de solicitações sem
     reduzir a quantidade nem a qualidade dos serviços já em uso.
  4. **Tolerância a falhas.** O sistema continua executando os serviços para os
     quais foi projetado mesmo quando falhas ocorrem.
  5. **Interoperabilidade.** O sistema pode conter componentes de fabricantes
     variados, e todos precisam conseguir se intercomunicar, por protocolos ou
     por mecanismos específicos.
  6. **Portabilidade.** Um componente de software pode ser transferido para
     outro sistema distribuído e continuar funcionando do mesmo modo.

  **Heterogeneidade e comunicação.** Um sistema distribuído costuma ser
  heterogêneo, com plataformas e linguagens diferentes, e a heterogeneidade não
  pode impedir o compartilhamento nem a comunicação. O capítulo cita três
  caminhos: metadados em JSON e XML, que são o assunto da Aula 09; camadas de
  software como o CORBA; e o uso de máquina virtual, como a JVM, que permite
  executar componentes segundo o modelo EJB, assunto da Aula 16.

  **Os desafios**, que o capítulo faz questão de nomear: as redes são
  confiáveis, mas não são livres de falha, então os componentes precisam lidar
  com atraso na comunicação, falha no envio e na recepção e perda de
  sincronismo. E há segurança, que aqui é confidencialidade das informações
  trocadas e autenticidade de quem está conectado.

  **O que piora quando o sistema é colaborativo.** O capítulo enumera: o
  controle de recursos compartilhados fica mais complexo, porque muitos
  usuários podem acessar o mesmo recurso exatamente ao mesmo tempo; a
  colaboração precisa de serviços complementares de troca de mensagens, áudio e
  vídeo em tempo real; podem existir grupos específicos de colaboração,
  exigindo políticas descentralizadas de gestão, segurança e compartilhamento;
  e o controle de uso passa a ser exercido **sobre os usuários**, enquanto nos
  demais sistemas distribuídos ele é exercido sobre os componentes. Esse último
  ponto é o que mais rende discussão e merece um slide próprio.

- **Demonstração no projetor.** Duas janelas do mesmo documento colaborativo
  abertas lado a lado. Digitar em uma e mostrar o texto aparecendo na outra:
  síncrono. Em seguida, mostrar um e-mail enviado e o intervalo até alguém
  abrir: assíncrono. Voltar à tabela do `docs/colaboracao.md` de um aluno e
  reclassificar em voz alta duas linhas, agora com a definição formal na mão.

- **Exercício curto.** Cinco minutos, individual. Na Rota Sul, dois expedidores
  abrem ao mesmo tempo a tela do mesmo pedido para montar a remessa. Descrever,
  em duas ou três linhas, o que acontece sob controle de concorrência
  pessimista e o que acontece sob controle otimista, e dizer qual dos dois o
  aluno escolheria para esse caso e por quê. Duas leituras em voz alta.

### Ciclo 2, 20h05 às 20h40

- **Conceito.** Os três modelos de arquitetura do capítulo, comparados pelas
  características do Ciclo 1.

  **Arquitetura centralizada.** Segue o mesmo tipo de processamento da
  arquitetura cliente-servidor: todo o processamento ocorre no servidor, e os
  clientes servem apenas de mecanismo de interação com o usuário. O exemplo do
  capítulo são as aplicações web baseadas apenas em páginas JSP, PHP ou ASP,
  que ficam instaladas no servidor e são processadas por ele, enquanto o
  resultado é exibido no navegador, que é o cliente.

  - **A favor:** facilita o desenvolvimento; facilita a gestão dos recursos
    compartilhados; evita boa parte dos problemas de concorrência; simplifica a
    segurança de acesso e a autenticação dos usuários.
  - **Contra:** com muitos usuários, o servidor demora a devolver resultado;
    pouca escalabilidade, porque com tudo num lugar só é difícil acrescentar
    hardware ou software para aumentar capacidade; pouca tolerância a falhas,
    porque se o servidor cair a aplicação fica indisponível, e as falhas serão
    percebidas pelos usuários. O capítulo aponta duas mitigações: distribuir
    parte do processamento entre cliente e servidor, e acrescentar uma segunda
    instância do servidor como *backup* de serviços.

  **Arquitetura descentralizada.** O processamento é distribuído pelos vários
  componentes, e cada um realiza algum processamento, sozinho ou cooperando com
  outros. O exemplo do capítulo é a própria Internet, com o servidor de DNS: o
  usuário digita uma URL e precisa que alguém traduza aquilo em endereço IP.

  - **A favor:** maior tolerância a falhas, e o exemplo do capítulo é preciso,
    se o DNS não responde, o servidor de destino não está indisponível, e quem
    souber o IP ainda o alcança; é possível acrescentar serviços novos sem
    interferir nos existentes; é mais fácil aumentar a capacidade acrescentando
    componentes; um componente pode ser reusado em outro sistema sem interferir
    nos demais.
  - **Contra:** mais difícil de controlar, tanto o compartilhamento de recursos
    quanto a segurança, a localização dos componentes e a verificação de quem
    está de fato conectado; exige uso intenso da rede, porque os componentes
    trocam dados com muito mais frequência; exige controle maior de
    consistência e integridade; e pode haver atraso de sincronização, que o
    projetista precisa manter em um nível que não impeça a colaboração.

  **Arquitetura híbrida.** Reúne vantagens dos dois modelos tentando eliminar
  ao máximo os aspectos negativos de cada um. O modelo que o capítulo destaca
  centraliza em servidores únicos os componentes que executam funções bastante
  específicas, e esses componentes ficam acessíveis aos diversos componentes
  espalhados pela rede. A Internet é o exemplo, e de modo eficiente: o site de
  uma empresa fica em um servidor único, com um IP único, e para chegar até ele
  por URL o usuário usa o DNS; para o DNS não virar ponto único de falha,
  existem vários servidores DNS que se substituem sem que o usuário perceba.
  O capítulo acrescenta que, nessa arquitetura, um servidor que centraliza
  determinado processamento pode ele mesmo ser implementado como componentes
  distribuídos internamente, e que a melhor forma de implementar depende do
  entendimento que o desenvolvedor tem do problema.

  **Fechamento do ciclo.** Montar no quadro a tabela de comparação, com os três
  modelos nas colunas e quatro linhas: escalabilidade, tolerância a falhas,
  facilidade de controle e uso de rede. Preencher com a turma. Essa tabela é o
  instrumento que o laboratório vai usar para justificar a escolha.

- **Demonstração no projetor.** Rodar `nslookup` para um domínio conhecido e
  mostrar a resposta, e depois acessar o mesmo domínio pelo IP retornado. É a
  demonstração literal do exemplo do capítulo: a URL depende do DNS, o IP não.
  Em seguida, esboçar no quadro como ficaria a Rota Sul em cada um dos três
  modelos, em três desenhos de trinta segundos.

- **Exercício curto.** Cinco minutos, em duplas. Escolher um dos três modelos
  para a Rota Sul e escrever duas frases: uma dizendo qual característica do
  Ciclo 1 o modelo favorece, e outra dizendo qual ele sacrifica. Não existe
  resposta única, existe justificativa boa e justificativa ruim.

### Quiz, 20h40 às 20h50

**Pergunta.** Na Rota Sul, dois expedidores tentam montar a remessa do mesmo
pedido ao mesmo tempo. O componente responsável decide serializar as duas
operações, atendendo uma de cada vez e bloqueando a segunda até a primeira
terminar. Segundo o capítulo, essa abordagem é chamada de:

- A) controle de concorrência otimista.
- B) controle de concorrência pessimista.
- C) transparência da distribuição dos componentes.
- D) tolerância a falhas.

**Correta:** B.

**Justificativa.** O capítulo define o controle pessimista exatamente como
aquele em que o componente controla, serializa e sincroniza todas as operações
sobre os recursos compartilhados. A alternativa A descreve o comportamento
oposto, o de deixar as operações seguirem e tentar detectar a inconsistência
quando ela estiver prestes a ocorrer. As alternativas C e D são características
de sistemas distribuídos, não abordagens de controle de concorrência, e estão
ali porque confundir as duas listas é o erro mais comum do capítulo.

### Ciclo 3, 20h50 às 21h25

Laboratório de modelagem. Sem código de aplicação. Os diagramas de hoje são
**esboços de arquitetura**: a notação UML é formalizada na Aula 05, e o que se
cobra agora é a decisão, não o rigor de notação.

A ferramenta é o PlantUML, escolhida porque o diagrama fica em arquivo de texto
versionável no fork, ao lado do código, e porque pode ser desenhado no
navegador sem instalar nada. Quem já tiver a extensão de PlantUML na IDE usa a
IDE; quem não tiver usa o editor on-line e salva a imagem exportada no fork.

1. **Preparar a pasta.** Criar `docs/diagramas/` no fork.
2. **Listar os componentes.** Antes de desenhar, escrever numa folha os
   componentes de software que a Rota Sul precisa ter, partindo das interações
   mapeadas em `docs/colaboracao.md`. Mínimo de quatro. Os quatro que a maior
   parte das listas contém: recebimento de pedidos, montagem de remessas,
   rastreamento e ocorrências, e integração com parceiros. Estes quatro nomes
   não são coincidência: eles reaparecem na Aula 19 como quatro processos
   separados.
3. **Desenhar o diagrama de componentes.** Criar
   `docs/diagramas/componentes.puml`. Cada componente é um retângulo, e entre
   eles ficam as interfaces, isto é, o que um componente oferece ao outro. A
   pergunta que orienta cada seta é: **que informação passa daqui para lá, e
   quem depende de quem?** O esqueleto mínimo, para o professor projetar:

   ```
   @startuml
   component "Recebimento de pedidos" as pedidos
   component "Montagem de remessas" as expedicao
   component "Rastreamento e ocorrências" as rastreamento
   component "Integração com parceiros" as parceiros
   pedidos --> expedicao : pedido validado
   expedicao --> rastreamento : remessa criada
   expedicao --> parceiros : volume da última milha
   parceiros --> rastreamento : evento de entrega
   @enduml
   ```

   Cada aluno adapta esse esqueleto ao que ele mesmo mapeou, e precisa
   acrescentar pelo menos uma seta que não esteja no exemplo.
4. **Exportar e salvar.** Gerar a imagem e salvar como
   `docs/diagramas/componentes.png`, ao lado do `.puml`. O arquivo de texto é o
   que se versiona de verdade; a imagem existe para quem for ler o repositório
   pelo navegador.

### Ciclo 4, 21h25 às 21h50

5. **Desenhar o diagrama de implantação.** Criar
   `docs/diagramas/implantacao.puml`. Aqui a pergunta muda: não é mais quem
   depende de quem, é **onde cada coisa roda**. Mínimo de três nós. Exemplo de
   partida: o navegador do atendente e do expedidor, o dispositivo móvel do
   motorista, o servidor de aplicação, o servidor de banco de dados e o sistema
   do parceiro, que roda fora da Rota Sul. Marcar em cada ligação entre nós se
   a comunicação é síncrona ou assíncrona, usando a definição formal do Ciclo 1.
6. **Escrever a decisão.** Criar `docs/arquitetura-colaborativa.md` com três
   seções: `## Modelo escolhido`, com um dos três, centralizada,
   descentralizada ou híbrida; `## Justificativa`, citando **pelo menos duas**
   das seis características de sistemas distribuídos do capítulo e dizendo o
   que a escolha favorece e o que ela sacrifica; e `## Diagramas`, com o link
   para os dois arquivos gerados.
7. **Registrar no inventário.** Acrescentar uma linha em `docs/decisoes.md`, da
   Aula 02, com o modelo de arquitetura escolhido hoje. O inventário é vivo, e
   é assim que ele cresce.

**Entregável do dia:** `docs/arquitetura-colaborativa.md` mais os quatro
arquivos em `docs/diagramas/`, dois `.puml` e duas imagens. Critério de
aceitação: diagrama de componentes com no mínimo quatro componentes e as
interfaces entre eles; diagrama de implantação com no mínimo três nós e as
ligações marcadas como síncronas ou assíncronas; justificativa citando pelo
menos duas das seis características do capítulo.

### Fechamento, 21h50 às 22h00

- `git add docs/arquitetura-colaborativa.md docs/diagramas docs/decisoes.md`
- `git commit -m "docs(arquitetura): escolhe o modelo colaborativo e esboça componentes e implantação"`
- `git push`
- **Prévia da Aula 05.** Os dois diagramas de hoje foram desenhados por
  intuição, e cada aluno usou uma notação um pouco diferente. A próxima aula
  responde de onde vem o termo arquitetura de software, por que ele existe, e
  qual é a notação padrão para representá-la. O entregável será a versão
  formalizada desses diagramas, mais o diagrama de classes do domínio.

### Referências

1. MESQUITA, Paulo Ricardo Batista. **Capítulo 03: Arquitetura de Sistemas
   Colaborativos.** Arquitetura de Software. AVA, Uninove. Fonte primária desta
   aula, `pdf/003.pdf`.
2. PIMENTEL, Mariano; FUCKS, Hugo. **Sistemas Colaborativos.** Rio de Janeiro:
   Campus, 2011. Referência indicada pelo capítulo.
3. PlantUML. **Documentação da linguagem.** <https://plantuml.com/pt/>
4. `docs/colaboracao.md` do fork do aluno, entregável da Aula 03, usado como
   ponto de partida da lista de componentes.

---

## Aula 05, Arquitetura de software e representação em UML

**Módulo:** M1, Fundamentos e sistemas colaborativos
**Capítulo do AVA:** `pdf/004.pdf`, Arquitetura de Software
**Entregável:** dois diagramas UML formalizados em `docs/diagramas/`, um de
classes do domínio e um de pacotes, cada um com o arquivo `.puml` e a imagem
exportada, mais a revisão do diagrama de componentes da Aula 04 com a notação
correta. Critério de aceitação: o diagrama de classes contendo as nove
entidades do case com atributos e relacionamentos com multiplicidade, e o
diagrama de pacotes refletindo a estrutura `br.uni9.rotasul` que a Aula 06 vai
usar para escrever código.

### Retomada, 5 minutos

Na Aula 04 cada aluno entregou `docs/arquitetura-colaborativa.md` e os dois
esboços em `docs/diagramas/`, um de componentes e um de implantação. Projetar
dois esboços de alunos diferentes lado a lado e mostrar que eles usam formas e
setas diferentes para dizer a mesma coisa. Enunciar o problema que a aula
resolve: enquanto cada um desenha do seu jeito, o diagrama comunica para quem o
desenhou e para mais ninguém.

### Ciclo 1, 19h30 às 20h05

- **Conceito.** O que é arquitetura de software, de onde vem o nome e por que
  ela passou a ser documentada, na narrativa do capítulo [1].

  **O aumento de complexidade.** Os primeiros softwares, dos anos 1950 aos
  1980, automatizavam tarefas bastante específicas, e por isso tinham
  requisitos mais simples: interoperabilidade, escalabilidade, armazenamento e
  segurança da informação não eram considerados ou não eram relevantes. Nos
  anos 1990, o aprimoramento das telecomunicações e da informática, com o uso
  comercial da Internet e a popularização do telefone celular, levou os
  sistemas a novos níveis de uso, e os requisitos ficaram muito mais complexos.

  **O problema central, que é o que justifica a disciplina inteira.** Essa
  evolução aumentou a complexidade do software principalmente **na hora de
  modificá-lo**. O capítulo é explícito: o principal problema das modificações
  é determinar o quanto elas afetam o que já está pronto, e o quanto podem
  afetar negativamente o software, exigindo trabalho novo para corrigir os
  problemas que a própria modificação causou.

  **De onde vem o nome.** Durante os anos 1960 e 1970, os desenvolvedores
  perceberam a necessidade de manter documentada a organização de um software,
  tanto para iniciar o desenvolvimento quanto para a manutenção. Como era algo
  análogo ao que acontecia na construção civil, usaram o nome **arquitetura de
  software**. Os primeiros cientistas a tratarem do assunto em publicações
  foram Edsger Dijkstra e David Parnas, em pesquisas sobre processamento
  concorrente e desenvolvimento modular.

  **O que ela queria mostrar, e como se organizou.** No início, a intenção era
  mostrar como se associavam a escolha das estruturas de dados e dos algoritmos
  ao processo que o software automatizava. Não havia técnica definida, e cada
  um fazia do seu jeito. Nos anos 1990 popularizaram-se modelos de arquitetura,
  padrões de projeto, padronização de estilo de codificação, boas práticas e
  frameworks, movimento ajudado pela popularização da orientação a objetos.
  Boa parte desse trabalho está centrada no SEI, o Instituto de Engenharia de
  Software da Universidade Carnegie Mellon: não há determinação formal, mas
  muito do que sai de lá é usado como padrão pela indústria.

  **Os dois modelos de projeto de software.** Para projetar um software, o
  capítulo apresenta dois modelos principais, e os dois orientam o
  desenvolvedor sobre o que considerar e como documentar:

  - **Análise estruturada**, popular nos anos 1980. Orienta a projetar o
    software considerando **os processos** que estão sendo automatizados e a
    forma como eles modificam uma determinada informação. A partir do conceito
    operacional do sistema, identificam-se com que dados um processo começa,
    onde eles são armazenados e quais módulos precisam ser desenvolvidos para
    processá-los. Como o modelo nasceu no auge do cliente-servidor, a
    documentação precisava indicar quais módulos rodariam no servidor e quais
    no cliente. O método mais conhecido é o de Edward Yourdon, o YSM, e o
    capítulo cita ainda o IDEF0, usado por órgãos do governo norte-americano, e
    o SSADM, usado no Reino Unido.
  - **Análise orientada a objetos**, popular a partir dos anos 1990 com a
    Internet e as linguagens orientadas a objetos. Diferentemente do que
    ocorreu com a análise estruturada, em que vários métodos concorriam, aqui
    um método se sobressaiu e virou padrão: o de Ivar Jacobson, Grady Booch e
    James Rumbaugh. O método consiste em determinar, a partir do conceito do
    sistema, quais objetos interagem com ele, e como cada um afeta o sistema ou
    é afetado por ele.

  **A UML.** O método dos três era apoiado por uma linguagem de documentação
  capaz de documentar as entidades que interagem com o sistema, os processos a
  automatizar, a interação dos objetos em relação ao tempo ou a prioridades, e
  a organização do software em componentes. Essa linguagem recebeu o nome de
  UML, Linguagem Unificada de Modelagem, e recebeu esse nome porque a
  comunidade percebeu a vantagem de ter um método padronizado em vez de vários
  métodos concorrentes. A UML continua sendo atualizada por um consórcio, que
  mantém o site `uml.org`, e por isso tem várias versões de especificação.

- **Demonstração no projetor.** Abrir os dois esboços da Aula 04 projetados na
  retomada e listar no quadro, em voz alta, cinco perguntas que um leitor de
  fora faria e que os desenhos não respondem: essa seta é chamada de método ou
  envio de mensagem? Essa caixa é uma classe, um componente ou uma máquina?
  Quantos volumes cabem numa remessa? Isso roda no servidor ou no celular? Esse
  retângulo maior é um agrupamento lógico ou uma máquina física? Cada pergunta
  dessas corresponde a um diagrama específico da UML, e é assim que se
  introduz o Ciclo 2.

- **Exercício curto.** Cinco minutos, individual. Dado o enunciado "o atendente
  consulta as ocorrências de uma remessa para responder ao cliente", escrever
  duas listas: o que a análise estruturada olharia (os processos e os dados que
  eles transformam) e o que a análise orientada a objetos olharia (as entidades
  envolvidas e como cada uma afeta ou é afetada). Duas leituras em voz alta.

### Ciclo 2, 20h05 às 20h40

- **Conceito.** Os diagramas da UML indicados para representar arquitetura de
  software. O capítulo indica cinco: classes, componentes, instalação ou
  implantação, pacotes e estrutura composta. Percorrer os cinco, dizendo em
  cada caso **qual pergunta ele responde**.

  **Diagrama de classes.** Um dos diagramas mais significativos da UML, usado
  para representar a estrutura e as relações das classes usadas para construir
  o software. É conceitual, e por isso pode representar o sistema inteiro ou
  apenas partes dele. As classes podem aparecer sob a forma de estereótipo,
  representando atores, telas, relatórios ou tabelas de banco. Como mostra o
  relacionamento entre classes, o capítulo registra que ele também serve para
  representar **mapas objeto-relacional**, usados por algumas tecnologias para
  ligar tabelas e outras entidades de uma base de dados aos objetos de um
  sistema orientado a objetos. Guardar essa frase: é o assunto das Aulas 14, 15
  e 18.

  **Diagrama de componentes.** Mostra como as classes devem ser organizadas
  segundo a noção de componente de software. A UML define componente como um
  programa que executa uma tarefa dentro do sistema, e o exemplo do capítulo é
  um componente que valida o CPF de um usuário: o diagrama mostra como ele se
  relaciona com os outros, quais dados ele precisa para validar e quais
  respostas ele dá. Além da distribuição dos componentes, o diagrama destaca as
  tarefas que eles executam, os parâmetros necessários e os resultados gerados,
  e permite identificar quais precisam ser desenvolvidos e quais já estão
  prontos e podem ser reusados. O capítulo acrescenta dois pontos importantes:
  esse diagrama também serve para mostrar a distribuição de componentes segundo
  modelos de arquitetura como SOA e MVC, porque a UML não define regras sobre
  como projetar, distribuir ou implementar internamente um componente; e não se
  costuma usar diagrama de componentes em aplicações de baixa complexidade, o
  uso comum é em sistemas de alta complexidade.

  **Diagrama de instalação, ou de implantação.** Usado para apresentar a
  arquitetura do sistema, mostrando a distribuição dos componentes de hardware
  e software e a interação deles com os demais elementos que processam os
  dados. Destaca a função de cada componente, a forma como eles se ligam, o
  modelo de arquitetura aplicado e os relacionamentos. O capítulo observa que
  ele não é tão usado durante o desenvolvimento: costuma aparecer nas fases
  finais, apresentando a versão pronta para instalar, ou quando é preciso ligar
  um software novo a um sistema existente e analisar o impacto sobre o que já
  existe.

  **Diagrama de pacotes.** Ilustra como as classes que implementam o sistema
  estão divididas em pacotes, que são agrupamentos lógicos. Normalmente os
  pacotes agrupam classes conforme as funcionalidades que executam, de modo que
  o diagrama mostra como as funcionalidades estão associadas e qual o
  relacionamento entre elas. O capítulo destaca que é um dos diagramas mais
  fáceis de aplicar para representar a adequação do software ao modelo de
  arquitetura escolhido.

  **Diagrama de estrutura composta.** Usado para demonstrar a arquitetura
  interna de alguma funcionalidade, ilustrando como os elementos que a
  implementam se relacionam, e descrevendo a colaboração interna de classes,
  interfaces ou componentes para especificar aquela funcionalidade.

  Fechar com a tabela pergunta e diagrama, que vai para o slide:

  | Pergunta | Diagrama |
  |---|---|
  | Que entidades existem e como se relacionam? | Classes |
  | Que partes executáveis existem e o que uma oferece à outra? | Componentes |
  | Onde cada parte roda? | Implantação |
  | Como o código está agrupado logicamente? | Pacotes |
  | Como uma funcionalidade específica é montada por dentro? | Estrutura composta |

- **Demonstração no projetor.** Reescrever ao vivo, em PlantUML, o esboço de
  componentes da Aula 04 usando a notação correta: `component` para componente,
  `interface` para o que ele oferece, e a seta de dependência. Em seguida,
  desenhar do zero um diagrama de classes com duas entidades do case, `Remessa`
  e `Volume`, com atributos, tipos e a multiplicidade `1..*` entre elas.
  Mostrar como a multiplicidade responde uma pergunta que o esboço da semana
  passada não respondia.

- **Exercício curto.** Cinco minutos, em duplas. Para cada uma das quatro
  perguntas a seguir, dizer qual dos cinco diagramas responde: (a) uma
  `Ocorrencia` pertence a um `Volume` ou a uma `Remessa`? (b) o serviço de
  rastreamento roda na mesma máquina que o banco? (c) as classes de
  apresentação e as de acesso a dados estão separadas? (d) o componente de
  integração com parceiro oferece qual interface? Gabarito: (a) classes, (b)
  implantação, (c) pacotes, (d) componentes.

### Quiz, 20h40 às 20h50

**Pergunta.** A equipe da Rota Sul quer documentar quais entidades existem no
sistema, quais atributos cada uma tem e quantos volumes uma remessa pode
conter. Segundo o capítulo, qual diagrama UML responde a essa necessidade, e
por quê?

- A) Diagrama de implantação, porque ele mostra a distribuição dos componentes
  de hardware e software.
- B) Diagrama de classes, porque ele representa a estrutura e as relações das
  classes usadas para construir o software.
- C) Diagrama de pacotes, porque ele mostra os agrupamentos lógicos das classes
  conforme as funcionalidades.
- D) Diagrama de estrutura composta, porque ele descreve a colaboração interna
  para especificar uma funcionalidade.

**Correta:** B.

**Justificativa.** O capítulo define o diagrama de classes como o que
representa a estrutura e as relações das classes usadas para construir o
software, o que inclui atributos e a multiplicidade dos relacionamentos. A
alternativa A responde onde as coisas rodam, não o que elas são. A C responde
como o código está agrupado, e agrupamento não diz quantos volumes cabem numa
remessa. A D descreve a montagem interna de uma funcionalidade específica, e
não o conjunto de entidades do domínio.

### Ciclo 3, 20h50 às 21h25

Laboratório de modelagem estrutural, formalizando o que a Aula 04 esboçou.
Continua sem código de aplicação, mas o que sai daqui é o desenho que a Aula 06
vai transformar em pacote Java.

1. **Revisar o diagrama de componentes.** Abrir
   `docs/diagramas/componentes.puml`, da Aula 04, e corrigir a notação: usar
   `component` para cada componente e declarar explicitamente as interfaces
   oferecidas, em vez de setas soltas com texto. Salvar por cima e exportar a
   imagem de novo. O histórico do Git guarda a versão anterior, e é ele que
   mostra a evolução do aluno.
2. **Listar as classes do domínio.** Escrever as nove entidades do case:
   `Cliente`, `Pedido`, `Remessa`, `Volume`, `Rota`, `Veiculo`, `Motorista`,
   `Ocorrencia` e `Parceiro`. Para cada uma, no mínimo três atributos com tipo.
   Sem métodos por enquanto: o comportamento entra na Aula 06, quando as
   camadas aparecem.
3. **Desenhar o diagrama de classes.** Criar
   `docs/diagramas/classes-dominio.puml`. Toda associação precisa de
   multiplicidade nas duas pontas. As decisões que a turma precisa tomar
   explicitamente, e que o professor circula perguntando:
   - um `Pedido` gera uma ou várias `Remessa`?
   - uma `Remessa` tem quantos `Volume`?
   - uma `Ocorrencia` se liga ao `Volume`, à `Remessa` ou aos dois?
   - o `Parceiro` se liga à `Remessa` ou ao `Volume` da última milha?
   Não há gabarito único. Há gabarito coerente: qualquer escolha vale, desde
   que o diagrama inteiro fique consistente com ela.

   Esqueleto de partida, para o professor projetar:

   ```
   @startuml
   class Pedido {
     +Long id
     +LocalDateTime criadoEm
     +String situacao
   }
   class Remessa {
     +Long id
     +String codigoRastreio
   }
   class Volume {
     +Long id
     +BigDecimal pesoKg
   }
   Pedido "1" -- "1..*" Remessa
   Remessa "1" -- "1..*" Volume
   @enduml
   ```

4. **Exportar.** Gerar `docs/diagramas/classes-dominio.png` ao lado do `.puml`.

### Ciclo 4, 21h25 às 21h50

5. **Desenhar o diagrama de pacotes.** Criar `docs/diagramas/pacotes.puml`. A
   estrutura é a que a Aula 06 vai criar de verdade no código, e por isso os
   nomes são fixados agora e não mudam:

   ```
   @startuml
   package "br.uni9.rotasul" {
     package "pedido" {
       package "pedido.web" {}
       package "pedido.service" {}
       package "pedido.repository" {}
       package "pedido.domain" {}
     }
     package "expedicao" {}
     package "rastreamento" {}
   }
   @enduml
   ```

   A convenção do semestre, que precisa ir para o slide: **contexto primeiro,
   camada depois**, no formato `br.uni9.rotasul.<contexto>.<camada>`. Os
   contextos são `pedido`, `expedicao` e `rastreamento`, os mesmos nomes dos
   componentes da Aula 04 e dos processos separados da Aula 19. As camadas são
   `web`, `service`, `repository` e `domain`, seguindo a convenção do framework
   em inglês, enquanto os nomes de domínio ficam em português. O aluno desenha
   as três camadas para os três contextos e marca a direção das dependências
   entre camadas, que sempre aponta de `web` para `service` e de `service` para
   `repository`, nunca ao contrário.
6. **Registrar a decisão.** Acrescentar em `docs/decisoes.md` uma linha
   registrando a convenção de pacotes escolhida, com a justificativa da direção
   das dependências.

**Entregável do dia:** `docs/diagramas/classes-dominio.puml` e
`docs/diagramas/pacotes.puml`, com as imagens exportadas, mais o
`componentes.puml` revisado. Critério de aceitação: as nove entidades presentes
no diagrama de classes, todas com atributos tipados e todas as associações com
multiplicidade nas duas pontas; o diagrama de pacotes com os três contextos e
as quatro camadas, e as dependências apontando de `web` para `service` e de
`service` para `repository`.

### Fechamento, 21h50 às 22h00

- `git add docs/diagramas docs/decisoes.md`
- `git commit -m "docs(uml): formaliza classes do domínio e pacotes da Rota Sul"`
- `git push`
- Abrir o fork no navegador e conferir que as imagens aparecem. Diagrama que
  ninguém consegue abrir não documenta nada.
- **Prévia da Aula 06.** O diagrama de pacotes de hoje tem três camadas
  desenhadas e nenhuma linha de código dentro. Na próxima aula essas camadas
  viram código: `web`, `service` e `repository`, com o primeiro endpoint da
  Rota Sul respondendo. É o primeiro encontro com código de aplicação no
  semestre.

### Referências

1. MESQUITA, Paulo Ricardo Batista. **Capítulo 04: Arquitetura de Software.**
   Arquitetura de Software. AVA, Uninove. Fonte primária desta aula,
   `pdf/004.pdf`.
2. YOURDON, Edward. **Análise Estruturada Moderna.** São Paulo: Campus, 1990.
   Referência indicada pelo capítulo para a análise estruturada.
3. FOWLER, Martin. **UML Essencial: um breve guia para a linguagem-padrão de
   modelagem de objetos.** 3. ed. Porto Alegre: Bookman, 2005.
4. OMG. **Unified Modeling Language.** <https://www.uml.org/>, o consórcio
   citado pelo capítulo como mantenedor da especificação.
5. SEI, Carnegie Mellon University. <https://www.sei.cmu.edu/>, citado pelo
   capítulo como centro de referência em arquitetura de software.
6. PlantUML. **Documentação da linguagem.** <https://plantuml.com/pt/>

---

## Aula 06, Arquitetura em 3 camadas e a evolução do MVC

**Módulo:** M1, Fundamentos e sistemas colaborativos
**Capítulo do AVA:** `pdf/005.pdf`, Arquitetura em 3 Camadas
**Entregável:** a primeira fatia vertical da Rota Sul em três camadas, no
pacote `br.uni9.rotasul.pedido`, com `PedidoController`, `PedidoService`,
a interface `PedidoRepository` e a implementação em memória, mais um teste
JUnit 5 do serviço, tudo compilando e com a aplicação respondendo em
`GET /pedidos` e `POST /pedidos`. Critério de aceitação: as quatro classes nos
pacotes corretos, nenhuma regra de negócio dentro do controlador, o teste
passando com `./mvnw test` e a saída de `GET /pedidos` colada no commit ou no
`docs/decisoes.md`.

### Retomada, 5 minutos

Na Aula 05 cada aluno entregou `docs/diagramas/pacotes.puml`, com os três
contextos e as quatro camadas, e `docs/diagramas/classes-dominio.puml`, com as
nove entidades. Projetar o diagrama de pacotes e dizer o que vai acontecer
hoje: aqueles retângulos viram diretórios de verdade dentro de
`src/main/java/br/uni9/rotasul`, e a seta que vai de `web` para `service` vira
uma chamada de método. Este é o primeiro encontro do semestre com código de
aplicação.

### Ciclo 1, 19h30 às 20h05

- **Conceito.** Componente de software e por que a indústria saiu do
  monolítico, conforme o capítulo [1].

  **O que é um componente de software.** O capítulo abre reconhecendo que o
  termo tem significado variável na literatura e que isso causa confusão, e por
  isso estabelece uma definição de trabalho: componente de software é **a parte
  de uma aplicação responsável pela execução de determinada tarefa ou serviço**.
  O exemplo é o mesmo do capítulo anterior, a verificação de que um número de
  CPF informado num sistema de vendas on-line é válido.

  Um componente pode conter uma ou várias classes que executam a tarefa
  atribuída a ele, e para executá-la precisa receber informação e devolver um
  resultado a quem o requisitou. Componentes servem para estruturar uma
  aplicação, assim como os frameworks, mas o capítulo os distingue: o
  componente é mais complexo, porque dependendo da tarefa ele pode ser usado
  como uma aplicação completa; e é mais independente, embora menos flexível que
  um framework. Pode ser reutilizado em outros softwares desde que seja
  possível acoplá-lo sem modificar a aplicação existente.

  **A regra de independência, que é a mais importante do ciclo.** O exemplo do
  capítulo é a máquina de cartão que precisa consultar a operadora para
  confirmar o pagamento. Se o sistema da operadora tiver problema, a máquina
  não pode ficar esperando indefinidamente. Daí a regra: **um componente de
  software deve ser capaz de executar sua tarefa sem depender do resultado de
  outros componentes**, e no exemplo, se a resposta não vier, a máquina deve
  parar o que está fazendo e ficar pronta para um novo uso. O capítulo observa
  que isso nem sempre acontece com o uso de frameworks. Na Rota Sul, o
  equivalente é a integração com o parceiro da última milha: se o parceiro não
  responde, a expedição não pode travar.

  **Por que a indústria adotou componentes.** A narrativa do capítulo, em
  etapas:

  1. Nos últimos trinta ou quarenta anos, a indústria saiu dos sistemas
     **monolíticos**, em que o computador era apenas uma interface para digitar
     e ler dados armazenados em bancos de dados.
  2. Com a popularização dos PCs em residências e empresas de pequeno e médio
     porte, o trabalho passou a ser feito em paralelo, e mais de um usuário
     precisava acessar dados recém-atualizados por outro. Surgem as propostas
     de dividir o processamento entre PCs e servidores.
  3. As aplicações que rodavam isoladas num servidor passaram a rodar em
     servidores interligados, ligando filiais de grandes corporações e, em
     alguns casos, ligando diretamente os sistemas a fornecedores e clientes.
     Com a web, a Internet virou plataforma de serviços, assumindo o papel que
     antes era do fax e do telefone.
  4. Ficou claro que a inflexibilidade e a falta de interoperabilidade das
     aplicações em duas camadas dificultavam a integração e o próprio
     desenvolvimento, porque a tecnologia da época inviabilizava o reuso de uma
     funcionalidade. Era difícil alterar aquelas aplicações, e era comum ter o
     mesmo aplicativo replicado em vários servidores executando a mesma tarefa,
     ocupando armazenamento e processamento à toa.
  5. A conclusão a que se chegou: um sistema projetado como componentes de
     software é flexível para ser alterado e mais fácil de integrar. Como
     bônus, componentes podem ser adaptados a vários modelos de arquitetura, e
     isso levou alguns desenvolvedores a **agrupar componentes de funções
     semelhantes dentro de camadas de serviço**, para facilitar a modelagem da
     arquitetura. É exatamente daí que sai o assunto do Ciclo 2.

- **Demonstração no projetor.** Abrir o `docs/diagramas/componentes.puml` da
  Aula 05 e apontar o componente de integração com parceiros. Perguntar à
  turma: se esse componente não responder, o que acontece com o resto? Marcar
  no diagrama, com um comentário, que essa é uma dependência que não pode
  bloquear. Em seguida, mostrar no fork que hoje existe uma classe só, a de
  inicialização do Spring Boot, e que ao final da aula existirão quatro em
  pacotes diferentes.

- **Exercício curto.** Cinco minutos, individual. Escolher uma das nove
  entidades do case e escrever, em três linhas, qual seria o componente de
  software responsável por ela, que informação ele precisa receber e que
  resultado ele devolve. É o vocabulário do capítulo aplicado ao case, e serve
  de aquecimento para escrever o serviço no Ciclo 3.

### Ciclo 2, 20h05 às 20h40

- **Conceito.** O MVC como o capítulo o define, e a evolução para 3 e N
  camadas.

  **MVC.** O capítulo apresenta o MVC como um dos primeiros padrões de projeto
  a surgir, anterior aos próprios componentes de software, e diz que ele
  orienta o desenvolvedor a organizar seus componentes em três camadas:

  - **Modelo.** Agrupa os componentes que executam **as regras de negócio**, o
    gerenciamento da conexão com as bases de dados, além da lógica e das
    funções necessárias para manter o software em execução.
  - **Visão.** Agrupa os componentes que permitem ao usuário informar dados ou
    ter acesso aos dados que o sistema movimenta.
  - **Controle.** Agrupa os componentes que controlam a troca de informações
    entre os componentes das outras duas camadas.

  **A interação entre elas**, na descrição do capítulo: os componentes de
  Controle enviam comandos para os de Visão atualizarem o que é apresentado ao
  usuário, ou para os de Modelo atualizarem o estado dos objetos quando esse
  estado mudar na memória; os componentes de Modelo notificam Visão e Controle
  sobre as mudanças de estado, de modo que essas duas camadas possam atualizar
  a interface e processar as alterações; e os componentes de Visão requisitam a
  Controle e Modelo possíveis atualizações a mostrar ao usuário.

  **A evolução para 3 e N camadas.** O MVC surgiu na década de 1970 para um
  cenário específico, e vem sendo aperfeiçoado desde então, com novas
  linguagens, novos procedimentos, frameworks, outros padrões e ambientes de
  desenvolvimento melhores. O capítulo usa o usuário móvel como exemplo do que
  forçou a mudança: num primeiro momento, o aplicativo móvel seria apenas um
  componente da camada Visão, mas ele tem o seu próprio modelo de arquitetura,
  adaptado à linguagem e ao ambiente em que roda.

  O resultado é que, embora o termo MVC continue em uso, os softwares não estão
  organizados apenas nas três camadas iniciais: **os componentes que estavam
  agrupados na camada Modelo precisaram ser redistribuídos em subcamadas**, cada
  uma com uma função específica. Surgem a camada de rede, que agrupa os
  componentes que gerenciam o uso da rede de dados, a camada de dados, que
  agrupa os que executam as transações no banco, e assim por diante. Como a
  camada Modelo passou a fazer muita coisa, ficou mais simples nomear as
  subcamadas pelo que elas fazem. Daí os termos **arquitetura em 3 camadas** e
  **arquitetura em N camadas**.

  **A tradução para a stack da disciplina**, que precisa ser dita com cuidado
  para o aluno não achar que o capítulo está errado ou desatualizado:

  | Capítulo | No projeto da Rota Sul | Papel |
  |---|---|---|
  | Visão | Thymeleaf, a partir da Aula 13, e o JSON devolvido pela API | Apresentação |
  | Controle | `PedidoController`, anotado com `@RestController` | Recebe a requisição, valida formato, delega |
  | Modelo, parte de regra | `PedidoService`, anotado com `@Service` | Regra de negócio |
  | Modelo, parte de dados | `PedidoRepository` e a implementação | Acesso aos dados |

  O ponto a enfatizar: o capítulo coloca **regra de negócio e acesso a dados
  juntos na camada Modelo**, e a evolução que o próprio capítulo descreve é
  justamente a separação disso em subcamadas. O projeto da Rota Sul já nasce
  com essa separação feita, e é por isso que aparecem três classes onde o MVC
  original previa duas.

- **Demonstração no projetor.** Escrever ao vivo, do zero, um controlador com
  um método `GET` que devolve uma lista fixa, rodar e mostrar funcionando.
  Depois, deliberadamente, escrever a regra de negócio dentro do controlador e
  perguntar à turma o que quebra: nada quebra agora, e é esse o problema. Em
  seguida, extrair a regra para um serviço, mostrar que o comportamento é o
  mesmo e enunciar o critério: **o controlador não decide nada de negócio, ele
  traduz requisição em chamada de método.**

- **Exercício curto.** Cinco minutos, em duplas. Classificar cinco
  responsabilidades da Rota Sul em Visão, Controle, Modelo com regra ou Modelo
  com dados: (a) converter o JSON recebido em objeto Java; (b) recusar pedido
  sem cliente informado; (c) devolver a lista de pedidos em JSON; (d) guardar o
  pedido na coleção em memória; (e) decidir se um pedido gera uma ou duas
  remessas. Gabarito: (a) Controle, (b) Modelo com regra, (c) Visão, (d) Modelo
  com dados, (e) Modelo com regra.

### Quiz, 20h40 às 20h50

**Pergunta.** Segundo o capítulo, qual das associações entre camada do MVC e
função é a correta?

- A) Modelo, interação com o usuário.
- B) Controle, regras de negócio do aplicativo.
- C) Controle, controle da troca de informações entre as outras duas camadas.
- D) Visão, gerenciamento da conexão com as bases de dados.

**Correta:** C.

**Justificativa.** O capítulo define a camada Controle exatamente como a que
agrupa os componentes que controlam a troca de informações entre os componentes
das outras duas camadas. A alternativa A atribui à camada Modelo a função da
Visão. A B atribui ao Controle a regra de negócio, que o capítulo coloca no
Modelo, e é o erro que a demonstração do Ciclo 2 mostrou na prática. A D
atribui à Visão o gerenciamento de conexão com base de dados, que o capítulo
também coloca no Modelo.

### Ciclo 3, 20h50 às 21h25

Primeiro laboratório de código do semestre. Todo o código vai para o pacote
`br.uni9.rotasul.pedido`, seguindo a convenção fixada no diagrama de pacotes da
Aula 05: contexto primeiro, camada depois. Textos e mensagens em português,
nomes de convenção do framework em inglês, nomes de domínio em português.

1. **Criar os pacotes.** Dentro de `src/main/java/br/uni9/rotasul/`, criar
   `pedido/domain`, `pedido/repository`, `pedido/service` e `pedido/web`. São
   quatro diretórios, e eles correspondem um a um às caixas do
   `docs/diagramas/pacotes.puml`.
2. **Escrever o domínio.** Em `pedido/domain`, criar a classe `Pedido` com os
   atributos que o aluno já definiu no diagrama de classes da Aula 05, no
   mínimo `id`, `cliente`, `descricao` e `situacao`, com construtor e
   getters. Sem anotação de framework nenhuma nesta classe: o domínio não
   depende de Spring, e isso vai importar na Aula 12.
3. **Escrever o contrato de persistência.** Em `pedido/repository`, criar a
   **interface** `PedidoRepository` com dois métodos, `salvar(Pedido)` e
   `listarTodos()`. Interface primeiro, implementação depois: é a interface que
   permite trocar a implementação sem tocar no serviço, e é isso que vai
   acontecer quando o banco real entrar no Módulo 4.
4. **Escrever a implementação em memória.** Ainda em `pedido/repository`, criar
   `PedidoRepositoryEmMemoria`, anotada com `@Repository`, guardando os pedidos
   numa `List` e gerando o `id` com um contador. Dizer em voz alta por que
   memória e não banco: o capítulo de hoje trata de camadas, não de
   persistência, e trocar essa classe por uma implementação com banco é
   exatamente o exercício da Aula 15. A separação de hoje é o que torna aquela
   troca barata.
5. **Compilar.** `./mvnw compile`. Erro de compilação aqui é quase sempre
   pacote errado ou `import` faltando, e é melhor descobrir agora do que no
   Ciclo 4.

### Ciclo 4, 21h25 às 21h50

6. **Escrever o serviço.** Em `pedido/service`, criar `PedidoService`, anotada
   com `@Service`, recebendo `PedidoRepository` pelo construtor. Dois métodos:
   `registrar(Pedido)`, que aplica a regra de negócio e delega ao repositório,
   e `listar()`, que devolve a lista. A regra mínima obrigatória: **pedido sem
   cliente informado é recusado**, com mensagem de erro em português. Quem
   quiser acrescenta uma segunda regra tirada do seu próprio
   `docs/colaboracao.md`.
7. **Escrever o controlador.** Em `pedido/web`, criar `PedidoController`,
   anotada com `@RestController` e mapeada em `/pedidos`, com `GET` devolvendo
   a lista e `POST` recebendo o pedido novo. O controlador chama o serviço e
   não decide nada: qualquer `if` de negócio dentro dele reprova o critério de
   aceitação do dia.
8. **Escrever o teste.** Em `src/test/java/br/uni9/rotasul/pedido/service/`,
   criar `PedidoServiceTest`, com JUnit 5 e no mínimo dois casos: um que
   registra um pedido válido e confirma que ele aparece em `listar()`, e outro
   que registra um pedido sem cliente e confirma que o serviço recusa. O teste
   é do serviço, não do controlador, porque é no serviço que está a regra.
   Rodar `./mvnw test` e ver os dois passarem.
9. **Subir e conferir.** `./mvnw spring-boot:run`, e chamar `GET /pedidos` e
   `POST /pedidos` na porta que o terminal imprimiu, pelo navegador ou por
   `curl`. Colar a saída do `GET` no corpo do commit ou numa seção nova de
   `docs/decisoes.md`.

**Entregável do dia:** as quatro classes de produção nos quatro pacotes, o
teste em `src/test`, e a aplicação respondendo nos dois endpoints. Critério de
aceitação: `./mvnw test` passando, nenhuma regra de negócio no controlador,
nenhuma anotação de framework na classe `Pedido`, e a saída do `GET /pedidos`
registrada.

### Fechamento, 21h50 às 22h00

- `git add src docs`
- `git commit -m "feat(pedido): primeira fatia em três camadas com repositório em memória"`
- `git push`
- Fechar o Módulo 1 em uma frase por aula: ambiente e fork, frameworks e
  padrões, sistemas colaborativos, arquitetura colaborativa, UML, e hoje as
  três camadas rodando. O aluno sai com um fork que tem documentação, diagramas
  e código, e nenhum deles foi escrito fora da sala.
- **Prévia da Aula 07.** Hoje as três camadas estão dentro de um processo só.
  O Módulo 2 abre perguntando o que acontece quando elas precisam morar em
  processos diferentes e conversar pela rede, começando pela arquitetura
  orientada a serviços.

### Referências

1. MESQUITA, Paulo Ricardo Batista. **Capítulo 05: Arquitetura em 3 Camadas.**
   Arquitetura de Software. AVA, Uninove. Fonte primária desta aula,
   `pdf/005.pdf`.
2. LARMAN, Craig. **Applying UML and Patterns: An Introduction to
   Object-Oriented Analysis and Design.** Prentice Hall, 1997. Referência
   indicada pelo capítulo.
3. FOWLER, Martin. **UML Essencial: um breve guia para a linguagem-padrão de
   modelagem de objetos.** 3. ed. Porto Alegre: Bookman, 2005. Referência
   indicada pelo capítulo.
4. Spring. **Documentação do Spring Boot**, seção de desenvolvimento de
   aplicações web. <https://docs.spring.io/spring-boot/index.html>
5. JUnit. **JUnit 5 User Guide.** <https://junit.org/junit5/docs/current/user-guide/>
