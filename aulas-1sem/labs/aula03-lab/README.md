# Laboratório da Aula 03: a Rota Sul no modelo 3C

Disciplina Arquitetura de Software, Uninove, Prof. José Romualdo. Roteiro dos
Ciclos 3 e 4 do encontro: laboratório de mapeamento, sem código.

## 1. O passo do case que esta aula resolve

Na Aula 02 cada aluno entregou `docs/decisoes.md` no próprio fork, com o
inventário de frameworks e padrões de projeto da Rota Sul. Uma das linhas
daquele inventário trata de expor operações para outros sistemas por HTTP, e
essa linha pressupõe que existem **outros sistemas** e **outras pessoas** do
lado de fora do software. Este laboratório retoma exatamente esse ponto:
quem são essas pessoas, e o que a presença delas muda nos requisitos do
sistema. O produto de hoje é `docs/colaboracao.md`, o mapeamento das
interações reais entre os cinco atores da Rota Sul, classificadas no modelo
3C e marcadas como síncronas ou assíncronas. Ele alimenta diretamente a Aula
04, que transforma esse mapeamento em diagrama de componentes.

> **Nota sobre a origem do modelo 3C.** O modelo 3C, comunicação, coordenação
> e cooperação, **não está no capítulo 02 do AVA**. O capítulo trata de
> groupware, dos exemplos de sistema colaborativo e dos requisitos funcionais
> e não funcionais, mas não usa esses três termos como modelo de
> classificação. O 3C vem de PIMENTEL, Mariano; FUCKS, Hugo. **Sistemas
> Colaborativos**. Rio de Janeiro: Campus, 2011, que é a única referência
> bibliográfica indicada pelo próprio capítulo. Se um aluno perguntar em que
> página do AVA está o 3C, a resposta é: em nenhuma, ele vem da bibliografia
> do capítulo, não do capítulo em si. O quiz de hoje cobra o conteúdo do
> capítulo, e não o 3C.

## 2. Pré-requisitos

- **O fork da Aula 01**, com `docs/decisoes.md` da Aula 02 já commitado e
  empurrado. Este laboratório não sobe a aplicação: ele só cria um novo
  arquivo Markdown dentro do mesmo fork.
- Nenhuma instalação nova é necessária: o ambiente da Aula 01 já é
  suficiente.
- Ter em mãos os cinco atores e as nove entidades da Rota Sul: lojista,
  expedidor, motorista, atendente e transportadora parceira; `Cliente`,
  `Pedido`, `Remessa`, `Volume`, `Rota`, `Veiculo`, `Motorista`, `Ocorrencia`,
  `Parceiro`.

## 3. Passo a passo

### 3.1 Criar o arquivo

Dentro do fork, criar `docs/colaboracao.md` com o título e um parágrafo de
abertura aplicando a definição do capítulo ao case: qual é o trabalho comum a
todos os atores.

```markdown
# A Rota Sul como sistema colaborativo

(um parágrafo respondendo: qual é o trabalho comum a todos os atores)
```

A resposta esperada, em uma frase, é entregar o volume certo no destino certo
com rastreio íntegro.

### 3.2 Levantar as interações

Listar no mínimo **nove interações reais** entre os cinco atores, cada uma
escrita no formato "quem faz o quê com quem". Exemplos para destravar quem
ficar parado, que podem ser trocados por outros que o próprio aluno enxergar:

- O lojista envia o pedido.
- O expedidor confirma que a remessa foi montada.
- O motorista registra a saída do veículo.
- O atendente consulta o rastreio para responder ao cliente.
- O parceiro informa a entrega da última milha.
- O expedidor reserva o volume para uma rota.
- O motorista registra uma ocorrência de avaria.
- O atendente reabre um pedido.
- O parceiro devolve um volume não entregue.

### 3.3 Montar a tabela

Quatro colunas, exatamente nesta ordem: `Interação`, `Dimensão 3C`, `Síncrona
ou assíncrona`, `Por quê`.

```markdown
| Interação | Dimensão 3C | Síncrona ou assíncrona | Por quê |
|---|---|---|---|
```

A coluna `Dimensão 3C` só aceita `comunicação`, `coordenação` ou
`cooperação`:

