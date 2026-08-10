# Plano de Ensino

## 1. Identificação

| Campo | Valor |
|---|---|
| Disciplina | Arquitetura de Software |
| Instituição | Uninove, Universidade Nove de Julho |
| Nível | Graduação |
| Semestre | 2026.2 |
| Professor | José Romualdo |
| Contato | <jose.romualdo@uni9.pro.br> |
| Turmas | Uma turma |
| Horário | 19h30 às 22h00 |
| Encontros | 20 encontros de 150 minutos cada |
| Carga horária total | 60 horas-aula |
| Repositório do acervo | <https://github.com/josercf/uninove-2026-2-arquitetura-software> |
| Repositório-esqueleto do case | <https://github.com/josercf/uninove-2026-2-rota-sul> |

A carga horária de **60 horas-aula** vem da conta institucional: a hora-aula da
Uninove tem 50 minutos, cada encontro de 150 minutos corridos equivale a 3
horas-aula, e 3 horas-aula vezes 20 encontros dão 60 horas-aula.

A disciplina tem uma turma só, e as datas dos 20 encontros não estão definidas
neste plano. O cronograma da seção 6 lista a sequência das aulas, sem coluna de
data.

## 2. Ementa

Evolução do desenvolvimento de software e origem dos padrões de projeto e dos
frameworks. Sistemas colaborativos e o modelo 3C, comunicação, coordenação e
cooperação. Arquitetura de sistemas colaborativos. Arquitetura de software e
sua representação em UML, com diagramas de componentes, implantação e classes.
Arquitetura em três camadas e a evolução do padrão MVC. Arquitetura orientada a
serviços, SOA. Servidores de aplicação e a plataforma Java EE. Metadados para
troca de dados em XML e JSON. Comunicação remota com RMI, SOAP e REST.
Catálogo de design patterns. Anatomia de frameworks e inversão de controle.
Frameworks para aplicativos web. Frameworks para gerenciamento de dados. API de
persistência Java, JPA. Enterprise Java Beans. Hibernate e JavaServer Faces.
Montagem de uma aplicação distribuída em camadas.

O conteúdo segue os 18 capítulos do Ambiente Virtual de Aprendizagem da
Uninove, que apresentam esses temas sobre a plataforma Java EE clássica:
servidor de aplicação, EJB, JSF e RMI. O laboratório da disciplina pratica os
mesmos conceitos sobre uma stack moderna, Java 21 com Spring Boot 3.x e Spring
Data JPA sobre Hibernate, de modo que o aluno reconhece o vocabulário do AVA e
constrói com as ferramentas usadas hoje pela indústria.

## 3. Objetivos gerais

Ao final da disciplina, o aluno deve ser capaz de:

1. Explicar a evolução do desenvolvimento de software e a origem dos padrões
   de projeto e dos frameworks.
2. Distinguir sistemas colaborativos segundo o modelo 3C, separando
   comunicação, coordenação e cooperação em um cenário real.
3. Representar uma arquitetura de software em UML, com diagramas de
   componentes, de implantação e de classes.
4. Projetar aplicações em três camadas segundo o padrão MVC.
5. Diferenciar arquitetura orientada a serviços e as formas de comunicação
   remota entre sistemas, RMI, SOAP e REST.
6. Modelar a troca de dados estruturados entre sistemas em XML e em JSON.
7. Aplicar um catálogo de design patterns e o princípio de inversão de
   controle na construção e no uso de frameworks.
8. Implementar persistência de dados com JPA sobre Hibernate, usando Spring
   Data JPA.
9. Construir e integrar uma aplicação distribuída em camadas, com Spring
   Boot, cobrindo apresentação, negócio e persistência.

## 4. Metodologia

A disciplina **não usa sala de aula invertida**. Cada encontro é
autossuficiente: tudo o que o aluno precisa para acompanhar chega dentro da
própria aula. Não há atividade prévia obrigatória, não há leitura antecipada e
nenhum conteúdo é cobrado antes de ter sido apresentado em sala.

### 4.1 A estrutura do encontro

