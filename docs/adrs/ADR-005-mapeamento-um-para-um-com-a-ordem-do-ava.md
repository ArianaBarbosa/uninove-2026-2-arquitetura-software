# ADR-005: Mapeamento 1 para 1 com a ordem do AVA

**Data:** 11/08/2026
**Status:** Aceita
**Decisores:** Prof. José Romualdo

## Contexto

O conteúdo da disciplina vem de 18 capítulos em PDF, extraídos do AVA da
Uninove, de autoria do Prof. Paulo Ricardo Batista Mesquita. A disciplina tem
20 encontros. A alternativa avaliada foi reordenar os capítulos por coerência
conceitual, por exemplo puxando o capítulo 04 (arquitetura de software) para
perto do início do semestre, antes dos capítulos que tratam de padrões e
frameworks.

## Decisão

As 20 aulas do semestre são mapeadas um para um com a ordem dos 18 capítulos
do AVA, a Aula 01 abrindo o semestre sem capítulo correspondente, as Aulas 02
a 19 cobrindo os capítulos 01 a 18 na ordem em que foram escritos, e a Aula 20
apresentando o projeto final sem capítulo correspondente.

## Motivações

O mapeamento 1 para 1 preserva a rastreabilidade entre cada aula e o capítulo
correspondente do AVA, que o aluno acessa em paralelo ao encontro presencial.
Reordenar os capítulos ganharia coerência conceitual pontual, mas perderia
esse casamento direto: o aluno que lê o capítulo N do AVA numa semana
qualquer do semestre sempre encontra, na aula da mesma semana, o assunto
daquele capítulo, sem precisar consultar uma tabela de correspondência à
parte.

## Riscos conhecidos

Manter a ordem do AVA em vez de reordenar por coerência conceitual assume
duas consequências:

- **A ordem do AVA trata de padrões e frameworks (capítulo 01, Aula 02) antes
  de definir formalmente arquitetura de software (capítulo 04, Aula 05).** Um
  aluno que seguisse a ordem lógica esperaria a definição do conceito antes
  do vocabulário que depende dele.
  - **Mitigação:** a espiral de conteúdo resolve a lacuna sem reordenar. A
    Aula 02 apresenta o vocabulário de padrões e frameworks em nível de
    panorama, sem exigir a definição formal ainda, e a Aula 05 retoma e
    formaliza o conceito de arquitetura de software, fechando o que a Aula 02
    deixou em aberto.
- **As Aulas 16 e 18 tratam de EJB e JSF (capítulos 15 e 17) enquanto a stack
  do laboratório é Spring Boot.** Isso reproduz, num ponto diferente do
  semestre, o mesmo descompasso entre material do AVA e stack de laboratório
  já registrado na ADR-001.
  - **Mitigação:** a mesma da ADR-001, comparação lado a lado nas Aulas 16 e
    18 entre o modelo Java EE do capítulo e o equivalente Spring construído
    na Rota Sul, sem depreciar o que os capítulos ensinam.

## Consequências

### Positivas

- Rastreabilidade completa e sem exceção entre aula e capítulo: qualquer
  aluno ou professor consegue apontar, para qualquer uma das 20 aulas,
  exatamente qual capítulo do AVA ela cobre, ou a ausência de capítulo, nas
  Aulas 01 e 20.
- Nenhuma decisão editorial de reordenação precisa ser justificada ou
  revisitada ao longo do semestre; a ordem segue o material institucional tal
  como ele existe.

### Negativas

- A progressão conceitual não é a ideal do ponto de vista puramente
  didático: dois pontos do semestre (Aula 02 e Aulas 16/18) exigem mitigação
  explícita porque a ordem do AVA não é a ordem que um currículo desenhado do
  zero escolheria.
- Qualquer mudança futura na ordem dos capítulos do AVA, feita pelo autor
  original fora do controle desta disciplina, exigiria reavaliar o
  mapeamento inteiro das 20 aulas.

## ADRs relacionadas

- ADR-001: stack Spring Boot no lugar de Jakarta EE clássico
- ADR-004: o case Rota Sul e o repositório-esqueleto único
