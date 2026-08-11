# ADR-001: Stack Spring Boot no lugar de Jakarta EE clássico

**Data:** 11/08/2026
**Status:** Aceita
**Decisores:** Prof. José Romualdo

## Contexto

O material do AVA desta disciplina, os 18 capítulos de autoria do Prof. Paulo
Ricardo Batista Mesquita, é fortemente ancorado em Jakarta EE (antigo Java EE)
clássico: servidor de aplicação completo, Enterprise Java Beans, JPA por XML ou
por anotação sobre um container gerenciado, JavaServer Faces, RMI e SOAP.
Reproduzir esse conjunto em sala de aula exigiria instalar e configurar um
servidor de aplicação (WebLogic, JBoss ou GlassFish) em cada máquina da turma,
algo que o encontro de 150 minutos, sem laboratório remoto dedicado, não
comporta.

## Decisão

O laboratório da disciplina usa Java 21 com Spring Boot 3.x, e não Jakarta EE
clássico, apesar de o material do AVA ser Java EE.

## Motivações

Spring Boot cobre a ementa inteira com código que roda em qualquer máquina da
sala, sem instalar servidor de aplicação: o Tomcat embarcado sobe com
`java -jar`. Três camadas, inversão de controle, JPA e Hibernate, REST, e troca
de dados em XML e JSON são todos exercitados de verdade, não simulados. O
vocabulário dos capítulos do AVA é preservado, porque Spring Data JPA usa
Hibernate por baixo e fala a mesma linguagem de mapeamento objeto-relacional.

## Riscos conhecidos

O aluno que ler o capítulo do AVA vai encontrar anotações e classes que não
aparecem em nenhum laboratório da disciplina, `@Stateless`, `@Remote`, `@Local`
e `@ManagedBean` entre elas. Sem contextualização, isso pode passar a impressão
de que o material do AVA está desatualizado ou de que o laboratório ignora o
que o capítulo ensina.

Mitigação, implementada em `PLANEJAMENTO_AULA_A_AULA.md`: as Aulas 16 e 18
trazem comparação lado a lado entre o modelo Java EE do capítulo e o
equivalente Spring construído no laboratório da Rota Sul.

Na Aula 16 (Enterprise Java Beans), o Ciclo 1 projeta `InterfaceHello` e
`BeanHello` do capítulo, anotados `@Local` e `@Stateless`, ao lado do esqueleto
de `RemessaService`, um `@Service` do Spring sem interface de negócios
separada nem anotação de bean de sessão, com uma nota explícita ao professor
sobre por que a indústria migrou de um modelo para o outro. O Ciclo 2 compara
o serviço declarativo de transação do EJB, citado pelo capítulo mas não
demonstrado em código, com `@Transactional` do Spring, aplicado ao vivo em
`RemessaService.baixarRemessa`.

Na Aula 18 (Hibernate e JavaServer Faces), o Ciclo 1 projeta a Listagem 3 do
capítulo, um `hibernate-mapping` em XML, ao lado da classe `Pedido` anotada com
`@Entity`, `@Table`, `@Id` e `@Column`. O Ciclo 2 projeta o `AbstractFacade<T>`
do capítulo (Listagem 7), a classe genérica que reimplementa `create`, `find` e
`findAll` à mão sobre um `EntityManager`, ao lado de
`JpaRepository<Remessa, Long>`, uma interface vazia que entrega os mesmos
métodos prontos. O fechamento da aula nomeia explicitamente as quatro
comparações honestas do Módulo 4: memória contra JDBC contra JPA, EJB contra
`@Transactional`, JSF contra Thymeleaf (fixado desde a Aula 13) e Hibernate por
trás de tudo desde a Aula 01. Nenhuma dessas comparações deprecia o que os
capítulos ensinam: o vocabulário de gerenciamento de ciclo de vida, injeção de
dependência e serviço declarativo é o mesmo, com um motor diferente por baixo.

## Consequências

### Positivas

- A turma inteira exercita de verdade os conceitos centrais da ementa
  (componentes, transação declarativa, mapeamento objeto-relacional,
  apresentação server-side) sem depender de infraestrutura pesada de servidor
  de aplicação.
- A leitura do capítulo do AVA continua sendo necessária e relevante, porque
  as Aulas 16 e 18 constroem pontes explícitas entre o texto e o laboratório,
  em vez de ignorar o descompasso.

### Negativas

- Nenhuma linha de `@Stateless`, `@Remote`, `@Local` ou JSF é escrita pela
  turma em nenhum momento do semestre: o contato com Jakarta EE clássico fica
  inteiramente na leitura e na comparação, nunca na prática.
- A comparação lado a lado depende de duas aulas específicas (16 e 18)
  preservarem essa ponte; se o roteiro dessas aulas mudar no futuro sem manter
  a comparação, o risco descrito acima volta a existir sem mitigação.

## ADRs relacionadas

- ADR-005: mapeamento 1 para 1 com a ordem do AVA