Os 150 minutos são organizados em quatro ciclos, mais um quiz de fixação e um
fechamento. Não há intervalo formal: a própria troca de ciclo funciona como
respiro.

```
19h30 às 20h05  Ciclo 1: conceito, demonstração, exercício curto (35 min)
20h05 às 20h40  Ciclo 2: conceito, demonstração, exercício curto (35 min)
20h40 às 20h50  Quiz de fixação (10 min)
20h50 às 21h25  Ciclo 3: laboratório guiado, parte 1 (35 min)
21h25 às 21h50  Ciclo 4: laboratório, parte 2, e entregável (25 min)
21h50 às 22h00  Fechamento, commit e prévia da próxima aula (10 min)
```

Os ciclos 1 e 2 seguem sempre o mesmo ritmo interno: o professor apresenta o
conceito, demonstra e o aluno reproduz num exercício curto, ainda dentro do
ciclo. Os ciclos 3 e 4 são laboratório: o aluno constrói uma etapa do case Rota
Sul, com o professor circulando pela sala. O entregável nasce dentro do ciclo
4, não fora da aula.

### 4.2 A espiral de conteúdo

O conteúdo avança em espiral, não em blocos isolados. Toda aula a partir da
Aula 02 abre com uma recapitulação curta da anterior e acrescenta uma camada
sobre o que já existe. O entregável de uma aula é o ponto de partida da
seguinte, de modo que ninguém começa do zero em nenhum encontro. Nas Aulas 01 a
05, o entregável dos ciclos 3 e 4 não é código de aplicação, é ambiente,
inventário de decisões e diagrama UML, versionados no fork do repositório-
esqueleto; o primeiro código de aplicação entra na Aula 06.

## 5. O case Rota Sul

Todo o semestre é construído em torno de um único sistema, a **Rota Sul**, uma
transportadora fictícia de médio porte. Hoje a Rota Sul opera com pedidos
vindos de lojistas, um armazém que monta remessas, frota própria na rota
principal e transportadoras parceiras na última milha, cada peça com seu
próprio sistema, integrada por planilha e telefone. O resultado é pedido
duplicado, remessa sem rastreio, parceiro que não recebe a carga e cliente que
liga para o atendimento porque ninguém sabe onde está o volume.

O case sustenta os três eixos da disciplina:

- **Colaborativo**, nas Aulas 03 e 04: expedidor, motorista, atendente e
  parceiro coordenam a mesma entrega, e o modelo 3C tem onde aterrissar.
- **Distribuído e integrado**, nas Aulas 07 a 10: serviços separados
  conversando por REST, um parceiro legado que só aceita SOAP com XML, e
  contratos de dados explícitos.
- **Em camadas com framework**, nas Aulas 11 a 19: apresentação, negócio e
  persistência, com inversão de controle e ORM reais.

**Atores:** lojista, expedidor, motorista, atendente e transportadora
parceira. **Entidades principais:** `Cliente`, `Pedido`, `Remessa`, `Volume`,
`Rota`, `Veiculo`, `Motorista`, `Ocorrencia`, `Parceiro`.

O aluno forka o repositório-esqueleto na Aula 01 e evolui esse mesmo fork
semana a semana. O primeiro código de aplicação entra na Aula 06, sobre Java
21, Maven, Spring Boot 3.x, Spring Data JPA sobre Hibernate, MySQL 8.4 com
Flyway, Thymeleaf, springdoc-openapi, Spring Web Services para o parceiro SOAP
e testes com JUnit 5 e Testcontainers. Na Aula 19, o case chega à sua forma
distribuída, com quatro processos subindo por um único `compose.yaml`:
`pedidos-service`, `expedicao-service`, `rastreamento-service` e `portal-web`.
A Aula 20 é a apresentação do projeto final, com o ambiente publicado em
GitHub Codespaces.

## 6. Cronograma

A tabela mapeia 1 para 1 com a ordem do Ambiente Virtual de Aprendizagem: a
Aula 01 abre o semestre, as Aulas 02 a 19 cobrem os capítulos 01 a 18 do AVA
na ordem em que foram escritos, e a Aula 20 é a apresentação do projeto final.

