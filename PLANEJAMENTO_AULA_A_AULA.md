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

**A ferramenta de diagrama é o PlantUML**, e a regra vale da Aula 04 em diante.
O motivo é a notação: esta é uma disciplina cuja Aula 05 se chama "Arquitetura
de software e representação em UML", e o PlantUML tem as notações nativas de
que os capítulos falam, `component` para componentes, `deployment` com `node`
para implantação, `package` para pacotes e `class` para classes. Ferramenta que
não tem a notação obriga a aproximar componente com fluxograma, e aí o aluno
confunde ferramenta com notação.

Cada diagrama entregue pelo aluno são **dois arquivos** em `docs/arquitetura/`
do fork: o `.puml` com a fonte, que é a fonte de verdade versionada, e um `.md`
irmão que embute a imagem pelo proxy oficial do PlantUML, apontando para o
`raw` do fork do próprio aluno:

```markdown
![Diagrama de componentes da Rota Sul](https://www.plantuml.com/plantuml/proxy?cache=no&src=https://raw.githubusercontent.com/SEU_USUARIO/uninove-2026-2-rota-sul/main/docs/arquitetura/componentes.puml)
```

Duas limitações desse mecanismo, que o roteiro manda o professor declarar em
sala nas Aulas 04 e 05: a imagem depende de um serviço externo, o
`plantuml.com`, e se ele cair a imagem some do `.md`, mas o `.puml` versionado
continua sendo a fonte de verdade; e o proxy só consegue ler a fonte se o
repositório do aluno for **público**, de modo que fork privado quebra a imagem.

Também é fixa a convenção de pacotes da Aula 05, válida o semestre inteiro:
`br.uni9.rotasul.<contexto>.<camada>`, com os contextos `pedido`, `expedicao` e
`rastreamento`, e as camadas `web`, `service`, `repository` e `domain`.

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

  > **Nota para o professor.** O modelo 3C **não aparece no capítulo 02 do
  > AVA**: o capítulo trata de groupware, dos exemplos de sistema colaborativo
  > e dos requisitos funcionais e não funcionais, e não usa os termos
  > comunicação, coordenação e cooperação como modelo. O 3C entra aqui vindo de
  > PIMENTEL e FUCKS, *Sistemas Colaborativos*, que é a única referência
  > bibliográfica listada pelo próprio capítulo. Dizer isso à turma ao
  > apresentar o modelo evita a pergunta "em que página do AVA está isso?" sem
  > resposta. Pela mesma razão, o quiz de hoje cobra conteúdo do capítulo, e
  > não o 3C.

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
dois diagramas em `docs/arquitetura/`, um de componentes e um de implantação,
cada um com o seu `.puml` e o `.md` irmão que embute a imagem pelo proxy.
Critério de aceitação: o diagrama de componentes com no mínimo quatro
componentes e as interfaces entre eles, o de implantação com no mínimo três
nós, os dois aparecendo como imagem na página do `.md` no fork, e a
justificativa da escolha citando pelo menos duas das seis características de
sistemas distribuídos do capítulo.

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
**esboços de arquitetura**: a notação vem pronta nos esqueletos que o professor
projeta, e o que se cobra hoje é a **decisão**, quais componentes existem e
quem depende de quem. A Aula 05 é que explica de onde vem essa notação, o que
cada símbolo significa e o que torna um diagrama rigoroso, e manda revisar o
que sair daqui.

A ferramenta é o **PlantUML**, e a escolha é pela notação: ele tem os diagramas
da UML com o desenho certo, `component` com as interfaces em pirulito e
soquete, `node` para implantação, `package` para pacotes e `class` para classes.
Nada de aproximar componente com fluxograma.

O diagrama é escrito em texto, e o texto fica versionado no fork ao lado do
código, o que faz o `git diff` mostrar a evolução da modelagem. Para que a
imagem apareça no GitHub, que não renderiza `.puml`, cada diagrama entra como
**dois arquivos**: o `.puml` com a fonte, e um `.md` irmão que embute a imagem
pelo proxy oficial do PlantUML, apontando para o `raw` do fork do aluno.

**Duas limitações, e o professor precisa declarar as duas em voz alta agora,
não quando a imagem quebrar:** a renderização depende de um serviço externo, o
`plantuml.com`, então se ele estiver fora do ar a imagem some do `.md`, e nesse
caso o `.puml` versionado continua sendo a fonte de verdade; e o proxy só
consegue ler a fonte se o repositório do aluno for **público**, de modo que
quem tornar o fork privado perde a imagem.

1. **Preparar a pasta.** Criar `docs/arquitetura/` no fork.
2. **Listar os componentes.** Antes de desenhar, escrever numa folha os
   componentes de software que a Rota Sul precisa ter, partindo das interações
   mapeadas em `docs/colaboracao.md`. Mínimo de quatro. Os quatro que a maior
   parte das listas contém: recebimento de pedidos, montagem de remessas,
   rastreamento e ocorrências, e integração com parceiros. Estes quatro nomes
   não são coincidência: eles reaparecem na Aula 19 como quatro processos
   separados.
3. **Desenhar o diagrama de componentes.** Criar
   `docs/arquitetura/componentes.puml`. Cada componente é declarado com
   `component`, e o que um oferece ao outro é declarado com `interface`. A
   pergunta que orienta cada ligação é: **que operação este componente oferece,
   e quem depende dela?** Na notação, `--` liga o componente à interface que
   ele **oferece**, e `--(` liga o componente à interface que ele **consome**.
   O esqueleto mínimo, para o professor projetar:

   ```
   @startuml
   title Componentes da Rota Sul

   component "Recebimento de pedidos" as pedidos
   component "Montagem de remessas" as expedicao
   component "Rastreamento e ocorrências" as rastreamento
   component "Integração com parceiros" as parceiros

   interface "receberPedidoValidado" as iPedido
   interface "registrarEvento" as iEvento
   interface "despacharUltimaMilha" as iUltimaMilha

   expedicao -up- iPedido
   pedidos --( iPedido

   rastreamento -up- iEvento
   expedicao --( iEvento
   parceiros --( iEvento

   parceiros -up- iUltimaMilha
   expedicao --( iUltimaMilha
   @enduml
   ```

   Cada aluno adapta esse esqueleto ao que ele mesmo mapeou, e precisa
   acrescentar pelo menos uma interface que não esteja no exemplo.
4. **Criar o `.md` irmão e conferir a imagem.** Criar
   `docs/arquitetura/componentes.md` com um título e a linha que embute a
   imagem, trocando `SEU_USUARIO` pelo nome de usuário do aluno no GitHub:

   ```markdown
   # Componentes da Rota Sul

   ![Diagrama de componentes da Rota Sul](https://www.plantuml.com/plantuml/proxy?cache=no&src=https://raw.githubusercontent.com/SEU_USUARIO/uninove-2026-2-rota-sul/main/docs/arquitetura/componentes.puml)
   ```

   Commitar, empurrar e abrir o `.md` na página do fork. A imagem precisa
   aparecer desenhada. Se aparecer um retângulo com texto de erro, o problema é
   sintaxe no `.puml`; se não aparecer nada, o caminho do `src` está errado ou
   o fork está privado.

### Ciclo 4, 21h25 às 21h50

5. **Desenhar o diagrama de implantação.** Criar
   `docs/arquitetura/implantacao.puml` e o `implantacao.md` irmão, no mesmo
   molde do passo 4. Aqui a pergunta muda: não é mais quem depende de quem, é
   **onde cada coisa roda**. Cada máquina é um `node`, com estereótipo entre
   `<<` e `>>` dizendo que tipo de nó é, e o que roda dentro dela é um
   `artifact` ou um `database`. Mínimo de três nós. Exemplo de partida: a
   estação do atendente e do expedidor, o dispositivo móvel do motorista, o
   servidor de aplicação, o servidor de banco de dados e o sistema do parceiro,
   que roda fora da Rota Sul. Marcar em cada ligação se a comunicação é síncrona
   ou assíncrona, usando a definição formal do Ciclo 1. O esqueleto mínimo:

   ```
   @startuml
   title Implantação da Rota Sul

   node "Estação do atendente e do expedidor" as estacao <<device>> {
     artifact "Navegador" as navegador
   }

   node "Dispositivo móvel do motorista" as celular <<device>> {
     artifact "Aplicativo de rota" as appRota
   }

   node "Servidor de aplicação" as servidorApp <<server>> {
     artifact "rotasul.jar, Spring Boot" as aplicacao
   }

   node "Servidor de banco de dados" as servidorBanco <<server>> {
     database "MySQL 8.4, schema rotasul" as banco
   }

   node "Sistema do parceiro, fora da Rota Sul" as sistemaParceiro <<externo>>

   navegador --> aplicacao : HTTP, síncrono
   appRota --> aplicacao : HTTP, síncrono
   aplicacao --> banco : JDBC, síncrono
   aplicacao --> sistemaParceiro : integração, assíncrono
   @enduml
   ```

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
arquivos em `docs/arquitetura/`, `componentes.puml` e `componentes.md`,
`implantacao.puml` e `implantacao.md`. Critério de aceitação: as duas imagens
aparecendo na página do `.md` no fork; componentes com no mínimo quatro
componentes e as interfaces entre eles; implantação com no mínimo três nós e as
ligações marcadas como síncronas ou assíncronas; justificativa citando pelo
menos duas das seis características do capítulo.

### Fechamento, 21h50 às 22h00

- `git add docs/arquitetura-colaborativa.md docs/arquitetura docs/decisoes.md`
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
**Entregável:** dois diagramas UML formalizados em `docs/arquitetura/`, um de
classes do domínio e um de pacotes, cada um com o seu `.puml` e o `.md` irmão,
mais a revisão do diagrama de componentes da Aula 04. Critério de aceitação: o
diagrama de classes contendo as nove entidades do case com atributos e
relacionamentos com multiplicidade, o diagrama de pacotes refletindo a
estrutura `br.uni9.rotasul` que a Aula 06 vai usar para escrever código, e as
três imagens aparecendo na página dos `.md` no fork.

### Retomada, 5 minutos

Na Aula 04 cada aluno entregou `docs/arquitetura-colaborativa.md` e os dois
esboços em `docs/arquitetura/`, um de componentes e um de implantação. Projetar
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

- **Demonstração no projetor.** Abrir o `componentes.puml` da Aula 04 e mostrar,
  ao vivo, que a notação de componentes que a turma usou na semana passada é a
  notação da UML de que o capítulo fala: `component` desenha o retângulo com o
  ícone de componente no canto, e `interface` desenha o pirulito da interface
  oferecida e o soquete de quem a consome. Ligar isso à frase do capítulo, de
  que o diagrama de componentes mostra quais dados o componente precisa e quais
  respostas ele dá. Em seguida, desenhar do zero um diagrama de classes com
  duas entidades do case, `Remessa` e `Volume`, com atributos, tipos e a
  multiplicidade `1..*` entre elas. Mostrar como a multiplicidade responde uma
  pergunta que o esboço da semana passada não respondia.

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
   `docs/arquitetura/componentes.puml`, da Aula 04, e conferir três coisas que
   na semana passada podiam ter passado: toda interface declarada tem nome de
   operação, e não descrição de conteúdo, `receberPedidoValidado` em vez de
   `pedido validado`; cada interface está ligada com `--` ao componente que a
   **oferece** e com `--(` ao que a **consome**, e não o contrário; e nenhum
   componente ficou sem interface, porque componente que não oferece nada nem
   consome nada não é componente, é caixa solta. Salvar por cima. O histórico do
   Git guarda a versão anterior, e é ele que mostra a evolução do aluno.
2. **Listar as classes do domínio.** Escrever as nove entidades do case:
   `Cliente`, `Pedido`, `Remessa`, `Volume`, `Rota`, `Veiculo`, `Motorista`,
   `Ocorrencia` e `Parceiro`. Para cada uma, no mínimo três atributos com tipo.
   Sem métodos por enquanto: o comportamento entra na Aula 06, quando as
   camadas aparecem.
3. **Desenhar o diagrama de classes.** Criar
   `docs/arquitetura/dominio.puml`, usando `class` e as associações da UML.
   Toda associação precisa de multiplicidade nas duas pontas. As decisões que a
   turma precisa tomar explicitamente, e que o professor circula perguntando:
   - um `Pedido` gera uma ou várias `Remessa`?
   - uma `Remessa` tem quantos `Volume`?
   - uma `Ocorrencia` se liga ao `Volume`, à `Remessa` ou aos dois?
   - o `Parceiro` se liga à `Remessa` ou ao `Volume` da última milha?
   Não há gabarito único. Há gabarito coerente: qualquer escolha vale, desde
   que o diagrama inteiro fique consistente com ela.

   Esqueleto de partida, para o professor projetar:

   ```
   @startuml
   title Classes do domínio da Rota Sul

   class Pedido {
     +Long id
     +LocalDateTime criadoEm
     +String situacao
   }

   class Remessa {
     +Long id
     +String codigoRastreio
     +LocalDate previsaoEntrega
   }

   class Volume {
     +Long id
     +BigDecimal pesoKg
     +String etiqueta
   }

   Pedido "1" -- "1..*" Remessa
   Remessa "1" -- "1..*" Volume
   @enduml
   ```

4. **Criar o `.md` irmão e conferir a imagem.** Criar
   `docs/arquitetura/dominio.md` com a mesma linha de imagem do passo 4 da Aula
   04, trocando o nome do arquivo para `dominio.puml`. Commitar, empurrar e
   abrir o `.md` na página do fork. As nove classes precisam aparecer
   desenhadas, com os atributos dentro de cada caixa e a multiplicidade nas
   pontas das associações.

### Ciclo 4, 21h25 às 21h50

