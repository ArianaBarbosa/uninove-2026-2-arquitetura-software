# ADR-002: Sem resolução de turma e sem data no deck

**Data:** 11/08/2026
**Status:** Aceita
**Decisores:** Prof. José Romualdo

## Contexto

A disciplina Arquitetura de Software, 2026.2, tem uma turma só e, no momento da
construção do acervo, nenhum calendário de encontros definido. O acervo irmão
de Desenvolvimento Web, que serve de padrão estrutural para este, resolve
turma no cliente: um módulo `assets/js/turmas.js`, um seletor no portal, e a
data do encontro escrita no slide de título de cada deck, validada contra o
número no nome do arquivo.

## Decisão

Este acervo não tem módulo de resolução de turma, o portal não tem seletor de
turma, e nenhum deck exibe data.

## Motivações

Com uma turma só, não existe nada para o aluno selecionar: um seletor de turma
sem opção real é interface morta. Sem calendário fechado, qualquer data escrita
num deck ficaria errada assim que o calendário real fosse definido, ou pior,
envelheceria silenciosamente se o encontro fosse remarcado sem que ninguém
lembrasse de atualizar o slide. O slide de título traz apenas a barra de aula
(`AULA XX | Módulo N, Nome do módulo`) e o `<h3>` com o nome do professor e o
semestre, informação que não expira.

## Riscos conhecidos

Um autor de deck, por hábito herdado do acervo de Desenvolvimento Web ou por
comodidade em sala, pode escrever a data do encontro à mão em algum slide, no
formato `DD/MM/AAAA` ou por extenso, reintroduzindo o problema que esta decisão
evita.

**Mitigação, na validação:** o `tools/check_decks.py` deste acervo inverte a
regra correspondente do acervo de Desenvolvimento Web. Lá, o validador confere
se o atributo `data-data-da-aula` do deck bate com o número do encontro no
nome do arquivo, isto é, exige uma data presente e correta. Aqui, o validador
faz o oposto: reprova qualquer data escrita à mão encontrada no corpo do deck,
no formato `DD/MM/AAAA` ou por extenso. Data escrita à mão é o defeito
equivalente neste acervo, porque envelhece o material sem que ninguém perceba,
e é coberta por fixture própria (`deck_com_data_manual.html`) na suíte pytest.

## Consequências

### Positivas

- Nenhum slide fica desatualizado por causa de uma data escrita e depois
  invalidada por remarcação de encontro.
- O portal e o deck ficam mais simples, sem um módulo JavaScript e um seletor
  que não teriam função real com turma única.
- A regra de validação é objetiva e automatizável: qualquer data escrita à mão,
  em qualquer aula, é pega em CI antes de chegar à publicação.

### Negativas

- Se a disciplina um dia ganhar mais de uma turma ou um calendário fixo, a
  ausência do módulo de resolução de turma precisa ser revertida, e não é uma
  reversão trivial: portal, deck e validador mudam junto.
- O aluno não tem, no material, nenhuma indicação de quando cada encontro
  efetivamente ocorre; essa informação vive fora do acervo, no calendário
  institucional.

## ADRs relacionadas

- ADR-003: cópia em vez de symlink