| Aula | Módulo | Título | Capítulo do AVA |
|---|---|---|---|
| 01 | M1 Fundamentos e sistemas colaborativos | Abertura do semestre e o problema da arquitetura | sem capítulo |
| 02 | M1 Fundamentos e sistemas colaborativos | Padrões de projeto e frameworks: origem e distinção | 01 |
| 03 | M1 Fundamentos e sistemas colaborativos | Sistemas colaborativos | 02 |
| 04 | M1 Fundamentos e sistemas colaborativos | Arquitetura de sistemas colaborativos | 03 |
| 05 | M1 Fundamentos e sistemas colaborativos | Arquitetura de software e representação em UML | 04 |
| 06 | M1 Fundamentos e sistemas colaborativos | Arquitetura em 3 camadas e a evolução do MVC | 05 |
| 07 | M2 Integração e serviços distribuídos | Arquitetura orientada a serviços, SOA | 06 |
| 08 | M2 Integração e serviços distribuídos | Servidores de aplicação e a plataforma Java EE | 07 |
| 09 | M2 Integração e serviços distribuídos | Metadados para troca de dados: XML e JSON | 08 |
| 10 | M2 Integração e serviços distribuídos | Objetos remotos: RMI, SOAP e REST | 09 |
| 11 | M3 Padrões e frameworks | Design Patterns | 10 |
| 12 | M3 Padrões e frameworks | Frameworks: anatomia e inversão de controle | 11 |
| 13 | M3 Padrões e frameworks | Frameworks para aplicativos web | 12 |
| 14 | M3 Padrões e frameworks | Frameworks para gerenciamento de dados | 13 |
| 15 | M4 Persistência e componentes | API de persistência Java, JPA | 14 |
| 16 | M4 Persistência e componentes | Enterprise Java Beans | 15 |
| 17 | M4 Persistência e componentes | Frameworks para software em 3 camadas | 16 |
| 18 | M4 Persistência e componentes | Hibernate e JavaServer Faces | 17 |
| 19 | M5 Projeto final | Montagem da aplicação distribuída | 18 |
| 20 | M5 Projeto final | Apresentação do projeto final | sem capítulo |

**Duas consequências assumidas nessa ordem**, herdadas do AVA: a Aula 02 trata
de padrões e frameworks antes de a Aula 05 formalizar o conceito de arquitetura
de software, resolvido pela espiral (a Aula 02 apresenta o vocabulário em nível
de panorama). E as Aulas 16 e 18 trazem EJB e JSF como conteúdo conceitual e
histórico, comparado lado a lado com o equivalente Spring que o laboratório
constrói de fato; Hibernate não tem esse problema, porque é o provedor JPA por
baixo do Spring Data e roda de verdade no laboratório.

## 7. Avaliação

| Instrumento | Peso |
|---|---|
| Checkpoints de laboratório | 40 |
| Prova | 30 |
| Projeto final | 30 |
| **Total** | **100** |

Os **checkpoints de laboratório** são os entregáveis produzidos nos ciclos 3 e
4 de cada encontro, avaliados ao longo do semestre pelos critérios de
aceitação descritos no kit de cada aula. A **prova** cobre o conteúdo teórico
da ementa. O **projeto final** é a Rota Sul construída ao longo do semestre,
na sua forma distribuída, apresentada na Aula 20.

```
Nota final = (checkpoints x 0,40) + (prova x 0,30) + (projeto final x 0,30)
```

Aprovação com **nota final maior ou igual a 6,0**, seguindo o critério
institucional da Uninove.

### 7.1 Critérios do projeto final

| Critério | Peso |
|---|---|
| Funcionalidade dos quatro serviços | 30% |
| Qualidade do código e da arquitetura em camadas | 25% |
| Modelagem e persistência de dados | 20% |
| Documentação do fork, incluindo `docs/decisoes.md` | 15% |
| Apresentação na Aula 20 | 10% |

**Forma de entrega:** o fork do repositório-esqueleto no GitHub, com histórico
de commits do próprio aluno, publicado via Docker Compose em GitHub
Codespaces com a porta encaminhada em modo público.

## 8. Bibliografia

### 8.1 Capítulos do AVA

