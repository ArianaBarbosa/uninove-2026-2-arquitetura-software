# ADR-009: Composição do repositório-esqueleto da Rota Sul

**Data:** 12/08/2026
**Status:** Aceita
**Decisores:** Prof. José Romualdo

## Contexto

A ADR-004 decidiu que o case Rota Sul é resolvido por um único
repositório-esqueleto, `josercf/uninove-2026-2-rota-sul`, forkado na Aula 01 e
evoluído até a Aula 20. O que ela não decidiu é **o que existe dentro desse
repositório no momento do fork**.

Enquanto o repositório não existiu, quatorze aulas foram construídas
referenciando-o: o Ciclo 1 da Aula 01 manda o professor abrir a página do
repositório no projetor e percorrer a estrutura, o Ciclo 3 manda a turma
forkar, o Ciclo 4 manda rodar `./mvnw spring-boot:run`, e o kit da Aula 08
inspeciona o `MANIFEST.MF` do jar gerado. Cada uma dessas referências fixou,
sem que houvesse repositório, uma exigência sobre o conteúdo do esqueleto. O
kit da Aula 01 chegou a trazer um aviso dizendo que o link de fork devolveria
404 até o professor publicar o repositório.

Construir o esqueleto, portanto, não foi um projeto novo: foi coletar
exigências já espalhadas pelo acervo e verificar que um único repositório as
satisfaz todas ao mesmo tempo. Três delas se contradiziam com a saída padrão
do Spring Initializr, que é a fonte óbvia de um esqueleto Spring Boot.

## Decisão

O esqueleto é um projeto Spring Boot 3.3.4 sobre Java 21, artefato
`br.uni9:rota-sul:0.0.1-SNAPSHOT`, com nove arquivos versionados, uma única
classe de código, `spring-boot-starter-web` e `spring-boot-starter-test` desde
o fork, e **nenhuma classe de teste**.

Estrutura completa:

```
uninove-2026-2-rota-sul/
├── .gitignore                    com .env na primeira regra
├── .mvn/wrapper/maven-wrapper.properties
├── README.md
├── docs/.gitkeep                 o docs/ vazio que a Aula 01 mostra no projetor
├── mvnw, mvnw.cmd
├── pom.xml
└── src/
    ├── main/java/br/uni9/rotasul/RotaSulApplication.java
    └── main/resources/application.properties      vazio
```

## Motivações

- **Spring Boot 3.3.4 fixado à mão, não o default do Initializr.** Os
  gabaritos das Aulas 06 a 14 declaram, cada um no seu rodapé de verificação,
  que foram conferidos contra `spring-boot-starter-parent` 3.3.4 com Java 21.
  O `start.spring.io` hoje só oferece a linha 4.x, então gerar o esqueleto por
  ele entregaria um projeto contra o qual nenhum gabarito do acervo foi
  verificado. A versão é escrita no `pom.xml` deliberadamente.

- **`spring-boot-starter-web` e `spring-boot-starter-test` desde o fork.** O
  kit da Aula 06 afirma "nenhuma dependência nova no `pom.xml`:
  `spring-boot-starter-web`, que traz o Tomcat", e o da Aula 07 afirma o mesmo
  dos dois starters, "presentes desde" o início. Sem o starter web, o passo
  3.6 da Aula 01 também não teria o que mostrar: a aplicação encerraria em vez
  de subir um servidor, e a página de erro padrão do Spring Boot, que é o
  critério de sucesso do passo, nunca apareceria.

- **Nenhuma classe de teste, apesar de o Initializr sempre gerar uma.** O
  critério de aceitação do kit da Aula 07 é "seis execuções verdes" em
  `./mvnw test`, contadas nominalmente: dois testes de `PedidoServicePadraoTest`
  mais dois da suíte abstrata rodando duas vezes. Um `RotaSulApplicationTests`
  com `contextLoads` herdado do Initializr faria sete, e o aluno que contasse
  concluiria que errou o laboratório. O mesmo vale para o kit da Aula 06, cujo
  critério é `./mvnw test` rodando `PedidoServiceTest` com dois casos. O
  esqueleto entrega o `spring-boot-starter-test` no classpath e deixa a
  primeira classe de teste para a Aula 06 escrever.

