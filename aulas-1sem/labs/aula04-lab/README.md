# Laboratório da Aula 04: a arquitetura colaborativa da Rota Sul

Disciplina Arquitetura de Software, Uninove, Prof. José Romualdo. Roteiro dos
Ciclos 3 e 4 do encontro: laboratório de modelagem, sem código de aplicação.

## 1. O passo do case que esta aula resolve

Na Aula 03 cada aluno entregou `docs/colaboracao.md` no próprio fork, com a
tabela das nove interações da Rota Sul classificadas no modelo 3C e marcadas
como síncronas ou assíncronas. Este laboratório parte dessas interações para
decidir **quais componentes de software existem** e **como eles se
comunicam**, primeiro num diagrama de componentes e depois num diagrama de
implantação, os dois em PlantUML. O produto de hoje é
`docs/arquitetura-colaborativa.md`, mais os quatro arquivos em
`docs/arquitetura/`. A Aula 05 revisa esses diagramas com a notação UML
formal e acrescenta o diagrama de classes do domínio.

> **Sem código de aplicação.** O que se cobra hoje é a decisão, quais
> componentes existem e quem depende de quem, e onde cada coisa roda. A
> notação vem pronta nos esqueletos abaixo; a Aula 05 explica de onde ela vem
> e o que torna um diagrama rigoroso.

## 2. Pré-requisitos

- **O fork da Aula 01**, com `docs/colaboracao.md` da Aula 03 já commitado e
  empurrado.
- Nenhuma instalação nova é necessária: os diagramas são texto puro, e a
  imagem é gerada por um serviço externo, não por ferramenta local.
- Ter em mãos a tabela de `docs/colaboracao.md`, com as nove interações da
  Rota Sul.

## 3. Passo a passo

### 3.1 Preparar a pasta

Dentro do fork, criar `docs/arquitetura/`.

### 3.2 Listar os componentes

Antes de desenhar, escrever numa folha os componentes de software que a Rota
Sul precisa, partindo das interações mapeadas em `docs/colaboracao.md`.
Mínimo de **quatro**. Os quatro que a maior parte das listas contém:
recebimento de pedidos, montagem de remessas, rastreamento e ocorrências, e
integração com parceiros. Estes quatro nomes não são coincidência: eles
reaparecem na Aula 19 como quatro processos separados.

### 3.3 Desenhar o diagrama de componentes

Criar `docs/arquitetura/componentes.puml`. Cada componente é declarado com
`component`, e o que um oferece ao outro é declarado com `interface`. A
pergunta que orienta cada ligação é: **que operação este componente oferece,
e quem depende dela?** Na notação, `--` liga o componente à interface que ele
**oferece**, e `--(` liga à interface que ele **consome**.

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
acrescentar **pelo menos uma interface** que não esteja no exemplo. Um
exemplo de interface a mais, ligando rastreamento e parceiros:

```
interface "confirmarEntregaParceiro" as iConfirmacao

rastreamento -up- iConfirmacao
parceiros --( iConfirmacao
```

### 3.4 Criar o `.md` irmão e conferir a imagem

Criar `docs/arquitetura/componentes.md` com um título e a linha que embute a
imagem, trocando `SEU_USUARIO` pelo nome de usuário do aluno no GitHub:

```markdown
# Componentes da Rota Sul

![Diagrama de componentes da Rota Sul](https://www.plantuml.com/plantuml/proxy?cache=no&src=https://raw.githubusercontent.com/SEU_USUARIO/uninove-2026-2-rota-sul/main/docs/arquitetura/componentes.puml)
```

Commitar, empurrar e abrir o `.md` na página do fork. A imagem precisa
aparecer desenhada.

> **Se der erro.** Um retângulo com texto de erro no lugar da imagem é
> sintaxe errada no `.puml`; nada aparecendo é caminho errado no `src` ou
> fork privado. Ver a nota da seção 3.6 sobre as duas limitações deste
> mecanismo.

### 3.5 Desenhar o diagrama de implantação

Criar `docs/arquitetura/implantacao.puml`, no mesmo molde do passo anterior.
Aqui a pergunta muda: não é mais quem depende de quem, é **onde cada coisa
roda**. Cada máquina é um `node`, com estereótipo entre `<<` e `>>` dizendo
que tipo de nó é, e o que roda dentro dela é um `artifact` ou um `database`.
Mínimo de **três nós**. Marcar em cada ligação se a comunicação é síncrona ou
assíncrona, usando a definição formal do Ciclo 1.

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