Os 18 capítulos abaixo são a fonte primária do conteúdo teórico da disciplina,
de autoria do **Prof. Paulo Ricardo Batista Mesquita**, publicados no Ambiente
Virtual de Aprendizagem da Uninove.

1. MESQUITA, Paulo Ricardo Batista. Capítulo 01: Padrões de projeto e
   frameworks: origem e distinção. Arquitetura de Software. AVA, Uninove.
2. MESQUITA, Paulo Ricardo Batista. Capítulo 02: Sistemas colaborativos.
   Arquitetura de Software. AVA, Uninove.
3. MESQUITA, Paulo Ricardo Batista. Capítulo 03: Arquitetura de sistemas
   colaborativos. Arquitetura de Software. AVA, Uninove.
4. MESQUITA, Paulo Ricardo Batista. Capítulo 04: Arquitetura de software e
   representação em UML. Arquitetura de Software. AVA, Uninove.
5. MESQUITA, Paulo Ricardo Batista. Capítulo 05: Arquitetura em 3 camadas e a
   evolução do MVC. Arquitetura de Software. AVA, Uninove.
6. MESQUITA, Paulo Ricardo Batista. Capítulo 06: Arquitetura orientada a
   serviços, SOA. Arquitetura de Software. AVA, Uninove.
7. MESQUITA, Paulo Ricardo Batista. Capítulo 07: Servidores de aplicação e a
   plataforma Java EE. Arquitetura de Software. AVA, Uninove.
8. MESQUITA, Paulo Ricardo Batista. Capítulo 08: Metadados para troca de
   dados: XML e JSON. Arquitetura de Software. AVA, Uninove.
9. MESQUITA, Paulo Ricardo Batista. Capítulo 09: Objetos remotos: RMI, SOAP e
   REST. Arquitetura de Software. AVA, Uninove.
10. MESQUITA, Paulo Ricardo Batista. Capítulo 10: Design Patterns. Arquitetura
    de Software. AVA, Uninove.
11. MESQUITA, Paulo Ricardo Batista. Capítulo 11: Frameworks: anatomia e
    inversão de controle. Arquitetura de Software. AVA, Uninove.
12. MESQUITA, Paulo Ricardo Batista. Capítulo 12: Frameworks para aplicativos
    web. Arquitetura de Software. AVA, Uninove.
13. MESQUITA, Paulo Ricardo Batista. Capítulo 13: Frameworks para
    gerenciamento de dados. Arquitetura de Software. AVA, Uninove.
14. MESQUITA, Paulo Ricardo Batista. Capítulo 14: API de persistência Java,
    JPA. Arquitetura de Software. AVA, Uninove.
15. MESQUITA, Paulo Ricardo Batista. Capítulo 15: Enterprise Java Beans.
    Arquitetura de Software. AVA, Uninove.
16. MESQUITA, Paulo Ricardo Batista. Capítulo 16: Frameworks para software em
    3 camadas. Arquitetura de Software. AVA, Uninove.
17. MESQUITA, Paulo Ricardo Batista. Capítulo 17: Hibernate e JavaServer
    Faces. Arquitetura de Software. AVA, Uninove.
18. MESQUITA, Paulo Ricardo Batista. Capítulo 18: Montagem da aplicação
    distribuída. Arquitetura de Software. AVA, Uninove.

### 8.2 Complementar

19. GAMMA, Erich; HELM, Richard; JOHNSON, Ralph; VLISSIDES, John. **Padrões de
    Projeto: Soluções Reutilizáveis de Software Orientado a Objetos.**
20. FOWLER, Martin. **Patterns of Enterprise Application Architecture.**
21. Spring. **Documentação do Spring Boot.**
    <https://docs.spring.io/spring-boot/index.html>
22. Spring. **Documentação do Spring Data JPA.**
    <https://docs.spring.io/spring-data/jpa/reference/>
23. Hibernate. **Hibernate ORM Documentation.**
    <https://hibernate.org/orm/documentation/>
24. Oracle. **MySQL Reference Manual.** <https://dev.mysql.com/doc/>

---

Prof. José Romualdo, Uninove, 2026.2.