- **Uma classe só em `src/main`.** O deck da Aula 06 diz na tela "hoje existe
  uma classe só, `RotaSulApplication`. Ao final da aula existirão quatro, em
  pacotes diferentes". Qualquer classe de conveniência acrescentada ao
  esqueleto desmentiria o slide.

- **`docs/` versionado e vazio.** O roteiro do Ciclo 1 da Aula 01 manda mostrar
  "o `docs/` vazio" na projeção, e o entregável do dia é `docs/ambiente.md`.
  Git não versiona diretório vazio, então o diretório existe por um
  `.gitkeep`, que é o menor arquivo que satisfaz as duas coisas.

- **`.env` como primeira regra do `.gitignore`.** O passo 3.7 da Aula 01 manda
  o aluno abrir o `.gitignore` e confirmar que `.env` está listado, e o
  critério de aceitação confere isso. A regra aparece no topo do arquivo, com
  o comentário que explica o porquê, para que o passo seja de leitura e não de
  busca.

- **Maven wrapper no modo `only-script`.** O `wrapperVersion=3.3.4` com
  `distributionType=only-script` não versiona `maven-wrapper.jar`: o script
  baixa o Maven na primeira execução. Evita um binário no repositório que a
  turma inteira forka, e o `./mvnw` continua funcionando como o kit da Aula 01
  promete.

## Riscos conhecidos

- **O 3.3.4 envelhece.** A versão está fixada no `pom.xml` do esqueleto e
  citada no rodapé de verificação de nove kits. Subir a versão do Spring Boot
  exige reverificar os gabaritos das Aulas 06 a 20, não só editar o `pom.xml`.
  - **Mitigação:** a versão está registrada no `README.md` do esqueleto, na
    tabela de contrato técnico, para que quem a mudar saiba que está mudando
    um contrato e não uma dependência.

- **A ausência de classe de teste parece descuido.** Um aluno ou um monitor
  que conheça o Initializr pode acrescentar um `RotaSulApplicationTests` por
  achar que faltou, e quebrar a contagem de seis execuções da Aula 07.
  - **Mitigação:** esta ADR é o registro do motivo. O Javadoc de
    `RotaSulApplication` também diz que ela é a única classe do esqueleto e
    que o primeiro código de aplicação entra na Aula 06.

- **Erro no esqueleto se propaga por vinte aulas.** É a mesma consequência
  negativa já registrada na ADR-004, agravada aqui porque o esqueleto está
  forkado nas contas dos alunos: corrigir o original não corrige os forks já
  criados.
  - **Mitigação:** o esqueleto foi verificado antes do push com JDK 21.0.12,
    conferindo `./mvnw clean package`, o `MANIFEST.MF` do jar contra o que o
    kit da Aula 08 exibe (`Implementation-Title: rota-sul` e
    `Start-Class: br.uni9.rotasul.RotaSulApplication`),
    `./mvnw spring-boot:run` e a página de erro padrão do Spring Boot na raiz.

## Consequências

### Positivas

- O passo 3.4 do kit da Aula 01 deixa de devolver 404, e o aviso que o
  antecipava saiu do kit.
- As quatorze aulas já construídas passam a ter o repositório que citam, e as
  seis restantes têm onde aterrissar.
- O `README.md` do esqueleto concentra o contrato técnico do semestre num
  lugar que o aluno visita no primeiro encontro e mantém no próprio fork.

### Negativas

- O esqueleto duplica, no seu `README.md`, informação que também vive em
  `PLANO_DE_ENSINO.md` e em `PLANEJAMENTO_AULA_A_AULA.md`. São dois
  repositórios distintos, então a duplicação é manual e pode divergir, como a
  ADR-003 já registra para os validadores e o tema.
- A versão do Spring Boot passa a estar declarada em dois repositórios, e
  atualizá-la exige tocar os dois.

## ADRs relacionadas

- ADR-004: o case Rota Sul e o repositório-esqueleto único, que decidiu que
  este repositório existe.
- ADR-001: stack Spring Boot no lugar de Jakarta EE, que decidiu o framework.
- ADR-006: PlantUML com proxy, que é a razão de o `README.md` do esqueleto
  exigir que o fork do aluno seja público.
