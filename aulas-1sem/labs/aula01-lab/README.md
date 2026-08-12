# Laboratório da Aula 01: ambiente da Rota Sul

Disciplina Arquitetura de Software, Uninove, Prof. José Romualdo. Roteiro dos
Ciclos 3 e 4 do encontro: nenhuma linha de código de aplicação é escrita hoje.

## 1. O passo do case que esta aula resolve

Esta é a primeira aula do semestre, então não existe entregável de uma aula
anterior para retomar. Este laboratório é o ponto de partida do case Rota
Sul: a partir de hoje existe um único repositório de trabalho, o fork de
`josercf/uninove-2026-2-rota-sul`, que evolui semana a semana até a Aula 20.
O que este laboratório entrega é o ambiente pronto para receber a primeira
linha de código de aplicação, que só entra na Aula 06.

## 2. Pré-requisitos

- **Java 21 LTS**, instalado e ativo no `PATH`.
- **Maven**, o `mvn` do sistema, usado para conferir a versão; a execução do
  projeto em si usa o `./mvnw` do próprio repositório-esqueleto.
- **Git**, instalado e configurado com `user.name` e `user.email`. Os commits
  do semestre inteiro precisam sair com o nome do aluno, porque o projeto
  final é avaliado também pelo histórico de commits.
- **Conta no GitHub**, para forkar o repositório-esqueleto.

> O repositório-esqueleto `josercf/uninove-2026-2-rota-sul` é do professor e
> está publicado. Ninguém escreve nele: cada aluno trabalha no próprio fork,
> criado no passo 3.4. Mantenha o seu fork **público**, porque os diagramas
> das Aulas 04 e 05 são renderizados por um serviço externo que precisa ler
> o arquivo `.puml` direto do seu repositório.

## 3. Passo a passo

### 3.1 Conferir o JDK

```bash
java -version
```

A saída precisa indicar versão 21. Quem tiver outra versão instala o JDK 21
LTS agora. Quem tiver mais de um JDK instalado confere qual está ativo no
`PATH`, porque o Maven vai usar esse.

### 3.2 Conferir o Maven

```bash
mvn -v
```

A saída precisa mostrar o Maven e, na linha `Java version`, o mesmo 21 do
passo anterior. Divergência entre os dois é a causa mais comum de erro de
compilação nas próximas aulas, e se resolve aqui.

### 3.3 Conferir o Git e a identidade

```bash
git --version
git config --global user.name
git config --global user.email
```

Quem estiver com os dois últimos comandos vazios configura agora:

```bash
git config --global user.name "Seu Nome Completo"
git config --global user.email "seu-email@exemplo.com"
```

### 3.4 Forkar o repositório-esqueleto

Abrir `https://github.com/josercf/uninove-2026-2-rota-sul`, clicar em
**Fork** e criar o fork na conta pessoal. Este é o único fork do semestre.

### 3.5 Clonar o fork

```bash
git clone https://github.com/SEU_USUARIO/uninove-2026-2-rota-sul.git
cd uninove-2026-2-rota-sul
git remote -v
```

Conferir que `origin` aponta para a conta do aluno, não para
`josercf/uninove-2026-2-rota-sul`. Clonar o repositório original em vez do
fork é o erro mais comum deste passo, e só aparece na hora do primeiro push,
quando o GitHub nega a escrita.

### 3.6 Subir o projeto vazio

```bash
./mvnw spring-boot:run
```

A primeira execução baixa dependências e demora. Ao final, o log imprime a
linha com a porta em que a aplicação subiu. Abrir essa porta no navegador: a
resposta esperada é a página de erro padrão do Spring Boot, e isso é
sucesso, porque ainda não existe nenhuma rota mapeada. Usar sempre a porta
que o terminal imprimiu, nunca uma porta fixa decorada.

### 3.7 Conferir o `.gitignore`

Abrir o `.gitignore` do fork e confirmar que `.env` está listado. Se não
estiver, acrescentar. A regra vale o semestre inteiro: senha de banco e
qualquer segredo vão para variável de ambiente e nunca para o repositório.

### 3.8 Escrever o entregável

Criar `docs/ambiente.md` no fork, com três seções: `## JDK`, `## Maven` e
`## Aplicação subindo`. Colar em cada uma a saída literal do comando
correspondente e, na terceira, a linha de log com a porta. Acrescentar uma
linha final informando o sistema operacional usado.

## 4. Entregável

Um arquivo `docs/ambiente.md` no fork do aluno, com três evidências coladas
na íntegra (a saída de `java -version`, a saída de `mvn -v` e a linha de log
em que a aplicação Spring Boot informa a porta em que subiu) mais uma linha
final com o sistema operacional usado, commitado e empurrado para o fork.

**Critério de aceitação:** as três evidências presentes e completas, o JDK
na versão 21 nas duas primeiras evidências, a aplicação subindo na terceira
e o `.env` já listado no `.gitignore`.

## 5. Critérios de aceitação

| Critério | Evidência conferida na correção |
|---|---|
| O fork existe na conta do aluno | A URL `github.com/<usuario>/uninove-2026-2-rota-sul` responde |
| O JDK instalado é a versão 21 LTS | A seção `## JDK` de `docs/ambiente.md` traz a saída de `java -version` mostrando `21` |
| O Maven está configurado com o mesmo JDK | A seção `## Maven` de `docs/ambiente.md` traz a saída de `mvn -v` com `Java version: 21` |
| A aplicação Spring Boot sobe sem erro | A seção `## Aplicação subindo` de `docs/ambiente.md` traz a linha de log com a porta em que a aplicação iniciou |
| O sistema operacional está registrado | `docs/ambiente.md` termina com uma linha informando o sistema operacional usado |
| O `.env` está protegido do commit | O `.gitignore` do fork lista `.env` |
| O commit da aula existe no fork | `git log` do fork mostra um commit com a mensagem `chore(ambiente): registra JDK 21, Maven e primeira execução` |

## 6. Commit e push esperados

```bash
git add docs/ambiente.md .gitignore
git commit -m "chore(ambiente): registra JDK 21, Maven e primeira execução"
git push
```

Conferir no navegador que o commit aparece no fork do aluno, na aba
**Commits** do GitHub. Quem receber erro de permissão no `git push`
provavelmente clonou o repositório original em vez do fork: corrigir o
`origin` com `git remote set-url origin
https://github.com/SEU_USUARIO/uninove-2026-2-rota-sul.git` e repetir o
push.