5. **Desenhar o diagrama de pacotes.** Criar `docs/arquitetura/pacotes.puml` e o
   `pacotes.md` irmão. Aqui a notação é `package`, aninhado, com pelo menos uma
   classe dentro de cada pacote para que ele não fique vazio, e a dependência
   entre pacotes desenhada com a seta tracejada `..>`. A estrutura é a que a
   Aula 06 vai criar de verdade no código, e por isso os nomes são fixados agora
   e não mudam:

   ```
   @startuml
   title Pacotes da Rota Sul

   package "br.uni9.rotasul" {

     package "pedido" {
       package "pedido.web" as web {
         class PedidoController
       }
       package "pedido.service" as service {
         class PedidoService
       }
       package "pedido.repository" as repository {
         interface PedidoRepository
       }
       package "pedido.domain" as domain {
         class Pedido
       }
     }

     package "expedicao" {
       class RemessaService
     }

     package "rastreamento" {
       class OcorrenciaService
     }
   }

   web ..> service
   service ..> repository
   service ..> domain
   repository ..> domain
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

**Entregável do dia:** `docs/arquitetura/dominio.puml` e `dominio.md`,
`docs/arquitetura/pacotes.puml` e `pacotes.md`, mais o `componentes.puml`
revisado. Critério de aceitação: as três imagens aparecendo na página dos `.md`
no fork; as nove entidades presentes no diagrama de classes, todas com
atributos tipados e todas as associações com multiplicidade nas duas pontas; o
diagrama de pacotes com os três contextos e as quatro camadas, e as
dependências apontando de `web` para `service` e de `service` para
`repository`.

### Fechamento, 21h50 às 22h00

- `git add docs/arquitetura docs/decisoes.md`
- `git commit -m "docs(uml): formaliza classes do domínio e pacotes da Rota Sul"`
- `git push`
- Abrir os três `.md` de `docs/arquitetura/` na página do fork no GitHub e
  conferir que as três imagens aparecem. Se alguma não aparecer, conferir nesta
  ordem: o fork está público, o caminho do `src` bate com o caminho real do
  `.puml`, e o `.puml` não tem erro de sintaxe.
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

Na Aula 05 cada aluno entregou `docs/arquitetura/pacotes.puml`, com os três
contextos e as quatro camadas, e `docs/arquitetura/dominio.puml`, com as
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

- **Demonstração no projetor.** Abrir o `docs/arquitetura/componentes.puml` da
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
   `docs/arquitetura/pacotes.puml`.
2. **Escrever o domínio.** Em `pedido/domain`, criar a classe `Pedido` com os
   atributos que o aluno já definiu no diagrama de classes da Aula 05, no
   mínimo `id`, `cliente`, `descricao` e `situacao`, com construtor e
   getters. Sem anotação de framework nenhuma nesta classe: o domínio não
   depende de Spring, e isso vai importar na Aula 12.
3. **Escrever o contrato de persistência.** Em `pedido/repository`, criar a
   **interface** `PedidoRepository` com dois métodos, `salvar(Pedido)` e
   `listarTodos()`. Interface primeiro, implementação depois: é a interface que
   permite trocar a implementação sem tocar no serviço, e é isso que vai
   acontecer quando o banco real entrar na Aula 14, ainda no Módulo 3.
4. **Escrever a implementação em memória.** Ainda em `pedido/repository`, criar
   `PedidoRepositoryEmMemoria`, anotada com `@Repository`, guardando os pedidos
   numa `List` e gerando o `id` com um contador. Dizer em voz alta por que
   memória e não banco: o capítulo de hoje trata de camadas, não de
   persistência, e trocar essa classe por uma implementação com banco é
   exatamente o exercício da Aula 14, que usa JDBC puro, e depois da Aula 15,
   que troca o JDBC por JPA. A separação de hoje é o que torna as duas trocas
   baratas.
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

---

## Aula 07, Arquitetura orientada a serviços, SOA

**Módulo:** M2, Integração e serviços distribuídos
**Capítulo do AVA:** `pdf/006.pdf`, Arquitetura Orientada a Serviços (SOA)
**Entregável:** a interface `PedidoService` no pacote
`br.uni9.rotasul.pedido.service`, com duas implementações trocáveis por perfil
do Spring, `PedidoServicePadrao` e `PedidoServiceComAnaliseDeRisco`, mais uma
suíte de teste JUnit 5 que roda os mesmos casos contra as duas implementações.
Critério de aceitação: as duas implementações passando na mesma suíte com
`./mvnw test`, nenhuma anotação de framework na interface, e o
`PedidoController` chamando apenas a interface, sem conhecer nenhuma das
classes concretas.

### Retomada, 5 minutos

Na Aula 06 cada aluno entregou a primeira fatia em três camadas do pacote
`br.uni9.rotasul.pedido`, com `PedidoController`, `PedidoService` como classe
concreta, a interface `PedidoRepository` e a implementação em memória.
Projetar o `PedidoService` de um aluno e apontar: ele é uma classe, não uma
interface, e o `PedidoController` depende diretamente dela. Perguntar à turma:
e se a Rota Sul precisar de duas formas diferentes de decidir se aceita um
pedido, uma para o fluxo normal e outra para quando o lojista está sob análise
de risco? Hoje o controlador precisaria mudar. A aula de hoje resolve isso do
mesmo jeito que a Aula 06 já resolveu para o repositório: separando contrato
de implementação, agora na camada de serviço.

### Ciclo 1, 19h30 às 20h05

- **Conceito.** Como componentes de software trocam mensagens, na descrição do
  capítulo [1], que é a base sobre a qual o modelo SOA se apoia.

  **Componente de software, revisitado.** O capítulo retoma a definição já
  vista na Aula 06 e a aplica à comunicação: componente de software é a parte
  do sistema responsável por executar um único serviço, como validar um número
  de CPF, verificar os dados de um endereço a partir de um CEP, ou gerar um
  número de identificação de usuário ao gravar seus dados numa base. Esse
  conceito é o mais comum ao modelo de Arquitetura Orientada a Serviços, SOA,
  sigla de *Service Oriented Architecture*, que orienta o desenvolvedor a
  basear o projeto em componentes que executam serviços específicos e se
  comunicam entre si, seja para realizar um serviço, seja para solicitar que
  outro componente o faça.

  **Comunicação entre componentes.** Um componente se comunica com outro por
  troca de mensagens: quem envia inicia a comunicação solicitando um
  processamento, quem recebe verifica o que precisa fazer e executa, e ao
  final envia outra mensagem de volta, com a resposta. Uma mensagem carrega ou
  uma solicitação de serviço ou o resultado de um processamento. Controlar
  esse tráfego exige uma estratégia.

  **Ponto a ponto, ou unicast.** Os dados são inseridos no sistema por um nó,
  que faz uma cópia da mensagem e a envia a um nó, ou conjunto de nós,
  conectados na rede. É chamado ponto a ponto porque só os nós de origem e de
  destino processam a mensagem; os demais apenas a repassam. O processamento é
  simples e rápido, mas cada novo cliente adicionado aumenta o uso da rede, e
  o capítulo lista três problemas que podem surgir: atraso nas transmissões,
  perda de sincronismo nas mensagens e escalabilidade que se torna inviável.

  **Cliente-servidor, como mitigação.** A mensagem inserida no sistema vai
  para um servidor que centraliza o processamento, e o servidor a distribui
  aos clientes. Vantagem: os clientes não precisam ficar sempre conectados,
  o que reduz o uso da rede. Problema: com o processamento centralizado
  espalhado por vários servidores, é possível que mais de um processe a mesma
  mensagem, gerando redundância.

  **Unicast, em geral.** Os dois modelos acima são unicast: um nó determina o
  nó, ou nós, que deve receber a mensagem, o que costuma exigir verificação de
  recebimento em cada nó, aumentando o processamento. Esse custo pode ser
  reduzido com broadcast ou multicast.

  **Broadcast.** Funciona como uma transmissão de rádio ou TV: um nó envia a
  mensagem, ela fica disponível a todo nó conectado na rede, e só quem deseja
  a processa. Isso evita redundância, mas exige que a rede suporte esse tipo
  de envio, e que os interessados estejam conectados no momento do envio,
  porque a mensagem é descartada depois de um tempo.

  **A convergência para o SOA.** O capítulo observa que combinar vários
  modelos de comunicação é comum, mas isso soma tanto as vantagens quanto as
  desvantagens de cada um. Para reduzir o impacto negativo, surgiu um modelo
  em que os nós podem desempenhar, ao mesmo tempo, os papéis de cliente e
  servidor. É esse modelo híbrido que torna o SOA popular, e é o assunto do
  Ciclo 2.

- **Demonstração no projetor.** Duas situações da Rota Sul, para distinguir os
  modelos na prática. Primeiro, o atendente liga para um motorista específico
  perguntando onde está o volume: ponto a ponto, só os dois nós participam,
  como já visto na Aula 03. Segundo, um alarme sonoro soa no armazém avisando
  todos os expedidores presentes de que um caminhão está atrasado: broadcast,
  a mensagem chega a todos os conectados, e só quem está prestando atenção a
  processa.

- **Exercício curto.** Cinco minutos, individual. Classificar três comunicações
  da Rota Sul como ponto a ponto, cliente-servidor ou broadcast: (a) o
  atendente liga para o motorista X perguntando sua posição; (b) o painel de
  ocorrências mostra, ao mesmo tempo, para todos os expedidores conectados,
  uma ocorrência recém-registrada; (c) o sistema recebe todos os pedidos do
  dia num servidor central, que os distribui aos expedidores conforme a rota.
  Gabarito: (a) ponto a ponto, (b) broadcast, (c) cliente-servidor.

### Ciclo 2, 20h05 às 20h40

- **Conceito.** O modelo de Arquitetura Orientada a Serviços, SOA, na
  definição do capítulo.

  **Serviço.** No modelo SOA, o termo serviço tem significado parecido com o
  de componente de software: é um componente que executa uma funcionalidade,
  independente dos demais e autocontido, ou seja, capaz de terminar o que está
  fazendo independentemente de o resultado do processamento ser negativo ou
  positivo. A forma de identificar os serviços de um sistema é praticamente a
  mesma usada para projetar componentes: o projetista identifica quais
  serviços o software precisa e como eles se comunicam, seja por metadados,
  seja por mensagens.

  **Os três componentes principais do modelo SOA:**

  - **Provedor de Serviço.** Executa um determinado serviço e mantém a rede
    informada sobre qual tipo de serviço está oferecendo.
  - **Serviço de Descoberta.** Armazena a localização dos serviços disponíveis
    na rede e conecta o serviço solicitado a quem o solicitou.
  - **Consumidor.** É quem solicita a execução de um serviço.

  O SOA se apoia no modelo de comunicação híbrida do Ciclo 1: um nó pode ser
  ao mesmo tempo Provedor e Consumidor.

  **Descrição de Serviço e interface de serviço.** Todo Provedor de Serviços
  define uma Descrição de Serviço: o que ele faz e quais informações o
  Consumidor precisa fornecer para usá-lo. Com isso, o Consumidor decide se o
  serviço atende às suas necessidades e como se conectar à interface de
  serviço, que é um conjunto de métodos invocáveis mais os tipos de dados
  usados na invocação. A interface permite que o Consumidor use o serviço sem
  saber como o Provedor funciona por dentro, o que é a base do reuso de
  software no modelo SOA.

  **Consequências dessas características.** Um sistema SOA é, por
  construção, um sistema distribuído, provavelmente rodando num ambiente
  heterogêneo, o que exige interoperabilidade: o Provedor pode ser acessado
  por Consumidores de outros aplicativos, escritos com outras tecnologias, e
  por isso precisa de padrões de protocolo e de metadados. O resultado é baixo
  acoplamento entre os componentes, que podem ser localizados e invocados
  dinamicamente. O capítulo acrescenta que é possível combinar serviços já
  existentes para criar novos serviços, e que nesse caso é necessário um
  componente que coordene a execução dos serviços combinados.

  **Aplicando o modelo a sistemas colaborativos.** O capítulo fecha ligando o
  SOA aos assuntos das Aulas 03 e 04: nos aplicativos colaborativos, os
  usuários podem atuar tanto como Provedores, ao criar e publicar um serviço,
  quanto como Consumidores, ao pesquisar um serviço que atenda a uma
  necessidade e invocá-lo.

- **Demonstração no projetor.** Abrir `docs/arquitetura/componentes.puml`, da
  Aula 05, e reler o diagrama com o vocabulário de hoje: o componente
  "Integração com parceiros" é um Provedor de Serviço, que oferece a interface
  `despacharUltimaMilha`; o componente "Montagem de remessas" é o Consumidor
  dessa interface. O diagrama que a turma desenhou há duas aulas já é, sem que
  ninguém tivesse dito o nome, um desenho de arquitetura orientada a serviços.
  Falta uma peça: o capítulo cita como exemplo real de Provedor de Serviço o
  serviço de consulta de CEP dos Correios, que a Aula 10 vai usar como modelo
  para o parceiro legado da Rota Sul.

- **Exercício curto.** Cinco minutos, em duplas. Para cada interação, decidir
  quem é o Provedor e quem é o Consumidor: (a) o motorista solicita ao
  servidor da Rota Sul a lista de entregas do dia; (b) o parceiro da última
  milha avisa a Rota Sul que um volume foi entregue; (c) o atendente da Rota
  Sul consulta o serviço de CEP dos Correios para validar um endereço.
  Gabarito: (a) Provedor é o servidor da Rota Sul, Consumidor é o aplicativo
  do motorista; (b) Provedor é o parceiro, Consumidor é a Rota Sul; (c)
  Provedor são os Correios, Consumidor é a Rota Sul.

### Quiz, 20h40 às 20h50

**Pergunta.** A Rota Sul decide expor a montagem de remessas como um serviço
que outros componentes podem invocar sem conhecer sua implementação interna.
Segundo o capítulo, qual afirmação descreve corretamente o conceito de serviço
no modelo SOA?

- A) Um serviço SOA é um conceito completamente diferente de componente de
  software, sem relação entre os dois.
- B) No modelo SOA, o termo serviço tem significado parecido com o de
  componente de software: é um componente independente e autocontido, capaz
  de terminar o que está fazendo independentemente de o resultado do
  processamento ser positivo ou negativo.
- C) Um serviço SOA só pode ser consumido por aplicativos escritos na mesma
  linguagem de programação do Provedor.
- D) O modelo SOA elimina a necessidade de qualquer comunicação em rede entre
  os componentes.

**Correta:** B.

**Justificativa.** É a definição literal do capítulo: o termo serviço tem
significado parecido com o de componente de software, e um serviço é
independente e autocontido, terminando o que está fazendo independentemente
do resultado ser positivo ou negativo. A alternativa A nega a relação que o
capítulo estabelece explicitamente entre os dois conceitos. A C contraria a
interoperabilidade que o capítulo aponta como consequência natural do
ambiente heterogêneo em que o SOA opera. A D ignora que toda a arquitetura
SOA existe justamente para orquestrar comunicação em rede entre Provedores e
Consumidores.

### Ciclo 3, 20h50 às 21h25

Laboratório de separação de contrato. O código de hoje não cria endpoint novo:
ele reorganiza o `pedido.service` que a Aula 06 entregou, aplicando à camada
de serviço a mesma lição que a Aula 06 já aplicou à camada de repositório.

1. **Extrair a interface.** Em `pedido/service`, criar a interface
   `PedidoService` com as duas assinaturas já existentes: `Pedido
   registrar(Pedido pedido)` e `List<Pedido> listar()`. Nenhuma anotação de
   framework na interface: ela é o contrato, não a implementação.
2. **Renomear a implementação atual.** A classe `PedidoService` da Aula 06
   passa a se chamar `PedidoServicePadrao` e a implementar a interface
   `PedidoService`, mantendo o construtor que recebe `PedidoRepository` e a
   regra de recusar pedido sem cliente. Anotar com `@Service` e com
   `@Profile("padrao")`.
3. **Ajustar o controlador.** Conferir que `PedidoController` passa a receber
   `PedidoService`, a interface, no construtor, e não mais o tipo concreto.
   Se o controlador ainda importa `PedidoServicePadrao` em algum lugar, é
   sinal de que a separação não terminou.
4. **Configurar o perfil padrão.** Em `src/main/resources/application.properties`,
   acrescentar `spring.profiles.active=padrao`. Sem essa linha, nenhum bean de
   `PedidoService` fica ativo, porque os dois candidatos estão guardados por
   `@Profile`, e o Spring recusa subir sem um deles disponível. Rodar
   `./mvnw spring-boot:run` e conferir que `GET /pedidos` continua respondendo
   exatamente como na Aula 06.
5. **Criar a segunda implementação.** `PedidoServiceComAnaliseDeRisco`,
   também implementando `PedidoService`, anotada `@Service` e
   `@Profile("risco")`, recebendo `PedidoRepository` pelo mesmo construtor.
   Mantém a regra herdada, pedido sem cliente é recusado, e acrescenta uma
   segunda: um conjunto fixo de lojistas bloqueados, por exemplo
   `Set.of("LOJISTA-BLOQUEADO")`, e pedido de um lojista bloqueado também é
   recusado. A assinatura dos métodos é idêntica à da outra implementação:
   é exatamente isso que faz das duas implementações trocáveis.

### Ciclo 4, 21h25 às 21h50

6. **Escrever a suíte de contrato.** Em
   `src/test/java/br/uni9/rotasul/pedido/service/`, criar a classe abstrata
   `PedidoServiceContratoTest`, com um método `protected abstract
   PedidoService criarServico()` e dois testes: `registraPedidoValido`, que
   registra um pedido com cliente e confirma que ele aparece em `listar()`, e
   `recusaPedidoSemCliente`, que confirma a recusa. Nenhum dos dois testes
   sabe qual implementação está rodando: eles testam apenas o contrato.
7. **Estender a suíte para cada implementação.** Duas classes concretas,
   `PedidoServicePadraoContratoTest` e
   `PedidoServiceComAnaliseDeRiscoContratoTest`, cada uma implementando
   `criarServico()` para devolver a sua própria implementação, com um novo
   `PedidoRepositoryEmMemoria` a cada teste. Rodar `./mvnw test`: os dois
   métodos da classe abstrata executam duas vezes, uma para cada
   implementação, e as quatro execuções precisam passar.
8. **Confirmar a troca de perfil em tempo de execução.** Subir a aplicação com
   `./mvnw spring-boot:run -Dspring-boot.run.profiles=risco` e enviar, por
   `curl` ou pelo navegador, um `POST /pedidos` com o cliente
   `LOJISTA-BLOQUEADO`. A resposta precisa ser de recusa. Voltar a subir sem o
   parâmetro de perfil, que volta para `padrao`, e enviar o mesmo pedido: a
   resposta precisa ser de sucesso. Colar as duas evidências no commit.
9. **Registrar a decisão.** Em `docs/decisoes.md`, uma linha nova explicando o
   padrão de contrato mais implementações trocáveis por perfil, e uma frase
   ligando isso ao vocabulário de hoje: a interface é a Descrição de Serviço,
   e cada implementação é um Provedor diferente por trás do mesmo contrato.

**Entregável do dia:** a interface `PedidoService`, as duas implementações
`PedidoServicePadrao` e `PedidoServiceComAnaliseDeRisco`, e a suíte de teste
abstrata estendida pelas duas. Critério de aceitação: `./mvnw test` passando
com as quatro execuções verdes, `PedidoController` dependendo apenas da
interface, e a troca de perfil mudando o comportamento observável da API sem
qualquer alteração no controlador.

### Fechamento, 21h50 às 22h00

- `git add src docs`
- `git commit -m "feat(pedido): separa contrato PedidoService de duas implementações trocáveis por perfil"`
- `git push`
- **Prévia da Aula 08.** Hoje a Rota Sul trocou a implementação de um serviço
  sem tocar em quem o consome. Amanhã ela troca a forma de empacotar e rodar
  a aplicação inteira, comparando o `.jar` executável que a turma já usa desde
  a Aula 01 com o modelo de servidor de aplicações que o próximo capítulo
  descreve. O entregável será o `.jar` rodando sozinho, sem `./mvnw`, mais a
  comparação escrita entre os dois modelos.

### Referências

1. MESQUITA, Paulo Ricardo Batista. **Capítulo 06: Arquitetura Orientada a
   Serviços (SOA).** Arquitetura de Software. AVA, Uninove. Fonte primária
   desta aula, `pdf/006.pdf`.
2. PIMENTEL, Mariano; FUCKS, Hugo. **Sistemas Colaborativos.** Rio de Janeiro:
   Campus, 2011. Referência indicada pelo capítulo, já usada na Aula 03.
3. SWENEY, R. **Achieving Service-Oriented Architecture: Applying an
   Enterprise Architecture Approach.** Wiley, 2010. Referência indicada pelo
   capítulo.
4. Spring. **Documentação do Spring Framework**, seção de perfis (`@Profile`).
   <https://docs.spring.io/spring-framework/reference/core/beans/environment.html>
5. JUnit. **JUnit 5 User Guide.** <https://junit.org/junit5/docs/current/user-guide/>
6. `docs/arquitetura/componentes.puml` do fork do aluno, entregável da Aula
   05, usado na demonstração do Ciclo 2.

---

## Aula 08, Servidores de aplicação e a plataforma Java EE

**Módulo:** M2, Integração e serviços distribuídos
**Capítulo do AVA:** `pdf/007.pdf`, Servidores de Aplicação
**Entregável:** o `.jar` executável do projeto, gerado por `./mvnw clean
package` e rodando com `java -jar`, mais o arquivo `docs/empacotamento.md`
comparando o modelo de JAR embarcado do laboratório com o modelo de WAR em
servidor de aplicações que o capítulo descreve. Critério de aceitação: a
aplicação respondendo em `GET /pedidos` a partir do `java -jar`, sem usar
`./mvnw spring-boot:run`, e a comparação cobrindo ao menos quatro pontos:
instalação, empacotamento, portabilidade e quem fornece os serviços de
infraestrutura.

### Retomada, 5 minutos

Na Aula 07 cada aluno entregou a interface `PedidoService` com duas
implementações trocáveis por perfil, `PedidoServicePadrao` e
`PedidoServiceComAnaliseDeRisco`, mais a suíte de teste que roda contra as
duas. Retomar uma frase da aula: a interface separa contrato de
implementação. Hoje essa mesma pergunta, contrato contra implementação, sobe
um nível: não é mais sobre um serviço dentro da aplicação, é sobre a própria
aplicação. Como ela é empacotada, e o que promete a quem vai executá-la.

### Ciclo 1, 19h30 às 20h05

- **Conceito.** O que é um servidor de aplicações e por que a plataforma Java
  EE depende de um, na descrição do capítulo [1].

  **Servidor, em geral.** Um servidor provê algum tipo de serviço aos seus
  usuários: armazenamento de dados, correio eletrônico, compartilhamento de
  arquivos, e os servidores web, usados para hospedar e executar aplicativos
  na Internet. O capítulo usa redes sociais como Facebook, WhatsApp,
  Instagram e Youtube como exemplo de aplicações de grande porte, acessadas
  por browser ou dispositivo móvel, e lista quatro requisitos comuns a esse
  tipo de aplicação: uso intensivo de uma rede de dados; autenticação de
  usuários para acesso ao conteúdo e gerenciamento dele; um sistema eficiente
  para armazenar dados; e sincronização entre as informações exibidas ao
  usuário, tanto pelo browser quanto pelo dispositivo móvel, garantindo que
  ele veja exatamente a mesma coisa nos dois casos.

  **De aplicação a plataforma.** Quando uma aplicação como o Facebook fica
  complexa o bastante para permitir que outros aplicativos usem seus
  recursos, ela deixa de ser entendida apenas como aplicação e passa a ser
  entendida como plataforma. Isso traz dois requisitos extras: verificar se o
  aplicativo que quer usar os recursos é uma fonte segura, e verificar quais
  informações do usuário esse aplicativo pode acessar. Consequência direta:
  a comunicação entre aplicativos remotos, e entre os servidores que os
  executam, precisa ser segura.

  **A definição de servidor de aplicações.** É "uma ferramenta para
  desenvolver e executar aplicações de grande porte". Além de aplicações como
  o Facebook, o capítulo enquadra nessa categoria os sistemas colaborativos,
  os sistemas corporativos como os de automação bancária, e os sistemas de
  gestão empresarial conhecidos como ERP.

  **Java EE.** É uma das plataformas que resolve esse tipo de necessidade,
  com um conjunto de frameworks, modelos de programação e APIs prontas para
  os serviços de infraestrutura que aplicações de grande porte precisam. Para
  ser usada, precisa de um servidor de aplicações, que é a forma pela qual a
  plataforma é disponibilizada aos desenvolvedores. Os problemas de
  infraestrutura que o Java EE resolve: segurança no acesso às informações;
  garantia de disponibilidade dos serviços; balanceamento da carga de uso dos
  servidores; e gerenciamento das bases de dados usadas pela aplicação. Isso
  permite que o desenvolvedor foque seus esforços nas regras de negócio,
  seguindo quatro regras: seguir os padrões e especificações da Java EE; que
  seu aplicativo possa prover serviços de infraestrutura para outras
  aplicações; que ele saiba gerenciar comunicação com outros servidores de
  aplicações; e, quando possível, disponibilizar frameworks para outras
  aplicações usarem.

  **Servidores usados no mercado.** JBoss e WebSphere, instalados sobre
  Linux ou Windows. O capítulo compara com a plataforma .Net, que é similar
  em proposta, mas onde o servidor de aplicações é qualquer versão do
  servidor Windows, e não uma ferramenta específica como no caso do Java.

  **Java EE contra .Net**, na comparação do capítulo, ponto a ponto: em
  portabilidade de sistema operacional, aplicativos Java rodam em qualquer
  SO, enquanto aplicativos .Net dependem do Windows para aproveitar todo o
  potencial da plataforma, apesar de iniciativas como Mono e DotGNU para
  Linux; em escalabilidade, as duas plataformas têm mecanismos eficazes; em
  linguagens de programação, o .Net permite VB.NET, C#, C/C++ ou J#, o que
  aumenta o custo de manutenção por exigir especialistas em várias
  linguagens, enquanto o Java EE usa só Java; a curva de aprendizado das duas
  é parecida, mas o Java tem mais material disponível; e em portabilidade
  final, um aplicativo Java EE roda em qualquer sistema operacional, enquanto
  o .Net só é totalmente aproveitado no sistema operacional da Microsoft.

- **Demonstração no projetor.** Rodar `./mvnw dependency:tree | grep -i
  tomcat` no fork da turma e mostrar que um servidor web, o Tomcat, já está
  entre as dependências transitivas do projeto, puxado pelo
  `spring-boot-starter-web`, sem ninguém ter instalado nada. Perguntar à
  turma: onde está o servidor de aplicações desta disciplina? A resposta é o
  gancho para o Ciclo 2.

- **Exercício curto.** Cinco minutos, individual. Para cada um dos quatro
  requisitos do capítulo, uso intensivo de rede, autenticação, armazenamento
  eficiente e sincronização, escrever uma frase dizendo como a Rota Sul já
  atende esse requisito com o que foi construído até a Aula 07, ou dizendo
  que ainda não atende e por quê. Duas ou três leituras em voz alta.

### Ciclo 2, 20h05 às 20h40

- **Conceito.** As tecnologias da plataforma Java EE, e o contraste honesto
  entre o modelo do capítulo e o modelo do laboratório.

  **As tecnologias da Java EE**, na lista do capítulo: Enterprise JavaBeans,
  EJB, modelo de programação para componentes escritos em Java que outros
  aplicativos, dentro ou fora do servidor, podem usar; API Java para Web
  Services, JAX-WS, para expor web services baseados em Servlets e EJBs; Java
  Remote Method Invocation, RMI, para comunicação remota entre componentes
  Java, assunto da Aula 10; Java Naming and Directory Interface, JNDI, para
  acessar serviços de nomenclatura e diretório espalhados pela rede; Java
  Database Connectivity, JDBC, para acessar bancos relacionais; Java
  Transaction API e Java Transaction Service, JTA e JTS, para realizar e
  acompanhar transações remotas; Java Messaging Service, JMS, para
  componentes que executam transações baseadas em troca de mensagens; Java
  Web, o conjunto de especificações para aplicações web dinâmicas baseadas em
  páginas JSP e Servlets, base de muitos frameworks; Java Server Faces, JSF,
  framework para desenvolvimento rápido de aplicações web baseadas em
  componentes reutilizáveis do lado do servidor, assunto da Aula 18; e Java
  Persistence API, JPA, API para gerenciar conexões com bases relacionais sem
  escrever todo o SQL na mão, usando um modelo baseado em classes de
  entidades controladas por beans de sessão, assunto das Aulas 15 e 16.

  **As vantagens do Java EE**, segundo o capítulo: agilidade no
  desenvolvimento; qualidade mais efetiva, por usar componentes já testados e
  reusados; flexibilidade para moldar o aplicativo a vários modelos de
  arquitetura; e a possibilidade de desenvolver componentes reusáveis em
  outros aplicativos, expandindo as possibilidades da plataforma. Seguindo os
  padrões e sem usar função específica de um fornecedor, o aplicativo fica
  garantido de rodar em qualquer servidor de aplicações, independentemente do
  fornecedor. A conclusão do capítulo: um servidor de aplicações é o
  ambiente que permite desenvolver e executar aplicações de grande porte
  baseadas em modelos de arquitetura distribuída, usado porque já traz
  pronta a implementação dos serviços da plataforma.

  > **Nota para o professor.** O capítulo descreve o aplicativo Java EE como
  > algo que é "instalado no servidor de aplicações que será usado", sem usar
  > o termo WAR. Isso é complemento de leitura atual, não do capítulo: o
  > formato de empacotamento padrão da Java EE clássica é o WAR, *Web
  > Application Archive*, um arquivo que contém só o código da aplicação e
  > pressupõe um servidor já instalado e em execução para interpretá-lo.
  > É esse modelo, WAR mais servidor de aplicações administrado à parte, que
  > o laboratório de hoje contrasta com o `.jar` executável que a turma usa
  > desde a Aula 01.

  **O contraste com o laboratório.** No modelo do capítulo, o desenvolvedor
  empacota a aplicação num WAR, que contém só o código dela, e a instala num
  servidor de aplicações, JBoss ou WebSphere, instalado e administrado à
  parte, que fornece os serviços de infraestrutura, segurança, transação,
  acesso a diretório, pool de conexão, via as APIs da Java EE. No laboratório
  da disciplina, decisão registrada na ADR-001 da spec do acervo, o Spring
  Boot embarca o próprio servidor web dentro do `.jar` que a build gera: não
  há servidor de aplicações separado para instalar, e `java -jar` já sobe a
  aplicação inteira. Boa parte do que a Java EE resolve com JTA, JNDI e EJB
  tem hoje equivalente dentro do próprio Spring, sem precisar de um servidor
  externo, o que a Aula 12 formaliza como inversão de controle.

- **Demonstração no projetor.** Rodar `./mvnw clean package` e, ao terminar,
  `jar tf target/*.jar | head -30`, mostrando as entradas `BOOT-INF/classes`,
  com as classes do aluno, `BOOT-INF/lib`, com o Tomcat embarcado e as demais
  dependências, e `META-INF/MANIFEST.MF`. Abrir o `MANIFEST.MF` com `unzip -p
  target/*.jar META-INF/MANIFEST.MF` e apontar duas linhas: `Start-Class`,
  que aponta para a classe do aluno, e `Main-Class`, que aponta para o
  launcher do próprio Spring Boot, não para o código do aluno. É esse launcher
  que sobe o Tomcat embarcado antes de entregar o controle à aplicação.

- **Exercício curto.** Cinco minutos, em duplas. Duas colunas no caderno: "o
  que o servidor de aplicações do capítulo faz por você" e "quem faz isso na
  Rota Sul hoje", para quatro itens: segurança de acesso, balanceamento de
  carga, gerenciamento de bases de dados, hospedagem HTTP. Gabarito parcial,
  para o professor conferir: hospedagem HTTP é o Tomcat embarcado; gerenciamento
  de bases de dados vai ser o Spring Data JPA a partir do Módulo 4; segurança e
  balanceamento ainda não existem no fork, e isso é lacuna consciente do
  estágio atual, não erro.

### Quiz, 20h40 às 20h50

**Pergunta.** Segundo o capítulo, qual das alternativas a seguir NÃO é um dos
requisitos que ele associa a aplicativos de grande porte, como as redes
sociais usadas como exemplo?

- A) Autenticação de usuários para o acesso ao conteúdo postado e
  gerenciamento de seu conteúdo.
- B) Uso intensivo de uma rede de dados.
- C) Sincronização entre as informações exibidas para um usuário, tanto pelo
  browser quanto pelo dispositivo móvel.
- D) Interface de usuário desenhada com um tema visual atraente.

**Correta:** D.

**Justificativa.** O capítulo lista, textualmente, quatro requisitos comuns a
aplicativos de grande porte: uso intensivo de rede, autenticação, um sistema
eficiente de armazenamento de dados, e sincronização entre o que é exibido no
browser e no dispositivo móvel. As alternativas A, B e C reproduzem três
desses quatro requisitos. A D fala de um atributo visual da interface, que
nenhuma parte do capítulo menciona como requisito de infraestrutura: toda
aplicação precisa de alguma interface, mas o capítulo nunca condiciona isso a
um "tema visual atraente", que é critério de design, não de infraestrutura.

### Ciclo 3, 20h50 às 21h25

Laboratório de empacotamento. Nenhuma linha de regra de negócio muda hoje: o
código de produção da Rota Sul continua o mesmo das Aulas 06 e 07, só a forma
de rodá-lo muda.

1. **Confirmar o empacotamento.** Abrir o `pom.xml` do fork e localizar o
   plugin `spring-boot-maven-plugin` dentro de `<build><plugins>`. É ele que
   transforma o `.jar` comum, que só teria o código do aluno, num `.jar`
   executável, com o Tomcat e as demais dependências embutidos.
2. **Gerar o `.jar`.** Parar qualquer `./mvnw spring-boot:run` em execução e
   rodar `./mvnw clean package`. Ao final, conferir que existe um arquivo em
   `target/`, terminado em `.jar`.
3. **Rodar com `java -jar`.** Num terminal novo, `java -jar target/*.jar`,
   trocando pelo nome real do arquivo gerado. Conferir no log a mesma
   inicialização e a mesma linha de porta de sempre, e chamar `GET /pedidos`
   na porta que o terminal imprimiu. Nenhum servidor de aplicações foi
   instalado para isso acontecer.
4. **Inspecionar o `.jar` por dentro.** Repetir a inspeção da demonstração,
   agora com as mãos do aluno: `jar tf target/*.jar | head -30` e abrir o
   `MANIFEST.MF`, localizando `Start-Class` e `Main-Class`.
5. **Escrever a comparação.** Criar `docs/empacotamento.md`, com uma tabela de
   quatro linhas, colunas `Aspecto`, `Modelo do capítulo, Java EE mais
   servidor de aplicações` e `Modelo do laboratório, Spring Boot com JAR
   executável`. Linhas mínimas: instalação (instala e administra JBoss ou
   WebSphere à parte, contra nenhuma instalação, `java -jar` já sobe tudo);
   empacotamento (WAR, só o código da aplicação, contra JAR, aplicação mais
   servidor embarcado); portabilidade (depende do servidor de aplicações do
   ambiente de destino, contra roda em qualquer máquina com a JVM 21); e quem
   fornece os serviços de infraestrutura (o servidor de aplicações, via JTA,
   JNDI e EJB, contra o próprio framework Spring, via inversão de controle,
   tema da Aula 12).

### Ciclo 4, 21h25 às 21h50

6. **Escrever a conclusão.** Ao final de `docs/empacotamento.md`, um
   parágrafo respondendo por que a indústria migrou do modelo do capítulo
   para o modelo do laboratório: o custo de instalar e administrar um
   servidor de aplicações em cada ambiente, a agilidade de empacotar tudo
   junto para rodar em contêineres, prévia da Aula 19, e o fato de boa parte
   dos serviços que a Java EE resolvia com JTA, JNDI e EJB terem hoje um
   equivalente mais simples dentro do próprio Spring. O parágrafo precisa
   citar pelo menos um serviço da Java EE e dizer o que faz o papel dele no
   laboratório.
7. **Conferir o `.gitignore`.** Garantir que `target/` está listado, para o
   `.jar` gerado não ser commitado. O que vai para o fork é a comparação
   escrita, não o binário.
8. **Registrar a decisão.** Em `docs/decisoes.md`, uma linha nova registrando
   a escolha de empacotamento executável em vez de WAR, com a justificativa
   resumida em uma frase.

**Entregável do dia:** o `.jar` executável rodando com `java -jar`, com a
evidência de `GET /pedidos` colada no commit, mais `docs/empacotamento.md`
com a tabela de comparação e a conclusão. Critério de aceitação: a tabela
cobrindo os quatro aspectos mínimos, a conclusão citando pelo menos um
serviço da Java EE com o seu equivalente no laboratório, e `target/` fora do
commit.

### Fechamento, 21h50 às 22h00

- `git add docs/empacotamento.md docs/decisoes.md`
- `git commit -m "docs(empacotamento): compara o JAR executável do laboratório com o modelo WAR do capítulo"`
- `git push`
- **Prévia da Aula 09.** Hoje a comparação foi sobre como a aplicação roda.
  Amanhã ela é sobre como a aplicação fala com quem consome os seus dados: os
  dois formatos de metadados que o próximo capítulo descreve, XML e JSON,
  aplicados a uma entidade nova da Rota Sul, `Remessa`. O entregável será um
  endpoint que responde nos dois formatos, dependendo do que o cliente pedir.

### Referências

1. MESQUITA, Paulo Ricardo Batista. **Capítulo 07: Servidores de Aplicação.**
   Arquitetura de Software. AVA, Uninove. Fonte primária desta aula,
   `pdf/007.pdf`.
2. Site do Java EE, Oracle. Referência indicada pelo capítulo.
   <http://www.oracle.com/technetwork/java/javaee/overview/index.html>
3. `docs/superpowers/specs/2026-08-10-acervo-arquitetura-software-design.md`,
   seção 6.1, ADR-001, decisão de usar Spring Boot no lugar de Jakarta EE
   clássico.
4. Spring. **Documentação do Spring Boot.**
   <https://docs.spring.io/spring-boot/index.html>
5. Oracle. **Java SE 21 Documentation.**
   <https://docs.oracle.com/en/java/javase/21/>

---

## Aula 09, Metadados para troca de dados: XML e JSON

**Módulo:** M2, Integração e serviços distribuídos
**Capítulo do AVA:** `pdf/008.pdf`, Metadados para Troca de Dados (XML e JSON)
**Entregável:** o endpoint `GET /remessas/{id}`, no novo contexto
`br.uni9.rotasul.expedicao`, respondendo em JSON ou em XML conforme o
cabeçalho `Accept` da requisição, usando Jackson, mais um teste JUnit 5 que
confirma os dois formatos. Critério de aceitação: `Accept: application/json`
devolvendo JSON, `Accept: application/xml` devolvendo XML válido, ambos com os
mesmos dados da `Remessa`, e `./mvnw test` passando.

### Retomada, 5 minutos

Na Aula 08 cada aluno entregou o `.jar` executável rodando com `java -jar` e
`docs/empacotamento.md`, comparando esse modelo com o WAR do capítulo.
Retomar: hoje a aplicação já roda sozinha, sem servidor de aplicações. A
pergunta de hoje é diferente: quando essa aplicação responde a quem pediu
alguma coisa, em que formato ela responde, e quem decide isso, ela ou quem
perguntou?

### Ciclo 1, 19h30 às 20h05

- **Conceito.** Metadados, e o formato XML, na descrição do capítulo [1].

  **Metadados.** São informações a respeito de outros dados, e existem desde
  os anos 1970, usados inicialmente para armazenar dados dos aplicativos e,
  depois, para comunicação e compartilhamento de informação entre eles.
  Costumam ser escritos em texto simples, por ser o formato mais fácil de
  processar e transmitir pela rede. Nos anos 1990, a Internet trouxe novos
  tipos de metadados baseados em padrões abertos, XML e JSON. A principal
  vantagem dos dois: podem ser escritos e lidos por rotinas de qualquer
  linguagem de programação, e os dois padrões definem só como os metadados
  devem ser formatados e referenciados, deixando os nomes livres para o
  desenvolvedor escolher. Por isso, arquivos JSON ou XML podem funcionar como
  protocolo ou interface de comunicação entre sistemas, o que os liga
  diretamente ao SOA da Aula 07.

  **XML, eXtensible Markup Language.** É uma recomendação do consórcio W3C,
  linguagem de marcação com cinco princípios, todos do capítulo: separar o
  conteúdo a ser apresentado da formatação do conteúdo, em arquivos DTD; ser
  uma estrutura entendível tanto por máquinas quanto por seres humanos; não
  ter limite na quantidade de tags que podem ser criadas; servir de agente de
  transporte de informação entre sistemas e bases de dados distintos; e
  manter o foco do desenvolvedor no conteúdo a ser transmitido, não na
  aparência. Por causa dessa liberdade, o XML popularizou-se além da
  tecnologia da informação, em telecomunicações, saúde e aplicações
  governamentais, e outros padrões nasceram baseados nele, como o XHTML, o
  protocolo de mensagens MMS e os próprios Web Services.

  **Estrutura.** Uma tag inicial declara a versão do XML e a codificação de
  caractere usada. As demais tags são hierárquicas, sempre em pares de
  abertura e fechamento, e podem representar coleções de dados repetidas.

  **A desvantagem que o capítulo aponta.** A quantidade de bytes gasta com o
  nome das tags, comparada ao conteúdo. No exemplo do capítulo, uma tag
  `nome` com o valor "Bilbo Bolseiro" usa treze bytes só para as tags de
  abertura e fechamento, contra catorze bytes de conteúdo: quase metade dos
  vinte e sete bytes do trecho é informação que o aplicativo descarta
  rapidamente, o que pesa quando a tarifação é por volume de bytes
  transmitido. Some-se a isso o processamento mais lento de abrir e fechar
  cada tag, que deixa mais demorado tanto gerar quanto ler arquivos XML.

- **Demonstração no projetor.** Escrever no quadro um XML pequeno para um
  `Volume` da Rota Sul: `<volume><etiqueta>VOL-001</etiqueta><pesoKg>12.5
  </pesoKg></volume>`. Contar ao vivo, com a turma, quantos bytes são de tag e
  quantos são de conteúdo, repetindo o exercício de contagem do capítulo, e
  chegar a uma proporção parecida, perto de quarenta por cento em tags.

- **Exercício curto.** Cinco minutos, individual. Escrever à mão um XML para
  uma `Remessa` com `codigoRastreio` e `previsaoEntrega`, e contar quantos
  bytes são de tag e quantos são de conteúdo, decidindo se o resultado fica
  acima ou abaixo dos quarenta por cento vistos na demonstração.

### Ciclo 2, 20h05 às 20h40

- **Conceito.** JSON, e como um mesmo dado pode falar dois formatos.

  **JSON, JavaScript Object Notation.** Alternativa popular ao XML, criada
  como padrão de baixo custo de processamento para transmitir informação
  entre cliente e servidor de aplicações web. Três características do
  capítulo: é uma coleção de dados no formato `nome da informação : valor da
  informação`, inspirada nas estruturas de dados das linguagens C e C++, e
  tratada como um vetor; tem estrutura facilmente entendida por seres humanos
  e por máquinas; e, apesar de ser um subconjunto da linguagem JavaScript, a
  forma como a informação é tratada é totalmente independente da linguagem de
  programação. As vantagens sobre o XML, segundo o capítulo: as mesmas
  vantagens do XML, mas com uso menor de bytes, por não depender de tags, e
  mais simples de escrever um interpretador para ele. Começou como
  substituto do XML em aplicações que usam Ajax e hoje é usado por portais
  como Google, Flickr, Yahoo e Facebook para expor pesquisas em suas bases a
  aplicativos externos. Estrutura: `{` e `}` delimitam o escopo dos dados,
  `[` e `]` delimitam coleções repetidas, e dentro deles sempre há o par
  `"nome da informação": "valor da informação"`, separado por vírgula.

  > **Nota para o professor.** O capítulo apresenta XML e JSON como dois
  > formatos de metadados, mas não trata de como um mesmo endpoint responde
  > nos dois formatos dependendo do que o cliente pede. Esse mecanismo, a
  > negociação de conteúdo HTTP pelo cabeçalho `Accept`, não está no
  > capítulo 08: é técnica de HTTP e do framework web, posterior ao material.
  > É a aplicação prática, na Rota Sul, do que o próprio capítulo já
  > estabelece como princípio, que os dois formatos "podem ser usados como
  > protocolos ou interfaces de comunicação", cabendo ao sistema decidir qual
  > usar para cada consumidor.

  **Negociação de conteúdo.** O cliente que chama a API da Rota Sul envia um
  cabeçalho HTTP `Accept`, dizendo em que formato quer a resposta,
  `application/json` ou `application/xml`. O Spring já traz um conversor para
  JSON, baseado no Jackson, ativado por padrão em qualquer projeto que use o
  `spring-boot-starter-web`. Para responder também em XML, é preciso
  acrescentar o módulo `jackson-dataformat-xml`: com ele no classpath, o
  Spring passa a ter um segundo conversor disponível e escolhe entre os dois
  comparando o `Accept` da requisição com o que o endpoint declara que
  produz.

- **Demonstração no projetor.** Sem ainda ter o código pronto, escrever no
  quadro os dois arquivos que a Rota Sul vai gerar para a mesma `Remessa` ao
  final do Ciclo 4, um JSON e um XML, no mesmo molde das listagens do
  capítulo, com `codigoRastreio`, `previsaoEntrega` e `situacao`. Apontar que
  o conteúdo é idêntico nos dois; só a casca muda.

- **Exercício curto.** Cinco minutos, em duplas. Dado um `Volume` com
  `etiqueta`, `pesoKg` e `remessaId`, escrever a representação em JSON e, em
  seguida, a mesma informação em XML, e comparar o total de bytes das duas.

### Quiz, 20h40 às 20h50

**Pergunta.** Segundo o capítulo, qual das afirmações a seguir NÃO é um
princípio correto sobre o uso de JSON?

- A) É facilmente entendido tanto por seres humanos quanto por máquinas.
- B) Usa um número maior de bytes do que o XML para representar os mesmos
  metadados.
- C) Pode ser gerado e interpretado em qualquer linguagem de programação.
- D) O escopo das coleções de dados é delimitado por caracteres simples, `{`
  e `}`, e `[` e `]`.

**Correta:** B.

**Justificativa.** O capítulo é explícito ao afirmar que o JSON "permite um
uso menor de bytes para transmissão da informação, por não ser baseado em
tags", justamente o oposto do que a alternativa B afirma. A A, a C e a D
reproduzem características que o capítulo atribui corretamente ao JSON: fácil
entendimento por humanos e máquinas, independência de linguagem de
programação, e a delimitação de escopo por `{}` e `[]`.

### Ciclo 3, 20h50 às 21h25

Laboratório de metadados. Hoje nasce o segundo contexto do case, `expedicao`,
já previsto no diagrama de pacotes da Aula 05.

1. **Criar o pacote de expedição.** Dentro de
   `src/main/java/br/uni9/rotasul/`, criar `expedicao/domain`,
   `expedicao/repository`, `expedicao/service` e `expedicao/web`, seguindo a
   mesma convenção contexto primeiro, camada depois, da Aula 05.
2. **Escrever o domínio.** Em `expedicao/domain`, a classe `Remessa`, com
   `id`, `codigoRastreio`, `previsaoEntrega` e `situacao`. Uma exceção
   pontual à regra da Aula 06 de domínio sem anotação de framework: a classe
   recebe `@JacksonXmlRootElement(localName = "remessa")`, porque, sem ela, a
   tag raiz do XML sairia com o nome da classe Java, não com um nome de
   domínio em português. É uma anotação de serialização, não de persistência
   nem de web, e por isso a exceção fica registrada e não vira regra geral.
3. **Escrever o repositório.** Interface `RemessaRepository`, com
   `buscarPorId(Long id)`, e a implementação `RemessaRepositoryEmMemoria`,
   pré-carregada com duas ou três remessas de exemplo, seguindo o mesmo
   padrão interface primeiro da Aula 06.
4. **Escrever o serviço.** `RemessaService`, anotado `@Service`, com o método
   `buscarPorId(Long id)` delegando ao repositório.
5. **Adicionar o módulo Jackson XML.** No `pom.xml`, a dependência
   `com.fasterxml.jackson.dataformat:jackson-dataformat-xml`. Sem ela, o
   Spring só tem o conversor de JSON disponível, e qualquer pedido de XML
   recebe erro 406, *Not Acceptable*.
6. **Escrever o controlador.** `RemessaController`, em `expedicao/web`,
   `@RestController` mapeado em `/remessas`, com `GET /remessas/{id}`
   declarado com `produces = { MediaType.APPLICATION_JSON_VALUE,
   MediaType.APPLICATION_XML_VALUE }`. O Spring escolhe sozinho qual dos dois
   usar, comparando essa lista com o `Accept` da requisição.

### Ciclo 4, 21h25 às 21h50

7. **Subir e testar manualmente.** `./mvnw spring-boot:run`, e então
   `curl -H "Accept: application/json" http://localhost:PORTA/remessas/1` e
   `curl -H "Accept: application/xml" http://localhost:PORTA/remessas/1`,
   trocando `PORTA` pela porta que o terminal imprimiu. Confirmar que o
   primeiro devolve `{ ... }` e o segundo devolve `<remessa>...</remessa>`,
   com o mesmo conteúdo nos dois.
8. **Escrever o teste.** `RemessaControllerTest`, anotado com
   `@WebMvcTest(RemessaController.class)` e `MockMvc`, com dois métodos: um
   chamando o endpoint com `Accept: application/json` e conferindo
   `content().contentType(MediaType.APPLICATION_JSON)`, outro com `Accept:
   application/xml` conferindo `content().contentType(MediaType.APPLICATION_XML)`.
   Rodar `./mvnw test` e ver os dois passarem.
9. **Registrar a decisão.** Em `docs/decisoes.md`, uma linha explicando a
   escolha de um único endpoint com negociação de conteúdo, em vez de dois
   endpoints separados, um para cada formato, com a justificativa: um único
   recurso deve ter uma única URI, princípio que a Aula 10, sobre REST, vai
   formalizar.

**Entregável do dia:** `RemessaController` respondendo `GET /remessas/{id}`
em JSON e em XML conforme o `Accept`, mais `RemessaControllerTest` cobrindo os
dois formatos. Critério de aceitação: as duas chamadas manuais devolvendo o
conteúdo correto no formato pedido, `./mvnw test` passando, e nenhum endpoint
duplicado por formato.

### Fechamento, 21h50 às 22h00

- `git add src/main/java/br/uni9/rotasul/expedicao src/test/java/br/uni9/rotasul/expedicao pom.xml docs`
- `git commit -m "feat(expedicao): remessa em JSON e em XML por negociação de conteúdo"`
- `git push`
- **Prévia da Aula 10.** Hoje a Rota Sul aprendeu a falar dois formatos para
  quem pergunta. Amanhã ela se conecta com quem só fala um formato antigo, o
  parceiro legado, que só entende SOAP, e documenta formalmente a sua própria
  API REST de remessas. É a última aula do Módulo 2 e fecha o assunto de
  integração.

### Referências

1. MESQUITA, Paulo Ricardo Batista. **Capítulo 08: Metadados para Troca de
   Dados (XML e JSON).** Arquitetura de Software. AVA, Uninove. Fonte
   primária desta aula, `pdf/008.pdf`.
2. CHOWDHURY, A.; CHAUDHARY, P. **JAX: Java APIs for XML.** Sams Publishing,
   2002. Referência indicada pelo capítulo.
3. FRIESEN, F. **Java XML and JSON.** Apress, 2016. Referência indicada pelo
   capítulo.
4. Spring. **Documentação do Spring Framework**, negociação de conteúdo HTTP
   e `HttpMessageConverter`.
   <https://docs.spring.io/spring-framework/reference/web/webmvc/mvc-config/content-negotiation.html>
5. FasterXML. **Jackson-dataformat-xml.**
   <https://github.com/FasterXML/jackson-dataformat-xml>

---

## Aula 10, Objetos remotos: RMI, SOAP e REST

**Módulo:** M2, Integração e serviços distribuídos
**Capítulo do AVA:** `pdf/009.pdf`, RMI, SOAP (Web Services) e REST
**Entregável:** o cliente SOAP em `br.uni9.rotasul.parceiro`, consumindo um
serviço que simula o parceiro legado, mais a API REST de remessas documentada
pelo springdoc-openapi. Critério de aceitação: o cliente SOAP devolvendo a
situação de entrega para um código de rastreio de teste, a interface Swagger
UI abrindo em `/swagger-ui/index.html` com os endpoints de `/remessas`
listados, e `./mvnw test` passando.

### Retomada, 5 minutos

Na Aula 09 cada aluno entregou `RemessaController`, respondendo `GET
/remessas/{id}` em JSON ou em XML conforme o cabeçalho `Accept`. Retomar: a
Rota Sul já sabe falar dois formatos com quem pergunta em português, por
assim dizer, o mesmo protocolo HTTP que ela já usa desde a Aula 06. A pergunta
de hoje é mais dura: e quando quem pergunta é um sistema mais antigo, que só
fala um protocolo específico, com regras próprias de envelope e assinatura?
É o capítulo mais longo dos dezoito do AVA, e fecha o Módulo 2.

### Ciclo 1, 19h30 às 20h05

- **Conceito.** A origem histórica da comunicação remota e o RMI, na
  descrição do capítulo [1]. RMI entra hoje como leitura, não como
  laboratório: o exercício prático da aula é sobre SOAP e REST, que é o que a
  Rota Sul de fato vai construir daqui a pouco.

  **SABRE, o primeiro sistema com necessidade de comunicação remota.**
  Desenvolvido nos anos 1950 pela IBM para a American Airlines, que precisava
  gerenciar reservas de lugares em seus aviões e não conseguia lidar com o
  aumento de passageiros. A solução foi um servidor central numa pequena
  cidade do estado de Nova Iorque, acessado por terminais de reservas
  espalhados pelos Estados Unidos, processando cerca de oitenta e três mil
  chamadas telefônicas por dia na primeira versão. Esse sistema abriu caminho
  para grandes corporações trocarem dados entre filiais e matriz, com
  soluções proprietárias de empresas como IBM, Unisys, NCR e Honeywell, até a
  mudança de foco da ARPANET, de uso militar para uso público, dar origem à
  Internet, que pedia por padrões abertos.

  **RPC, Remote Procedure Call, 1976.** Implementação de software para
  compartilhamento remoto de recursos: permite que um programa chame e
  execute outro programa rodando em outro computador da mesma rede, sem o
  programador precisar implementar a conexão entre os dois, porque isso já é
  resolvido pelos protocolos de transferência de dados da Internet. A chamada
  ao programa remoto acontece como se fosse local. Em 1976 a Internet ainda
  tinha alcance restrito ao meio acadêmico, então o primeiro uso comercial do
  RPC ocorreu em soluções cliente-servidor, e ele se popularizou quando os
  fabricantes de sistemas Unix passaram a disponibilizar pacotes para
  facilitar seu uso. As plataformas de desenvolvimento incorporaram
  implementações de RPC: RMI para Java, DCOM para .Net.

  **RMI, Remote Method Invocation.** O aplicativo cliente invoca um aplicativo
  no servidor, envia uma mensagem com os dados a processar e espera uma
  mensagem de volta com o resultado. O servidor precisa estar sempre em
  execução, processando ou esperando requisição. Cinco cuidados que o
  capítulo exige do desenvolvedor: tratar erros de falha na rede, tanto no
  cliente quanto no servidor; considerar possíveis falhas no aplicativo do
  servidor; trocar informação só por mensagens, já que variáveis apontam
  endereços de memória que um lado não alcança do outro; aceitar queda de
  desempenho, porque a comunicação remota consome tempo; e garantir que o
  servidor saiba sempre quem fez a solicitação, para devolver o resultado ao
  cliente certo, de modo seguro. Implementar um serviço RMI exige, depois de
  iniciar o `rmiregistry`, criar uma interface que estende `Remote`, com
  métodos que declaram `throws RemoteException`, e uma classe que a
  implementa, registrada no `rmiregistry` por `registry.bind`; o cliente
  localiza o serviço por `Naming.lookup`. Vantagem apontada pelo capítulo: a
  programação do cliente é facilitada, porque o objeto remoto pode ser usado
  como se fosse uma instância local, e a segurança é reforçada porque o
  acesso só acontece pela interface. Desvantagens: o software inteiro precisa
  ser Java, e mudanças nas políticas de segurança das versões mais recentes
  da JVM podem exigir atualizar classes e chamadas já escritas.

- **Demonstração no projetor.** Ler em voz alta a interface `ServicoPotencia`
  do capítulo, `extends Remote` e cada método com `throws RemoteException`, e
  comparar com a interface `PedidoService` da Aula 07, que não lança nada
  parecido. A diferença de assinatura é o preço da transparência de
  localização: toda chamada remota pode falhar por rede, e a linguagem
  obriga o desenvolvedor a admitir isso já na assinatura do método; uma
  chamada local, como a da Aula 07, não precisa admitir isso, porque não
  atravessa rede nenhuma.

- **Exercício curto.** Cinco minutos, individual. Diante do trecho do
  capítulo que registra o serviço no `rmiregistry`, responder por escrito: o
  que aconteceria se o `rmiregistry` não estivesse em execução no momento em
  que o servidor tentasse `registry.bind`? E por que o `main` do servidor
  precisa capturar tanto `RemoteException` quanto `AlreadyBoundException`?
  Duas leituras em voz alta.

### Ciclo 2, 20h05 às 20h40

- **Conceito.** SOAP e REST, os dois modelos que o laboratório de hoje usa de
  verdade.

  **SOAP, Simple Object Access Protocol.** Especificação de protocolo para
  troca de dados estruturados entre aplicativos pela Internet, por meio de
  web services. A especificação começou na Microsoft, e sua coordenação foi
  transferida para a W3C [2]. O exemplo do capítulo é o serviço de consulta
  de CEP dos Correios do Brasil: o sistema que consulta informa parâmetros
  de busca, e recebe a resposta, tudo em protocolo baseado em XML definido
  pelo web service. A proposta do SOAP é estender funcionalidades entre
  aplicativos mantendo neutralidade quanto a sistema operacional e linguagem
  de programação, o que ele consegue porque as mensagens são sempre
  formatadas segundo o padrão XML e transmitidas por protocolos de camada de
  aplicação da Internet, normalmente HTTP ou SMTP. Toda mensagem SOAP segue
  uma estrutura fixa: um elemento Envelope, que identifica o arquivo XML como
  mensagem SOAP; um elemento Header, opcional, com informação específica da
  aplicação, como autenticação; um elemento Body, com o conteúdo real da
  requisição ou da resposta; e um elemento Fault, dentro do Body, para erros
  e status. O atributo `mustUnderstand`, quando presente, diz se um elemento
  do cabeçalho é obrigatório, valor 1, ou opcional, valor 0, para quem
  recebe. Em Java, a implementação moderna que o capítulo apresenta usa a API
  JAX-WS, com anotações como `@WebService`, `@WebMethod` e `@WebParam`
  substituindo a escrita manual do XML.

  **REST, Representational State Transfer.** Outra solução para integração
  de aplicativos por web services, mas ao contrário do SOAP, que troca
  arquivos XML entre cliente e serviço, o REST foca o uso do protocolo HTTP e
  das URIs. Em suma: o REST disponibiliza recursos identificados por URIs,
  manipulados por uma interface padrão, o próprio HTTP, e a troca de
  informação ocorre pelas representações desses recursos. Na plataforma Java
  EE, a API JAX-RS implementa esse modelo, com anotações como `@Path`, `@GET`
  e `@Produces(MediaType.APPLICATION_JSON)` para declarar o que cada recurso
  responde. O exemplo do capítulo mostra a resposta chegando direto no
  navegador, pela própria barra de endereço, sem precisar montar um envelope
  como no SOAP.

  > **Nota para o professor.** O capítulo não fala de `springdoc-openapi` nem
  > de documentação automática de API REST: a ferramenta é posterior ao
  > material. Mas o problema que ela resolve é o mesmo que o capítulo chama,
  > na Aula 07, de Descrição de Serviço: uma descrição do que o serviço faz e
  > do que o Consumidor precisa fornecer. O `springdoc-openapi` gera essa
  > descrição automaticamente a partir do código da Rota Sul, publicada em
  > `/v3/api-docs` e navegável em `/swagger-ui/index.html`, cumprindo para o
  > REST o mesmo papel que o WSDL cumpre para o SOAP.

  **Contraste dos três modelos**, para fechar o ciclo: RMI só funciona entre
  aplicativos Java, com objetos trafegando de forma nativa, sem XML; SOAP é
  neutro quanto a linguagem e sistema operacional, mas exige o envelope XML
  inteiro, com header, body e fault; REST é neutro do mesmo jeito, mas mais
  leve, apoiado só em HTTP, URIs e na representação do recurso, que a Aula 09
  já mostrou poder ser JSON ou XML conforme quem pergunta.

- **Demonstração no projetor.** Lado a lado, a mensagem SOAP `GetPrice` do
  capítulo, copiada no quadro com o Envelope, o Body e a operação, contra a
  saída do `curl -H "Accept: application/json"` da Aula 09 para uma
  `Remessa`. Contar as linhas de cada uma até chegar ao dado que interessa,
  `1.90` num caso, o `codigoRastreio` no outro, e apontar a diferença de
  verbosidade entre os dois modelos.

- **Exercício curto.** Cinco minutos, em duplas. Preencher uma tabela de três
  linhas, RMI, SOAP e REST, e três colunas, "formato de dado", "protocolo de
  transporte" e "só funciona em Java?". Gabarito: RMI, objetos Java nativos,
  protocolo próprio do RMI sobre TCP, sim; SOAP, XML, HTTP ou SMTP, não;
  REST, o que o servidor decidir produzir, HTTP, não.

### Quiz, 20h40 às 20h50

**Pergunta.** A Rota Sul precisa se conectar ao sistema do parceiro legado,
que só entende arquivos XML, e depois documentar sua própria API para os
demais sistemas consumirem. Dos três modelos de comunicação remota
apresentados pelo capítulo, qual deles NÃO permite a transferência de dados
usando arquivos em formato XML?

- A) RMI, porque a troca de dados entre cliente e servidor usa objetos Java
  diretamente, e não arquivos XML.
- B) SOAP, porque suas mensagens usam sempre arquivos em formato JSON, e não
  XML.
- C) REST, porque seus recursos nunca podem ser representados em formato
  XML.
- D) Nenhum dos três, porque todos usam XML de forma obrigatória.

**Correta:** A.

**Justificativa.** O capítulo descreve o RMI como comunicação por troca de
mensagens que carregam objetos Java, sem qualquer menção a XML: a JVM
serializa os próprios objetos, não um envelope de metadados. A alternativa B
está errada porque o capítulo é explícito ao dizer que as mensagens SOAP "são
formatadas de acordo com o padrão XML", não JSON. A C está errada porque o
capítulo apresenta o REST como flexível quanto à representação do recurso, o
que a Aula 09 já demonstrou na prática ao responder a mesma `Remessa` em JSON
ou em XML. A D erra ao generalizar para os três, quando o próprio capítulo
descreve o RMI sem nenhuma menção a arquivos XML.

### Ciclo 3, 20h50 às 21h25

Laboratório de integração. A Rota Sul não tem um parceiro real para a turma
acessar, então o laboratório simula o parceiro legado dentro do próprio fork:
um endpoint SOAP simples, no pacote `br.uni9.rotasul.parceiro`, representando
o sistema que a transportadora parceira expõe. O cliente que a turma escreve
na sequência é o mesmo tipo de código que se escreveria para consumir um
parceiro de verdade; só o endereço muda.

> **O que chega pronto no kit `aulas-1sem/labs/aula10-lab/`.** Dois arquivos,
> e os dois são andaime, não conteúdo da aula:
> `src/main/resources/parceiro.xsd`, o contrato do serviço, e
> `src/main/java/br/uni9/rotasul/parceiro/WebServiceConfig.java`, a classe de
> configuração que publica o `MessageDispatcherServlet` em `/ws/*` e expõe o
> WSDL a partir do XSD. Escrever um XSD à mão e acertar os três beans de
> configuração do Spring Web Services consome o laboratório inteiro e não
> ensina nada sobre objetos remotos. O que ensina, e o que o aluno escreve
> hoje, são três peças: o `@Endpoint` que atende, o cliente que chama e o
> teste que prova.

1. **Instalar o kit e ler o contrato.** Copiar os dois arquivos do kit para as
   posições correspondentes no fork e criar o pacote `br.uni9.rotasul.parceiro`
   com os subpacotes `endpoint`, o parceiro simulado, e `client`, quem consome,
   do lado da Rota Sul. É o primeiro contexto que se soma aos três da Aula 05,
   o que a convenção do semestre já previa: acrescentar contexto novo ao lado
   dos existentes, nunca renomear os já fixados. Projetar o `parceiro.xsd` e
   ler os dois elementos em voz alta, `consultaEntregaRequest`, com
   `codigoRastreio`, e `consultaEntregaResponse`, com `situacao` e
   `previsaoEntrega`. O XSD faz aqui o papel que o capítulo chamou de
   Descrição de Serviço na Aula 07: diz o que o Provedor espera receber e o
   que ele devolve.

   ```xml
   <xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema"
              xmlns:tns="http://rotasul.uni9.br/parceiro"
              targetNamespace="http://rotasul.uni9.br/parceiro"
              elementFormDefault="qualified">

     <xs:element name="consultaEntregaRequest">
       <xs:complexType>
         <xs:sequence>
           <xs:element name="codigoRastreio" type="xs:string"/>
         </xs:sequence>
       </xs:complexType>
     </xs:element>

     <xs:element name="consultaEntregaResponse">
       <xs:complexType>
         <xs:sequence>
           <xs:element name="situacao" type="xs:string"/>
           <xs:element name="previsaoEntrega" type="xs:date"/>
         </xs:sequence>
       </xs:complexType>
     </xs:element>
   </xs:schema>
   ```

2. **Adicionar as dependências e o gerador de classes.** No `pom.xml`,
   `spring-boot-starter-web-services` e `wsdl4j`, já fixados no contrato
   técnico da disciplina desde a Aula 01, mais o `jaxb2-maven-plugin`
   apontando para o `parceiro.xsd`, **com a versão presa na linha 3.x**:

   ```xml
   <plugin>
     <groupId>org.codehaus.mojo</groupId>
     <artifactId>jaxb2-maven-plugin</artifactId>
     <version>3.2.0</version>
     <executions>
       <execution>
         <id>xjc</id>
         <goals><goal>xjc</goal></goals>
       </execution>
     </executions>
     <configuration>
       <sources><source>src/main/resources/parceiro.xsd</source></sources>
       <packageName>br.uni9.rotasul.parceiro.gerado</packageName>
     </configuration>
   </plugin>
   ```

   **A versão precisa ser dita em voz alta, não só copiada.** A linha 2.x do
   plugin gera classes anotadas com `javax.xml.bind`, o pacote antigo; o
   Spring Boot 3.x sobre Java 21 usa `jakarta.xml.bind`, e o
   `Jaxb2Marshaller` do passo 6 simplesmente não reconhece as classes geradas
   pela linha antiga. O sintoma é um erro de contexto JAXB que não menciona
   versão nenhuma, e é o tipo de armadilha que trava um aluno por quarenta
   minutos. Sem `<version>` explícito, o Maven pode resolver a linha 2.x.
3. **Gerar as classes Java do XSD.** `./mvnw generate-sources`. Conferir em
   `target/generated-sources` as classes `ConsultaEntregaRequest` e
   `ConsultaEntregaResponse`, geradas automaticamente, sem uma linha escrita à
   mão. Abrir uma das duas e conferir que os `import` são de
   `jakarta.xml.bind.annotation`, e não de `javax`: é a confirmação, em cinco
   segundos, de que a versão do passo 2 pegou.
4. **Escrever o endpoint que simula o parceiro.** Em `parceiro/endpoint`,
   `ParceiroEndpoint`, anotado `@Endpoint`, com um método anotado
   `@PayloadRoot(namespace = "http://rotasul.uni9.br/parceiro", localPart =
   "consultaEntregaRequest")`, recebendo `@RequestPayload
   ConsultaEntregaRequest` e devolvendo `@ResponsePayload
   ConsultaEntregaResponse`. Regra simples para simular o parceiro: se o
   `codigoRastreio` começar com "RS", devolve situação `EM_TRANSITO`; caso
   contrário, `DESCONHECIDO`.

### Ciclo 4, 21h25 às 21h50

5. **Subir e conferir o WSDL.** `./mvnw spring-boot:run` e abrir
   `/ws/parceiro.wsdl` na porta que o terminal imprimiu. O WSDL não foi
   escrito por ninguém: o `WebServiceConfig` do kit o gera a partir do
   `parceiro.xsd`, e é esse documento que um parceiro real publicaria para a
   Rota Sul consumir. Apontar na tela onde aparecem a operação
   `consultaEntrega`, o tipo da requisição e o tipo da resposta.
6. **Escrever o cliente.** Em `parceiro/client`, `ParceiroClient`, estendendo
   `WebServiceGatewaySupport`, com o método `consultarEntrega(String
   codigoRastreio)`, que monta um `ConsultaEntregaRequest`, chama
   `getWebServiceTemplate().marshalSendAndReceive(request)` e devolve o
   `ConsultaEntregaResponse`. Junto, um bean `Jaxb2Marshaller` apontando para
   o pacote das classes geradas no passo 3, injetado no cliente. **A URI do
   parceiro não fica escrita dentro da classe**: o bean lê a propriedade
   `rotasul.parceiro.uri`, que em `application.properties` vale
   `http://localhost:${server.port:8080}/ws`, e o cliente expõe
   `apontarPara(String uri)`, que chama
   `getWebServiceTemplate().setDefaultUri(uri)`, para quem precisar trocar o
   endereço em tempo de execução. É exatamente o que o teste do passo 7 vai
   precisar fazer, e é também o que mudaria no dia em que o parceiro deixasse
   de ser simulado.
7. **Testar o cliente.** `ParceiroClientTest`, anotado
   `@SpringBootTest(webEnvironment = SpringBootTest.WebEnvironment.RANDOM_PORT)`,
   com a porta injetada por `@LocalServerPort` e o cliente apontado para ela
   antes da chamada:

   ```java
   @SpringBootTest(webEnvironment = SpringBootTest.WebEnvironment.RANDOM_PORT)
   class ParceiroClientTest {

       @LocalServerPort
       int porta;

       @Autowired
       ParceiroClient parceiroClient;

       @Test
       void devolveEmTransitoParaCodigoDaRotaSul() {
           parceiroClient.apontarPara("http://localhost:" + porta + "/ws");
           var resposta = parceiroClient.consultarEntrega("RS12345");
           assertEquals("EM_TRANSITO", resposta.getSituacao());
       }
   }
   ```

   **O `webEnvironment` não é detalhe de configuração.** No modo padrão de
   `@SpringBootTest`, que é `MOCK`, nenhum container servlet sobe, não existe
   porta aberta e a chamada SOAP não tem para onde ir: o teste falha com erro
   de conexão. `RANDOM_PORT` sobe o Tomcat embarcado numa porta livre, e
   `@LocalServerPort` diz qual foi. É a mesma forma que a Aula 17 usa no teste
   de integração ponta a ponta, e vale dizer isso à turma: o cliente e o
   endpoint estão no mesmo processo, mas a chamada entre eles atravessa HTTP
   de verdade, como atravessaria contra um parceiro externo. Rodar
   `./mvnw test`.
8. **Fechar a integração pelo lado REST.** Acrescentar ao `RemessaController`
   da Aula 09 o método `GET /remessas/{id}/situacao-parceiro`, que busca a
   `Remessa`, chama `ParceiroClient.consultarEntrega` com o seu
   `codigoRastreio` e devolve o resultado em JSON. É o ponto em que a
   integração se fecha: o dado que chegou por SOAP sai por REST, para
   qualquer consumidor da Rota Sul.
9. **Documentar a API e registrar a decisão.** No `pom.xml`,
   `springdoc-openapi-starter-webmvc-ui`. Subir a aplicação e abrir
   `/swagger-ui/index.html` na porta que o terminal imprimiu, conferindo que
   os endpoints de `/remessas` aparecem listados, com o schema de `Remessa`
   gerado a partir das anotações Jackson da Aula 09. Em seguida, uma linha em
   `docs/decisoes.md` explicando a escolha de simular o parceiro legado dentro
   do próprio fork, e por quê: a Rota Sul não tem um parceiro real disponível
   para a turma, e o contrato XSD mais o endpoint reproduzem o mesmo tipo de
   código que se escreveria contra um parceiro de verdade.

**Entregável do dia:** o cliente SOAP em `br.uni9.rotasul.parceiro`,
consumindo o endpoint simulado, com `ParceiroClientTest` passando, mais a API
REST de `/remessas` documentada pelo springdoc-openapi. Critério de
aceitação: `consultarEntrega("RS12345")` devolvendo `EM_TRANSITO` no teste com
`RANDOM_PORT`, a Swagger UI listando os endpoints de `/remessas` em
`/swagger-ui/index.html`, e `./mvnw test` passando.

### Fechamento, 21h50 às 22h00

- `git add src pom.xml docs`
- `git commit -m "feat(parceiro): consome o parceiro legado por SOAP e documenta a API REST com springdoc"`
- `git push`
- Fechar o Módulo 2 em uma frase por aula: contrato separado de implementação
  na Aula 07, empacotamento comparado na Aula 08, metadados em JSON e XML na
  Aula 09, e hoje SOAP e REST juntos, fechando a integração da Rota Sul com o
  mundo fora dela.
- **Prévia da Aula 11.** Hoje a turma usou vários padrões sem nomeá-los: a
  interface `PedidoService` da Aula 07 separando contrato de implementação, e
  a suíte de teste abstrata que roda contra as duas implementações, que é uma
  aplicação do padrão Template Method. A próxima aula abre o catálogo formal
  de Design Patterns e dá nome a cada um deles.

### Referências

1. MESQUITA, Paulo Ricardo Batista. **Capítulo 09: RMI, SOAP (Web Services) e
   REST.** Arquitetura de Software. AVA, Uninove. Fonte primária desta aula,
   `pdf/009.pdf`.
2. W3C. **SOAP Specification.** Referência indicada pelo capítulo, no corpo
   do texto. <https://www.w3.org/TR/soap/>
3. Spring. **Documentação do Spring Web Services.**
   <https://docs.spring.io/spring-ws/docs/current/reference/html/>
4. springdoc-openapi. **Documentação.** <https://springdoc.org/>
5. `docs/arquitetura/componentes.puml` do fork do aluno, entregável da Aula
   05, componente "Integração com parceiros" que ganha implementação real
   nesta aula.

---

## Aula 11, Design Patterns

**Módulo:** M3, Padrões e frameworks
**Capítulo do AVA:** `pdf/010.pdf`, Design Patterns
**Entregável:** o padrão Strategy aplicado ao cálculo de frete, com a interface
`CalculadoraDeFrete` e as implementações `FreteRotaPropria` e
`FreteTransportadoraParceira`, selecionadas em tempo de execução por
`CalculoDeFreteService`; e o padrão Factory Method aplicado à criação de
`Ocorrencia`, com a classe `OcorrenciaCreator` e as implementações
`AtrasoOcorrenciaCreator` e `ExtravioOcorrenciaCreator`. Critério de aceitação:
`CalculoDeFreteServiceTest` e `OcorrenciaCreatorTest` passando com `./mvnw
test`, nenhuma anotação de framework nas classes de domínio envolvidas, e
nenhuma classe fora dos pacotes `pedido.domain`, `pedido.service` e
`rastreamento.domain` instanciando diretamente uma das quatro implementações
concretas.

### Retomada, 5 minutos

Na Aula 10 cada aluno entregou o cliente SOAP em `br.uni9.rotasul.parceiro`,
consumindo o endpoint que simula o parceiro legado, mais a API REST de
`/remessas` documentada pelo springdoc-openapi, fechando o Módulo 2. A prévia
daquela aula deixou uma dívida em aberto: a interface `PedidoService` da Aula
07, com duas implementações trocáveis por perfil, e a suíte de teste abstrata
`PedidoServiceContratoTest`, que roda os mesmos casos contra as duas, já eram
um padrão de projeto usado sem nome. Projetar `PedidoServiceContratoTest` na
tela e perguntar à turma: quem sabe como se chama uma classe abstrata que
define um algoritmo em etapas fixas e deixa uma etapa específica para cada
subclasse preencher? Hoje esse nome chega, Template Method, junto com o
catálogo inteiro de onde ele vem.

### Ciclo 1, 19h30 às 20h05

- **Conceito.** A origem dos padrões de projeto, na descrição do capítulo [1].

  **Os dois caminhos do desenvolvimento de software.** O capítulo abre
  descrevendo dois modos de trabalho. No primeiro, por questão cultural, o
  desenvolvedor constrói o aplicativo sem avaliar devidamente os problemas que
  o software pode vir a ter, nem quando uma solução pode ser reaproveitada, e
  acaba replicando o que já foi desenvolvido em vez de reaproveitar; se a
  parte replicada precisar mudar depois, o custo de atualização e de reteste é
  alto. No segundo modo, o desenvolvedor segue regras definidas por modelos de
  arquitetura, orientações de frameworks e padrões de projeto: é mais
  complexo, gasta mais tempo em planejamento, mas gasta bem menos tempo nas
  demais atividades. O capítulo cita uma estimativa: no Brasil, cerca de 10%
  do tempo de projeto vai para análise, 20% para programação e o restante para
  correção de erros e outras alterações; num país com cultura de
  desenvolvimento mais estruturada, como a Alemanha do exemplo do capítulo, a
  proporção se inverte, cerca de 60% para análise, 30% para programação e 10%
  para correção. A frase do capítulo que resume a diferença: "fazer e depois
  pensar no que foi feito" contra "pensar em como deve ser feito, e depois
  fazer".

  **Origem histórica.** Os padrões de projeto, também chamados design
  patterns, vêm de boas práticas de programação definidas por desenvolvedores
  no início dos anos 1970. Em congressos e seminários, a troca de experiências
  entre eles revelou problemas comuns a qualquer tipo de software: o primeiro
  problema atacado foi a relação entre interface de usuário, regras de negócio
  e base de dados, e como modificar uma dessas partes sem quebrar as outras
  duas; o segundo foi a possibilidade de construir um novo software sem
  precisar recomeçar do zero. O capítulo cita dois livros como referência
  clássica do assunto, GAMMA e JOHNSON [2] e LARMAN [3].

  **MVC como primeiro exemplo do capítulo.** Dessa troca de experiências
  nasceu o MVC, Model-View-Controller, publicado por volta de 1975 e ainda em
  uso, talvez o padrão de projeto mais aplicado entre os desenvolvedores. O
  capítulo descreve o MVC como um padrão que orienta a separação do
  código-fonte em três partes independentes entre si: interação com o usuário
  (view), regras de negócio e acesso à base de dados (model), e algo que
  conecta as duas (controller). A analogia do capítulo é o quebra-cabeça: cada
  parte do software é uma peça com um desenho específico que conecta a outras
  peças, e se todas encaixarem, formam uma ilustração completa. O objetivo do
  MVC é reduzir o tempo de desenvolvimento e de teste em atualizações
  futuras: uma vez pronta, cada parte pode ser reaproveitada em novos
  softwares, e o responsável pelo projeto decide o que reaproveitar e o que
  construir de novo.

- **Demonstração no projetor.** Abrir o fork num terminal e listar
  `src/main/java/br/uni9/rotasul/pedido`: `web`, `service`, `repository`,
  `domain`. Ler em voz alta a definição de MVC do capítulo e perguntar à
  turma onde está cada peça do quebra-cabeça. `PedidoController`, em `web`, é
  quem recebe a requisição, mas hoje ele devolve JSON puro, sem um View
  separado, porque a Rota Sul ainda não tem apresentação server-side; isso
  muda na Aula 13. `PedidoService` e `Pedido`, em `service` e `domain`, fazem
  o papel do Model. Não há, ainda, um Controller no sentido clássico do MVC
  do capítulo, conectando view e model; o próprio `PedidoController` do
  Spring acumula parte desse papel. A turma está usando uma variação do
  padrão descrito no capítulo desde a Aula 06, sem ter lido a definição
  formal até hoje.

- **Exercício curto.** Cinco minutos, em duplas. Reler a frase já usada na
  Aula 02, tirada do capítulo anterior do AVA: "os padrões de projeto são
  modelos abstratos que orientam a implementação de um software para resolver
  um problema específico, enquanto um framework inclui a implementação de
  código para prover soluções". Classificar cada item como padrão de projeto
  ou framework: (a) MVC; (b) Hibernate; (c) Spring Boot; (d) Strategy.
  Gabarito: (a) padrão de projeto, é um modelo abstrato de organização, não
  código pronto; (b) framework, é uma biblioteca com implementação; (c)
  framework, pelo mesmo motivo; (d) padrão de projeto, ainda não apresentado
  nesta aula, mas já classificável pela mesma definição.

### Ciclo 2, 20h05 às 20h40

- **Conceito.** O catálogo de padrões de projeto e os dois padrões do
  laboratório de hoje.

  > **Nota para o professor.** O capítulo do AVA apresenta a origem dos
  > padrões de projeto e um único exemplo detalhado, o MVC. Ele não organiza
  > os padrões em categorias, não lista o catálogo de 23 padrões e não nomeia
  > Strategy nem Factory Method, os dois que o laboratório de hoje pede. Essa
  > organização vem da própria bibliografia que o capítulo cita como
  > referência, GAMMA, HELM, JOHNSON e VLISSIDES, **Design Patterns:
  > Elements of Reusable Object-Oriented Software** (1994) [2], o livro que
  > formalizou o catálogo e é conhecido pelo apelido "Gang of Four", GoF. Dizer
  > isso à turma antes de avançar: o capítulo abre a porta, o catálogo vem de
  > onde o próprio capítulo manda buscar.

  **As três famílias do catálogo GoF.** Os 23 padrões do livro se organizam
  em três categorias, pela pergunta que cada uma responde. **Criacionais**
  respondem "como um objeto é instanciado": Factory Method, Abstract Factory,
  Builder, Prototype e Singleton estão aqui. **Estruturais** respondem "como
  classes e objetos se compõem para formar algo maior": Adapter, Bridge,
  Composite, Decorator, Facade e Proxy estão aqui. **Comportamentais**
  respondem "como os objetos interagem e distribuem responsabilidade":
  Strategy, Template Method, Observer, State e Command estão entre eles.
  Template Method, o padrão que a turma já usou na Aula 07 sem saber o nome,
  é comportamental; os dois padrões de hoje são um de cada uma das outras duas
  famílias.

  **Strategy, comportamental.** Define uma família de algoritmos, encapsula
  cada um numa classe própria e os torna intercambiáveis, de modo que o
  algoritmo pode variar independentemente de quem o usa. Na Rota Sul: o
  cálculo do valor do frete de um pedido muda de fórmula dependendo de quem
  faz a entrega, a frota própria na rota principal ou uma transportadora
  parceira na última milha, do jeito que o `PLANO_DE_ENSINO.md` descreve o
  case. A operação é sempre a mesma, calcular o frete, mas o algoritmo por
  trás muda, e a escolha acontece a cada pedido novo, em tempo de execução.
  Isso é diferente do que a Aula 07 fez com `PedidoService`: lá a
  implementação inteira é fixada uma vez, quando a aplicação sobe, pelo
  parâmetro de perfil; aqui a escolha acontece de novo a cada chamada, dentro
  do processo em execução, com base num dado do próprio pedido.

  **Factory Method, criacional.** Define uma interface para criar um objeto,
  mas deixa que subclasses decidam qual classe concreta instanciar. Na Rota
  Sul: quando o atendente registra uma ocorrência por telefone, ele informa o
  tipo, atraso ou extravio, e o sistema precisa instanciar a subclasse de
  `Ocorrencia` correspondente sem que o código que atende a ligação conheça
  as subclasses. Isso isola a decisão de qual classe instanciar dentro de uma
  hierarquia de criadores, em vez de espalhar `if` de tipo pelo código que usa
  o objeto.

  **A diferença entre os dois, em uma frase.** Strategy troca o algoritmo de
  uma operação que já tem um objeto para atuar; Factory Method troca qual
  objeto é criado, antes de qualquer operação acontecer sobre ele.

- **Demonstração no projetor.** Diagrama de classes do Strategy de hoje,
  desenhado ao vivo com a mesma notação da Aula 05, para o professor colar no
  editor on-line do PlantUML e projetar:

  ```
  @startuml
  interface CalculadoraDeFrete {
    +calcular(pedido: Pedido): BigDecimal
  }
  class FreteRotaPropria {
    +calcular(pedido: Pedido): BigDecimal
  }
  class FreteTransportadoraParceira {
    +calcular(pedido: Pedido): BigDecimal
  }
  class CalculoDeFreteService {
    -rotaPropria: CalculadoraDeFrete
    -transportadoraParceira: CalculadoraDeFrete
    +calcular(pedido: Pedido): BigDecimal
  }
  CalculadoraDeFrete <|.. FreteRotaPropria
  CalculadoraDeFrete <|.. FreteTransportadoraParceira
  CalculoDeFreteService o-- CalculadoraDeFrete
  @enduml
  ```

  Ler a seta `o--`: `CalculoDeFreteService` guarda uma referência às duas
  estratégias e decide qual delas invocar a cada chamada, o "contexto" do
  padrão Strategy na terminologia do GoF. Comparar com o diagrama de
  componentes da Aula 05: lá as setas eram entre componentes inteiros; aqui
  são entre classes dentro de um único componente, um nível de detalhe
  abaixo.

- **Exercício curto.** Cinco minutos, em duplas. Duas situações da Rota Sul,
  decidir qual dos dois padrões se aplica a cada uma: (a) o cálculo do frete
  de um pedido muda de fórmula conforme o destino é atendido pela frota
  própria ou por um parceiro, e a escolha acontece a cada pedido novo; (b) ao
  registrar uma ocorrência por telefone, o atendente informa o tipo, e o
  sistema precisa instanciar a subclasse correta de `Ocorrencia` sem que o
  código que atende a ligação conheça as subclasses. Gabarito: (a) Strategy,
  o algoritmo varia e é intercambiável em tempo de execução; (b) Factory
  Method, a decisão de qual classe concreta instanciar fica isolada na
  hierarquia de criadores.

### Quiz, 20h40 às 20h50

**Pergunta.** Segundo o capítulo, qual das alternativas a seguir NÃO é
característica de um design pattern?

- A) Apresenta um modelo de organização de classes para resolver um problema
  já conhecido.
- B) É resultado de uma boa prática de programação, aplicada para resolver
  problemas conhecidos.
- C) Provê um mecanismo para estruturar o software de modo organizado,
  facilitando manutenções futuras.
- D) Não pode ser aplicado em arquiteturas organizadas em camadas.

**Correta:** D.

**Justificativa.** O próprio capítulo contradiz a alternativa D ao descrever o
MVC, um design pattern, como um modelo que organiza o código-fonte
exatamente em camadas independentes, interação com o usuário, regras de
negócio e acesso a dados. Um padrão de projeto aplicado em camadas não é
exceção, é o exemplo que o capítulo escolheu para explicar o conceito. As
alternativas A, B e C são características reais, tiradas quase literalmente
do texto: A e B descrevem a origem do padrão como boa prática que organiza
uma solução para um problema conhecido, e C descreve o objetivo de
estruturar o software e facilitar manutenção, presente na discussão inicial
do capítulo sobre o custo de atualizar software mal organizado.

### Ciclo 3, 20h50 às 21h25

Laboratório de dois padrões de projeto. Nenhum endpoint novo nasce hoje: o
Strategy entra na camada `domain` e `service` do contexto `pedido`, e o
Factory Method abre o contexto `rastreamento`, reservado desde o diagrama de
pacotes da Aula 05 e ainda sem nenhuma linha de código.

1. **Criar o contrato da estratégia.** Em `pedido/domain`, criar a interface
   `CalculadoraDeFrete`, com um único método, `BigDecimal calcular(Pedido
   pedido)`. Sem anotação de framework: é domínio.
2. **Acrescentar a região ao `Pedido`.** Em `pedido/domain/Pedido`, criado na
   Aula 06, acrescentar o atributo `regiao`, do tipo `String`, com os valores
   possíveis `"PRINCIPAL"` e `"ULTIMA_MILHA"`, mais o getter e o ajuste no
   construtor. É a primeira vez que a classe `Pedido` muda desde que nasceu, e
   ela continua sem depender de nada do Spring.
3. **Escrever a primeira estratégia.** `FreteRotaPropria implements
   CalculadoraDeFrete`, em `pedido/domain`, com uma tarifa fixa de `new
   BigDecimal("15.00")` para qualquer pedido, representando o custo da frota
   própria na rota principal.
4. **Escrever a segunda estratégia.** `FreteTransportadoraParceira implements
   CalculadoraDeFrete`, também em `pedido/domain`, aplicando um adicional de
   30% sobre a mesma tarifa base, `new BigDecimal("15.00")` multiplicado por
   `new BigDecimal("1.30")`, resultando em `19.50`, representando o repasse
   pago ao parceiro da última milha.
5. **Escrever o contexto do Strategy.** Em `pedido/service`, criar
   `CalculoDeFreteService`, anotada `@Service`, recebendo `FreteRotaPropria` e
   `FreteTransportadoraParceira` pelo construtor e guardando as duas. O
   método `calcular(Pedido pedido)` decide qual delas chamar olhando
   `pedido.getRegiao()`: `"ULTIMA_MILHA"` usa a segunda, qualquer outro valor
   usa a primeira. É o único ponto do código que conhece as duas
   implementações concretas; todo o resto do sistema só vai conhecer a
   interface `CalculadoraDeFrete` e o serviço.
6. **Testar o Strategy.** `CalculoDeFreteServiceTest`, em
   `src/test/java/br/uni9/rotasul/pedido/service/`, com dois casos: um
   `Pedido` com `regiao` `"PRINCIPAL"` calcula `15.00`, e um `Pedido` com
   `regiao` `"ULTIMA_MILHA"` calcula `19.50`. Rodar `./mvnw test`.

### Ciclo 4, 21h25 às 21h50

7. **Criar o contexto `rastreamento`.** Dentro de
   `src/main/java/br/uni9/rotasul/`, criar `rastreamento/domain`. É o
   primeiro código real do terceiro contexto previsto desde a Aula 05; até
   hoje só existiam `pedido` e `expedicao`.
8. **Escrever a hierarquia de produtos.** Em `rastreamento/domain`, a classe
   abstrata `Ocorrencia`, com os atributos `codigoRastreio` e `registradaEm`
   (`LocalDateTime`) e o método abstrato `String getTipo()`. Duas subclasses:
   `OcorrenciaAtraso`, com o atributo extra `horasDeAtraso` e `getTipo()`
   devolvendo `"ATRASO"`, e `OcorrenciaExtravio`, com o atributo extra
   `ultimaLocalizacaoConhecida` e `getTipo()` devolvendo `"EXTRAVIO"`.
9. **Escrever a hierarquia de criadores, o Factory Method.** Também em
   `rastreamento/domain`, a classe abstrata `OcorrenciaCreator`:

   ```java
   public abstract class OcorrenciaCreator {

       public final Ocorrencia registrar(String codigoRastreio) {
           if (codigoRastreio == null || codigoRastreio.isBlank()) {
               throw new IllegalArgumentException(
                   "codigo de rastreio e obrigatorio");
           }
           return criarOcorrencia(codigoRastreio, LocalDateTime.now());
       }

       protected abstract Ocorrencia criarOcorrencia(
           String codigoRastreio, LocalDateTime registradaEm);
   }
   ```

   O método `registrar` é final, de propósito: ele é o passo comum a toda
   ocorrência, validar o código de rastreio antes de criar qualquer coisa. O
   método `criarOcorrencia` é o Factory Method propriamente dito, abstrato,
   deixado para cada subclasse decidir qual produto concreto instanciar.
   Duas subclasses: `AtrasoOcorrenciaCreator`, recebendo `horasDeAtraso` pelo
   construtor e devolvendo `new OcorrenciaAtraso(...)`, e
   `ExtravioOcorrenciaCreator`, recebendo `ultimaLocalizacaoConhecida` pelo
   construtor e devolvendo `new OcorrenciaExtravio(...)`.
10. **Testar o Factory Method.** `OcorrenciaCreatorTest`, em
    `src/test/java/br/uni9/rotasul/rastreamento/domain/`, com três casos:
    `new AtrasoOcorrenciaCreator(3).registrar("RS12345")` devolve uma
    instância de `OcorrenciaAtraso` com `getTipo()` igual a `"ATRASO"`; `new
    ExtravioOcorrenciaCreator("Galpao Osasco").registrar("RS99999")` devolve
    uma instância de `OcorrenciaExtravio` com `getTipo()` igual a
    `"EXTRAVIO"`; e chamar `registrar("")` em qualquer um dos dois criadores
    lança `IllegalArgumentException`. Rodar `./mvnw test`.
11. **Registrar as duas decisões.** Em `docs/decisoes.md`, duas linhas novas:
    uma explicando que o cálculo de frete usa Strategy porque a fórmula
    precisa variar por pedido, em tempo de execução, e outra explicando que a
    criação de `Ocorrencia` usa Factory Method porque o código que recebe a
    ligação do atendente não deve conhecer as subclasses concretas.

**Entregável do dia:** `CalculadoraDeFrete` com `FreteRotaPropria` e
`FreteTransportadoraParceira`, mais `CalculoDeFreteService` escolhendo entre
elas; `OcorrenciaCreator` com `AtrasoOcorrenciaCreator` e
`ExtravioOcorrenciaCreator`, mais as duas subclasses de `Ocorrencia`. Critério
de aceitação: `CalculoDeFreteServiceTest` e `OcorrenciaCreatorTest` passando
com `./mvnw test`, nenhuma anotação de framework em `Ocorrencia` nem em suas
subclasses, e as duas decisões registradas em `docs/decisoes.md`.

### Fechamento, 21h50 às 22h00

- `git add src docs`
- `git commit -m "feat(padroes): aplica Strategy no calculo de frete e Factory Method na criacao de Ocorrencia"`
- `git push`
- Fechar o Ciclo 4 relendo em voz alta a frase que abre o Módulo 3: até aqui a
  Rota Sul usou padrões sem nomear (Template Method na Aula 07), e hoje
  nomeou dois novos e aplicou os dois de propósito. A próxima aula pergunta de
  onde vem o poder de um framework de controlar essa aplicação inteira.
- **Prévia da Aula 12.** O capítulo de hoje citou, de passagem, que um
  framework "determina como o aplicativo funcionará". A Aula 12 abre
  exatamente esse ponto, batizado de inversão de controle, e mostra como o
  Spring decide, sozinho, qual bean injetar em cada perfil, `dev` ou `prod`.
  O contraste com o Strategy de hoje vai ficar explícito: aqui quem decide
  qual implementação usar é o código da Rota Sul; lá, quem decide é o
  framework.

### Referências

1. MESQUITA, Paulo Ricardo Batista. **Capítulo 10: Design Patterns.**
   Arquitetura de Software. AVA, Uninove. Fonte primária desta aula,
   `pdf/010.pdf`.
2. GAMMA, Erich; HELM, Richard; JOHNSON, Ralph; VLISSIDES, John. **Design
   Patterns: Elements of Reusable Object-Oriented Software.**
   Addison-Wesley, 1994. Referência indicada pelo capítulo, e a fonte do
   catálogo das três famílias apresentado no Ciclo 2.
3. LARMAN, Craig. **Utilizando UML e Padrões.** Bookman, 2007. Referência
   indicada pelo capítulo.
4. JUnit. **JUnit 5 User Guide.** <https://junit.org/junit5/docs/current/user-guide/>
5. PlantUML. **Documentação da linguagem.** <https://plantuml.com/pt/>
6. `docs/arquitetura/pacotes.puml` do fork do aluno, entregável da Aula 05,
   contexto `rastreamento` que ganha seu primeiro código nesta aula.

---

## Aula 12, Frameworks: anatomia e inversão de controle

**Módulo:** M3, Padrões e frameworks
**Capítulo do AVA:** `pdf/011.pdf`, Frameworks
**Entregável:** a interface `NotificadorDeOcorrencia`, com as implementações
`NotificadorDeOcorrenciaConsole` e `NotificadorDeOcorrenciaWebhookSimulado`,
ligadas explicitamente aos perfis `dev` e `prod` por métodos `@Bean` na classe
`NotificacaoConfig`, mais um `CommandLineRunner` que registra no log, a cada
subida, qual implementação o container injetou. Critério de aceitação: subir
com `-Dspring-boot.run.profiles=dev` e depois com `=prod` e ver, nos dois
logs, o nome de uma classe diferente; `NotificacaoConfigDevTest` e
`NotificacaoConfigProdTest` passando com `./mvnw test`.

### Retomada, 5 minutos

Na Aula 11 cada aluno entregou dois padrões de projeto: o Strategy no cálculo
de frete, com `CalculadoraDeFrete`, `FreteRotaPropria` e
`FreteTransportadoraParceira`, e o Factory Method na criação de `Ocorrencia`,
com `OcorrenciaCreator` e seus dois criadores concretos. Projetar
`CalculoDeFreteService` na tela e relembrar: ali, quem decide qual estratégia
usar é o próprio código da Rota Sul, uma linha de `if` dentro do serviço.
Perguntar à turma: e a interface `PedidoService` da Aula 07, com duas
implementações escolhidas pelo parâmetro de perfil, quem decidiu ali qual
classe usar? Ninguém no código da Rota Sul escreveu esse `if`. Foi o Spring.
A aula de hoje abre exatamente essa caixa.

### Ciclo 1, 19h30 às 20h05

- **Conceito.** O que é um framework, na definição do capítulo [1].

  **Framework, definição do capítulo.** Um framework é uma solução
  desenvolvida para resolver um problema específico, mas que ainda não é um
  software executável por si só: é um conjunto de bibliotecas associado a
  interfaces que permitem acoplar essas bibliotecas ao software em
  desenvolvimento. O objetivo é fornecer uma funcionalidade genérica que, ao
  ser usada por um desenvolvedor, implementa uma funcionalidade específica.
  O exemplo do capítulo é gráfico: os componentes de interface do Android
  permitem ao desenvolvedor implementar rapidamente as telas de um
  aplicativo, sem escrever cada botão do zero.

  **A frase central do capítulo, sobre controle.** "Um framework determina
  como o aplicativo funcionará, pois ele é que controla o fluxo de execução
  de operações que o aplicativo necessita. A isso se dá o nome de inversão
  de controle." É a passagem que dá nome à aula de hoje: não é o código da
  Rota Sul que decide quando cada parte do framework roda, é o framework que
  decide quando chamar o código da Rota Sul. Comparar com uma biblioteca
  comum, onde é o próprio programa que decide quando chamar cada função: com
  um framework, a direção da chamada se inverte.

  **Framework contra padrão de projeto, revisitado.** O capítulo repete a
  distinção já usada nas Aulas 02 e 11: padrões de projeto são modelos
  abstratos que orientam a implementação para resolver um problema
  específico, enquanto um framework inclui a implementação de código para
  prover soluções. Um framework pode ser modelado com vários padrões de
  projeto ao mesmo tempo, mas sempre tem domínio de uma aplicação
  particular, o que os padrões de projeto, sozinhos, não têm.

  **Cinco vantagens do capítulo:** maior facilidade para detectar erros;
  garantia melhor de qualidade do software; o desenvolvedor se concentra no
  desenvolvimento do aplicativo final, não na infraestrutura; reuso de
  soluções que já resolvem problemas conhecidos; uso otimizado de recursos.
  **A desvantagem central:** o código-fonte do framework normalmente não é
  editável, de propósito, porque a intenção é que o desenvolvedor use o
  framework para formar o núcleo do aplicativo e adicione blocos de código
  novos em torno dele, não que reescreva o núcleo. O capítulo soma a isso o
  aumento de tamanho final do software, as classes de acoplamento que
  seriam desnecessárias num aplicativo do zero, e o tempo de aprendizado, que
  se gasto durante a execução do projeto pode anular o ganho esperado de
  produtividade.

  **Frameworks de empresa, exemplo do capítulo.** Além dos frameworks
  genéricos, como o próprio Spring que a turma já usa desde a Aula 01, o
  capítulo cita empresas com problemas específicos o bastante para
  justificar um framework próprio: a Sony, para o processamento de imagens
  das suas câmeras, e a Ericsson, para as centrais de comunicação telefônica
  que produz.

- **Demonstração no projetor.** Abrir `PedidoServicePadrao` e
  `PedidoServiceComAnaliseDeRisco`, da Aula 07, e apontar: nenhuma das duas
  classes chama a outra, nenhuma delas decide qual vai rodar. Quem decide é
  o `spring.profiles.active` do `application.properties`, lido pelo Spring
  antes de qualquer linha do código da Rota Sul executar. Essa é a inversão
  de controle em ação: o framework decide o quê instanciar e quando, o
  desenvolvedor só descreve as opções.

- **Exercício curto.** Cinco minutos, individual. Responder por escrito: no
  `PedidoServicePadrao` da Aula 07, quem chama o construtor da classe, o
  código da Rota Sul ou o Spring? E se a turma removesse a anotação
  `@Service` dessa classe, o que aconteceria ao subir a aplicação com o
  perfil `padrao`? Gabarito: quem chama o construtor é o Spring, durante a
  inicialização do container; sem `@Service`, o Spring não teria como saber
  que aquela classe deve virar um bean, e a aplicação falharia ao subir,
  porque nenhum candidato a `PedidoService` estaria disponível para injetar
  no `PedidoController`.

### Ciclo 2, 20h05 às 20h40

- **Conceito.** A anatomia do container de inversão de controle, e a
  diferença entre configuração implícita e explícita.

  **O que o container faz ao subir.** Quando `./mvnw spring-boot:run`
  executa, o Spring varre o código em busca de candidatos a bean: classes
  anotadas `@Component`, `@Service`, `@Repository`, e métodos anotados
  `@Bean` dentro de classes `@Configuration`. Para cada candidato, ele
  registra uma definição de bean; se a definição tiver `@Profile`, o
  container só a ativa quando o perfil correspondente está entre os
  ativos, lidos de `spring.profiles.active`. Só depois de resolver todas as
  definições o container começa a instanciar os beans e a injetá-los onde
  um construtor pede, como no `PedidoController` recebendo `PedidoService`.
  É esse mecanismo, e não mágica, que decide qual `PedidoServiceX` vira
  ativo em cada subida.

  **Configuração implícita, o que a Aula 07 já fez.** Anotar a própria
  classe de implementação com `@Service` e `@Profile("padrao")` é a forma
  mais comum de registrar um bean no Spring, e funciona bem quando a decisão
  de qual implementação existe é simples. A decisão de qual perfil usa qual
  classe fica espalhada, uma anotação por classe.

  **Configuração explícita, o que o laboratório de hoje pede.** Uma classe
  `@Configuration` concentra, num único lugar, a decisão de qual
  implementação vira bean em qual perfil, por meio de métodos `@Bean`. As
  classes de implementação em si não precisam de nenhuma anotação de
  framework: elas só implementam a interface, e é o método `@Bean` que as
  registra. A vantagem pedagógica: quem lê a classe de configuração vê, de
  uma vez, o mapa inteiro de "qual implementação em qual ambiente", sem
  precisar abrir cada classe candidata para procurar `@Profile`.

- **Demonstração no projetor.** Esqueleto de uma classe `@Configuration`
  qualquer, para mostrar a anatomia antes de escrever a de hoje:

  ```java
  @Configuration
  public class ExemploConfig {

      @Bean
      @Profile("dev")
      public MinhaInterface implementacaoDeDev() {
          return new ImplementacaoDeDev();
      }

      @Bean
      @Profile("prod")
      public MinhaInterface implementacaoDeProd() {
          return new ImplementacaoDeProd();
      }
  }
  ```

  Apontar as três peças: o método é o que o container chama para obter o
  bean; o `@Profile` decide se o método participa da subida atual; o tipo de
  retorno, `MinhaInterface`, é o que fica disponível para qualquer construtor
  que peça essa interface, não o tipo concreto. Só um dos dois métodos roda
  em cada subida, nunca os dois ao mesmo tempo.

- **Exercício curto.** Cinco minutos, em duplas. Prever a saída: se a
  aplicação subir sem nenhum parâmetro de perfil, e nenhum dos dois métodos
  `@Bean` do exemplo tiver um perfil `default`, o que acontece ao Spring
  tentar montar um bean que dependa de `MinhaInterface`? Gabarito: a subida
  falha, porque nenhum dos dois beans fica ativo sem um perfil declarado
  como ativo, e o container não tem candidato para injetar, o mesmo problema
  que a Aula 07 já preveniu fixando `spring.profiles.active=padrao` no
  `application.properties`.

### Quiz, 20h40 às 20h50

**Pergunta.** Segundo o capítulo, quando um desenvolvedor usa um framework
para estruturar seu aplicativo, quem passa a controlar o fluxo de execução
das operações que o aplicativo necessita?

- A) O próprio desenvolvedor, que chama cada função do framework
  manualmente, na ordem que escolher.
- B) O framework, que determina como o aplicativo vai funcionar, fenômeno
  que o capítulo chama de inversão de controle.
- C) O sistema operacional, que agenda a execução de cada classe do
  framework por prioridade.
- D) Framework e aplicativo executam em processos totalmente independentes,
  sem nenhuma relação de controle entre os dois.

**Correta:** B.

**Justificativa.** É a frase literal do capítulo: "um framework determina
como o aplicativo funcionará, pois ele é que controla o fluxo de execução de
operações que o aplicativo necessita. A isso se dá o nome de inversão de
controle." A alternativa A descreve o oposto do que o capítulo afirma, o uso
comum de uma biblioteca, não de um framework. A C inventa um mecanismo de
sistema operacional que o capítulo não menciona em nenhum momento. A D nega
a própria definição de framework do capítulo, que descreve bibliotecas
acopladas ao aplicativo por interfaces, e não dois processos independentes.

### Ciclo 3, 20h50 às 21h25

Laboratório de configuração explícita. O código de hoje mora no contexto
`rastreamento`, aberto na aula passada, e acrescenta a camada `service`, ainda sem
nenhuma classe.

1. **Criar o contrato de notificação.** Em `rastreamento/service`, criar a
   interface `NotificadorDeOcorrencia`, com um único método, `void
   notificar(Ocorrencia ocorrencia)`. Nenhuma anotação de framework: como
   toda interface de contrato do semestre, ela não sabe que o Spring existe.
2. **Escrever a implementação de dev.** `NotificadorDeOcorrenciaConsole`,
   também em `rastreamento/service`, sem anotação nenhuma, registrando no
   log, via `Logger` do SLF4J, uma linha como `"[DEV] ocorrencia {} do tipo
   {} registrada"`, com o `codigoRastreio` e o `getTipo()` da ocorrência.
3. **Escrever a implementação de prod.** `NotificadorDeOcorrenciaWebhookSimulado`,
   recebendo `urlWebhook` pelo construtor, também sem anotação. O método
   `notificar` não faz chamada de rede real, só registra no log `"[PROD]
   enviaria POST para {} com a ocorrencia {}"`, com a URL e o código de
   rastreio. É simulado de propósito, pela mesma razão da Aula 10: a aula
   não pode depender de um endpoint externo de verdade para funcionar em
   qualquer sala.
4. **Registrar os dois beans, explicitamente.** Criar
   `NotificacaoConfig`, anotada `@Configuration`, em `rastreamento/service`,
   com dois métodos `@Bean`: `notificadorDeOcorrenciaDev()`, anotado
   `@Profile("dev")`, devolvendo `new NotificadorDeOcorrenciaConsole()`; e
   `notificadorDeOcorrenciaProd(@Value("${rotasul.webhook.parceiro-notificacao}")
   String urlWebhook)`, anotado `@Profile("prod")`, devolvendo `new
   NotificadorDeOcorrenciaWebhookSimulado(urlWebhook)`.
5. **Criar os dois arquivos de propriedades por perfil.** Em
   `src/main/resources`, `application-dev.properties`, vazio por enquanto, e
   `application-prod.properties`, com a linha
   `rotasul.webhook.parceiro-notificacao=https://parceiro.rotasul.exemplo/webhook`.
   É a segunda metade da "configuração por perfil" do entregável de hoje: não
   só o bean muda, a propriedade também muda, e só o perfil `prod` precisa
   saber o endereço do parceiro.
6. **Comprovar por log.** Acrescentar, ainda em `NotificacaoConfig`, um
   terceiro `@Bean`, `logarNotificadorAtivo(NotificadorDeOcorrencia
   notificador)`, do tipo `CommandLineRunner`, que registra no log, ao subir,
   `"Notificador ativo: " + notificador.getClass().getSimpleName()`. Esse
   bean não tem `@Profile`: ele roda em qualquer perfil e imprime qual dos
   dois foi injetado, o mesmo `NotificadorDeOcorrencia` que os outros beans
   da aplicação vão receber.

### Ciclo 4, 21h25 às 21h50

7. **Subir com o perfil `dev`.** `./mvnw spring-boot:run
   -Dspring-boot.run.profiles=dev` e conferir, no log de inicialização, a
   linha `Notificador ativo: NotificadorDeOcorrenciaConsole`.
8. **Subir com o perfil `prod`.** Parar a aplicação e subir de novo com
   `./mvnw spring-boot:run -Dspring-boot.run.profiles=prod`, conferindo a
   linha `Notificador ativo: NotificadorDeOcorrenciaWebhookSimulado`. As
   duas capturas de log, dev e prod, são a evidência literal que o
   entregável de hoje pede.
9. **Testar os dois perfis.** Duas classes de teste em
   `src/test/java/br/uni9/rotasul/rastreamento/service/`:
   `NotificacaoConfigDevTest`, anotada `@SpringBootTest` e
   `@ActiveProfiles("dev")`, injetando `NotificadorDeOcorrencia` e
   confirmando `instanceof NotificadorDeOcorrenciaConsole`; e
   `NotificacaoConfigProdTest`, com `@ActiveProfiles("prod")`, confirmando
   `instanceof NotificadorDeOcorrenciaWebhookSimulado`. Rodar `./mvnw test`
   e ver as duas passarem sem que a suíte precise escolher perfil nenhum na
   linha de comando: cada teste fixa o seu.
10. **Deixar o gancho para a Aula 19.** Ninguém chama `notificar(...)` de
    dentro de `OcorrenciaCreator` ainda, e está certo que seja assim: hoje o
    objetivo é a configuração por perfil, não o fluxo completo de
    notificação. Anotar em `docs/decisoes.md` que a chamada real a
    `NotificadorDeOcorrencia` entra quando os serviços da Rota Sul
    conversarem entre si de verdade, na Aula 19.
11. **Registrar a decisão.** Em `docs/decisoes.md`, uma linha explicando a
    escolha de configuração explícita por `@Configuration` em vez de
    `@Profile` direto na classe, e por quê: concentrar a decisão de ambiente
    num único lugar, legível sem abrir cada implementação.

**Entregável do dia:** `NotificadorDeOcorrencia` com
`NotificadorDeOcorrenciaConsole` e `NotificadorDeOcorrenciaWebhookSimulado`,
a classe `NotificacaoConfig` com os dois `@Bean` por perfil e o
`CommandLineRunner` de log, mais os dois arquivos de propriedades por
perfil. Critério de aceitação: o log de `dev` e o log de `prod` mostrando
classes diferentes na mesma linha de saída, e `NotificacaoConfigDevTest` e
`NotificacaoConfigProdTest` passando com `./mvnw test`.

### Fechamento, 21h50 às 22h00

- `git add src docs`
- `git commit -m "feat(rastreamento): configura NotificadorDeOcorrencia por perfil dev e prod, com injecao explicita"`
- `git push`
- Fechar o ciclo comparando as duas aulas: na aula passada a Rota Sul decidiu, dentro
  do próprio código, qual estratégia de frete usar; hoje foi o container do
  Spring que decidiu, fora do código de negócio, qual notificador injetar.
  As duas são formas legítimas de trocar comportamento, e a diferença entre
  elas é exatamente o que separa um padrão de projeto de uma característica
  de framework.
- **Prévia da Aula 13.** Até aqui a Rota Sul só devolve JSON. A próxima aula
  acrescenta uma segunda porta de entrada, uma tela de verdade, com
  Thymeleaf, layout e fragments, para o atendente cadastrar um pedido sem
  abrir o navegador numa URL de API. O mesmo `PedidoService` de sempre vai
  atender as duas portas, REST e HTML, sem duplicar regra de negócio.

### Referências

1. MESQUITA, Paulo Ricardo Batista. **Capítulo 11: Frameworks.** Arquitetura
   de Software. AVA, Uninove. Fonte primária desta aula, `pdf/011.pdf`.
2. KRTZIG, M. **A Software Framework For Data Based Analysis.** VDM Verlag,
   Alemanha, 2008. Referência indicada pelo capítulo.
3. SURHONE, L. M.; TENNOE, M. T.; HESSONOW, S. F. **Software Framework.**
   Betascript, 2010. Referência indicada pelo capítulo.
4. Spring. **Documentação do Spring Framework**, seção do container de IoC e
   de beans. <https://docs.spring.io/spring-framework/reference/core/beans.html>
5. Spring Boot. **Documentação**, seção de propriedades específicas de
   perfil. <https://docs.spring.io/spring-boot/reference/features/external-config.html>
6. JUnit. **JUnit 5 User Guide.** <https://junit.org/junit5/docs/current/user-guide/>

---

## Aula 13, Frameworks para aplicativos web

**Módulo:** M3, Padrões e frameworks
**Capítulo do AVA:** `pdf/012.pdf`, Frameworks para Aplicativos Web
**Entregável:** a tela de cadastro de pedido em `/pedidos/novo`, construída em
Thymeleaf com um layout compartilhado por fragments, o formulário validando o
campo `cliente` como obrigatório, e uma tela de confirmação mostrando o frete
calculado pelo `CalculoDeFreteService` da Aula 11. Critério de aceitação:
submeter o formulário sem preencher `cliente` devolve a mesma tela com a
mensagem de erro, sem registrar nada; submeter com `cliente` preenchido
registra o pedido e mostra a confirmação; `PedidoFormControllerTest` passando
com `./mvnw test`.

### Retomada, 5 minutos

Na Aula 12 cada aluno entregou `NotificadorDeOcorrencia`, com
`NotificadorDeOcorrenciaConsole` para o perfil `dev` e
`NotificadorDeOcorrenciaWebhookSimulado` para o perfil `prod`, ligados
explicitamente por `NotificacaoConfig`, e comprovou pelo log que o container
troca de implementação sozinho conforme o perfil ativo. Projetar a tabela da
Aula 06 que compara o capítulo com a stack da Rota Sul, na linha Visão:
"Thymeleaf, a partir da Aula 13". A promessa feita há sete aulas vence hoje: a
Rota Sul ganha sua primeira tela de verdade, e o `PedidoService` que já existe
desde a Aula 06 vai atender essa tela sem que uma linha de regra de negócio
precise ser reescrita.

### Ciclo 1, 19h30 às 20h05

- **Conceito.** A origem das tecnologias de apresentação web, na narrativa do
  capítulo [1].

  **Da ARPANET ao HTML.** O capítulo reconstrói a linha do tempo: nos anos
  1960, militares americanos idealizaram uma base de informações
  descentralizada, para que um ataque não apagasse dados de toda a rede; daí
  nasceu a ARPANET, construída por um consórcio de universidades, que evoluiu
  para a Internet. No início bastava apresentar informação, e para organizar
  essa apresentação surgiu o HTML, HyperText Markup Language, uma linguagem
  de marcação que qualquer navegador interpreta do mesmo jeito. Com o uso
  comercial da Internet nos anos 1990, foi preciso deixar o usuário
  interagir com a página, e o próprio HTML precisou mudar; surgiram o CSS,
  para o leiaute, e o JavaScript, definido pela W3C para controlar
  dinamicamente o conteúdo a partir da interação do usuário. Antes do
  JavaScript, formulários eram tratados por Applets Java, logo substituídos
  por Servlets e por CGI, rotinas de servidor escritas em C ou C++.

  **De site estático a site orientado a serviços.** Até o início dos anos
  2000, um site podia ser puramente de conteúdo estático, apresentando
  informação de uma empresa. O outro tipo, orientado a serviços, muda o
  conteúdo conforme a interação do usuário; hoje é raro encontrar um site
  puramente estático, e redes sociais, portais de notícia e comércio
  eletrônico são exemplos do segundo tipo, citados pelo capítulo.

  **A tríade Java Web do capítulo.** Para sistemas de alta complexidade, o
  capítulo descreve o subconjunto Java Web da plataforma Java EE, formado
  por três peças: **JSP**, misturado ao HTML em arquivos de extensão `.jsp`,
  controla o conteúdo apresentado ao usuário; **Servlet**, classe que trata
  requisições e gera respostas, controla a navegação entre páginas e o uso
  das classes JavaBeans; **JavaBeans**, classes que executam a regra de
  negócio e as tarefas de infraestrutura, como o acesso à base de dados. Para
  funcionar, uma aplicação Java Web precisa do Descritor de Deployment,
  `web.xml`, que configura como os Servlets são mapeados e como o Servlet
  Container deve operar.

- **Demonstração no projetor.** Ler as três definições do capítulo, JSP,
  Servlet e JavaBeans, e escrever ao lado o equivalente que a Rota Sul vai
  construir hoje: Thymeleaf no lugar de JSP, controlando o que é apresentado;
  `PedidoFormController`, um `@Controller` novo, no lugar do Servlet,
  recebendo a requisição e decidindo qual página devolver; `PedidoService` e
  `Pedido`, que já existem desde a Aula 06, no lugar das JavaBeans, com a
  regra de negócio. O `web.xml` do capítulo não tem equivalente direto: o
  Spring Boot resolve o mapeamento de URLs por anotação, sem descritor de
  deployment separado.

- **Exercício curto.** Cinco minutos, individual. Responder por escrito: na
  tríade do capítulo, JSP, Servlet e JavaBeans, qual das três teria a regra
  "pedido sem cliente é recusado", herdada da Aula 06? E, na versão da Rota
  Sul, em qual classe essa mesma regra continua morando hoje? Gabarito: na
  tríade do capítulo, a regra pertence à JavaBean; na Rota Sul, ela continua
  em `PedidoService`, e vai continuar lá mesmo depois que a tela de hoje
  existir, porque trocar a porta de entrada não muda onde a regra de negócio
  mora.

### Ciclo 2, 20h05 às 20h40

- **Conceito.** Como o servidor decide sincronizar dados com o cliente, e a
  fronteira entre apresentação e regra de negócio.

  **PUSH e PULL, a classificação do capítulo.** O capítulo descreve dois
  modos de sincronizar dados entre cliente e servidor. No modo **PUSH**, os
  componentes do lado do servidor enviam os dados já prontos para o lado do
  cliente; os frameworks mais conhecidos para esse mecanismo são Struts,
  Ruby on Rails e **Spring MVC**, citado nominalmente pelo capítulo. No modo
  **PULL**, os componentes do lado do cliente solicitam a componentes de
  controle do servidor que lhes enviem as informações a mostrar; os
  frameworks mais conhecidos aqui são JavaServer Faces, Struts2, ASP.Net Web
  Forms e Laravel. O laboratório de hoje é PUSH: o `PedidoFormController` já
  monta a página inteira, com os dados prontos, antes de enviá-la ao
  navegador.

  > **Nota para o professor.** O capítulo cita o Hibernate como framework
  > para aplicativos web, ao lado de BootStrap, jQuery e Ajax, descrevendo-o
  > como algo que conecta interfaces gráficas às classes de persistência.
  > Essa classificação mistura camadas, apresentação e persistência não são a
  > mesma coisa, e o Hibernate volta com mais precisão na Aula 15. Dizer isso
  > à turma sem corrigir o capítulo na frente dela: o texto do AVA é a fonte,
  > e esta observação é só para o professor não repetir a mistura em sala.

  **A fronteira entre view e regra de negócio, o ponto central de hoje.** O
  formulário de hoje vai validar que o campo `cliente` foi preenchido, antes
  mesmo de qualquer dado chegar ao `PedidoService`. Essa validação de tela
  não substitui a regra "pedido sem cliente é recusado" que o `PedidoService`
  já aplica desde a Aula 06; ela apenas antecipa o mesmo problema, numa
  camada mais barata de errar. Se alguém pular a tela e chamar `POST
  /pedidos` direto, sem passar pelo formulário, o `PedidoService` continua
  sendo a última linha de defesa, porque é ele quem carrega a regra, não o
  Thymeleaf.

  **Layout e fragments, o padrão de composição de hoje.** Em vez de repetir
  cabeçalho e rodapé em cada página, o Thymeleaf permite marcar um trecho de
  um arquivo com `th:fragment` e incluí-lo em outra página com `th:replace`
  ou `th:insert`. É composição de página, não herança de classe: a página
  final é montada colando pedaços marcados, o mesmo princípio de reuso que
  já apareceu nos componentes de software desde a Aula 06, agora aplicado à
  camada de visão.

- **Demonstração no projetor.** Esqueleto mínimo de um fragment, para mostrar
  a mecânica antes de escrever o layout de verdade:

  ```html
  <header th:fragment="cabecalho(titulo)">
    <h1 th:text="${titulo}">Título da página</h1>
  </header>
  ```

  E o uso desse fragment em outra página:

  ```html
  <div th:replace="~{fragments/layout :: cabecalho(titulo='Novo pedido')}"></div>
  ```

  Apontar: o parâmetro `titulo` entra pelo fragment, exatamente como um
  parâmetro de método; `th:replace` troca a própria `div` pelo conteúdo do
  fragment, `th:insert` inseriria o conteúdo dentro da `div`, mantendo a
  tag. A aula de hoje usa `th:replace` nos dois casos, cabeçalho e rodapé.

- **Exercício curto.** Cinco minutos, em duplas. Decidir, para cada situação,
  se a validação pertence à view ou à regra de negócio, e por quê: (a)
  impedir que o formulário seja enviado sem o campo `cliente` preenchido; (b)
  recusar um pedido cujo lojista está na lista de bloqueados, herdada da
  Aula 07; (c) mostrar uma mensagem de erro em português perto do campo
  vazio. Gabarito: (a) e (c) são view, cuidam da experiência de quem
  preenche o formulário; (b) é regra de negócio, porque depende de dado que
  só o domínio conhece e precisa valer para qualquer porta de entrada, tela
  ou API.

### Quiz, 20h40 às 20h50

**Pergunta.** A Rota Sul decide que, ao processar um novo pedido, o servidor
já gera a página HTML pronta com os dados atualizados e a envia ao navegador
do atendente, sem que o navegador precise pedir nada além da requisição
inicial. Segundo a classificação do capítulo, esse mecanismo de sincronização
de dados entre cliente e servidor é conhecido como:

- A) PUSH, mecanismo implementado por frameworks como Struts, Ruby on Rails e
  Spring MVC.
- B) PULL, mecanismo implementado por frameworks como JavaServer Faces e
  Struts2.
- C) Ajax, técnica que atualiza parcialmente uma página sem recarregá-la por
  inteiro.
- D) ORM, mecanismo que mapeia objetos da aplicação para tabelas do banco de
  dados.

**Correta:** A.

**Justificativa.** O capítulo descreve o PUSH exatamente assim: "os
componentes de software que são executados do lado do servidor enviam os
dados para os componentes executados do lado do cliente", citando Struts,
Ruby on Rails e Spring MVC como frameworks conhecidos para esse mecanismo, o
mesmo Spring MVC que sustenta o Thymeleaf usado no laboratório de hoje. A
alternativa B descreve o modo PULL, o oposto, em que o cliente é quem
solicita os dados a componentes de controle do servidor, e cita outra
família de frameworks. A C descreve Ajax, uma técnica do mesmo capítulo, mas
para atualização parcial de página, não para o mecanismo de sincronização
completa descrito no enunciado. A D descreve mapeamento objeto-relacional,
assunto de um capítulo diferente, sem relação com sincronização entre
cliente e servidor.

### Ciclo 3, 20h50 às 21h25

Laboratório de apresentação. O laboratório de hoje não é sobre visual: o
foco é o papel da camada de apresentação, o padrão de composição por layout
e fragments, e a fronteira entre view e regra de negócio. O HTML fica
deliberadamente simples, sem framework de CSS.

1. **Acrescentar as dependências.** No `pom.xml`,
   `spring-boot-starter-thymeleaf`, fixada no contrato técnico desde a Aula
   01 e usada pela primeira vez hoje, e `spring-boot-starter-validation`,
   nova, necessária para `@NotBlank` e `@Valid` no formulário.
2. **Criar o layout compartilhado.** Em
   `src/main/resources/templates/fragments/layout.html`, dois fragments:
   `cabecalho(titulo)`, com um `<h1>` mostrando o título recebido por
   parâmetro e um menu com dois links, um para `/pedidos` (a API REST da
   Aula 06) e outro para `/pedidos/novo` (a tela de hoje); e `rodape`, com
   uma linha fixa identificando o painel interno da Rota Sul.
3. **Criar o modelo de formulário.** Em `pedido/web`, a classe `PedidoForm`,
   com os atributos `cliente` (anotado `@NotBlank(message = "Cliente e
   obrigatorio")`), `descricao` (sem validação) e `regiao` (`String`, com
   valor padrão `"PRINCIPAL"`, o mesmo atributo que a Aula 11 acrescentou ao
   `Pedido`). Diferente de `Pedido`, `PedidoForm` pode ter anotação de
   framework: ela pertence à camada `web`, não ao domínio.
4. **Escrever o controlador da tela.** `PedidoFormController`, em
   `pedido/web`, anotado `@Controller`, não `@RestController`, mapeado em
   `/pedidos/novo`. Recebe `PedidoService` e `CalculoDeFreteService` pelo
   construtor. O método `GET` monta um `PedidoForm` vazio, adiciona ao
   `Model` com o nome `pedidoForm` e devolve o nome lógico da view,
   `"pedidos/formulario"`, sem o `.html`, resolvido pelo Thymeleaf.
5. **Escrever o template do formulário.** Em
   `src/main/resources/templates/pedidos/formulario.html`, incluir o
   cabeçalho e o rodapé com `th:replace`, e um `<form>` com
   `th:object="${pedidoForm}"`, um `<input th:field="*{cliente}">`, um
   `<span th:if="${#fields.hasErrors('cliente')}" th:errors="*{cliente}">`
   para a mensagem de erro, um campo de texto para `descricao` e um
   `<select th:field="*{regiao}">` com as opções `PRINCIPAL` e
   `ULTIMA_MILHA`.
6. **Subir e ver a tela.** `./mvnw spring-boot:run` e abrir
   `http://localhost:PORTA/pedidos/novo` no navegador, na porta que o
   terminal imprimiu. Conferir que o cabeçalho, o formulário e o rodapé
   aparecem, mesmo sem nenhuma folha de estilo.

### Ciclo 4, 21h25 às 21h50

7. **Escrever o `POST` com validação.** No mesmo `PedidoFormController`, um
   método `POST` em `/pedidos/novo`, recebendo `@Valid @ModelAttribute("pedidoForm")
   PedidoForm form` e `BindingResult resultado`. Se `resultado.hasErrors()`,
   devolver de novo `"pedidos/formulario"`, sem redirecionar, para o
   Thymeleaf reconstruir a página com as mensagens de erro ao lado dos
   campos. Se não houver erro, montar um `Pedido` a partir do `PedidoForm`,
   chamar `pedidoService.registrar(pedido)`, calcular o frete com
   `calculoDeFreteService.calcular(pedido)`, e devolver a view
   `"pedidos/confirmacao"`, com o pedido e o frete no `Model`.
8. **Escrever o template de confirmação.** Em
   `templates/pedidos/confirmacao.html`, reaproveitando o cabeçalho e o
   rodapé do mesmo jeito, mostrando o nome do cliente registrado e o valor
   do frete calculado, com o texto "Frete calculado pela estratégia de
   $regiao$", ligando visualmente o formulário de hoje ao Strategy da Aula
   11.
9. **Testar a validação sem navegador.** `PedidoFormControllerTest`, em
   `src/test/java/br/uni9/rotasul/pedido/web/`, anotado `@WebMvcTest(PedidoFormController.class)`,
   com `PedidoService` e `CalculoDeFreteService` como `@MockBean`. Dois
   casos com `MockMvc`: um `POST` para `/pedidos/novo` sem o parâmetro
   `cliente` devolve status 200 e a view `pedidos/formulario` de novo, sem
   chamar `pedidoService.registrar`; um `POST` com `cliente` preenchido
   devolve a view `pedidos/confirmacao` e chama `pedidoService.registrar`
   exatamente uma vez. Rodar `./mvnw test`.
10. **Confirmar a fronteira em voz alta.** Enviar, por `curl`, um `POST
    /pedidos` (a API REST da Aula 06, não a tela) sem o campo `cliente`, e
    conferir que o `PedidoService` recusa do mesmo jeito que recusaria vindo
    da tela. É a prova de que a regra de negócio não migrou para o
    Thymeleaf, só ganhou uma segunda porta de entrada na frente dela.
11. **Registrar a decisão.** Em `docs/decisoes.md`, uma linha explicando a
    escolha de layout e fragments em vez de repetir HTML em cada página, e
    outra linha explicitando que a validação de `PedidoForm` é
    responsabilidade da view, sem substituir a regra de `PedidoService`.

**Entregável do dia:** `PedidoFormController`, `PedidoForm`,
`templates/fragments/layout.html`, `templates/pedidos/formulario.html` e
`templates/pedidos/confirmacao.html`. Critério de aceitação: `POST
/pedidos/novo` sem `cliente` devolvendo a mesma tela com erro, com `cliente`
devolvendo a confirmação com o frete calculado, `PedidoFormControllerTest`
passando com `./mvnw test`, e o `POST /pedidos` da API REST continuando a
recusar pedido sem cliente, comprovando que a regra não saiu do
`PedidoService`.

### Fechamento, 21h50 às 22h00

- `git add src docs`
- `git commit -m "feat(pedido): adiciona tela de cadastro em Thymeleaf com layout, fragments e validacao"`
- `git push`
- Fechar o ciclo relendo a tabela da Aula 06: a linha "Visão" que dizia
  "Thymeleaf, a partir da Aula 13" acaba de se cumprir, e as outras três
  linhas, Controle, Modelo com regra e Modelo com dados, não mudaram uma
  vírgula.
- **Prévia da Aula 14.** A tela de hoje ainda grava tudo em
  `PedidoRepositoryEmMemoria`, a mesma implementação da Aula 06: fechar a
  aplicação apaga todo pedido cadastrado pela tela nova. A próxima aula
  ataca exatamente esse ponto, trocando o repositório em memória por JDBC
  puro, e a turma vai medir, em linhas de código, o preço dessa mudança.

### Referências

1. MESQUITA, Paulo Ricardo Batista. **Capítulo 12: Frameworks para
   Aplicativos Web.** Arquitetura de Software. AVA, Uninove. Fonte primária
   desta aula, `pdf/012.pdf`.
2. LINWOOD, J.; MINTER, D.; OTTINGER, J. **Beginning Hibernate.** Apress,
   2014. Referência indicada pelo capítulo.
3. FLORES, R. **Getting Started With Bootstrap 3.** Smashwords, 2015.
   Referência indicada pelo capítulo.
4. SILVA, M. S. **jQuery, a Biblioteca do Programador JavaScript.** Novatec,
   2013. Referência indicada pelo capítulo.
5. Thymeleaf. **Documentação**, seção de layout e fragments.
   <https://www.thymeleaf.org/doc/tutorials/3.1/usingthymeleaf.html>
6. Spring. **Documentação do Spring Framework**, seção de validação de
   formulário. <https://docs.spring.io/spring-framework/reference/web/webmvc/mvc-controller/ann-validation.html>
7. JUnit. **JUnit 5 User Guide.** <https://junit.org/junit5/docs/current/user-guide/>

---

## Aula 14, Frameworks para gerenciamento de dados

**Módulo:** M3, Padrões e frameworks
**Capítulo do AVA:** `pdf/013.pdf`, Frameworks para Gerenciamento de Dados
**Entregável:** `PedidoRepositoryJdbc`, nova implementação de `PedidoRepository`
usando JDBC puro contra um MySQL real, no lugar de
`PedidoRepositoryEmMemoria`, mais a contagem de linhas de código das duas
implementações registrada em `docs/decisoes.md`. Critério de aceitação: a
aplicação subindo com `PedidoRepositoryJdbc` como único bean de
`PedidoRepository`, um pedido sobrevivendo a um reinício da aplicação,
`PedidoRepositoryJdbcTest` passando com `./mvnw test` usando Testcontainers, e
a contagem de linhas antes e depois registrada.

> **Nota para o professor.** A troca do repositório em memória por um banco
> real, anunciada lá atrás no passo 4 do Ciclo 3 da Aula 06, acontece em duas
> etapas, e hoje é a primeira: a Aula 14 troca a memória por JDBC puro,
> sentindo a verbosidade na mão; a Aula 15 troca o JDBC por JPA, sentindo o
> alívio. Vale dizer isso à turma na abertura do laboratório, para ninguém
> esperar o ORM já hoje: a verbosidade de hoje é proposital, e é ela a régua
> que a próxima aula vai usar.

### Retomada, 5 minutos

Na Aula 13 cada aluno entregou a tela de cadastro de pedido em
`/pedidos/novo`, com layout, fragments e validação do campo `cliente`. Abrir
essa tela, cadastrar um pedido, reiniciar a aplicação com `Ctrl+C` e `./mvnw
spring-boot:run`, e voltar em `/pedidos`: o pedido sumiu. Perguntar à turma
por quê. A resposta está em `PedidoRepositoryEmMemoria`, viva desde a Aula
06: uma `List` dentro da JVM, que existe enquanto o processo existe e some
quando ele para. A aula de hoje ataca exatamente esse ponto.

### Ciclo 1, 19h30 às 20h05

- **Conceito.** Persistência de dados e a motivação de um framework ou API
  dedicados a ela, na descrição do capítulo [1].

  **Por que persistir com um mecanismo eficiente.** O capítulo abre
  afirmando que o objetivo principal de um aplicativo é prover dados a seus
  usuários, obtidos de outros sistemas ou digitados pelo próprio usuário; para
  isso, o aplicativo precisa persistir esses dados com eficiência,
  mantendo-os sempre disponíveis e atualizados. A forma mais comum de
  armazenamento é um SGBD, sistema de gerenciamento de banco de dados, e o
  capítulo cita uma proporção de mercado de aproximadamente 80% de SGBDs
  relacionais, que executam SQL, contra 20% para os demais modelos,
  incluindo NoSQL.

  **A origem do ODBC, e a ideia de independência.** Entre os anos 1970 e
  1990, os aplicativos evoluíram até um padrão chamado ODBC, Open DataBase
  Connectivity, a primeira solução, segundo o capítulo, a manter alguma
  independência entre o aplicativo e o SGBD que ele usa. A ideia do ODBC era
  prover uma interface que o desenvolvedor acopla aos drivers específicos de
  cada fornecedor de SGBD, deixando a camada de execução de transações
  desacoplada do driver de conexão. Uma camada de persistência assim,
  totalmente independente da aplicação, pode ser reaproveitada por qualquer
  aplicativo que precise persistir dados, na forma de um framework ou de uma
  API.

  **Framework contra API de persistência, a distinção do capítulo.** No caso
  de um framework, os componentes têm interfaces de conexão que acoplam o
  framework ao aplicativo, e é o framework quem determina como a camada de
  persistência funciona, ainda que o desenvolvedor mantenha algum controle.
  No caso de uma API, os componentes também têm interfaces de conexão, mas
  quem realiza as tarefas de persistir é a própria API, sem o desenvolvedor
  controlar como isso acontece por dentro. `PedidoRepositoryJdbc`, que a
  turma escreve hoje, não é nenhum dos dois: é o próprio desenvolvedor
  controlando cada instrução SQL, sem framework nem API de persistência no
  meio. É exatamente esse contraste, sentido na mão, que prepara a Aula 15.

- **Demonstração no projetor.** Projetar `PedidoRepositoryEmMemoria`, da
  Aula 06, ao lado da definição de camada de persistência do capítulo:
  independente da aplicação, reutilizável por qualquer aplicativo. A versão
  em memória cumpre a independência da interface, `PedidoRepository`, mas
  não cumpre a persistência de verdade: os dados não sobrevivem ao processo.
  Hoje a turma escreve uma implementação que cumpre as duas coisas.

- **Exercício curto.** Cinco minutos, individual. Segundo a definição do
  capítulo, framework de persistência é quem determina como a camada de
  dados funciona, com algum controle do desenvolvedor; API de persistência é
  quem executa as tarefas de persistir sem o desenvolvedor controlar como.
  Classificar: Spring Data JPA, que a Aula 15 vai apresentar, é mais parecido
  com framework ou com API, segundo essa definição? Gabarito: mais parecido
  com framework, porque o desenvolvedor escreve a interface do repositório e
  mantém controle sobre o mapeamento das entidades, mesmo que o Spring Data
  gere a implementação.

### Ciclo 2, 20h05 às 20h40

- **Conceito.** Mapa objeto-relacional e os padrões de projeto que o
  capítulo lista para persistência de dados.

  **A raiz do problema do ORM.** O capítulo explica por que existe o mapa
  objeto-relacional: a estrutura de tabelas de um SGBD relacional não é
  diretamente mapeável para a forma como a programação orientada a objetos
  estrutura classes e objetos. Um mapa objeto-relacional, ORM, orienta o
  desenvolvedor a escrever classes de entidade, cada uma representando uma
  entidade do SGBD, informando à API o nome da entidade associada, as
  colunas e as restrições de chave. A API usa reflexão de objetos, a técnica
  que permite a uma classe examinar a estrutura de outra em tempo de
  execução, para elaborar os comandos SQL a partir dessas classes.

  > **Nota para o professor.** O capítulo ilustra ORM com uma classe `Banda`
  > anotada `@Entity`, `@Table`, `@Id` e `@OneToMany`, e com uma
  > `AbstractFacade<T>` genérica chamando `EntityManager`. Isso é JPA, o
  > assunto da Aula 15, não de hoje. Ler esse trecho do capítulo com a turma
  > é útil para mostrar aonde o semestre está indo, mas nenhuma dessas
  > anotações entra no laboratório de hoje: o laboratório de hoje é
  > deliberadamente o oposto disso, JDBC sem nenhum mapeamento automático.

  **Os cinco padrões de projeto que o capítulo lista para persistência.**
  Unit-of-Work, que agrupa várias instruções SQL numa única transação, para
  não gastar uma transação por comando; **Repository Pattern**, que orienta o
  desenvolvedor a escrever uma camada abstrata de dados, usada pela aplicação
  para obter o que precisa, em vez de se conectar diretamente à base; Bridge
  Pattern, que conecta um aplicativo a diferentes tipos de base de dados;
  Factory Pattern, que define um modo conveniente de criar os objetos que a
  regra de negócio precisa; Gateway Pattern, que determina a lógica de
  conexão entre regra de negócio e banco de dados.

  **O nome que faltava desde a Aula 06.** `PedidoRepository`, a interface
  criada na Aula 06 e ainda o contrato de hoje, é uma aplicação do Repository
  Pattern do capítulo: uma camada abstrata de dados, que `PedidoService`
  usa sem se conectar diretamente a banco nenhum. A turma usa esse padrão há
  oito aulas sem o nome; hoje o capítulo devolve o nome, e mostra por que a
  interface valeu a pena, trocar a implementação de hoje não vai custar uma
  linha sequer em `PedidoService`.

- **Demonstração no projetor.** Ler em voz alta a listagem do capítulo com a
  classe `Banda`, contando as anotações de mapeamento numa única declaração
  de atributo, `@Id`, `@GeneratedValue`, `@Column`. Contrastar com o que a
  turma vai escrever daqui a pouco em `PedidoRepositoryJdbc`: nenhuma
  anotação de mapeamento, e em troca, cada coluna lida com
  `resultado.getString("cliente")`, à mão. É o preço e o benefício invertidos
  entre os dois mundos, e a Aula 15 mostra o outro lado da balança.

- **Exercício curto.** Cinco minutos, em duplas. Reler a definição de
  Repository Pattern do capítulo e decidir: se `PedidoService` chamasse
  `DriverManager.getConnection(...)` diretamente, dentro de si mesmo, em vez
  de depender de `PedidoRepository`, isso ainda seria uma aplicação do
  Repository Pattern? Gabarito: não, porque o padrão exige exatamente a
  camada abstrata entre a aplicação e a base, e uma conexão direta dentro do
  serviço apaga essa camada, mesmo que o resultado funcione.

### Quiz, 20h40 às 20h50

**Pergunta.** O capítulo lista cinco padrões de projeto usados no
desenvolvimento de frameworks e APIs de persistência de dados. Desde a Aula
06, a Rota Sul já usa a interface `PedidoRepository`, com implementações
trocáveis (a de hoje troca a versão em memória por JDBC), sem que
`PedidoService` precise mudar uma linha. Qual dos cinco padrões do capítulo
descreve exatamente essa prática?

- A) Unit-of-Work, que agrupa várias instruções SQL dentro de uma única
  transação.
- B) Repository Pattern, que orienta o desenvolvedor a escrever uma camada
  abstrata de dados, usada pela aplicação para obter o que precisa, em vez
  de se conectar diretamente à base de dados.
- C) Bridge Pattern, que conecta um aplicativo a diferentes tipos de base de
  dados.
- D) Gateway Pattern, que determina a lógica de conexão entre regra de
  negócio e banco de dados.

**Correta:** B.

**Justificativa.** É a definição literal do capítulo para o Repository
Pattern, e descreve exatamente o papel de `PedidoRepository`: uma camada
abstrata entre `PedidoService` e a origem real dos dados, trocável sem
alterar quem a consome. A é um padrão real do capítulo, mas resolve outro
problema, agrupar comandos numa transação, não abstrair o acesso. A C
descreve conectar-se a diferentes tipos de banco ao mesmo tempo, o que não é
o caso da Rota Sul, que troca uma implementação por outra, não usa as duas
juntas. A D descreve uma lógica de conexão entre regra de negócio e banco,
mais próxima do que um `Gateway` faria dentro do próprio repositório do que
do papel da interface em si.

### Ciclo 3, 20h50 às 21h25

Laboratório de troca de implementação. O contrato `PedidoRepository`, com
`salvar(Pedido)` e `listarTodos()`, não muda uma linha; só a implementação
por trás dele muda, de memória para um MySQL real acessado por JDBC puro,
sem `JdbcTemplate` e sem ORM.

1. **Acrescentar as dependências.** No `pom.xml`:
   `spring-boot-starter-jdbc`, que traz o `DataSource` autoconfigurado pelo
   Spring Boot; `mysql-connector-j`, o driver JDBC do MySQL; `flyway-core`, já
   fixado no contrato técnico para controlar a evolução do schema; e
   `org.testcontainers:mysql`, para o teste de hoje subir um MySQL descartável
   automaticamente.
2. **Subir um MySQL local.** `docker run --name rotasul-mysql -e
   MYSQL_ROOT_PASSWORD=${DB_PASSWORD} -e MYSQL_DATABASE=rotasul -p
   3306:3306 -d mysql:8.4`, com `DB_PASSWORD` lida do `.env`, nunca escrita
   no comando nem no repositório.
3. **Escrever a migration.** Em
   `src/main/resources/db/migration/V1__cria_tabela_pedido.sql`, criar a
   tabela `pedido`, com `id` (chave primária autoincremento), `cliente`
   (obrigatório), `descricao`, `situacao` (obrigatório) e `regiao`
   (obrigatório, o atributo que a Aula 11 acrescentou ao domínio). O Flyway
   aplica essa migration sozinho na próxima subida da aplicação.
4. **Configurar o datasource.** Em `application.properties`,
   `spring.datasource.url=jdbc:mysql://localhost:3306/rotasul`,
   `spring.datasource.username=root` e
   `spring.datasource.password=${DB_PASSWORD}`. Nenhuma senha em texto puro
   no arquivo, a mesma regra desde a Aula 01.
5. **Escrever `PedidoRepositoryJdbc`.** Em `pedido/repository`, implementando
   `PedidoRepository` com `java.sql` puro, recebendo `DataSource` pelo
   construtor:

   ```java
   @Override
   public Pedido salvar(Pedido pedido) {
       String sql = "INSERT INTO pedido (cliente, descricao, situacao, regiao) "
           + "VALUES (?, ?, ?, ?)";
       try (Connection conexao = dataSource.getConnection();
            PreparedStatement comando = conexao.prepareStatement(
                sql, Statement.RETURN_GENERATED_KEYS)) {
           comando.setString(1, pedido.getCliente());
           comando.setString(2, pedido.getDescricao());
           comando.setString(3, pedido.getSituacao());
           comando.setString(4, pedido.getRegiao());
           comando.executeUpdate();
           try (ResultSet chaves = comando.getGeneratedKeys()) {
               if (chaves.next()) {
                   pedido.setId(chaves.getLong(1));
               }
           }
           return pedido;
       } catch (SQLException erro) {
           throw new IllegalStateException("falha ao salvar pedido", erro);
       }
   }
   ```

   `listarTodos()` segue o mesmo padrão, com `SELECT`, um
   `PreparedStatement`, um `ResultSet` percorrido em `while (resultado.next())`
   e a montagem manual de cada `Pedido` a partir das colunas lidas. Ajustar
   os nomes de campo e o construtor de `Pedido` conforme a versão que cada
   aluno já tem, escrita na Aula 06 e ajustada na Aula 11.
6. **Compilar e contar as linhas.** `./mvnw compile`, e então `wc -l
   src/main/java/br/uni9/rotasul/pedido/repository/PedidoRepositoryEmMemoria.java
   src/main/java/br/uni9/rotasul/pedido/repository/PedidoRepositoryJdbc.java`,
   anotando os dois números num papel ou num editor de texto à parte, para o
   registro do Ciclo 4.

### Ciclo 4, 21h25 às 21h50

7. **Desativar a implementação em memória.** Remover a anotação
   `@Repository` de `PedidoRepositoryEmMemoria`. A classe continua existindo
   no código, intacta, só deixa de ser candidata a bean; é o material de
   comparação da contagem de linhas, não código morto para apagar. Acrescentar
   `@Repository` em `PedidoRepositoryJdbc`, que passa a ser a única
   implementação que o Spring enxerga.
8. **Provar a persistência real.** Subir a aplicação, `./mvnw
   spring-boot:run`, cadastrar um pedido pela tela `/pedidos/novo` da Aula
   13, parar a aplicação com `Ctrl+C`, subir de novo, e conferir em
   `/pedidos` que o pedido continua lá. É o oposto exato do que a retomada
   de hoje mostrou com a versão em memória.
9. **Testar com Testcontainers.** `PedidoRepositoryJdbcTest`, em
   `src/test/java/br/uni9/rotasul/pedido/repository/`, anotado
   `@Testcontainers` e `@SpringBootTest`, com um `@Container static
   MySQLContainer<?> mysql = new MySQLContainer<>("mysql:8.4")`, e um método
   `@DynamicPropertySource` sobrescrevendo `spring.datasource.url`,
   `username` e `password` com os valores do container. Um caso: salvar um
   `Pedido` e conferir que `listarTodos()` devolve uma lista de tamanho um.
   Esse teste sobe um MySQL descartável a cada execução, sem depender do
   container manual do passo 2. Rodar `./mvnw test`.
10. **Registrar a contagem, o entregável central de hoje.** Em
    `docs/decisoes.md`, uma linha com os dois números do passo 6, por
    exemplo "`PedidoRepositoryEmMemoria`: 24 linhas; `PedidoRepositoryJdbc`:
    58 linhas", mais uma frase curta explicando de onde vem a diferença:
    abertura e fechamento de conexão, `PreparedStatement`, tratamento de
    `SQLException` e montagem manual de cada `Pedido` a partir do
    `ResultSet`, tudo isso que a versão em memória nunca precisou fazer.
11. **Registrar a decisão de arquitetura.** Uma segunda linha em
    `docs/decisoes.md`, nomeando o Repository Pattern do capítulo como a
    razão de essa troca ter custado zero linha em `PedidoService`.

**Entregável do dia:** `PedidoRepositoryJdbc` como única implementação ativa
de `PedidoRepository`, a migration Flyway, `PedidoRepositoryJdbcTest` com
Testcontainers, e a contagem de linhas registrada em `docs/decisoes.md`.
Critério de aceitação: um pedido cadastrado pela tela sobrevivendo a um
reinício da aplicação, `./mvnw test` passando, e as duas linhas de
`docs/decisoes.md` do passo 10 e do passo 11 presentes.

### Fechamento, 21h50 às 22h00

- `git add src docs pom.xml`
- `git commit -m "feat(pedido): troca PedidoRepositoryEmMemoria por PedidoRepositoryJdbc com JDBC puro"`
- `git push`
- Fechar o Módulo 3 relendo as quatro aulas em uma frase cada: Strategy e
  Factory Method nomeando o que a Rota Sul já fazia, inversão de controle
  explicando quem decide qual bean sobe, Thymeleaf abrindo uma segunda porta
  de entrada sem duplicar regra de negócio, e hoje o primeiro contato com um
  banco de verdade, sentido na mão em linhas de código.
- **Prévia da Aula 15.** A contagem de hoje não é só estatística: é a régua
  que a próxima aula usa. A Aula 15 troca `PedidoRepositoryJdbc` por uma
  versão sobre a API de Persistência Java, e a turma mede de novo quantas
  linhas isso custa, desta vez para menos. O nome dessa API já apareceu hoje,
  de relance, na classe `Banda` do capítulo: é o assunto da próxima aula.

### Referências

1. MESQUITA, Paulo Ricardo Batista. **Capítulo 13: Frameworks para
   Gerenciamento de Dados.** Arquitetura de Software. AVA, Uninove. Fonte
   primária desta aula, `pdf/013.pdf`.
2. BALZER, Stephanie. **Contracted Persistent Object Programming.**
   University of Glasgow, School of CS Research; ETH Zürich, 2015.
   Referência indicada pelo capítulo.
3. Oracle. **MySQL Reference Manual.** <https://dev.mysql.com/doc/>
4. Flyway. **Documentação**, seção de migrations.
   <https://documentation.red-gate.com/fd/migrations-184127470.html>
5. Testcontainers. **Documentação do módulo MySQL.**
   <https://java.testcontainers.org/modules/databases/mysql/>
6. Oracle. **JDBC API Documentation.**
   <https://docs.oracle.com/javase/8/docs/technotes/guides/jdbc/>
7. JUnit. **JUnit 5 User Guide.** <https://junit.org/junit5/docs/current/user-guide/>

---

## Aula 15, API de persistência Java, JPA

**Módulo:** M4, Persistência e componentes
**Capítulo do AVA:** `pdf/014.pdf`, API de Persistência Java
**Entregável:** CRUD completo de `Pedido` (criar, listar, buscar por id, atualizar,
excluir) persistindo no MySQL através de `PedidoRepository` migrado para Spring
Data JPA, com a migration da Aula 14 permanecendo a única fonte de verdade do
schema. Critério de aceitação: os cinco verbos do CRUD respondendo em
`/pedidos`, `PedidoRepository` sem nenhuma linha de implementação escrita à
mão, `PedidoRepositoryTest` passando com `./mvnw test` usando Testcontainers, e
a contagem de linhas das três versões do repositório (memória, JDBC, JPA)
fechada em `docs/decisoes.md`.

### Retomada, 5 minutos

Projetar `docs/decisoes.md` da Aula 14, na linha que registrou a contagem de
linhas: `PedidoRepositoryEmMemoria`, algo como 24 linhas, contra
`PedidoRepositoryJdbc`, algo como 58 linhas, mais a segunda linha explicando de
onde vinha a diferença, abertura e fechamento de conexão, `PreparedStatement`,
tratamento de `SQLException` e montagem manual de cada `Pedido` a partir do
`ResultSet`. Perguntar à turma: e se existisse uma terceira versão, que não
escreve nenhuma dessas quatro coisas? A aula de hoje escreve essa terceira
versão, e a régua de comparação é a mesma planilha de linhas que a turma já
tem na mão.

### Ciclo 1, 19h30 às 20h05

- **Conceito.** Os problemas do JDBC, na lista do próprio capítulo [1], e a
  resposta que a JPA propõe.

  **Os cinco problemas do JDBC, segundo o capítulo.** Apesar de simples, o
  capítulo lista o JDBC como tendo os seguintes problemas: mau gerenciamento
  das conexões de banco de dados, já que elas devem ser abertas e fechadas
  manualmente, e se uma falhar, há mau uso de recursos; necessidade de
  escrever comandos SQL no meio do código Java, que precisam ser configurados
  e enviados manualmente, com o resultado também tratado manualmente; bastante
  código repetido nas interações com o banco; segurança, porque o envio manual
  de comandos pode dar brecha para interceptação ou para um invasor inserir
  seus próprios comandos SQL; e o descompasso entre Java, orientado a objetos,
  e os bancos relacionais, que dificulta o mapeamento de tabelas em classes, e
  tende a exigir uma classe de entidade e uma classe DAO para cada tabela, além
  de jogar manualmente cada linha lida num objeto. Ler essa lista de frente
  para `PedidoRepositoryJdbc`, escrito na aula passada, e marcar cada problema com um
  visto: os cinco estão lá.

  **Por que a JPA se chama API de persistência.** O capítulo explica a origem
  do nome: enquanto os objetos são enviados e recebidos do banco, a JPA os
  mantém ativos na memória do servidor de aplicações, enquanto as transações
  SQL são executadas, em vez de usar intensivamente o servidor de dados. Ela
  resolve os problemas do JDBC delegando ao servidor o gerenciamento das
  conexões, a instalação do driver e o controle da execução dos comandos SQL.

  **O Mapa O/R, com o exemplo do capítulo.** A JPA possui um mecanismo chamado
  Mapa O/R (Objetos/Relacionamentos), que joga o resultado das interações com
  o banco diretamente em objetos que representam as tabelas, respeitando o
  relacionamento entre elas. O capítulo ilustra com duas tabelas, Aluno e
  Disciplina, numa relação "um aluno cursa várias disciplinas": ao consultar
  os dados de um aluno chamado "Manuelo", já se sabe as disciplinas que ele
  cursa, sem uma nova consulta nem um `inner join` escrito à mão. É exatamente
  o problema cinco da lista de cima, resolvido.

- **Demonstração no projetor.** Abrir `PedidoRepositoryJdbc` e
  `PedidoRepositoryEmMemoria` lado a lado, e contar em voz alta, sobre o
  código da aula passada, quantas linhas resolvem cada um dos cinco problemas do
  JDBC: abertura e fechamento de `Connection`, escrita do `INSERT` e do
  `SELECT` como `String`, `try/catch` de `SQLException`, e o `while
  (resultado.next())` que monta cada `Pedido` campo a campo. Prometer à turma:
  a versão de hoje não vai ter nenhuma dessas quatro coisas escrita à mão.

- **Exercício curto.** Cinco minutos, individual. Para cada um dos cinco
  problemas do JDBC listados pelo capítulo, escrever se `PedidoRepositoryJdbc`
  da Aula 14 sofre dele (sim ou não) e por quê. Gabarito: sofre dos cinco,
  porque é exatamente o que o laboratório da aula passada pediu, JDBC puro, sem
  `JdbcTemplate` e sem ORM; a JPA de hoje ataca os cinco ao mesmo tempo,
  delegando ao provedor de persistência o que na semana passada era escrito à
  mão.

### Ciclo 2, 20h05 às 20h40

- **Conceito.** Entidades, o gerenciador de entidades e o vocabulário que a
  turma vai usar em `Pedido` daqui a pouco.

  **Entidades e suas três características, segundo o capítulo.** Uma entidade
  continua tendo a mesma definição usada em bancos de dados: um nome ou
  agrupamento de estados associados a uma única unidade. Para a JPA, uma
  classe de entidade precisa ter três características: **persistibilidade**,
  o estado do objeto pode ser armazenado sob a forma de dados e recuperado a
  qualquer momento; **identidade**, uma característica única que distingue um
  objeto dos demais, de modo equivalente à chave primária; e
  **transacionalidade**, a entidade permite `insert`, `update` e `delete`
  dentro de um contexto de transação, para serem confirmados ou desfeitos sem
  causar dano aos dados. O capítulo mostra essas três características ganhando
  vida através de anotações do pacote `javax.persistence` (hoje,
  `jakarta.persistence`, o pacote foi renomeado depois da doação do Java EE à
  Eclipse Foundation), como `@Entity` na classe e `@Column` em cada atributo.

  **O gerenciador de entidades, `EntityManager`.** É a interface que conecta o
  aplicativo à JPA, e quem efetivamente executa `insert`, `delete`, `update` e
  `select` na base. Um gerenciador de entidades administra um conjunto de
  entidades chamado contexto de persistência, dentro do qual cada classe de
  entidade é instanciada uma única vez. O provedor de persistência (no caso da
  Rota Sul, o Hibernate, que a Aula 18 aprofunda) implementa esse mecanismo, e
  mantém o contexto de persistência através de um `EntityManagerFactory`. O
  capítulo mostra a criação manual desses dois objetos:

  ```java
  EntityManagerFactory emf =
      Persistence.createEntityManagerFactory("ServicoDeUsuarios");
  EntityManager em = emf.createEntityManager();
  ```

  > **Nota para o professor.** Spring Data JPA, que a turma usa a partir de
  > hoje, cria e gerencia o `EntityManager` por baixo dos panos: nenhuma linha
  > de `Persistence.createEntityManagerFactory` entra no código da Rota Sul. O
  > capítulo ensina o mecanismo cru para a turma entender o que o Spring está
  > escondendo, não para reproduzir manualmente.

  **Persistir, buscar, atualizar e excluir, no vocabulário do capítulo.** Uma
  entidade é persistida com `em.persist(objeto)`; buscada pelo atributo
  anotado `@Id` com `em.find(Classe.class, id)`; atualizada lendo o objeto
  gerenciado, alterando seus campos com os métodos `set`, e confirmando com
  `em.merge(objeto)`; excluída buscando primeiro e depois chamando
  `em.remove(objeto)`. Consultas mais amplas usam JPQL, a linguagem de
  consulta da JPA, através de `TypedQuery`, como no exemplo do capítulo,
  `em.createQuery("SELECT u FROM Usuario u", Usuario.class)`.

- **Demonstração no projetor.** Ler a Listagem 1 do capítulo, a classe
  `Usuario` com `@Entity`, `@Table(name="Usuario")`, `@Id`,
  `@GeneratedValue(strategy = GenerationType.AUTO)` sobre o atributo `id`.
  Projetar ao lado a classe `Pedido` da Rota Sul, ainda sem anotação nenhuma,
  e perguntar à turma: o que falta para `Pedido` virar uma entidade JPA, na
  mesma lógica do exemplo? A resposta guia o passo 3 do Ciclo 3.

- **Exercício curto.** Cinco minutos, em duplas. Para cada verbo do CRUD que a
  Aula 06 já expõe em `PedidoController`, `POST`, `GET`, escrever qual método
  do `EntityManager` o capítulo usaria por baixo: `POST /pedidos` chama
  `em.persist`; `GET /pedidos/{id}` chama `em.find`. Gabarito: exatamente
  esses dois, e a dupla que também escrever `em.merge` para um futuro `PUT` e
  `em.remove` para um futuro `DELETE` já adiantou o Ciclo 4 de hoje.

### Quiz, 20h40 às 20h50

**Pergunta.** O capítulo lista o mau gerenciamento de conexões, a escrita
manual de SQL no meio do código Java, o código repetido e o risco de
segurança como problemas do JDBC. Entre as alternativas abaixo, qual descreve
uma característica da JPA, e não um problema do JDBC que ela resolve?

- A) Controle manual das conexões abertas com o banco de dados.
- B) Gerenciador de Entidades, que executa `insert`, `delete`, `update` e
  `select` sem o desenvolvedor escrever SQL a cada operação.
- C) Necessidade de escrever comandos SQL no meio do código Java.
- D) Mau gerenciamento das conexões de banco de dados.

**Correta:** B.

**Justificativa.** O Gerenciador de Entidades, implementado pela interface
`EntityManager`, é exatamente o mecanismo que a JPA introduz para resolver os
problemas do JDBC: ele conecta o aplicativo à JPA e executa as operações de
persistência sem exigir SQL manual a cada chamada, e é a peça que
`PedidoRepository`, hoje estendendo `JpaRepository` sem uma linha de
implementação, delega ao Spring Data para instanciar. As alternativas A, C e D
são, ao contrário, os próprios
problemas do JDBC listados pelo capítulo, o ponto de partida que a JPA existe
para resolver, não uma característica dela.

### Ciclo 3, 20h50 às 21h25

Laboratório de troca de implementação, terceira e última rodada. O contrato
`PedidoRepository` muda de forma pela primeira vez desde a Aula 06: hoje ele
deixa de ser uma interface escrita à mão para se tornar uma extensão de
`JpaRepository`.

1. **Acrescentar a dependência.** No `pom.xml`, `spring-boot-starter-data-jpa`,
   fixada no contrato técnico desde a Aula 01. Ela traz o Hibernate como
   provedor de JPA (o assunto da Aula 18) e o Spring Data JPA por cima dele.
   `mysql-connector-j` e `flyway-core`, já presentes desde a Aula 14,
   continuam.
2. **Anotar `Pedido` como entidade.** Em `pedido/domain`, acrescentar
   `@Entity`, `@Table(name = "pedido")` na classe, `@Id` e `@GeneratedValue(strategy
   = GenerationType.IDENTITY)` no atributo `id`, e `@Column(nullable = false)`
   em `cliente` e `situacao`. **Isso é a segunda exceção explícita à regra de
   "domínio sem anotação de framework"** fixada na Aula 06, a primeira foi
   `@JacksonXmlRootElement` em `Remessa`, na Aula 09. A diferença é que aquela
   era uma exceção pontual, e esta é estrutural: toda entidade JPA da Rota Sul
   vai carregar anotação de mapeamento a partir de hoje, porque é assim que o
   Spring Data localiza e mapeia a classe. Registrar essa decisão em
   `docs/decisoes.md`.
3. **Reescrever `PedidoRepository`.** Em `pedido/repository`, a interface
   deixa de declarar `salvar` e `listarTodos` e passa a ser:

   ```java
   public interface PedidoRepository extends JpaRepository<Pedido, Long> {
   }
   ```

   Zero linhas de corpo. `save`, `findById`, `findAll` e `deleteById` chegam
   de graça, herdados de `JpaRepository`, implementados pelo Spring Data em
   tempo de execução, sem uma classe `Impl` em lugar nenhum do código-fonte.
4. **Remover as duas implementações anteriores.** `git rm` em
   `PedidoRepositoryEmMemoria.java` e `PedidoRepositoryJdbc.java`. As duas
   já cumpriram seu papel pedagógico, e a contagem de linhas de ambas já está
   registrada em `docs/decisoes.md` desde o passo 10 da Aula 14; mantê-las no
   código faria a compilação falhar, porque nenhuma das duas implementa mais
   a nova assinatura de `PedidoRepository`.
5. **Ajustar as duas implementações de `PedidoService`.** Da Aula 07,
   `PedidoServiceComAnaliseDeRisco` e a implementação padrão trocam
   `pedidoRepository.salvar(pedido)` por `pedidoRepository.save(pedido)`, e
   `pedidoRepository.listarTodos()` por `pedidoRepository.findAll()`. Nenhuma
   regra de negócio muda, só o nome do método chamado, porque
   `PedidoService.registrar` continua sendo o único ponto de entrada que os
   controladores conhecem.
6. **Configurar a coexistência com o Flyway.** Em `application.properties`,
   `spring.jpa.hibernate.ddl-auto=validate`. Essa propriedade impede o
   Hibernate de gerar ou alterar tabelas sozinho: ele só confere se o
   mapeamento de `Pedido` bate com o schema que o Flyway já criou na Aula 14.
   O Flyway continua sendo a única fonte de verdade do schema, e a migration
   `V1__cria_tabela_pedido.sql` não muda uma linha, porque as colunas que ela
   já criou, `id`, `cliente`, `descricao`, `situacao`, `regiao`, já batem com
   o mapeamento de hoje. A migration escrita na Aula 14 ganha hoje um segundo
   papel: além de criar o schema, ela passa a ser o contrato contra o qual o
   Hibernate valida o mapeamento da entidade na subida.

### Ciclo 4, 21h25 às 21h50

7. **Completar o CRUD em `PedidoController`.** `POST /pedidos` e `GET
   /pedidos` já existem desde a Aula 06. Acrescentar `GET /pedidos/{id}`
   (`pedidoRepository.findById(id)`, devolvendo 404 se vazio), `PUT
   /pedidos/{id}` (buscar por `findById`, aplicar as mudanças recebidas no
   corpo, chamar `save` de novo, o mesmo método cobre `insert` e `update`) e
   `DELETE /pedidos/{id}` (`pedidoRepository.deleteById(id)`). Os cinco verbos
   do CRUD completo, todos delegando ao repositório sem SQL escrito à mão.
8. **Subir e testar manualmente.** `./mvnw spring-boot:run`, e usar `curl` ou
   o navegador para exercitar os cinco verbos na porta que o terminal
   imprimiu, conferindo que um `Pedido` criado aparece no `GET`, sobrevive a
   um `PUT` e desaparece depois do `DELETE`.
9. **Testar com Testcontainers.** `PedidoRepositoryTest`, em
   `src/test/java/br/uni9/rotasul/pedido/repository/`, anotado
   `@DataJpaTest`, `@AutoConfigureTestDatabase(replace = Replace.NONE)` e
   `@Testcontainers`, subindo um `@Container static MySQLContainer<?>` e
   apontando o `DataSource` para ele com `@DynamicPropertySource`, exatamente
   como a Aula 14 fez. Um caso: salvar um `Pedido` com
   `pedidoRepository.save(...)` e conferir que `findAll()` devolve uma lista de
   tamanho um, sem uma linha de SQL escrita no teste. Rodar `./mvnw test`.

   ```java
   @DataJpaTest
   @AutoConfigureTestDatabase(replace = AutoConfigureTestDatabase.Replace.NONE)
   @Testcontainers
   class PedidoRepositoryTest { }
   ```

   **A segunda anotação não é decoração.** Por padrão, `@DataJpaTest`
   substitui o `DataSource` da aplicação por um banco embarcado em memória,
   justamente para o teste rodar sem infraestrutura. Se ela ficar de fora, o
   `MySQLContainer` sobe, gasta os segundos de inicialização e é ignorado: o
   teste passa contra o banco embarcado, e o aluno acredita ter validado o
   mapeamento contra o MySQL quando validou contra outra coisa.
   `replace = Replace.NONE` manda o Spring manter o `DataSource` que o
   `@DynamicPropertySource` apontou para o container. Vale dizer isso em voz
   alta: é um erro que não dá mensagem nenhuma, o teste fica verde do mesmo
   jeito.
10. **Fechar a contagem de linhas, o entregável central de hoje.** Em
    `docs/decisoes.md`, uma terceira linha ao lado das duas que a Aula 14 já
    registrou: `PedidoRepository` (JPA): uma linha de assinatura, zero linhas
    de corpo. A tabela completa fica, por exemplo, `PedidoRepositoryEmMemoria`:
    24 linhas; `PedidoRepositoryJdbc`: 58 linhas; `PedidoRepository` sobre
    Spring Data JPA: 0 linhas de implementação. Escrever a frase que fecha o
    arco: o preço do JDBC (verbosidade) e o preço do mapa objeto-relacional
    (mágica que esconde o SQL) são dois lados da mesma balança que o capítulo
    [1] descreve, e hoje a turma sentiu os dois extremos na própria mão.
11. **Registrar a decisão da segunda exceção de anotação no domínio.** Uma
    linha adicional em `docs/decisoes.md`, nomeando `@Entity` em `Pedido`
    como a segunda exceção à regra "domínio sem anotação de framework", ao
    lado de `@JacksonXmlRootElement` em `Remessa`.

**Entregável do dia:** `Pedido` anotado como entidade JPA, `PedidoRepository`
estendendo `JpaRepository<Pedido, Long>` sem corpo, os cinco verbos do CRUD em
`PedidoController`, `PedidoRepositoryTest` com Testcontainers passando, e a
contagem de linhas das três implementações fechada em `docs/decisoes.md`.
Critério de aceitação: `./mvnw test` verde, os cinco verbos do CRUD
respondendo pela porta que o terminal imprimiu, e a migration
`V1__cria_tabela_pedido.sql` inalterada desde a Aula 14, validada pelo
Hibernate na subida.

### Fechamento, 21h50 às 22h00

- `git add src docs pom.xml`
- `git commit -m "feat(pedido): migra PedidoRepository para Spring Data JPA e completa o CRUD"`
- `git push`
- Reler em voz alta a tabela de três linhas de `docs/decisoes.md`: memória,
  JDBC, JPA. É a mesma lição da Aula 06 sobre interface e implementação, vista
  três vezes, com o mesmo contrato `PedidoRepository` (hoje reescrito, mas com
  o mesmo papel) sobrevivendo às três trocas sem que `PedidoService` mudasse
  de comportamento.
- **Prévia da Aula 16.** O provedor por trás do que o Spring Data acabou de
  esconder tem nome, Hibernate, e a Aula 18 abre essa caixa. Antes disso, a
  Aula 16 muda de assunto por um encontro: transações. Hoje `save` e
  `deleteById` já rodam dentro de uma transação implícita que o Spring abre e
  fecha sozinho; na próxima aula a turma aprende a controlar isso explicitamente com
  `@Transactional`, no momento em que uma operação da Rota Sul precisa fazer
  duas escritas como uma coisa só, ou nenhuma das duas.

### Referências

1. MESQUITA, Paulo Ricardo Batista. **Capítulo 14: API de Persistência
   Java.** Arquitetura de Software. AVA, Uninove. Fonte primária desta aula,
   `pdf/014.pdf`.
2. SCHINCARIOL, M.; KEITH, M. **Pro JPA 2: Mastering the Java Persistence
   API.** Apress, 2009. Referência indicada pelo capítulo.
3. Spring. **Documentação do Spring Data JPA.**
   <https://docs.spring.io/spring-data/jpa/reference/>
4. Hibernate. **Hibernate ORM Documentation.**
   <https://hibernate.org/orm/documentation/>
5. Flyway. **Documentação**, seção de migrations.
   <https://documentation.red-gate.com/fd/migrations-184127470.html>
6. Testcontainers. **Documentação do módulo MySQL.**
   <https://java.testcontainers.org/modules/databases/mysql/>
7. JUnit. **JUnit 5 User Guide.** <https://junit.org/junit5/docs/current/user-guide/>

---

## Aula 16, Enterprise Java Beans

**Módulo:** M4, Persistência e componentes
**Capítulo do AVA:** `pdf/015.pdf`, Enterprise Java Beans
**Entregável:** baixa de remessa transacional. Um método `RemessaService.baixarRemessa(Long
id)`, anotado `@Transactional`, que atualiza a situação da `Remessa` e cria uma
`Ocorrencia` de entrega como uma única unidade atômica, mais
`RemessaServiceTest`, que comprova o rollback: quando a criação da ocorrência
falha, a situação da remessa não muda no banco. Critério de aceitação:
`./mvnw test` verde com os dois casos, sucesso e rollback, e a explicação de
propagação e de qual tipo de exceção dispara o rollback registrada em
`docs/decisoes.md`.

> **Nota para o professor.** EJB e JSF (na Aula 18) entram como conteúdo
> conceitual e histórico, comparado lado a lado com o equivalente Spring. O
> laboratório de hoje constrói apenas o equivalente Spring; nenhuma linha de
> `@Stateless`, `@Remote` ou `@Local` é escrita pela turma. A leitura do
> capítulo continua sendo necessária, porque é o texto que o aluno acessa no
> AVA, e o roteiro de hoje explica com honestidade por que a indústria migrou
> de um modelo para o outro, sem depreciar o que o capítulo ensina.

### Retomada, 5 minutos

Na Aula 15 cada aluno entregou o CRUD completo de `Pedido` sobre
`PedidoRepository extends JpaRepository<Pedido, Long>`, sem uma linha de
implementação escrita à mão. Abrir `docs/decisoes.md` na linha da contagem
final: `PedidoRepositoryEmMemoria`, `PedidoRepositoryJdbc` e o `JpaRepository`
da aula passada. A régua de hoje é diferente: não é mais sobre quantas linhas o
repositório custa, é sobre o que garante que duas operações de escrita
aconteçam juntas, ou nenhuma delas aconteça.

### Ciclo 1, 19h30 às 20h05

- **Conceito.** Componentes de aplicação corporativa e o modelo dos EJBs, na
  descrição do capítulo [1].

  **Componente e o modelo EJB.** O capítulo repete a definição já conhecida
  desde a Aula 06 e a Aula 07, unidade de software reutilizável, auto
  contida, integrável a uma aplicação, com contratos bem definidos para quem a
  usa. Em Java, a forma mais simples de implementar um componente é através de
  um JavaBean, cujo contrato é dado pelo padrão de nomenclatura dos métodos.
  Nas aplicações corporativas, o foco dos componentes é resolver problemas de
  regra de negócio, e o modelo padrão do Java EE para isso é o EJB, que define
  métodos para empacotar, instalar e interagir com serviços de regra de
  negócio auto contidos. O tipo de EJB determina o contrato que os clientes
  usam para interagir com ele. O capítulo é explícito: usar ou não um modelo
  de componentes depende do desenvolvedor, porque a maioria dos serviços de um
  servidor Java EE também pode ser acessada diretamente por Servlets.

  **As cinco vantagens do EJB, segundo o capítulo.** Baixo acoplamento, a
  implementação de um componente muda sem impacto em quem depende dele;
  gerenciamento de dependência, declarada em metadados e resolvida
  automaticamente pelo container; gerenciamento do ciclo de vida, o servidor
  decide criar, manter e remover instâncias, e o componente participa dessas
  operações para obter e liberar recursos; **serviços declarativos de
  conteiner**, métodos de negócio incorporados pelo servidor para aplicar
  concorrência, **gerenciamento de transações**, segurança e ações remotas; e
  portabilidade, escalabilidade e eficiência entre servidores padronizados. A
  terceira vantagem grifada acima é o gancho do dia: gerenciamento de
  transações como serviço declarativo do container, aplicado sem o
  desenvolvedor escrever o controle manualmente.

  **Beans de sessão sem estado, lidos, não escritos.** O capítulo mostra a
  interface de negócios `InterfaceHello`, anotada `@Local`, e a classe que a
  implementa, `BeanHello`, anotada `@Stateless`. O `@Local` indica que a
  interface é acessível por clientes no mesmo servidor; a existência de uma
  interface remota, anotada `@Remote`, do pacote `java.rmi.Remote`, atende
  clientes fora do servidor, seguindo o modelo RMI já apresentado na Aula 10.
  Um bean de sessão sem estado assume que nenhum de seus métodos foi chamado
  antes, o que permite atender muitos clientes com o mínimo de impacto sobre
  os recursos do servidor.

- **Demonstração no projetor.** Ler em voz alta, sem digitar, `InterfaceHello`
  e `BeanHello` do capítulo. Ao lado, projetar o esqueleto de
  `RemessaService` que a turma vai escrever hoje, um `@Service` do Spring,
  sem interface de negócios separada nem anotação `@Stateless`. Nomear a
  primeira diferença honesta: o EJB precisa de um servidor Java EE completo
  rodando por baixo para interpretar `@Stateless`; o `@Service` do Spring roda
  dentro do próprio processo do `java -jar`, no Tomcat embarcado que a
  Aula 08 já mostrou.

  > **Nota para o professor.** Por que a indústria migrou. O modelo de EJB
  > amarra a aplicação a um servidor de aplicações Java EE pesado (WebLogic,
  > JBoss, GlassFish), com ciclos de deploy mais lentos e um modelo de objetos
  > distribuídos (interfaces remotas via RMI) desenhado para um problema que a
  > maioria das aplicações não tem, transações distribuídas entre várias
  > instâncias de servidor. O Spring manteve as mesmas ideias, dependência
  > gerenciada, ciclo de vida gerenciado, transação declarativa, mas entregou
  > isso como biblioteca, dentro de qualquer processo Java, sem exigir um
  > servidor de aplicações dedicado. Isso não invalida o que o capítulo
  > ensina: os conceitos são os mesmos, e um desenvolvedor que entende EJB
  > entende `@Service` e `@Transactional` rapidamente, porque o vocabulário
  > (gerenciamento de ciclo de vida, injeção de dependência, serviço
  > declarativo) é o mesmo vocabulário, com um motor diferente por baixo.

- **Exercício curto.** Cinco minutos, em duplas. Classificar três operações da
  Rota Sul como candidatas a bean de sessão **sem estado** ou **com estado**,
  segundo a distinção do capítulo (sem estado: cada método assume que nenhum
  outro foi chamado antes; com estado: uma instância é mantida enquanto o
  cliente usa vários métodos em sequência, como o carrinho de compras do
  exemplo do capítulo): (a) calcular o frete de um pedido, como a Aula 11 já
  faz; (b) montar um pedido em várias etapas de formulário, mantendo os dados
  parciais entre uma tela e outra; (c) dar baixa numa remessa. Gabarito: (a) e
  (c) são sem estado, cada chamada é independente e autocontida; (b) é com
  estado, porque depende de dados acumulados entre chamadas, o mesmo padrão
  do carrinho de compras do capítulo.

### Ciclo 2, 20h05 às 20h40

- **Conceito.** Transações declarativas, do jeito do EJB ao jeito do Spring.

  **O que o capítulo não mostra, e por que hoje precisa disso.** O capítulo
  lista "gerenciamento de transações" entre os serviços declarativos de
  conteiner, mas não demonstra o código de uma anotação de transação do EJB
  (`@TransactionAttribute`, fora do capítulo). O que ele mostra, ao descrever
  o serviço, é o suficiente para o gancho de hoje: o container aplica a
  transação em volta do método de negócio, sem o desenvolvedor escrever
  `begin`, `commit` e `rollback` à mão, o mesmo mecanismo que a Aula 15
  mostrou existir de forma implícita em cada `save` do Spring Data.

  **`@Transactional`, o equivalente Spring do serviço declarativo de
  transação.** Uma anotação em cima de um método de um `@Service` faz o
  Spring embrulhar a chamada num proxy: antes do método, abre uma transação;
  se o método terminar normalmente, confirma (`commit`); se o método lançar
  uma exceção **não verificada** (uma `RuntimeException` ou subclasse), o
  proxy desfaz tudo o que o método fez no banco (`rollback`), como se nada
  tivesse acontecido. Exceções verificadas (subclasses de `Exception` que não
  são `RuntimeException`) **não** disparam rollback por padrão, uma armadilha
  comum: se o método de hoje lançasse uma exceção verificada, a remessa
  ficaria com o estado mudado e a ocorrência não criada, meio caminho andado,
  exatamente o problema que a transação existe para evitar.

  **Duas escritas, uma unidade.** A baixa de uma remessa muda dois registros:
  a situação da própria `Remessa` e a criação de uma nova `Ocorrencia` de
  entrega, usando o `OcorrenciaCreator` da Aula 11. Sem transação, um erro no
  meio do caminho deixaria a remessa marcada como entregue sem nenhuma
  ocorrência registrada, ou uma ocorrência órfã sem a remessa correspondente.
  Com `@Transactional`, as duas escritas são uma coisa só.

- **Demonstração no projetor.** Escrever ao vivo o esqueleto:

  ```java
  @Service
  public class RemessaService {

      private final RemessaRepository remessaRepository;
      private final OcorrenciaRepository ocorrenciaRepository;

      @Transactional
      public Remessa baixarRemessa(Long id) {
          Remessa remessa = remessaRepository.findById(id)
              .orElseThrow(() -> new IllegalArgumentException("remessa nao encontrada"));
          remessa.setSituacao("ENTREGUE");
          remessaRepository.save(remessa);

          Ocorrencia ocorrencia = new OcorrenciaDeEntregaCreator().criarOcorrencia(remessa);
          ocorrenciaRepository.save(ocorrencia);

          return remessa;
      }
  }
  ```

  Apontar: as duas chamadas de `save` estão dentro do mesmo método anotado,
  então participam da mesma transação, aberta e fechada pelo proxy do Spring,
  sem um `begin` ou `commit` visível no código, a mesma promessa que o
  capítulo faz para o EJB, cumprida aqui por um mecanismo diferente.

- **Exercício curto.** Cinco minutos, individual. Se `ocorrenciaRepository.save(ocorrencia)`
  lançar uma `RuntimeException` no meio do método acima, o que acontece com a
  mudança de situação da `Remessa`, já enviada ao `EntityManager` pela linha
  anterior? Gabarito: ela é desfeita também, porque as duas chamadas
  pertencem à mesma transação, e o rollback desfaz tudo que a transação fez,
  não só a última linha executada.

### Quiz, 20h40 às 20h50

**Pergunta.** O EJB possui características que o tornam popular entre os
desenvolvedores. Entre as alternativas abaixo, uma delas **não** é uma
característica de EJB, segundo o capítulo:

- A) Baixo acoplamento.
- B) Executado do lado do cliente.
- C) Portabilidade entre servidores.
- D) Gerenciado pelo servidor Java EE.

**Correta:** B.

**Justificativa.** O capítulo é explícito: os beans de sessão são gerenciados
pelo servidor, que decide criar, manter em execução e remover as instâncias,
e a interação começa quando um cliente pede a execução de um método e
termina quando o método finaliza. Um EJB é sempre executado do **lado do
servidor**, nunca do lado do cliente, o mesmo motivo pelo qual
`RemessaService`, hoje, roda dentro do processo do servidor Spring Boot da
Rota Sul e nunca no navegador de quem opera o painel. As alternativas A, C e
D são, ao contrário, vantagens do EJB citadas literalmente pelo capítulo:
baixo acoplamento, portabilidade entre servidores padronizados, e
gerenciamento do ciclo de vida pelo servidor Java EE.

### Ciclo 3, 20h50 às 21h25

Laboratório de transação. `Remessa`, existente desde a Aula 09, e `Ocorrencia`,
existente desde a Aula 11 apenas como objeto do Factory Method, ganham hoje
seu primeiro mapeamento JPA, migrando direto para `JpaRepository`, sem passar
pela etapa JDBC que `Pedido` cumpriu nas Aulas 14 e 15: o aprendizado já
aconteceu uma vez, e não precisa se repetir.

1. **Migration para as duas tabelas novas.** Em
   `src/main/resources/db/migration/V2__cria_tabelas_remessa_e_ocorrencia.sql`,
   criar `remessa` (`id` autoincremento, `pedido_id`, `situacao`) e
   `ocorrencia` (`id` autoincremento, `tipo`, `descricao`, `registrada_em`),
   sem nenhuma coluna de relacionamento entre as duas ainda, isso é assunto da
   Aula 18.
2. **Anotar `Remessa` e `Ocorrencia` como entidades.** `@Entity`, `@Table`,
   `@Id`, `@GeneratedValue(strategy = GenerationType.IDENTITY)`, seguindo
   exatamente o padrão que `Pedido` fixou na aula passada.
3. **Escrever `RemessaRepository` e `OcorrenciaRepository`.** Duas
   interfaces, `extends JpaRepository<Remessa, Long>` e `extends
   JpaRepository<Ocorrencia, Long>`, ambas sem corpo, herdando `save` e
   `findById` de graça, a mesma economia de linhas que a Aula 15 mediu para
   `Pedido`.
4. **Escrever `RemessaService.baixarRemessa`.** Exatamente o esqueleto
   demonstrado no Ciclo 2, usando `OcorrenciaCreator` da Aula 11 para
   construir a `Ocorrencia` de entrega, e `@Transactional` no método.
5. **Escrever o caso de sucesso.** `RemessaServiceTest`, com
   `@SpringBootTest` e `@Testcontainers`, subindo um `MySQLContainer<?>`.
   Salvar uma `Remessa` de teste, chamar `remessaService.baixarRemessa(id)`, e
   conferir que a situação mudou para `"ENTREGUE"` e que existe uma
   `Ocorrencia` nova associada à baixa.
6. **Escrever o caso de rollback, o entregável central de hoje.** No mesmo
   arquivo de teste, usar `@MockBean` para substituir `OcorrenciaRepository`
   por um dublê configurado para lançar `RuntimeException` ao chamar `save`.
   Chamar `remessaService.baixarRemessa(id)` dentro de um
   `assertThrows(RuntimeException.class, () -> ...)`, e depois buscar a
   `Remessa` de novo, **por fora** da transação que falhou, usando o
   `remessaRepository` real (não mockado). Conferir que a situação continua a
   original, não `"ENTREGUE"`: a prova de que o rollback desfez a primeira
   escrita mesmo ela tendo acontecido antes da falha.

### Ciclo 4, 21h25 às 21h50

7. **Rodar os dois casos.** `./mvnw test`, conferindo que tanto o caso de
   sucesso quanto o caso de rollback passam.
8. **Provar visualmente, com o banco aberto.** Opcional, mas recomendado:
   com um cliente MySQL (`docker exec -it rotasul-mysql mysql -u root -p`),
   consultar a tabela `remessa` antes e depois de rodar o teste de rollback, e
   ver que nenhuma linha ficou com situação inconsistente.
9. **Registrar a explicação de propagação e de exceção.** Em
   `docs/decisoes.md`, uma linha explicando que `@Transactional`, sem
   parâmetro de propagação, usa `REQUIRED` (participa de uma transação
   existente, ou cria uma nova se não houver), e que o rollback automático só
   acontece para exceções não verificadas, `RuntimeException` e suas
   subclasses, nunca para exceções verificadas, a menos que
   `@Transactional(rollbackFor = ...)` diga o contrário.
10. **Registrar o comparativo com EJB.** Uma segunda linha em
    `docs/decisoes.md`, nomeando `@Transactional` como o equivalente direto do
    "gerenciamento de transações" que o capítulo lista entre os serviços
    declarativos de conteiner do EJB, e citando a diferença operacional: o
    EJB precisa de um servidor Java EE completo, o Spring roda no mesmo
    processo do `java -jar`.

**Entregável do dia:** `RemessaService.baixarRemessa`, anotado
`@Transactional`, `Remessa` e `Ocorrencia` mapeadas como entidades JPA,
`RemessaRepository` e `OcorrenciaRepository` sem corpo, e
`RemessaServiceTest` com os dois casos, sucesso e rollback. Critério de
aceitação: `./mvnw test` verde, o caso de rollback provando que a `Remessa`
não mudou de situação quando a criação da `Ocorrencia` falhou, e as duas
linhas de `docs/decisoes.md` presentes.

### Fechamento, 21h50 às 22h00

- `git add src docs`
- `git commit -m "feat(expedicao): adiciona baixa de remessa transacional com @Transactional"`
- `git push`
- Reler em voz alta a nota do professor do Ciclo 1: o vocabulário do EJB,
  gerenciamento de ciclo de vida, injeção de dependência, serviço
  declarativo, é o mesmo vocabulário de `@Service` e `@Transactional`, com um
  motor diferente. Quem entende um, entende o outro rápido.
- **Prévia da Aula 17.** A Rota Sul agora tem três camadas completas em três
  contextos, `pedido`, `expedicao` e `rastreamento`, cada uma com sua própria
  suíte de teste isolada. A próxima aula não escreve regra de negócio nova:
  ela consolida as três camadas com um teste de integração único, que sobe
  tudo de uma vez, o `MySQLContainer`, os `@Service`, os `@Controller`, e
  bate numa URL real de ponta a ponta.

### Referências

1. MESQUITA, Paulo Ricardo Batista. **Capítulo 15: Enterprise Java Beans.**
   Arquitetura de Software. AVA, Uninove. Fonte primária desta aula,
   `pdf/015.pdf`.
2. SRIGANESH, R. P.; BROSE, G.; SILVERMAN, M. **Mastering EJB.** 4. ed.
   Wiley Publishing, 2006. Referência indicada pelo capítulo.
3. Spring. **Documentação do Spring Framework**, seção de gerenciamento
   declarativo de transações.
   <https://docs.spring.io/spring-framework/reference/data-access/transaction/declarative.html>
4. Testcontainers. **Documentação do módulo MySQL.**
   <https://java.testcontainers.org/modules/databases/mysql/>
5. JUnit. **JUnit 5 User Guide.** <https://junit.org/junit5/docs/current/user-guide/>

---

## Aula 17, Frameworks para software em 3 camadas

**Módulo:** M4, Persistência e componentes
**Capítulo do AVA:** `pdf/016.pdf`, Frameworks usados para implementar
software em 3 camadas
**Entregável:** uma suíte de integração de ponta a ponta,
`PedidoIntegrationTest`, subindo a aplicação inteira num `MySQLContainer` e
exercitando `POST /pedidos` seguido de `GET /pedidos/{id}` por HTTP real, mais
um checklist de consolidação das três camadas em `docs/decisoes.md`. Critério
de aceitação: `./mvnw test` verde com a nova suíte, o `MySQLContainer` sobe e
morre sozinho a cada execução, e o checklist confirmando que `pedido`,
`expedicao` e `rastreamento` têm as quatro camadas (`web`, `service`,
`repository`, `domain`) completas.

### Retomada, 5 minutos

Na Aula 16 cada aluno entregou `RemessaService.baixarRemessa`, transacional,
com `RemessaServiceTest` provando o rollback quando a criação da `Ocorrencia`
falha. Contar: até aqui, cada teste da Rota Sul olha uma fatia isolada, um
repositório aqui, um serviço ali, um controlador em outro arquivo. Nenhum
teste, até hoje, sobe a aplicação inteira e bate numa URL real de ponta a
ponta. É exatamente essa lacuna que a aula de hoje fecha.

### Ciclo 1, 19h30 às 20h05

- **Conceito.** Frameworks, frozen spots e hot spots, na descrição do
  capítulo [1].

  **Por que frameworks existem, segundo o capítulo.** Frameworks agilizam o
  desenvolvimento porque já resolvem requisitos não funcionais, o que o
  software precisa **para ser executado**, não o que ele precisa **fazer**,
  direcionando o desenvolvedor para as regras de negócio. Um framework sempre
  atende um domínio específico de problemas, e o capítulo lista dez exemplos:
  modelagem de aplicações do mercado financeiro, modelagem de processos
  corporativos, sistemas de suporte a decisão, sistemas de informação
  geográfica, autoração e reprodução multimídia, sincronização entre cliente e
  servidor, sincronização entre sistemas remotos, middleware em geral,
  desenvolvimento rápido de interfaces gráficas, e gerenciamento de bases de
  dados. O Spring, usado pela Rota Sul desde a Aula 06, cobre pelo menos três
  desses dez ao mesmo tempo: sincronização cliente-servidor (REST, desde a
  Aula 09), middleware (o cliente SOAP da Aula 10) e gerenciamento de bases de
  dados (JPA, desde a Aula 15).

  **Frozen spots e hot spots, o vocabulário do capítulo.** Um framework tem
  componentes que raramente precisam ser modificados, estruturados de acordo
  com um modelo de arquitetura, chamados **frozen spots**; e componentes que
  permitem a conexão com o software do desenvolvedor, usados para implementar
  as regras de negócio, chamados **hot spots**, conectados via classes
  abstratas, interfaces, agregação e composição. Traduzindo para a Rota Sul:
  o `DispatcherServlet` do Spring, o proxy de `@Transactional` da Aula 16, o
  mecanismo de injeção de dependência da Aula 12, são frozen spots, a turma
  nunca escreveu uma linha deles. `PedidoController`, `RemessaService`,
  `PedidoRepository`, são hot spots, o código que a turma escreve toda
  semana, plugado nos pontos de extensão que o framework oferece.

  **Vantagens e desvantagens, preservadas as duas.** O capítulo lista
  vantagens (menos erro por reaproveitamento errado de código antigo, menos
  tempo em rotinas de verificação de relacionamento e tratamento de erro,
  menos tempo integrando componentes distribuídos em várias camadas, redução
  de recursos humanos, técnicos e financeiros) e uma desvantagem central: o
  tempo para aprender o framework pode, num primeiro momento, ser maior do
  que construir do zero, e o framework cria automaticamente componentes que
  assume necessários, mas que às vezes são desnecessários, gerando sobrecarga
  de código que o desenvolvedor nem sempre verifica.

- **Demonstração no projetor.** Abrir o projeto da Rota Sul no editor e
  apontar, um a um, cinco arquivos ou mecanismos, pedindo à turma para
  classificar cada um como frozen ou hot spot antes de revelar a resposta:
  `application.properties` (frozen, configura o frozen spot), `PedidoController`
  (hot), o Tomcat embarcado (frozen), `CalculoDeFreteService` (hot), o
  Flyway rodando sozinho na subida (frozen).

- **Exercício curto.** Cinco minutos, em duplas. Listar dois hot spots e dois
  frozen spots do próprio código que a dupla já escreveu, com uma frase
  justificando cada classificação segundo a definição do capítulo. Sem
  gabarito único, correção é feita circulando pela sala.

### Ciclo 2, 20h05 às 20h40

- **Conceito.** O panorama de frameworks do capítulo, com Spring no centro.

  **Os quatro frameworks do capítulo, e onde a Rota Sul se encaixa.** O
  capítulo compara quatro: **Spring**, framework de aplicação open source
  para Java EE, com núcleo central (Core Container) que usa reflexão de
  objetos para gerenciar o ciclo de vida dos "objetos gerenciados",
  configurável por XML ou, desde a versão 3.0, por anotação (o caminho que a
  Aula 12 já usou), com módulos para banco (JDBC ou JPA), transações remotas,
  regras de negócio, comunicação remota e interface de usuário; **ASP.NET**,
  da Microsoft, sobre o Framework .Net, dependente de runtime Windows e
  servidor IIS, com dois padrões de arquitetura, Web Forms e MVC, que podem
  conviver; **Ruby on Rails**, em Ruby, MVC no servidor, com uso "abusivo" de
  serviços web RESTful sempre acionados por Ajax, páginas como templates
  `.erb` convertidos em HTML em tempo de execução, alta modularização às
  custas de desempenho, porque as respostas são sempre montadas na hora; e
  **Laravel**, em PHP, MVC, com um componente a mais que os outros três, um
  roteador que identifica o controle certo para cada requisição.

  > **Nota para o professor.** O capítulo também registra uma crítica ao
  > Spring, preservada aqui porque é do próprio texto: os modelos de
  > programação do Spring não são totalmente compatíveis com os padrões de
  > Java EE, o que pode gerar dificuldade de uso, e a reflexão de objetos
  > combinada ao uso extensivo de XML pode sobrecarregar os recursos de
  > processamento. O capítulo pondera que, mesmo assim, a relação
  > custo-benefício explica a popularidade do framework, e isso é o que a
  > Rota Sul vem confirmando desde a Aula 06.

  **Todos os quatro seguem o MVC.** É o ponto de convergência do capítulo:
  apesar das diferenças de linguagem e de infraestrutura, os quatro
  frameworks orientam o desenvolvedor a organizar o código segundo o padrão
  MVC, o mesmo padrão que a Aula 06 apresentou e que estrutura a Rota Sul
  inteira, `web`, `service` mais `domain`, e `repository`.

- **Demonstração no projetor.** Montar uma tabela na lousa ou no editor,
  cruzando os módulos do Spring citados pelo capítulo com o código real da
  Rota Sul: módulo de banco (JDBC ou JPA) = `PedidoRepository` desde a
  Aula 15; módulo de regras de negócio = `PedidoService` e `RemessaService`;
  módulo de comunicação remota = o cliente SOAP da Aula 10 e o `RestTemplate`
  implícito no `GET /remessas/{id}`; módulo de interface de usuário = as
  telas Thymeleaf da Aula 13. Todo módulo que o capítulo cita para o Spring
  já está presente e nomeado no código da turma.

- **Exercício curto.** Cinco minutos, individual. Para cada um dos quatro
  frameworks do capítulo, escrever uma palavra que resume seu diferencial
  central: Spring (módulos), ASP.NET (dois padrões coexistentes), Ruby on
  Rails (convenção e RESTful), Laravel (roteador). Correção coletiva, sem
  gabarito fechado.

### Quiz, 20h40 às 20h50

**Pergunta.** O capítulo descreve um framework de aplicação que encoraja seus
usuários a explorarem o uso "abusivo" de serviços web do tipo RESTful,
sempre acionados por Ajax, para atender e processar as requisições dos
usuários. Qual framework, entre os quatro apresentados, é esse?

- A) Spring.
- B) ASP.NET.
- C) Ruby on Rails.
- D) Laravel.

**Correta:** C.

**Justificativa.** É a descrição literal do capítulo para o Ruby on Rails: as
conexões entre os componentes são feitas por arquivos de configuração,
arquivos de indexação e um uso "abusivo" de serviços web do tipo RESTful,
sempre acionados por Ajax. É o mesmo vocabulário, REST e comunicação remota,
que a Rota Sul já pratica desde a Aula 09, só que aqui aplicado ao
funcionamento interno do próprio framework. A alternativa A descreve o
Spring, cujo diferencial no capítulo é a organização em módulos configuráveis
por XML ou anotação, não o uso de web services internos. A B descreve o
ASP.NET, cujo diferencial é ter dois padrões de arquitetura coexistentes,
Web Forms e MVC. A D descreve o Laravel, cujo diferencial é o componente
roteador, não o uso de web services RESTful.

### Ciclo 3, 20h50 às 21h25

Laboratório de consolidação. Nenhuma regra de negócio nova entra hoje. O
trabalho é auditar as três camadas já construídas e cobri-las com um teste
que sobe a aplicação inteira, HTTP incluído, contra um banco real e
descartável.

1. **Checklist de consolidação, primeiro passo.** Em `docs/decisoes.md`,
   abrir uma tabela nova conferindo, para cada contexto (`pedido`,
   `expedicao`, `rastreamento`), se as quatro camadas existem:
   `web` (um `@Controller` ou `@RestController`), `service` (um `@Service`),
   `repository` (uma interface `JpaRepository`) e `domain` (a entidade). Marcar
   cada célula como presente ou ausente, e completar o que estiver faltando
   antes de seguir (por exemplo, se `rastreamento` ainda não tiver um
   `@RestController` para `Ocorrencia`, este é o momento de escrever um
   mínimo, `GET /ocorrencias/{id}`, sem inventar regra de negócio nova).
2. **Escolher a estratégia de container compartilhado.** Subir um novo
   `MySQLContainer` a cada classe de teste, como as Aulas 14, 15 e 16 fizeram
   isoladamente, é lento quando a suíte cresce. Criar uma classe base,
   `IntegrationTestBase`, com um `@Container static MySQLContainer<?> mysql`
   e um `@DynamicPropertySource` compartilhado, que as classes de integração
   estendem, subindo o container **uma única vez** para toda a suíte.
3. **Escrever `PedidoIntegrationTest`.** Estendendo `IntegrationTestBase`,
   anotado `@SpringBootTest(webEnvironment = SpringBootTest.WebEnvironment.RANDOM_PORT)`,
   injetando um `TestRestTemplate`. Diferente de `@WebMvcTest` (Aula 13, só a
   camada web, com dependências mockadas) e de `@DataJpaTest` (Aula 15, só o
   repositório), `@SpringBootTest` sobe o contexto Spring completo: todas as
   três camadas, reais, ligadas ao `MySQLContainer` real.
4. **Escrever o caso de ponta a ponta.** Um `POST` em
   `http://localhost:" + port + "/pedidos"` com um `Pedido` no corpo, via
   `testRestTemplate.postForEntity(...)`, conferindo status `201`. Em seguida,
   um `GET` no `Location` devolvido, ou em `/pedidos/{id}` usando o `id` do
   corpo de resposta, conferindo que os dados batem com o que foi enviado.
   Diferente dos testes anteriores, esta chamada atravessa `PedidoController`,
   `PedidoService` e `PedidoRepository` numa única execução, exatamente como
   um cliente real faria.

### Ciclo 4, 21h25 às 21h50

5. **Rodar a suíte inteira.** `./mvnw test`, conferindo que o
   `MySQLContainer` sobe uma vez só (visível no log, um único bloco de
   inicialização do Testcontainers) e que todas as suítes anteriores, Aulas
   14, 15 e 16, continuam passando ao lado da nova suíte de integração.
6. **Medir o tempo.** Anotar quanto tempo `./mvnw test` leva com o container
   compartilhado, contra o que levaria se cada classe de teste subisse o seu
   próprio (estimativa, não é preciso medir de fato): a base compartilhada é
   a diferença entre uma suíte de segundos e uma de minutos, à medida que o
   projeto cresce.
7. **Fechar o checklist do passo 1.** Confirmar, na tabela de
   `docs/decisoes.md`, que as três linhas (`pedido`, `expedicao`,
   `rastreamento`) têm as quatro colunas marcadas como presentes, e assinar a
   linha de baixo com a data da consolidação (sem escrever a data por
   extenso no documento, só no commit, que já carrega timestamp).
8. **Registrar a decisão de container compartilhado.** Uma linha em
   `docs/decisoes.md` nomeando `IntegrationTestBase` como o padrão que os
   testes de integração seguintes devem estender, para não repetir o custo
   de um `MySQLContainer` por classe.

**Entregável do dia:** `IntegrationTestBase` com o `MySQLContainer`
compartilhado, `PedidoIntegrationTest` exercitando `POST` seguido de `GET`
por HTTP real, e o checklist de consolidação das três camadas fechado em
`docs/decisoes.md`. Critério de aceitação: `./mvnw test` verde, com o
container subindo uma única vez para toda a suíte, e nenhuma célula do
checklist marcada como ausente.

### Fechamento, 21h50 às 22h00

- `git add src docs`
- `git commit -m "test(pedido): adiciona suite de integracao de ponta a ponta com container compartilhado"`
- `git push`
- Fechar o Módulo 4 relendo as quatro aulas em uma frase cada: a Aula 15
  trocou verbosidade por mágica, a Aula 16 deu nome a uma unidade atômica de
  escrita, a Aula 17 provou que as três camadas conversam de ponta a ponta, e
  a próxima aula vai abrir o motor que faz a mágica funcionar.
- **Prévia da Aula 18.** Toda vez que `RemessaRepository.findAll()` rodou até
  hoje, cada `Remessa` veio sozinha, sem suas ocorrências. A próxima aula
  cria esse relacionamento, e mostra o problema que ele traz de graça se
  ninguém prestar atenção: uma consulta que sozinha vira dezenas.

### Referências

1. MESQUITA, Paulo Ricardo Batista. **Capítulo 16: Frameworks Usados para
   Implementar Software em 3 Camadas.** Arquitetura de Software. AVA,
   Uninove. Fonte primária desta aula, `pdf/016.pdf`.
2. SPRING. **Página do grupo de desenvolvimento do Spring Framework.**
   <https://docs.spring.io/spring-framework/reference/> Referência indicada
   pelo capítulo.
3. Testcontainers. **Documentação**, seção de reutilização de containers
   entre testes. <https://java.testcontainers.org/features/reuse/>
4. Spring. **Documentação do Spring Boot**, seção de testes de integração
   com `@SpringBootTest` e `TestRestTemplate`.
   <https://docs.spring.io/spring-boot/reference/testing/spring-boot-applications.html>
5. JUnit. **JUnit 5 User Guide.** <https://junit.org/junit5/docs/current/user-guide/>

---

## Aula 18, Hibernate e JavaServer Faces

**Módulo:** M4, Persistência e componentes
**Capítulo do AVA:** `pdf/017.pdf`, Hibernate ou JavaServer Faces
**Entregável:** o relacionamento `Remessa` para `Ocorrencia` mapeado com
`@OneToMany`/`@ManyToOne`, uma consulta com `JOIN FETCH` em
`RemessaRepository`, e a evidência numérica do problema N+1 antes e depois,
capturada por um teste que conta as consultas SQL executadas pelo Hibernate.
Critério de aceitação: `./mvnw test` verde, com um caso provando N+1 consultas
na versão ingênua e exatamente uma consulta na versão com `JOIN FETCH`, e a
comparação registrada em `docs/decisoes.md`.

> **Nota para o professor.** Como na Aula 16, JSF entra hoje só como leitura e
> comparação lado a lado com o equivalente Spring que a Rota Sul já usa desde
> a Aula 13 (Thymeleaf). Nenhuma linha de Facelets, `@ManagedBean` ou
> `AbstractFacade` é escrita pela turma. O laboratório de hoje constrói
> apenas o relacionamento JPA e a correção do N+1, sobre o que já existe.

### Retomada, 5 minutos

Na Aula 17 cada aluno entregou `PedidoIntegrationTest`, subindo a aplicação
inteira contra um `MySQLContainer` compartilhado e batendo em `/pedidos` por
HTTP real. Abrir `Remessa` e `Ocorrencia`, mapeadas desde a Aula 16, e
perguntar à turma: essas duas classes têm alguma ligação hoje? A resposta é
não, `Ocorrencia` não sabe a que `Remessa` pertence, e `Remessa` não sabe
quais ocorrências tem. A aula de hoje cria esse laço, e mostra o preço que
ele cobra se ninguém prestar atenção.

### Ciclo 1, 19h30 às 20h05

- **Conceito.** Hibernate, o provedor de JPA por trás do Spring Data desde a
  Aula 15, na descrição do capítulo [1].

  **De onde o Hibernate vem.** O capítulo situa o Hibernate entre as
  ferramentas que ajudam no desenvolvimento de aplicativos de grande porte na
  plataforma Java EE, junto de ferramentas RAD que geram software a partir de
  modelos UML (Together, IBM Rational Rose, Enterprise Architect) ou de regras
  de negócio (Genexus). O Hibernate nasceu como solução livre para resolver
  um problema já conhecido da turma desde a Aula 14, mapear efetivamente as
  entidades de dados e seus relacionamentos para o modelo de objetos da
  orientação a objetos, técnicas que, segundo o capítulo, "são bem
  divergentes entre si". Começou em Java, ganhou uma versão para .Net chamada
  NHibernate, e hoje é coordenado pela RedHat, a mesma empresa por trás do
  JBoss, um servidor de aplicações Java EE.

  **O que o Hibernate faz, na descrição literal do capítulo.** Ele transforma
  classes Java em tabelas, e atributos em dados SQL; a partir do modelo de
  classes, cria as chamadas SQL que o software precisa para consultar e
  atualizar dados; e livra o desenvolvedor de escrever código de criação e
  execução de comandos SQL, de verificar o resultado das transações, e de
  converter tipos de dados Java para tipos de dados do banco, mantendo
  portabilidade entre bancos diferentes. O mapeamento é feito por arquivos XML
  ou por anotações Java, e o capítulo mostra os dois: a Listagem 3 do
  capítulo é um `hibernate-mapping` em XML, com `<class name="Usuario"
  table="USUARIO">`, `<id name="idUsuario" ...>` e `<property name="nome"
  column="NOME" .../>` para cada atributo.

  **A dívida que fecha desde a Aula 15.** `@Entity`, `@Table`, `@Id` e
  `@Column`, que a turma já escreveu em `Pedido`, `Remessa` e `Ocorrencia`,
  são exatamente o que o XML da Listagem 3 faz, só que declarado dentro da
  própria classe Java, em vez de um arquivo separado. "Spring Data JPA sobre
  Hibernate", fixado no contrato técnico desde a Aula 01, se fecha hoje: o
  Hibernate é o motor que lê essas anotações e gera o SQL que
  `PedidoRepository.save` executa por baixo, desde sempre, sem que a turma
  precisasse saber o nome dele até agora.

- **Demonstração no projetor.** Projetar a Listagem 3 do capítulo (o XML de
  mapeamento) ao lado da classe `Pedido` anotada, escrita na Aula 15. Ligar
  cada linha: `<class name="Usuario" table="USUARIO">` corresponde a
  `@Entity` mais `@Table(name = "pedido")`; `<id name="idUsuario"
  type="int" column="IDUSUARIO">` corresponde a `@Id` mais `@GeneratedValue`;
  cada `<property name="..." column="..." type="..."/>` corresponde a cada
  `@Column`. O capítulo também cita a **HQL**, Hibernate Query Language, que
  permite escrever consultas usando herança, polimorfismo e encapsulamento; a
  JPQL que a Aula 14 e a Aula 15 usaram é, na prática, o dialeto padronizado
  dessa mesma ideia.

  > **Nota para o professor.** O capítulo qualifica uma desvantagem, e a
  > qualificação vale preservar: as facilidades do Hibernate não estão livres
  > de efeitos colaterais, e o mais imediato é o aumento do tempo necessário
  > para executar os processos SQL, porque o mapeamento das classes depende
  > de reflexão de objetos. É essa mesma reflexão, e a facilidade de navegar
  > de um objeto para outro sem escrever `JOIN` manualmente, que abre a porta
  > para o problema do Ciclo 2 de hoje.

- **Exercício curto.** Cinco minutos, em duplas. Traduzir três linhas do XML
  de mapeamento do capítulo (`<id>`, `<property name="senha"
  column="SENHA"/>`, `<class name="Usuario" table="USUARIO">`) para a
  anotação JPA equivalente, sem olhar o código já escrito. Gabarito: `@Id`;
  `@Column(name = "SENHA") private String senha;`; `@Entity @Table(name =
  "USUARIO") public class Usuario`.

### Ciclo 2, 20h05 às 20h40

- **Conceito.** Relacionamentos, carregamento preguiçoso e o problema N+1.

  > **Nota para o professor.** O capítulo não usa os termos "lazy loading"
  > nem "N+1": ele descreve o Hibernate no nível de mapeamento
  > objeto-relacional geral, sem entrar no comportamento de carregamento de
  > coleções relacionadas. O conteúdo desta seção é aprofundamento necessário
  > para o laboratório de hoje, ancorado na própria documentação oficial do
  > Hibernate, referência [3] desta aula, e em FOWLER, **Patterns of
  > Enterprise Application Architecture**, que descreve o problema de
  > consultas N+1 sob o nome "Select N+1 problem". Dizer isso à turma antes de
  > seguir: o texto do AVA continua sendo a fonte do mapeamento
  > objeto-relacional em si, só o problema de desempenho de hoje vem de fora
  > dele.

  **O relacionamento de hoje.** `Remessa` ganha uma lista de `Ocorrencia`
  (`@OneToMany`), e cada `Ocorrencia` ganha uma referência de volta para sua
  `Remessa` (`@ManyToOne`, o lado dono do relacionamento, que carrega a chave
  estrangeira). Por padrão, o JPA carrega coleções (`@OneToMany`) de forma
  **preguiçosa** (`FetchType.LAZY`): a lista de ocorrências só é buscada no
  banco no momento em que o código chama `remessa.getOcorrencias()`, não no
  momento em que a `Remessa` é carregada.

  **O problema N+1.** Se o código busca todas as remessas com `findAll()` (1
  consulta) e depois, para cada uma, acessa `getOcorrencias()` dentro de um
  laço, o Hibernate dispara **uma consulta adicional por remessa**, porque
  cada acesso preguiçoso é resolvido individualmente. Para `N` remessas, isso
  é 1 consulta inicial mais `N` consultas de coleção, N+1 no total, em vez de
  uma única consulta bem escrita. O problema é silencioso: o código compila,
  os testes anteriores passam, e a lentidão só aparece quando o volume de
  dados cresce, exatamente o tipo de defeito que a diretiva de testes do
  professor pede para tornar visível antes que aconteça em produção.

  **A correção com `JOIN FETCH`.** Uma consulta JPQL explícita, com `JOIN
  FETCH`, instrui o Hibernate a trazer a `Remessa` e suas `Ocorrencia`s numa
  única consulta SQL, com um `JOIN` de verdade, em vez de uma consulta por
  remessa:

  ```java
  @Query("SELECT DISTINCT r FROM Remessa r LEFT JOIN FETCH r.ocorrencias")
  List<Remessa> buscarTodasComOcorrencias();
  ```

  O `DISTINCT` evita linhas repetidas de `Remessa` quando ela tem mais de uma
  `Ocorrencia`, um efeito colateral comum do `JOIN` que o time precisa saber
  explicar, não só copiar.

- **Demonstração no projetor.** Projetar o `AbstractFacade<T>` do capítulo
  (Listagem 7), a classe genérica que encapsula `create`, `edit`, `remove`,
  `find`, `findAll`, `findRange` e `count`, todos delegando a um
  `EntityManager` injetado por `@PersistenceContext`. Ao lado, projetar
  `JpaRepository<Remessa, Long>`, escrito pela turma como uma interface vazia
  desde a Aula 16. Apontar: o `AbstractFacade` do capítulo reimplementa à mão
  o que `JpaRepository` já entrega pronto, com os mesmos métodos, `create`
  contra `save`, `find` contra `findById`, `findAll` contra `findAll`. É o
  mesmo Spring Data JPA sobre Hibernate de sempre, só que hoje a turma vê o
  código que ele evita escrever.

- **Exercício curto.** Cinco minutos, individual. Dado o método
  `remessaRepository.findAll()` seguido de um laço que chama
  `remessa.getOcorrencias().size()` para cada remessa, quantas consultas SQL
  o Hibernate dispara para 10 remessas? Gabarito: 11, uma para o `findAll` e
  uma para cada acesso preguiçoso à coleção de ocorrências, o N+1 do nome.

### Quiz, 20h40 às 20h50

**Pergunta.** Segundo a descrição do capítulo, qual das alternativas resume
corretamente o que o Hibernate faz pelo desenvolvedor, ao transformar classes
Java em tabelas de um banco de dados?

- A) Elimina a necessidade de um banco de dados relacional, substituindo-o
  por armazenamento em memória.
- B) Cria as chamadas SQL necessárias a partir do modelo de classes, e livra
  o desenvolvedor de escrever e verificar manualmente os comandos SQL e as
  conversões de tipo entre Java e o banco, mantendo a portabilidade do
  aplicativo entre bancos diferentes.
- C) Garante desempenho superior ao SQL escrito manualmente, em qualquer
  cenário, sem custo adicional de processamento.
- D) Substitui a linguagem SQL nas bases de dados por HQL, exigindo que o
  banco de dados a interprete diretamente.

**Correta:** B.

**Justificativa.** É a descrição literal do capítulo: o Hibernate cria as
chamadas SQL que o software precisa, a partir do modelo de classes, e livra o
desenvolvedor de escrever código de criação e execução de SQL, de verificar
o resultado das transações e de converter tipos de dados, mantendo a
portabilidade entre bancos. A alternativa A está errada porque o Hibernate
mapeia para um banco relacional, não o substitui. A C contradiz o próprio
capítulo, que qualifica o aumento do tempo de processamento SQL como efeito
colateral da reflexão de objetos usada pelo Hibernate, o exato oposto de
"sem custo adicional". A D está errada porque a HQL é traduzida pelo
Hibernate em SQL de verdade, executado pelo banco; o banco nunca interpreta
HQL diretamente.

### Ciclo 3, 20h50 às 21h25

Laboratório do relacionamento e da evidência de desempenho.

1. **Migration do relacionamento.** Em
   `src/main/resources/db/migration/V3__adiciona_relacionamento_remessa_ocorrencia.sql`,
   `ALTER TABLE ocorrencia ADD COLUMN remessa_id BIGINT`, com um índice, mas
   **sem `CONSTRAINT` de chave estrangeira formal**.

   > **Nota para o professor.** Dispensar a `FOREIGN KEY` é opinião de
   > arquitetura, não regra do capítulo, e o professor pode discordar dela em
   > sala. O argumento a favor: a integridade do relacionamento é garantida
   > hoje pelo código Java, via Hibernate, e a ausência da `CONSTRAINT` é o
   > que permite que a Aula 19 separe a tabela `remessa` e a tabela
   > `ocorrencia` em dois processos donos diferentes sem escrever nenhuma
   > migration de remoção de restrição. O argumento contra, que vale colocar
   > para a turma: sem `FOREIGN KEY`, o banco aceita uma `ocorrencia`
   > apontando para uma `remessa` que não existe, e nada além do código
   > impede isso. Se o professor preferir a `CONSTRAINT`, o custo é uma
   > migration a mais na Aula 19, com `ALTER TABLE ocorrencia DROP FOREIGN
   > KEY`, antes da separação em serviços. A decisão precisa ser tomada hoje,
   > porque a Aula 19 depende dela.
2. **Mapear o relacionamento nas duas entidades.** Em `Ocorrencia`, o lado
   dono: `@ManyToOne @JoinColumn(name = "remessa_id") private Remessa
   remessa;`. Em `Remessa`, o lado inverso, só leitura:
   `@OneToMany(mappedBy = "remessa", fetch = FetchType.LAZY) private
   List<Ocorrencia> ocorrencias = new ArrayList<>();`.
3. **Ajustar `RemessaService.baixarRemessa`.** Da Aula 16, ao criar a nova
   `Ocorrencia`, associar `ocorrencia.setRemessa(remessa)` antes de salvar,
   preenchendo a chave estrangeira nova.
4. **Habilitar as estatísticas do Hibernate.** Em `application.properties`,
   `spring.jpa.properties.hibernate.generate_statistics=true`. Essa
   propriedade liga um contador interno de consultas executadas, acessível
   via `EntityManagerFactory.unwrap(SessionFactory.class).getStatistics()`,
   usado no teste de hoje para medir, não só observar no log, quantas
   consultas cada estratégia dispara.
5. **Escrever o teste do "antes", provando o N+1.** Em
   `RemessaRepositoryTest`, salvar 3 remessas com 2 ocorrências cada. Zerar as
   estatísticas (`getStatistics().clear()`), chamar `remessaRepository.findAll()`,
   percorrer o resultado chamando `remessa.getOcorrencias().size()` para
   cada uma, e então ler `getStatistics().getQueryExecutionCount()`. Afirmar
   que o valor é exatamente 4 (1 consulta do `findAll` mais 3 consultas de
   coleção, uma por remessa), a evidência numérica do N+1 antes da correção.
6. **Escrever o teste do "depois", provando o `JOIN FETCH`.** No mesmo
   arquivo, zerar as estatísticas de novo, chamar
   `remessaRepository.buscarTodasComOcorrencias()`, e afirmar que
   `getQueryExecutionCount()` é exatamente 1. As mesmas 3 remessas e 6
   ocorrências, uma única consulta.

### Ciclo 4, 21h25 às 21h50

7. **Rodar os dois casos.** `./mvnw test`, conferindo que as duas afirmações
   de contagem passam, a evidência do "antes" e do "depois" pedida pelo
   entregável do dia, comprovada por asserção, não por leitura visual de log.
8. **Trocar o uso em produção.** Localizar onde `RemessaService` ou qualquer
   outro ponto do código chama `remessaRepository.findAll()` para listar
   remessas com suas ocorrências, e trocar pela versão com `JOIN FETCH`,
   `buscarTodasComOcorrencias()`, aplicando a correção onde ela importa, não
   só no teste.
9. **Registrar a evidência numérica, o entregável central de hoje.** Em
   `docs/decisoes.md`, uma linha com os dois números: "3 remessas com 2
   ocorrências cada: 4 consultas sem `JOIN FETCH`, 1 consulta com `JOIN
   FETCH`", mais uma frase explicando a causa, carregamento preguiçoso
   resolvido individualmente por linha, em vez de um `JOIN` só.
10. **Registrar a decisão da chave estrangeira sem `CONSTRAINT`.** Uma
    segunda linha em `docs/decisoes.md`, explicando que `remessa_id` existe
    como coluna simples, sem `FOREIGN KEY` formal no banco, de propósito,
    para não travar a divisão de serviços da próxima aula.

**Entregável do dia:** `Ocorrencia` com `@ManyToOne` para `Remessa`,
`Remessa` com `@OneToMany` preguiçoso para `Ocorrencia`,
`buscarTodasComOcorrencias()` com `JOIN FETCH` em `RemessaRepository`, e
`RemessaRepositoryTest` com os dois casos de contagem de consultas. Critério
de aceitação: `./mvnw test` verde, com N+1 consultas comprovadas na versão
ingênua e exatamente uma na versão com `JOIN FETCH`, e as duas linhas de
`docs/decisoes.md` presentes.

### Fechamento, 21h50 às 22h00

- `git add src docs`
- `git commit -m "fix(expedicao): corrige N+1 com join fetch no relacionamento remessa-ocorrencia"`
- `git push`
- Fechar o Módulo 4 relendo a régua que ele usou o semestre inteiro: memória
  contra JDBC contra JPA (linhas de código), EJB contra `@Transactional`
  (onde a transação é declarada), JSF contra Thymeleaf (PUSH contra PULL,
  fixado na Aula 13), Hibernate por trás de tudo desde a Aula 01. Quatro
  aulas, quatro comparações honestas, nenhuma delas depreciando o que os
  capítulos ensinam.
- **Prévia da Aula 19.** Tudo o que a Rota Sul construiu até hoje roda num
  processo só, uma JVM, um `java -jar`. A próxima aula quebra esse processo
  em quatro, e a chamada que `RemessaService` faz para `OcorrenciaRepository`
  hoje, dentro do mesmo processo, vira uma chamada de rede entre dois
  serviços separados. A relação sem `CONSTRAINT` formal que a turma acabou de
  registrar é exatamente o que torna essa quebra possível sem reescrever o
  banco.

### Referências

1. MESQUITA, Paulo Ricardo Batista. **Capítulo 17: Hibernate ou JavaServer
   Faces.** Arquitetura de Software. AVA, Uninove. Fonte primária desta aula,
   `pdf/017.pdf`.
2. Oracle / Eclipse Foundation. **JavaServer Faces**, documentação
   histórica citada pelo capítulo.
   <https://javaserverfaces.java.net/users.html>
3. Hibernate. **Hibernate ORM Documentation**, seção de estratégias de
   `fetch` e o problema de consultas N+1.
   <https://hibernate.org/orm/documentation/>
4. FOWLER, Martin. **Patterns of Enterprise Application Architecture.**
   Addison-Wesley, 2002.
5. Spring. **Documentação do Spring Data JPA**, seção de `@Query` e `JOIN
   FETCH`. <https://docs.spring.io/spring-data/jpa/reference/jpa/query-methods.html>
6. JUnit. **JUnit 5 User Guide.** <https://junit.org/junit5/docs/current/user-guide/>

---

## Aula 19, Montagem da aplicação distribuída

**Módulo:** M5, Projeto final
**Capítulo do AVA:** `pdf/018.pdf`, Projeto Final
**Entregável:** o monólito quebrado em quatro processos,
`pedidos-service`, `expedicao-service`, `rastreamento-service` e
`portal-web`, subindo juntos com um único `compose.yaml`, publicados em
GitHub Codespaces com a porta do `portal-web` marcada como pública. Critério
de aceitação: `docker compose up --build` sobe os quatro serviços mais o banco
sem erro, a URL pública do Codespaces responde ao portal, um pedido cadastrado
pelo `portal-web` aparece no `pedidos-service` e uma baixa de remessa gera uma
ocorrência visível pelo `rastreamento-service`, tudo através de chamadas de
rede reais entre os quatro processos.

### Retomada, 5 minutos

Na Aula 18 cada aluno entregou o relacionamento `Remessa` para `Ocorrencia`
corrigido do problema N+1 com `JOIN FETCH`, e uma decisão registrada em
`docs/decisoes.md`: a coluna `remessa_id` existe sem `CONSTRAINT` formal de
chave estrangeira, de propósito, para não travar o que viria a seguir. Hoje é
o dia em que essa decisão paga o dividendo. Perguntar à turma: até agora,
`RemessaService.baixarRemessa` chama `OcorrenciaRepository.save` dentro do
mesmo método, no mesmo processo. Depois de hoje, esses dois pedaços de código
moram em dois processos diferentes, em dois containers diferentes. O que
precisa mudar para essa chamada continuar funcionando?

### Ciclo 1, 19h30 às 20h05

- **Conceito.** O capítulo de hoje é o mais curto dos dezoito, e ele mesmo diz
  por quê: "todos os outros tópicos apresentaram conceitos que permitem o
  desenvolvimento rápido de aplicações distribuídas" [1]. O papel deste
  capítulo não é ensinar algo novo, é montar o que já foi ensinado.

  **O exemplo do capítulo, e a tradução para a Rota Sul.** O capítulo
  descreve uma agenda de contatos construída sobre um banco já estruturado,
  usando JPA para a conexão com o banco, o modelo de programação EJB para as
  regras de negócio, e JSP com Servlets para a interface de usuário,
  "estruturados de acordo com o modelo de arquitetura MVC". Ler essa frase em
  voz alta e traduzir, peça por peça, para o que a Rota Sul já tem: JPA sobre
  Hibernate para a conexão com o banco, é a Aula 15 e a Aula 18; o modelo de
  programação para as regras de negócio, é `@Service` com `@Transactional`,
  o equivalente Spring do EJB, é a Aula 16; a interface de usuário, é
  Thymeleaf sobre Spring MVC, o equivalente do JSP com Servlets, é a Aula 13.
  A Rota Sul já é, desde a Aula 18, exatamente o que o capítulo descreve
  como "aplicação distribuída": três tecnologias combinadas num único
  aplicativo MVC.

  > **Nota para o professor.** Uma distinção honesta que vale explicitar. O
  > "distribuída" do capítulo, no vocabulário do Java EE clássico, significa
  > um aplicativo cujos componentes **podem** rodar em hardware diferente
  > (via RMI, EJB remoto, apresentado na Aula 16), mas que normalmente é
  > empacotado e implantado como uma unidade só, um único WAR ou EAR num
  > único servidor. O "distribuída" de hoje é mais radical: quatro processos
  > independentes, cada um com seu próprio ciclo de vida, sua própria
  > imagem de container, capazes de subir, cair e escalar separadamente. O
  > capítulo não cobre Docker nem orquestração de containers, porque esse
  > vocabulário é posterior ao material. O Ciclo 2 de hoje entra nesse
  > território com a documentação oficial do Docker Compose e do GitHub
  > Codespaces como fonte, referências [3] e [4] desta aula.

- **Demonstração no projetor.** Abrir `docs/arquitetura/componentes.puml`, da
  Aula 04, e reler os componentes que ele já desenhava como esboço:
  "Pedidos", "Expedição e roteirização", "Rastreamento e ocorrências",
  "Integração com parceiros". Apontar: os nomes que a turma escolheu para os
  quatro serviços de hoje, `pedidos-service`, `expedicao-service`,
  `rastreamento-service` e `portal-web`, não são novos, eles só dão
  materialidade de processo a componentes que já estavam desenhados desde a
  quarta semana de aula.

- **Exercício curto.** Cinco minutos, individual. Para cada um dos quatro
  serviços de hoje, escrever de qual pacote do monólito atual ele herda
  código: `pedidos-service` recebe `pedido.*`; `rastreamento-service` recebe
  `rastreamento.*`; `portal-web` recebe os templates Thymeleaf e os
  controladores de tela da Aula 13; e `expedicao-service` recebe
  `expedicao.*` mais um quinto pacote que ainda não foi encaixado em nenhum
  serviço até agora. Gabarito: o quinto pacote é `parceiro`, da Aula 10, com
  seus subpacotes `endpoint` e `client`. **Decisão de hoje:** ele entra em
  `expedicao-service`, porque é a expedição quem faz o handoff da última
  milha para a transportadora parceira simulada, o mesmo ator que a Aula 05
  já descrevia no case.

### Ciclo 2, 20h05 às 20h40

- **Conceito.** Quatro armadilhas da quebra em processos, e a publicação em
  GitHub Codespaces.

  **O host do banco dentro do compose não é `localhost`.** Desde a Aula 14,
  `application.properties` aponta para `jdbc:mysql://localhost:3306/rotasul`,
  porque o MySQL rodava com `docker run -p 3306:3306`, na mesma máquina que a
  aplicação. Dentro de um `compose.yaml`, cada serviço tem seu próprio nome
  como hostname de rede, e a aplicação e o banco não compartilham mais
  `localhost`: o banco passa a se chamar `db`, o nome do serviço no
  `compose.yaml`, e a URL vira `jdbc:mysql://db:3306/rotasul`. Esquecer essa
  troca é o erro mais comum de quem containeriza pela primeira vez, e a
  aplicação falha na subida com "connection refused", porque está tentando
  falar com ela mesma em vez de falar com o banco.

  **Configuração por variável de ambiente, a convenção do duplo
  sublinhado.** O Spring Boot lê variáveis de ambiente e as converte em
  propriedades, sem editar `application.properties`, sem reconstruir a
  imagem. A regra: cada ponto (`.`) do nome canônico da propriedade vira um
  sublinhado simples (`_`); cada hífen (`-`) que já existir dentro de um
  trecho do nome vira **sublinhado duplo** (`__`). Por isso,
  `spring.datasource.url` vira `SPRING_DATASOURCE_URL` (sem hífen no nome
  original, um sublinhado por ponto), mas `spring.jpa.hibernate.ddl-auto`,
  que a Aula 15 fixou em `application.properties`, vira
  `SPRING_JPA_HIBERNATE_DDL__AUTO` (o hífen de `ddl-auto` virou sublinhado
  duplo). Quem escreve `SPRING_JPA_HIBERNATE_DDL_AUTO`, com um sublinhado só,
  erra silenciosamente: a variável não é reconhecida, e o valor de
  `application.properties` continua valendo sem aviso nenhum.

  **`healthcheck` e `depends_on: condition: service_healthy`.** Um MySQL
  leva alguns segundos para aceitar conexões depois que o container sobe,
  mesmo que o processo já esteja rodando. Sem um `healthcheck`, o
  `pedidos-service` tenta conectar assim que o `db` inicia, não quando ele
  está pronto, e falha na primeira tentativa. A correção: o serviço `db`
  declara um `healthcheck` que testa a conexão de verdade, e cada serviço
  que depende dele usa `depends_on: db: condition: service_healthy`, em vez
  de um `depends_on` simples, que só espera o container **existir**, não
  espera ele **responder**.

  **Três serviços, um schema, três históricos de migration.** Esta é a
  armadilha que não aparece no `compose.yaml` e derruba a subida do dia. A
  especificação da disciplina fixa **um único schema**, `rotasul`, e o
  `compose.yaml` de hoje tem **um único** serviço `db`: os três serviços com
  banco apontam `SPRING_DATASOURCE_URL` para o mesmo lugar. Só que o Flyway,
  por padrão, grava o que já aplicou numa tabela de controle de nome fixo,
  `flyway_schema_history`. Três serviços com o mesmo schema e o mesmo nome de
  tabela de controle disputam **um histórico só**: o primeiro a subir grava
  ali as suas migrations; o segundo lê a mesma tabela, encontra migrations
  aplicadas que não existem no próprio `db/migration`, conclui que o histórico
  está corrompido e aborta a subida com "Detected applied migration not
  resolved locally". O `docker compose up` não completa, e o erro não fala de
  arquitetura, fala de arquivo faltando.

  O problema é de arquitetura distribuída, não de configuração: **estado
  compartilhado sem dono definido**. Três processos independentes escrevendo
  na mesma estrutura de controle, cada um com a sua verdade parcial sobre o
  que já foi aplicado. Num desenho de microsserviços maduro a resposta seria
  um banco por serviço, e é a resposta que vale citar em voz alta. Como o
  case fixa schema único, a Rota Sul usa a segunda melhor: **cada serviço tem
  a sua própria tabela de histórico dentro do mesmo schema**, declarada em
  `application.properties`, e cuida apenas das próprias tabelas.

  ```properties
  spring.flyway.table=flyway_schema_history_pedidos
  ```

  Com isso, `pedidos-service` só conhece a tabela `pedido`,
  `expedicao-service` só conhece `remessa` e `rastreamento-service` só conhece
  `ocorrencia`; cada um aplica o seu conjunto de migrations, numerado a partir
  de `V1` dentro do próprio módulo, sem enxergar o histórico dos outros.
  `portal-web` não tem banco, não tem JPA e não tem Flyway.

  **Migration aplicada não se edita.** O corolário precisa ficar dito: o
  Flyway guarda o checksum de cada arquivo aplicado, e alterar o conteúdo de
  uma migration que já rodou faz a subida seguinte falhar com erro de
  validação. Como o laboratório de hoje **recorta** as migrations do monólito,
  redistribuindo `pedido`, `remessa` e `ocorrencia` entre três módulos, os
  arquivos mudam de nome, de numeração e de conteúdo. Isso só é legítimo
  porque o banco do `compose.yaml` é um banco **novo**, num volume novo, que
  nunca viu essas migrations. Se a turma já tiver subido o compose antes e
  precisar recomeçar, a instrução é uma só: `docker compose down -v`, que
  apaga o volume junto com os containers, e depois `docker compose up
  --build`. Sem o `-v`, o volume antigo sobrevive, as tabelas já existem, e o
  `CREATE TABLE` da migration recortada falha.

  **A URL do Codespaces existe enquanto o codespace está rodando.** Isso
  precisa ficar dito com todas as letras: o GitHub Codespaces **hiberna por
  inatividade**, e quando isso acontece, a URL pública para de responder. O
  ambiente publicado hoje não é permanente como um deploy em produção. **Cada
  equipe precisa iniciar o próprio codespace antes da apresentação da Aula
  20**, porque uma URL que respondeu perfeitamente durante o laboratório de
  hoje pode estar hibernada no dia da apresentação se ninguém a acordar
  antes.

  **O checklist de publicação, com a linha que mais gera 401.** Ao
  encaminhar a porta do `portal-web` no Codespaces, ela nasce **privada** por
  padrão. Uma porta privada devolve `401 Unauthorized` para qualquer pessoa
  que não seja o dono do codespace, incluindo o professor avaliando de fora.
  O checklist de publicação de hoje tem uma linha que resolve exatamente
  isso: **a porta está marcada como pública, e não privada**. É o
  esquecimento mais comum desta aula, e o único capaz de fazer um projeto
  funcionar perfeitamente para quem o construiu e não abrir para mais
  ninguém.

- **Demonstração no projetor.** Projetar o trecho do `compose.yaml` do kit que
  resolve as armadilhas de uma vez:

  ```yaml
  services:
    db:
      image: mysql:8.4
      environment:
        MYSQL_ROOT_PASSWORD: ${DB_PASSWORD}
        MYSQL_DATABASE: rotasul
      healthcheck:
        test: ["CMD", "mysqladmin", "ping", "-h", "localhost", "-uroot", "-p${DB_PASSWORD}"]
        interval: 5s
        timeout: 5s
        retries: 10

    pedidos-service:
      build: ./pedidos-service
      environment:
        SPRING_DATASOURCE_URL: jdbc:mysql://db:3306/rotasul
        SPRING_DATASOURCE_USERNAME: root
        SPRING_DATASOURCE_PASSWORD: ${DB_PASSWORD}
        SPRING_JPA_HIBERNATE_DDL__AUTO: validate
        SPRING_FLYWAY_TABLE: flyway_schema_history_pedidos
      depends_on:
        db:
          condition: service_healthy
      ports:
        - "8081:8080"
  ```

  Apontar as cinco linhas que resolvem as quatro armadilhas: `db` como host,
  não `localhost`; `SPRING_JPA_HIBERNATE_DDL__AUTO` com sublinhado duplo,
  não simples; `healthcheck` no serviço `db`; `condition: service_healthy`
  no `depends_on` de quem depende dele; e `SPRING_FLYWAY_TABLE` com sufixo do
  serviço, que aqui repete, em variável de ambiente, o que cada
  `application.properties` já declara, para o valor ficar visível no mesmo
  arquivo em que se lê o resto do desenho.

- **Exercício curto.** Cinco minutos, em duplas. Quatro trechos quebrados de
  `compose.yaml` são projetados, um de cada vez, e cada dupla identifica qual
  das quatro armadilhas cada um representa: (a) `SPRING_DATASOURCE_URL:
  jdbc:mysql://localhost:3306/rotasul` dentro de um serviço do compose; (b)
  `SPRING_JPA_HIBERNATE_DDL_AUTO: validate`, com um sublinhado só; (c)
  `depends_on: - db`, sem `condition`; (d) os três serviços com banco sem
  nenhuma linha de `SPRING_FLYWAY_TABLE`. Gabarito: (a) host errado, devia ser
  `db`; (b) falta o segundo sublinhado do hífen de `ddl-auto`; (c) falta
  `condition: service_healthy`, o compose só espera o container existir, não
  espera o banco responder; (d) os três vão disputar a mesma
  `flyway_schema_history` no schema `rotasul`, e o segundo a subir aborta com
  "Detected applied migration not resolved locally".

### Quiz, 20h40 às 20h50

**Pergunta.** Segundo a ATIVIDADE FINAL do capítulo, para configurar um
componente de software que responde às requisições de vários tipos de
clientes, a solução indicada é representada pela alternativa:

- A) um EJB configurado com `@Stateful`, sem interfaces.
- B) um EJB configurado com `@Stateless`, sem interfaces.
- C) um EJB configurado apenas como `@Remote`.
- D) um EJB configurado com interfaces de acesso remota e local.

**Correta:** D.

**Justificativa.** É o gabarito do capítulo, e ele conecta diretamente ao
laboratório de hoje: um componente pensado para atender clientes variados
precisa do contrato certo para cada tipo de acesso, local (mesmo servidor,
mais barato) e remoto (rede, mais caro), a mesma distinção que a Aula 16
apresentou. Hoje, cada serviço da Rota Sul expõe um contrato REST único, que
qualquer cliente consegue chamar, seja o `portal-web` de dentro da rede do
`compose.yaml`, seja um `curl` de fora para depuração: o desenho de "servir
vários tipos de clientes" que a alternativa D descreve para o EJB é o mesmo
desenho que uma API REST bem definida cumpre para os serviços de hoje. As
alternativas A e B estão erradas por alcance, não por ilegalidade: um
`@Stateless` sem interface nenhuma é perfeitamente válido desde o EJB 3.1, que
introduziu a *no-interface view*, mas essa visão é **local por definição**, só
enxergada por clientes que rodam na mesma aplicação e na mesma JVM. Um
componente sem interface, portanto, atende um tipo de cliente só, e é
exatamente isso que a pergunta exclui; a A ainda agrava, porque `@Stateful`
amarra uma instância a cada conversa de cliente, o contrário de um componente
compartilhado por clientes variados. A C erra pelo lado oposto: atende só
clientes remotos, deixando de fora quem está no mesmo servidor e pagando custo
de rede sem necessidade.

> **Nota para o professor.** Se algum aluno perguntar se um EJB pode existir
> sem interface, a resposta é sim, desde o EJB 3.1. A razão de descartar A e B
> aqui é o alcance da *no-interface view*, que é local, e não uma proibição da
> especificação.

### Ciclo 3, 20h50 às 21h25

Laboratório de quebra do monólito. O andaime da montagem chega pronto no kit;
o tempo de aula é gasto nas três coisas que ensinam arquitetura distribuída:
quebrar o relacionamento de objeto, trocar a chamada em processo por chamada
de rede, e publicar.

> **O que chega pronto no kit `aulas-1sem/labs/aula19-lab/`.** Tudo o que é
> montagem repetitiva, e nada do que é decisão de arquitetura:
>
> - `pom.xml` pai na raiz, tipo `pom`, com os quatro módulos declarados e as
>   versões de Spring Boot e Java 21 herdadas.
> - Os quatro esqueletos de módulo, cada um com o seu `pom.xml` filho, a sua
>   classe `Application` e o seu `application.properties` já preenchido. Nos
>   três serviços com banco, isso inclui a linha `spring.flyway.table` própria
>   de cada um, o `ddl-auto=validate` e a URL apontando para `db`; em
>   `portal-web`, que não tem banco, o `pom.xml` filho não traz JPA, MySQL nem
>   Flyway. Os diretórios de código e de `db/migration` chegam vazios: quem os
>   preenche é o aluno.
> - Os quatro `Dockerfile`, de duas etapas cada (build com Maven, execução em
>   imagem JRE enxuta), o mesmo `.jar` executável que a Aula 08 já mostrou
>   rodando com `java -jar`, agora empacotado numa imagem.
> - O `compose.yaml` completo, com os cinco serviços, o `healthcheck` do `db`
>   e os `depends_on` com `condition: service_healthy`.
>
> A justificativa é de tempo de aula: escrever quatro `pom.xml`, quatro
> `Dockerfile` e um `compose.yaml` de cinco serviços é trabalho de várias
> horas de digitação que não produz nenhum entendimento novo, e o critério de
> aceitação do dia é o sistema **subindo**. O professor projeta os arquivos do
> kit no Ciclo 2, e o aluno os lê antes de usá-los.

1. **Instalar o kit e conferir que o esqueleto compila.** Copiar o conteúdo do
   kit para a raiz do fork e rodar `./mvnw -q -DskipTests package`. Os quatro
   módulos, ainda vazios de código de negócio, precisam compilar antes de
   receber qualquer classe: se o `pom.xml` pai não estiver enxergando os
   quatro módulos, é melhor descobrir agora. Abrir os quatro
   `application.properties` e ler em voz alta a linha `spring.flyway.table` de
   cada um, ligando com a quarta armadilha do Ciclo 2.
2. **Mover `pedido.*` para `pedidos-service`.** Copiar `pedido/web`,
   `pedido/service`, `pedido/repository` e `pedido/domain` para dentro do
   módulo, e a migration da tabela `pedido` para o `db/migration` dele,
   renumerada como `V1__cria_tabela_pedido.sql`, que é o `V1` **deste**
   serviço. `pedidos-service` passa a ser dono da tabela `pedido` e de mais
   nada.
3. **Distribuir os outros dois contextos e recortar as migrations.**
   `expedicao.*` e `parceiro.*` vão para `expedicao-service`, que recebe em
   `db/migration` um `V1__cria_tabela_remessa.sql` contendo só a parte de
   `remessa` da antiga migration de remessa e ocorrência. `rastreamento.*` vai
   para `rastreamento-service`, que recebe um `V1__cria_tabela_ocorrencia.sql`
   com a tabela `ocorrencia` **já com a coluna `remessa_id`**, isto é, com o
   que a Aula 16 e a Aula 18 escreveram em duas migrations separadas fundido
   numa só. As antigas migrations do monólito somem junto com o monólito;
   nenhum banco existente é alterado, porque o `db` do compose sobe vazio.
4. **Quebrar o relacionamento de objeto entre `Remessa` e `Ocorrencia`.**
   Este é o ponto central do dia. `Ocorrencia` não mora mais no mesmo
   classpath de `Remessa`: `expedicao-service` não tem mais a classe
   `Ocorrencia`, e `rastreamento-service` não tem mais a classe `Remessa`.
   O `@ManyToOne`/`@OneToMany` da Aula 18 deixa de compilar dos dois lados.
   A correção: em `Ocorrencia` (agora só em `rastreamento-service`), o
   campo `private Remessa remessa;` vira `private Long remessaId;`, uma
   referência por valor, não mais um objeto. Em `Remessa` (agora só em
   `expedicao-service`), a lista `ocorrencias` é removida por completo. A
   coluna `remessa_id`, sem `CONSTRAINT` formal desde a Aula 18, não precisa
   de nenhuma restrição a remover: o preço dessa decisão está sendo pago
   agora, e é zero.
5. **Mover a apresentação para `portal-web`.** Os templates Thymeleaf e
   `PedidoFormController`, da Aula 13, migram para `portal-web`, que **não
   tem banco próprio, nenhuma dependência de JPA, de MySQL nem de Flyway**:
   ele consome os três outros serviços por REST, via `RestTemplate` ou
   `WebClient`, apontando para `http://pedidos-service:8080` e os demais,
   sempre pelo nome do serviço no compose.

### Ciclo 4, 21h25 às 21h50

6. **Trocar a chamada em processo por uma chamada de rede.**
   `RemessaService.baixarRemessa`, que chamava `ocorrenciaRepository.save`
   diretamente, passa a chamar um cliente HTTP,
   `RastreamentoServiceClient`, apontando para
   `http://rastreamento-service:8080/ocorrencias` (o nome do serviço no
   compose, não `localhost`), enviando `remessaId` no corpo da requisição.
   `rastreamento-service` ganha um `OcorrenciaController` novo, com `POST
   /ocorrencias`, para receber essa chamada. Dizer em voz alta o que se perdeu
   no caminho: a transação única da Aula 16 acabou. Se a chamada HTTP falhar
   depois de a remessa ter sido baixada, não existe `rollback` que desfaça as
   duas coisas, porque são dois bancos lógicos e dois processos.
7. **Subir tudo no Codespace.** `docker compose up --build`, conferindo que os
   cinco containers sobem sem erro. Se o compose já tiver sido subido antes
   nesta máquina, começar por `docker compose down -v`, para o volume do banco
   ser recriado: as migrations recortadas no passo 3 pressupõem um schema
   vazio. Acompanhar no log a linha do Flyway de cada serviço e conferir que
   cada uma cita a sua própria tabela de histórico.
8. **Publicar a porta como pública, o passo que mais gera 401.** No painel
   de portas do Codespaces, clicar com o botão direito na porta do
   `portal-web` e trocar a visibilidade de "Private" para "Public".
   Confirmar abrindo a URL numa aba anônima do navegador, sem estar
   autenticado como dono do codespace: se a tela do portal aparecer sem
   pedir login, a porta está pública de verdade.
9. **Testar a jornada completa pela URL pública.** Cadastrar um pedido pelo
   `portal-web`, conferir que ele aparece em `pedidos-service`, dar baixa
   numa remessa correspondente, e conferir que uma nova ocorrência aparece
   em `rastreamento-service`, tudo através da URL pública, não de
   `localhost`.
10. **Atualizar o diagrama e registrar as decisões.** Editar
    `docs/arquitetura/implantacao.puml`, esboçado na Aula 04, para representar
    os quatro `node` reais mais o `database`, exatamente como o `compose.yaml`
    de hoje os sobe: o esboço da quarta semana vira o retrato fiel do sistema.
    Em `docs/decisoes.md`, quatro linhas: onde o contexto `parceiro` foi
    encaixado (`expedicao-service`, pela relação com a última milha); a quebra
    do relacionamento de objeto entre `Remessa` e `Ocorrencia` em referência
    por `remessaId`; a tabela de histórico do Flyway separada por serviço
    dentro do schema único, com o motivo; e o lembrete, escrito em letras
    maiúsculas no próprio arquivo, de iniciar o codespace antes da Aula 20.

**Entregável do dia:** os quatro módulos Maven (`pedidos-service`,
`expedicao-service`, `rastreamento-service`, `portal-web`) preenchidos com o
código do monólito redistribuído, subindo juntos pelo `compose.yaml` do kit,
com a URL pública do Codespaces respondendo e a porta do `portal-web` marcada
como pública. Critério de aceitação: `docker compose up --build` sobe os cinco
containers sem erro de Flyway; a jornada completa, cadastro de pedido pelo
portal, baixa de remessa, ocorrência visível em rastreamento, funcionando pela
URL pública; e as quatro linhas do passo 10 registradas em
`docs/decisoes.md`.

### Fechamento, 21h50 às 22h00

- `git add pedidos-service expedicao-service rastreamento-service portal-web compose.yaml docs pom.xml`
- `git commit -m "feat(rotasul): quebra o monolito em quatro servicos distribuidos com compose.yaml"`
- `git push`
- Repetir em voz alta, para a turma sair da sala com isso guardado: o
  codespace hiberna por inatividade, e a URL de hoje pode não responder
  amanhã sem ninguém tocar em nada. **Cada equipe precisa reabrir e iniciar o
  próprio codespace antes de chegar para a apresentação da Aula 20.**
- O trabalho de ajuste fino, documentação e polimento do repositório
  continua até a apresentação; nenhum código novo é obrigatório entre hoje e
  a Aula 20, mas o fork inteiro, incluindo `docs/decisoes.md`, é o que será
  avaliado como projeto final.
- **Prévia da Aula 20.** Não há laboratório na próxima aula. Cada equipe
  apresenta o que a Rota Sul se tornou, em dez minutos, com o codespace já
  rodando, e a turma avalia as apresentações umas das outras, com a rubrica
  que a Aula 20 detalha.

### Referências

1. MESQUITA, Paulo Ricardo Batista. **Capítulo 18: Projeto Final.**
   Arquitetura de Software. AVA, Uninove. Fonte primária desta aula,
   `pdf/018.pdf`.
2. SCHINCARIOL, M.; KEITH, M. **Pro JPA 2: Mastering the Java Persistence
   API.** Apress, 2009. Referência indicada pelo capítulo.
3. Docker. **Documentação do Docker Compose**, seções de `healthcheck` e
   `depends_on`. <https://docs.docker.com/compose/how-tos/startup-order/>
4. GitHub. **Documentação do GitHub Codespaces**, seção de encaminhamento e
   visibilidade de portas.
   <https://docs.github.com/en/codespaces/developing-in-a-codespace/forwarding-ports-in-your-codespace>
5. Spring. **Documentação do Spring Boot**, seção de configuração externa
   por variáveis de ambiente.
   <https://docs.spring.io/spring-boot/reference/features/external-config.html>
6. Docker. **Documentação de referência do `Dockerfile`.**
   <https://docs.docker.com/reference/dockerfile/>
7. Flyway. **Documentação**, propriedade `flyway.table` e validação por
   checksum. <https://documentation.red-gate.com/fd/table-184127474.html>

---

## Aula 20, Apresentação do projeto final

**Módulo:** M5, Projeto final
**Capítulo do AVA:** sem capítulo correspondente.
**Entregável:** a apresentação de dez minutos por equipe, feita ao vivo pela
URL pública do Codespaces, mais o repositório final entregue, o fork inteiro
com o histórico de commits do próprio aluno, avaliado pelos critérios da
seção 7.1 do `PLANO_DE_ENSINO.md`. Critério de aceitação: os quatro serviços
respondendo pela URL pública durante a apresentação da própria equipe, a
ficha de avaliação por pares preenchida pela turma para cada equipe
apresentada, e o fork publicado no estado em que foi apresentado.

Esta é a última aula do semestre, e a única, além da Aula 01, sem capítulo do
AVA correspondente. Seguindo a regra fixada no cabeçalho deste documento, a
posição [1] das referências é ocupada pelo documento que faz as vezes de
fonte primária de hoje: o `PLANO_DE_ENSINO.md`, seções 7 e 7.1, que definem a
composição da nota e os critérios do projeto final. É a mesma solução que a
Aula 01 já usou para o mesmo problema, na abertura do semestre.

> **Nota para o professor.** Os quatro ciclos de hoje não seguem a tríade
> conceito, demonstração, exercício curto das demais aulas: são ciclos de
> **apresentação**, não de laboratório, como o brief desta passagem
> instrui explicitamente. A estrutura de oito subseções permanece intacta,
> só o conteúdo interno dos Ciclos 1 a 4 muda de natureza.

### Retomada, 5 minutos

Na Aula 19 cada equipe entregou os quatro serviços da Rota Sul,
`pedidos-service`, `expedicao-service`, `rastreamento-service` e
`portal-web`, publicados por `compose.yaml` em GitHub Codespaces, com a porta
do `portal-web` marcada como pública. Antes de qualquer outra coisa, uma
pergunta de chamada, equipe por equipe: "o codespace de vocês está rodando
agora?" Codespace hibernado é resolvido nos primeiros minutos, não durante o
tempo de apresentação de ninguém.

### Ciclo 1, 19h30 às 20h05

**Logística e rubrica, antes da primeira equipe subir.** O professor
apresenta, em até cinco minutos, a mecânica do dia: cada equipe tem dez
minutos de apresentação, seguidos de até três minutos de perguntas e
pontuação pela plateia, antes da próxima equipe começar. A grade dos quatro
ciclos, 130 minutos de tempo útil descontados o quiz e o fechamento, comporta
essa sequência se repetindo até o fim da lista de equipes.

**O que cada apresentação precisa mostrar, em dez minutos.** Uma demonstração
ao vivo pela URL pública (não por `localhost`, não por captura de tela): um
pedido sendo cadastrado pelo `portal-web`, uma baixa de remessa gerando uma
ocorrência visível em `rastreamento-service`, e uma frase da equipe
explicando por que os quatro serviços foram divididos daquele jeito,
incluindo onde o contexto `parceiro` foi encaixado. Nenhum slide é
obrigatório; o sistema rodando é a evidência.

**A ordem de apresentação.** Sorteada no início do Ciclo 1, não por ordem
alfabética nem por ordem de chegada, para que nenhuma equipe tenha vantagem
ou desvantagem sistemática de horário. A ordem sorteada é lida em voz alta e
escrita na lousa, para a plateia acompanhar quantas apresentações faltam.

**Se a URL pública de uma equipe não responder.** Antes de qualquer coisa,
conferir se o codespace está apenas hibernado (o painel do GitHub mostra o
status e reinicia em cerca de um minuto); se reiniciar a tempo, a
apresentação segue normalmente, só com um atraso curto absorvido pelo tempo
de perguntas. Se não reiniciar dentro de um tempo razoável, a equipe
apresenta com o que conseguir mostrar, `localhost` dentro do próprio
codespace via terminal integrado incluído, e a professor registra a falha
de publicação como uma perda de pontos no critério de funcionalidade (30% da
nota do projeto final, seção 7.1 do `PLANO_DE_ENSINO.md`), não como
desculpa para pontuação cheia.

**Primeiro bloco de apresentações.** As primeiras equipes da lista apresentam
dentro deste ciclo, cada uma seguida da rodada de perguntas e pontuação da
plateia descrita acima.

### Ciclo 2, 20h05 às 20h40

**Continuação das apresentações.** O mesmo formato do Ciclo 1, dez minutos
por equipe mais até três de perguntas, para as próximas equipes da lista.

**Papel do professor durante as apresentações.** Cronometrar cada
apresentação, garantindo que nenhuma equipe avance sobre o tempo da
seguinte, e preencher a própria ficha de avaliação, com os critérios da
seção 7.1 do `PLANO_DE_ENSINO.md`, em paralelo à ficha de avaliação por
pares que a turma preenche.

**Perguntas sugeridas para a rodada de Q&A, um roteiro para quem não sabe o
que perguntar.** Nem toda plateia chega com perguntas prontas, e o professor
pode usar este roteiro como reserva, sem obrigação de usá-lo se a turma já
estiver perguntando por conta própria: "por que o contexto `parceiro` ficou
nesse serviço, e não em outro?"; "o que acontece se `rastreamento-service`
estiver fora do ar no momento em que `expedicao-service` tenta registrar uma
ocorrência?"; "qual foi a decisão mais difícil de justificar em
`docs/decisoes.md`?". As três perguntas miram exatamente os pontos que a
ficha de pares avalia, arquitetura distribuída e domínio da equipe sobre o
próprio código.

### Quiz, 20h40 às 20h50

**Pergunta.** Segundo a tabela de critérios do projeto final na seção 7.1 do
`PLANO_DE_ENSINO.md`, qual dos cinco critérios abaixo tem o **maior** peso na
nota do projeto final?

- A) Documentação do fork, incluindo `docs/decisoes.md`.
- B) Modelagem e persistência de dados.
- C) Funcionalidade dos quatro serviços.
- D) Apresentação na Aula 20.

**Correta:** C.

**Justificativa.** A tabela da seção 7.1 do plano de ensino atribui 30% à
funcionalidade dos quatro serviços, o maior peso entre os cinco critérios,
seguido por 25% de qualidade do código e da arquitetura em camadas, 20% de
modelagem e persistência de dados, 15% de documentação do fork e 10% de
apresentação na Aula 20. A alternativa A vale 15%, a B vale 20%, e a D, a
própria apresentação de hoje, vale apenas 10%: o peso maior está em o
sistema **funcionar de ponta a ponta**, exatamente o que a demonstração ao
vivo de cada equipe precisa provar, mais do que em qualquer slide ou
narrativa sobre o sistema.

### Ciclo 3, 20h50 às 21h25

**Continuação das apresentações**, mesmo formato, até o fim da lista de
equipes. Se a lista terminar antes do tempo do ciclo, o tempo restante é
usado para perguntas adicionais e para a plateia revisar suas fichas de
avaliação por pares enquanto a memória da apresentação ainda está fresca.

**A rubrica de avaliação por pares.** Cada equipe da plateia preenche, para
cada equipe apresentada (exceto a própria), uma ficha curta com quatro
critérios, pontuados de 1 a 5, deliberadamente restritos ao que é observável
em dez minutos de apresentação ao vivo, e não ao código que só o professor
revisa com profundidade:

| Critério da ficha de pares | O que observa |
|---|---|
| Demonstração funcionando ao vivo | O pedido foi cadastrado, a baixa de remessa gerou ocorrência, tudo pela URL pública, sem falha nem improviso |
| Clareza da arquitetura distribuída | A equipe explicou com clareza por que os quatro serviços existem e como eles conversam entre si |
| Domínio da equipe sobre o próprio código | As respostas às perguntas da plateia mostraram que a equipe entende as próprias decisões, não só as executou |
| Organização e tempo da apresentação | A equipe usou os dez minutos com objetividade, sem estourar o tempo nem deixar de mostrar o essencial |

**Por que avaliação por pares, e não só nota do professor.** A turma passou
o semestre inteiro assistindo demonstrações umas das outras, nos exercícios
curtos dos Ciclos 1 e 2 de cada aula, desde a Aula 02. Pedir que a mesma
turma avalie a apresentação final de cada equipe aproveita esse hábito já
formado, e dá a cada aluno prática em julgar criticamente uma arquitetura
que não é a sua, uma habilidade tão relevante quanto construir a própria.

**Como a ficha de pares se conecta aos pesos do plano de ensino.** A média
das notas de pares, por equipe, alimenta especificamente o critério
"Apresentação na Aula 20", os 10% da tabela da seção 7.1. Os outros quatro
critérios da tabela, funcionalidade (30%), qualidade do código (25%),
modelagem e persistência (20%) e documentação (15%), continuam sendo
avaliados pelo professor diretamente sobre o repositório de cada equipe, não
pela votação da plateia, porque só o professor revisa o código com
profundidade suficiente para julgar esses quatro critérios com justiça. A
avaliação por pares participa apenas da fatia que ela está em posição de
julgar de verdade, o que a própria apresentação demonstra.

### Ciclo 4, 21h25 às 21h50

**Consolidação da avaliação por pares.** O professor recolhe as fichas
preenchidas por cada equipe da plateia, tabula a média por equipe
apresentada, e converte essa média na fatia de 10% de "Apresentação na Aula
20" da tabela de critérios.

**Confirmação do estado final do repositório.** Cada equipe confirma, com o
professor, que o fork está no estado que foi apresentado: `git log
--oneline` mostrando o histórico completo desde a Aula 01, e o `compose.yaml`
da Aula 19 subindo sem alteração de última hora não commitada.

**O que "repositório final entregue" significa, na prática.** Não é um
arquivo novo nem um pacote separado: é o próprio fork, no estado do commit
apresentado, com o histórico de vinte aulas visível em `git log`, cada
commit correspondendo a um entregável do dia, do `docs/ambiente.md` da Aula
01 até o `compose.yaml` da Aula 19. O critério "documentação do fork,
incluindo `docs/decisoes.md`" (15% da nota, seção 7.1 do
`PLANO_DE_ENSINO.md`) é avaliado sobre esse mesmo histórico: um
`docs/decisoes.md` que só ganhou linhas nas últimas duas aulas conta uma
história diferente de um que foi alimentado desde a Aula 02, e o professor
consegue ver a diferença direto no `git log`.

**Entregável do dia:** a apresentação de dez minutos feita ao vivo pela URL
pública, a ficha de avaliação por pares preenchida pela turma para cada
equipe, e o repositório final confirmado no estado apresentado. Critério de
aceitação: os quatro serviços respondendo durante a janela de apresentação da
própria equipe, e a ficha de pares recolhida ao final do Ciclo 4.

### Fechamento, 21h50 às 22h00

- Para a equipe que fez algum ajuste de última hora antes de subir ao
  "palco": `git add`, `git commit` em Conventional Commits, e `git push`, do
  mesmo jeito de todas as dezenove aulas anteriores.
- Como fechamento simbólico do fork inteiro, cada equipe marca o commit
  apresentado com uma tag: `git tag entrega-final -m "Entrega do projeto
  final, Rota Sul"`, seguido de `git push --tags`, um marco permanente no
  histórico, distinto de qualquer commit de aula.
- Não há prévia de próxima aula: este é o último encontro do semestre. A
  nota final segue a fórmula da seção 7 do `PLANO_DE_ENSINO.md`, checkpoints
  de laboratório (40%), prova (30%) e projeto final (30%), com aprovação a
  partir de 6,0.

### Referências

1. Prof. José Romualdo. **`PLANO_DE_ENSINO.md`**, seções 7 (Avaliação) e 7.1
   (Critérios do projeto final). Fonte primária desta aula, na ausência de
   capítulo do AVA correspondente, a mesma solução adotada pela Aula 01.
2. GitHub. **Documentação do GitHub Codespaces**, seção de ciclo de vida e
   hibernação por inatividade.
   <https://docs.github.com/en/codespaces/getting-started/the-codespace-lifecycle>
3. Docker. **Documentação do Docker Compose.**
   <https://docs.docker.com/compose/>

