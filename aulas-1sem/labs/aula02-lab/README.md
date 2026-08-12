# Laboratório da Aula 02: inventário de decisões da Rota Sul

Disciplina Arquitetura de Software, Uninove, Prof. José Romualdo. Roteiro dos
Ciclos 3 e 4 do encontro: ainda não há código de aplicação, e o produto do dia
é um documento que vale nota até o fim do semestre.

## 1. O passo do case que esta aula resolve

Na Aula 01 cada aluno entregou `docs/ambiente.md` no próprio fork, com o JDK
21, o Maven e a aplicação Spring Boot subindo, sem nenhuma linha de código de
aplicação escrita pelo aluno. Este laboratório retoma exatamente esse ponto:
alguém escreveu o código que faz o projeto existir, e hoje o aluno registra,
pela primeira vez, **por que** escolher código pronto em vez de escrever tudo
na mão. O produto de hoje é `docs/decisoes.md`, o inventário de frameworks e
padrões de projeto que a Rota Sul vai usar, com a justificativa de cada
escolha. Ele é o primeiro capítulo de um documento que a disciplina volta a
abrir em quase toda aula seguinte, porque a documentação do fork responde por
15% da nota do projeto final.

## 2. Pré-requisitos

- **O fork da Aula 01**, clonado e com a aplicação Spring Boot já testada.
  Este laboratório não sobe a aplicação: ele só cria um arquivo Markdown
  dentro do mesmo fork.
- **O contrato técnico da disciplina**, com a lista de frameworks e
  bibliotecas que valem o semestre inteiro. Consultar a tabela projetada em
  sala ou a seção 5.4 do `aulas-1sem/SKILL.md` deste acervo.
- Nenhuma instalação nova é necessária: o ambiente da Aula 01 já é
  suficiente.

## 3. Passo a passo

### 3.1 Criar o arquivo

Dentro do fork, criar `docs/decisoes.md` com o título e um parágrafo de
abertura:

```markdown
# Decisões técnicas da Rota Sul

Este arquivo registra as escolhas de framework e de padrão de projeto do
sistema, com a justificativa de cada uma. É atualizado ao longo do
semestre.
```

### 3.2 Criar a tabela

Quatro colunas, exatamente nesta ordem: `Problema`, `Escolha`, `Tipo`,
`Justificativa`. A coluna `Tipo` só aceita dois valores, `framework` ou
`padrão de projeto`, e é essa coluna que exercita a distinção do Ciclo 2 da
aula.

```markdown
| Problema | Escolha | Tipo | Justificativa |
|---|---|---|---|
```

### 3.3 Preencher as cinco linhas de framework

Todas as escolhas precisam estar dentro do contrato técnico da disciplina.
Um problema sugerido por linha:

- Estruturar a aplicação e gerenciar o ciclo de vida dos objetos.
- Expor operações para outros sistemas por HTTP.
- Gravar e ler dados relacionais sem escrever SQL na mão.
- Gerar as telas do portal no servidor.
- Escrever testes automatizados.

A coluna `Escolha` recebe o nome do framework do contrato técnico, e a
`Justificativa` responde em uma frase **por que esse framework, e não
escrever na mão**. Justificativa que só repete a escolha, do tipo "escolhi
Spring Boot porque Spring Boot é bom", não é aceita.

### 3.4 Conferência cruzada

Trocar de lugar com um colega e ler a tabela dele procurando uma coisa só:
justificativa que apenas repete a escolha com outras palavras. Justificativa
assim volta para o autor reescrever antes do Ciclo 4.

### 3.5 Preencher as três linhas de padrão de projeto

Aqui não se exige o nome canônico do padrão, que só é catalogado na Aula 11.
Exige-se a **descrição do problema específico** e a forma da solução.
Escolher pelo menos três destes problemas:

- Evitar remessa duplicada para o mesmo pedido.
- Paginar em memória a consulta de ocorrências que o atendente faz ao
  telefone.
- Variar o cálculo de frete conforme o parceiro, sem espalhar condicionais.
- Padronizar a criação de uma `Remessa` a partir de um `Pedido`.

Na coluna `Escolha`, descrever a solução em uma frase e, se souber o nome do
padrão, escrever entre parênteses.

### 3.6 Escrever a nota de rastreabilidade

Ao final do arquivo, acrescentar um parágrafo dizendo quais linhas ainda são
hipóteses e serão revisitadas quando a disciplina chegar aos capítulos
correspondentes. Decisão registrada com data de revisão é decisão; decisão
sem revisão é palpite.

## 4. Entregável

Um arquivo `docs/decisoes.md` no fork do aluno, com no mínimo **oito linhas**
na tabela, sendo pelo menos **cinco de framework** e pelo menos **três de
padrão de projeto**, todas com as quatro colunas preenchidas, mais o
parágrafo de abertura e a nota de rastreabilidade, commitado e empurrado.

**Critério de aceitação:** nenhuma linha com justificativa vazia, nenhuma
justificativa que apenas repete a escolha, e nenhuma escolha de framework
fora do contrato técnico da disciplina.

## 5. Critérios de aceitação

| Critério | Evidência conferida na correção |
|---|---|
| A tabela tem no mínimo oito linhas | `docs/decisoes.md` traz cinco ou mais linhas de framework e três ou mais de padrão de projeto |
| Nenhuma justificativa vazia | As quatro colunas preenchidas em cada linha da tabela |
| Framework dentro do contrato técnico | O nome da coluna `Escolha`, nas linhas de framework, bate com a tabela da seção 5.4 do contrato técnico |
| Nenhuma justificativa que repete a escolha | A frase da coluna `Justificativa` explica o motivo da escolha, não apenas nomeia o framework ou o padrão |
| A coluna `Tipo` está correta | Cada linha traz exatamente `framework` ou `padrão de projeto`, nunca outro valor |
| A nota de rastreabilidade existe | Um parágrafo ao final do arquivo aponta quais linhas ainda são hipóteses |
| O commit da aula existe no fork | `git log` do fork mostra um commit com a mensagem `docs(decisoes): inventário inicial de frameworks e padrões da Rota Sul` |

## 6. Commit e push esperados

```bash
git add docs/decisoes.md
git commit -m "docs(decisoes): inventário inicial de frameworks e padrões da Rota Sul"
git push
```

Conferir no navegador que o commit aparece no fork do aluno, na aba
**Commits** do GitHub. Quem receber erro de permissão no `git push`
provavelmente está usando um `origin` incorreto: corrigir com `git remote
set-url origin https://github.com/SEU_USUARIO/uninove-2026-2-rota-sul.git` e
repetir o push.