> **Duas armadilhas de sintaxe que já custaram tempo de aula.**
> `device` não aceita bloco com chaves: `device "Nome" { ... }` falha. A
> forma correta é `node "Nome" as apelido <<device>> { ... }`, com o
> estereótipo sobre um `node` comum, como no exemplo acima. E `package` vazio
> ao lado de `class` no mesmo diagrama falha com "Use 'allowmixing'"; este
> diagrama não usa `package`, então não se aplica aqui, mas volta a valer na
> Aula 05.

Criar `docs/arquitetura/implantacao.md`, no mesmo formato do passo 3.4,
trocando `componentes.puml` por `implantacao.puml` no `src`.

### 3.6 Escrever a decisão

Criar `docs/arquitetura-colaborativa.md` com três seções:

- `## Modelo escolhido`: um dos três do Ciclo 2, centralizada,
  descentralizada ou híbrida.
- `## Justificativa`: citando **pelo menos duas** das seis características de
  sistemas distribuídos do capítulo, e dizendo o que a escolha favorece e o
  que ela sacrifica.
- `## Diagramas`: link para os dois `.md` gerados nos passos 3.4 e 3.5.

> **Duas limitações do mecanismo de imagem, para ter em mente o semestre
> inteiro.** A renderização depende de um serviço externo, o `plantuml.com`:
> se ele ficar fora do ar, a imagem some do `.md`, mas o `.puml` versionado
> continua sendo a fonte de verdade e pode ser reaberto em qualquer ferramenta
> PlantUML. E o proxy só consegue ler a fonte se o repositório do aluno for
> **público**: quem tornar o fork privado perde a imagem, mesmo com o
> `.puml` correto.

### 3.7 Registrar no inventário

Acrescentar uma linha em `docs/decisoes.md`, criado na Aula 02, com o modelo
de arquitetura escolhido hoje. O inventário é vivo, e é assim que ele cresce.

```markdown
| Escolha | Motivo |
|---|---|
| ... linhas da Aula 02 ... | ... |
| Arquitetura híbrida para a Rota Sul | Centraliza pedidos e rastreamento no servidor de aplicação; expedição e integração com parceiros ficam descentralizadas para tolerar falha de um parceiro sem derrubar o pedido |
```

A linha acima é um exemplo; o modelo e o motivo de cada aluno seguem o que
foi decidido em `docs/arquitetura-colaborativa.md`.

## 4. Entregável

No fork do aluno:

- `docs/arquitetura-colaborativa.md`, com as três seções.
- `docs/arquitetura/componentes.puml` e `componentes.md`.
- `docs/arquitetura/implantacao.puml` e `implantacao.md`.
- Uma linha nova em `docs/decisoes.md`.

Tudo commitado e empurrado.

## 5. Critérios de aceitação

| Critério | Evidência conferida na correção |
|---|---|
| Diagrama de componentes com no mínimo quatro componentes | `componentes.puml` declara quatro ou mais `component` |
| Interfaces entre os componentes, com pelo menos uma além do exemplo do professor | `componentes.puml` declara `interface` além das três do esqueleto |
| Diagrama de implantação com no mínimo três nós | `implantacao.puml` declara três ou mais `node` |
| Ligações de implantação marcadas como síncronas ou assíncronas | Cada seta de `implantacao.puml` traz `: ..., síncrono` ou `: ..., assíncrono` |
| As duas imagens aparecem na página do `.md` no fork | Abrir `componentes.md` e `implantacao.md` no GitHub e ver a imagem desenhada, sem retângulo de erro |
| Justificativa cita ao menos duas características do capítulo | `arquitetura-colaborativa.md`, seção `## Justificativa`, nomeia duas das seis características de sistemas distribuídos |
| Linha nova no inventário | `docs/decisoes.md` com uma linha a mais, referente ao modelo de arquitetura de hoje |
| O commit da aula existe no fork | `git log` do fork mostra o commit `docs(arquitetura): escolhe o modelo colaborativo e esboça componentes e implantação` |

## 6. Commit e push esperados

```bash
git add docs/arquitetura-colaborativa.md docs/arquitetura docs/decisoes.md
git commit -m "docs(arquitetura): escolhe o modelo colaborativo e esboça componentes e implantação"
git push
```

Conferir no navegador que os dois diagramas aparecem desenhados nas páginas
`componentes.md` e `implantacao.md` do fork. Quem receber erro de permissão
no `git push` provavelmente está usando um `origin` incorreto: corrigir com
`git remote set-url origin https://github.com/SEU_USUARIO/uninove-2026-2-rota-sul.git`
e repetir o push.