- **Comunicação.** Troca de mensagens e de informação entre as pessoas.
- **Coordenação.** Gestão de pessoas, tarefas e recursos ao longo do tempo,
  para que o trabalho de um não atropele o do outro.
- **Cooperação.** Atuação conjunta sobre um mesmo artefato compartilhado.

A regra do exercício é que as três dimensões apareçam, com **pelo menos duas
interações em cada**. Quem classificar tudo como comunicação não separou
colaboração de conversa.

### 3.4 Discussão dirigida

Trocar de lugar com um colega e ler uma linha que ele classificou como
cooperação. Debater se é mesmo cooperação ou se é coordenação disfarçada. O
critério de desempate é a pergunta: **existe um artefato compartilhado que as
duas pessoas alteram?** Se existe, é cooperação; se o que existe é ordem de
execução e responsabilidade, é coordenação.

### 3.5 Escolher os requisitos não funcionais

No mesmo arquivo, criar a seção `## Requisitos não funcionais`, com duas
listas:

- **`Necessários`**, com os requisitos da lista do capítulo que a Rota Sul
  precisa, cada um com uma frase ligando o requisito a uma interação da
  tabela anterior.
- **`Descartados nesta etapa`**, com no mínimo três requisitos e a
  justificativa do descarte. Justificativa aceitável é do tipo
  "gerenciamento de clusters fica fora porque o sistema roda em um processo
  só até a Aula 19"; justificativa inaceitável é "não precisa".

Os onze requisitos não funcionais do capítulo, para escolher: balanceamento
de carga, transparência a falhas, controle de transações de acesso,
gerenciamento de clusters, reinstalação dinâmica, desligamento limpo,
serviços de log e auditoria, gerenciamento de sistemas, uso de threads, pool
de recursos, segurança de acesso.

### 3.6 Escrever a conclusão

Um parágrafo final respondendo, com base no que foi mapeado, se a Rota Sul é
uma aplicação corporativa, um sistema colaborativo, ou as duas coisas, e por
quê, usando o critério do objetivo final do software.

## 4. Entregável

Um arquivo `docs/colaboracao.md` no fork do aluno, com:

- O título e o parágrafo de abertura sobre o trabalho comum aos atores.
- A tabela de no mínimo **nove interações**, com as **três dimensões do 3C**
  representadas e **pelo menos duas interações em cada**.
- A seção `## Requisitos não funcionais`, com a lista de necessários ligados
  a uma interação e no mínimo **três descartados com justificativa**.
- O parágrafo de conclusão.

Tudo commitado e empurrado.

**Critério de aceitação:** nenhuma linha da tabela sem a coluna `Por quê`
preenchida, e a conclusão presente.

## 5. Critérios de aceitação

| Critério | Evidência conferida na correção |
|---|---|
| A tabela tem no mínimo nove interações | `docs/colaboracao.md` traz nove ou mais linhas no formato "quem faz o quê com quem" |
| As três dimensões do 3C aparecem | Pelo menos duas interações marcadas como comunicação, duas como coordenação e duas como cooperação |
| Nenhuma linha sem a coluna "Por quê" | As quatro colunas preenchidas em toda linha da tabela |
| A seção de requisitos não funcionais existe | `## Requisitos não funcionais` com as listas `Necessários` e `Descartados nesta etapa` |
| No mínimo três requisitos descartados, com justificativa | Cada item de `Descartados nesta etapa` traz uma frase de motivo, não um "não precisa" |
| A conclusão está presente | Um parágrafo final classifica a Rota Sul como aplicação corporativa, sistema colaborativo, ou as duas coisas, com justificativa |
| O commit da aula existe no fork | `git log` do fork mostra um commit com a mensagem `docs(colaboracao): mapeia as interações da Rota Sul no modelo 3C` |

## 6. Commit e push esperados

```bash
git add docs/colaboracao.md
git commit -m "docs(colaboracao): mapeia as interações da Rota Sul no modelo 3C"
git push
```

Conferir no navegador que o commit aparece no fork do aluno, na aba
**Commits** do GitHub. Quem receber erro de permissão no `git push`
provavelmente está usando um `origin` incorreto: corrigir com `git remote
set-url origin https://github.com/SEU_USUARIO/uninove-2026-2-rota-sul.git` e
repetir o push.
