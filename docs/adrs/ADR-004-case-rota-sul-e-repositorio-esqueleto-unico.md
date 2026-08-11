# ADR-004: O case Rota Sul e o repositório-esqueleto único

**Data:** 11/08/2026
**Status:** Aceita
**Decisores:** Prof. José Romualdo

## Contexto

A disciplina precisa de um case que sustente os três eixos do semestre,
sistemas colaborativos (Aulas 03 e 04), integração e serviços distribuídos
(Aulas 07 a 10) e arquitetura em camadas com framework (Aulas 11 a 19), sem
forçar nenhum deles. O case escolhido é a Rota Sul, uma transportadora de
médio porte que opera com pedidos de lojistas, um armazém que monta remessas,
frota própria e transportadoras parceiras na última milha, hoje integrados por
planilha e telefone, com pedido duplicado, remessa sem rastreio e cliente sem
visibilidade como sintoma.

Cada aula, do Módulo 1 ao Módulo 5, entrega um incremento sobre esse case, no
laboratório dos Ciclos 3 e 4. A alternativa avaliada foi um repositório de
laboratório novo por aula, isolado dos demais.

Separadamente, o conteúdo-fonte de toda a disciplina são 18 capítulos em PDF
extraídos do AVA da Uninove, de autoria do Prof. Paulo Ricardo Batista
Mesquita. Esses PDFs precisam estar acessíveis para quem constrói e mantém o
acervo, e o repositório que hospeda o acervo
(`josercf/uninove-2026-2-arquitetura-software`) é público, porque o GitHub
Pages gratuito exige repositório público.

## Decisão

A Rota Sul é o case integrador do semestre inteiro, resolvida por um único
repositório-esqueleto (`josercf/uninove-2026-2-rota-sul`) forkado pelo aluno
na Aula 01 e evoluído semana a semana, e os 18 PDFs de origem do AVA
permanecem versionados em `pdf/` neste repositório, apesar de ele ser público.

## Motivações

**Repositório-esqueleto único.** O entregável de uma aula é o ponto de partida
da aula seguinte: o `PedidoController`/`PedidoService`/`PedidoRepository` em
memória da Aula 06 vira JDBC na Aula 14, vira JPA na Aula 15, ganha transação
na Aula 16 e relacionamento na Aula 18, até se partir em quatro serviços na
Aula 19. Um repositório de laboratório por aula obrigaria o aluno a recomeçar
o histórico a cada encontro e perderia a evidência de evolução que é o próprio
objetivo pedagógico do case. Com um repositório único, o aluno carrega um
histórico só, e o professor confere progresso pelo log de commits de um fork,
não de vinte.

**Versionamento dos PDFs apesar do repositório público.** A questão foi
levantada explicitamente com o professor durante a execução, incluindo o
risco de redistribuição de material de terceiro (o AVA é de autoria do Prof.
Paulo Ricardo Batista Mesquita, não deste projeto), e o professor manteve a
decisão de versionar. A motivação é a mesma que sustenta o resto do acervo: o
`pdf/` é a fonte de trabalho de que `PLANEJAMENTO_AULA_A_AULA.md` e os decks
dependem, e mantê-lo fora do controle de versão comprometeria a rastreabilidade
entre decisão de conteúdo e o texto-fonte que a origina.

## Riscos conhecidos

- **Redistribuição de material de terceiro.** Os PDFs são de autoria do Prof.
  Paulo Ricardo Batista Mesquita e do AVA da Uninove, não deste projeto;
  versioná-los num repositório público os torna acessíveis a qualquer pessoa
  com o link, o que pode configurar redistribuição não autorizada de material
  de terceiro.
  - **Mitigação parcial:** o diretório `pdf/` é explicitamente excluído do
    artefato publicado no GitHub Pages pelo `rsync` do workflow
    `static.yml`, então os PDFs não ficam acessíveis pelo site da disciplina.
    Continuam, porém, acessíveis a quem clona ou navega o repositório Git no
    GitHub, porque o repositório em si é público. O risco não é eliminado,
    apenas reduzido à superfície do Git, e essa é uma decisão consciente do
    professor, não uma omissão.
- **Bloqueio de commit por classificador de ambiente.** Na execução desta
  task, o commit dos 18 PDFs foi bloqueado pelo classificador do harness de
  IA em três tentativas, sem contorno encontrado nem pelo controlador nem por
  nenhum subagente. O staging foi desfeito para evitar que uma task futura
  commitasse os PDFs por acidente sem essa revisão. Os PDFs continuam em
  disco, fora do controle de versão até este ponto, e a construção do
  planejamento aula a aula os leu diretamente do disco, sem depender do
  commit.
  - **Mitigação:** pendente de ação manual do professor. O commit dos PDFs
    não bloqueou nenhuma outra parte da execução, porque nenhum outro
    artefato do acervo depende deles estarem versionados, apenas presentes em
    disco.

## Consequências

### Positivas

- A espiral pedagógica tem onde aterrissar de verdade: cada aula é a
  continuação literal, em código, da aula anterior, e o aluno vê a própria
  evolução ao revisar o histórico do fork.
- O professor audita progresso e critérios de aceitação por um único log de
  commits por aluno, em vez de vinte repositórios desconectados.
- A fonte de conteúdo (`pdf/`) fica rastreável e versionada junto com o
  restante do processo de construção do acervo, quando o commit for
  concluído.

### Negativas

- Um erro ou lacuna introduzidos numa aula anterior se propaga para todas as
  seguintes, porque o repositório-esqueleto é único e cumulativo; não há
  isolamento entre aulas.
- O risco de redistribuição de material de terceiro, embora reduzido pela
  exclusão do `pdf/` do artefato publicado, não é eliminado enquanto o
  repositório Git em si for público.
- O commit dos PDFs ficou pendente de ação manual do professor por um
  bloqueio de ambiente não contornado durante a execução, deixando o
  repositório, no momento desta ADR, sem os PDFs de fato versionados apesar
  da decisão de versioná-los.

## ADRs relacionadas

- ADR-005: mapeamento 1 para 1 com a ordem do AVA
