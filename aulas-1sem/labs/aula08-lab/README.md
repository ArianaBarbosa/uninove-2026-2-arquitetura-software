# Laboratório da Aula 08: o `.jar` executável, e o contraste com o WAR

Disciplina Arquitetura de Software, Uninove, Prof. José Romualdo. Roteiro dos
Ciclos 3 e 4 do encontro: empacotamento executável e comparação escrita com o
modelo de servidor de aplicações do capítulo.

## 1. O passo do case que esta aula resolve

Na Aula 07 cada aluno entregou a interface `PedidoService` com duas
implementações trocáveis por perfil, `PedidoServicePadrao` e
`PedidoServiceComAnaliseDeRisco`, mais a suíte de teste de contrato que roda
contra as duas. Nenhuma linha de regra de negócio muda hoje: o código de
produção da Rota Sul continua exatamente o das Aulas 06 e 07.

O que muda hoje é **como a aplicação é empacotada e executada**. Até aqui, a
turma sempre subiu o projeto com `./mvnw spring-boot:run`. O capítulo de hoje
descreve o modelo clássico da Java EE: empacotar a aplicação num **WAR**,
*Web Application Archive*, um arquivo que contém só o código, e instalá-lo
num servidor de aplicações administrado à parte, JBoss ou WebSphere. Este
laboratório contrasta esse modelo com o que a disciplina usa desde a Aula 01,
decisão registrada na ADR-001 da spec do acervo: o Spring Boot embarca o
próprio servidor web dentro do `.jar` que a build gera, e `java -jar` já sobe
a aplicação inteira, sem instalar nada além da JVM.

> **Nenhum servidor de aplicações é instalado hoje.** O laboratório é
> empacotar o `.jar`, rodar com `java -jar`, e escrever a comparação. Quem
> procurar um passo de "instalar o JBoss" aqui não vai encontrar: é
> exatamente essa ausência que o laboratório de hoje evidencia e explica.

## 2. Pré-requisitos

- **O fork da Aula 07**, com a interface `PedidoService`, as duas
  implementações e a suíte de contrato já commitadas e empurradas.
- **Java 21 LTS** e **Maven** ativos, conferidos na Aula 01.
- Nenhuma dependência nova no `pom.xml`. O plugin que faz o empacotamento
  executável, `spring-boot-maven-plugin`, já está no projeto desde o fork,
  herdado do `spring-boot-starter-parent`.

## 3. Passo a passo

### 3.1 Confirmar o empacotamento

Abrir o `pom.xml` do fork e localizar o plugin dentro de
`<build><plugins>`:

```xml
<plugin>
  <groupId>org.springframework.boot</groupId>
  <artifactId>spring-boot-maven-plugin</artifactId>
</plugin>
```

É ele que transforma o `.jar` comum, que só teria o código do aluno, num
`.jar` executável, com o Tomcat e as demais dependências embutidos.

### 3.2 Gerar o `.jar`

Parar qualquer `./mvnw spring-boot:run` em execução e rodar o empacotamento
completo:

```bash
./mvnw clean package
```

Ao final, conferir que existe um arquivo terminado em `.jar` dentro de
`target/`.

### 3.3 Rodar com `java -jar`

Num terminal novo, sem nenhum `./mvnw` envolvido:

```bash
java -jar target/*.jar
```

```bash
# noutro terminal, trocando 8080 pela porta que o seu terminal imprimiu
curl http://localhost:8080/pedidos
```

Conferir no log a mesma inicialização e a mesma linha de porta de sempre.
**Nenhum servidor de aplicações foi instalado para isso acontecer.**

Saída de referência, obtida rodando este mesmo gabarito com Java 21 e Maven
localmente (seção 5 do relatório desta tarefa detalha o ambiente):

```
$ java -jar target/rota-sul-0.0.1-SNAPSHOT.jar
...
Starting RotaSulApplication v0.0.1-SNAPSHOT using Java 21.0.12
...
Tomcat initialized with port 8080 (http)
...
Tomcat started on port 8080 (http) with context path '/'
Started RotaSulApplication in 0.609 seconds (process running for 0.807)

$ curl http://localhost:8080/pedidos
[]

$ curl -i -X POST http://localhost:8080/pedidos \
  -H "Content-Type: application/json" \
  -d '{"cliente":"Lojista Ana","descricao":"Duas caixas de pecas automotivas"}'
HTTP/1.1 201
Content-Type: application/json

{"id":1,"cliente":"Lojista Ana","descricao":"Duas caixas de pecas automotivas","situacao":"RECEBIDO"}

$ curl http://localhost:8080/pedidos
[{"id":1,"cliente":"Lojista Ana","descricao":"Duas caixas de pecas automotivas","situacao":"RECEBIDO"}]
```

**Colar a saída do `GET /pedidos` (a última chamada, com o pedido já
registrado) no corpo do commit da aula.**

### 3.4 Inspecionar o `.jar` por dentro

Repetir a inspeção da demonstração, agora com as mãos do aluno:

```bash
jar tf target/*.jar | head -30
```

```bash
unzip -p target/*.jar META-INF/MANIFEST.MF
```

Saída de referência do manifesto, obtida rodando este mesmo gabarito:

```
Manifest-Version: 1.0
Created-By: Maven JAR Plugin 3.4.2
Build-Jdk-Spec: 21
Implementation-Title: rota-sul
Implementation-Version: 0.0.1-SNAPSHOT
Main-Class: org.springframework.boot.loader.launch.JarLauncher
Start-Class: br.uni9.rotasul.RotaSulApplication
Spring-Boot-Version: 3.3.4
Spring-Boot-Classes: BOOT-INF/classes/
Spring-Boot-Lib: BOOT-INF/lib/
Spring-Boot-Classpath-Index: BOOT-INF/classpath.idx
Spring-Boot-Layers-Index: BOOT-INF/layers.idx
```

Duas linhas para localizar: `Start-Class`, que aponta para
`br.uni9.rotasul.RotaSulApplication`, a classe do aluno, e `Main-Class`, que
aponta para `org.springframework.boot.loader.launch.JarLauncher`, o launcher
do próprio Spring Boot, não para o código do aluno. É esse launcher que sobe
o Tomcat embarcado (localizável em `jar tf` dentro de
`BOOT-INF/lib/tomcat-embed-core-*.jar`) antes de entregar o controle à
aplicação.

### 3.5 Escrever a comparação

Criar `docs/empacotamento.md` no fork, com uma tabela de quatro linhas,
colunas `Aspecto`, `Modelo do capítulo, Java EE mais servidor de aplicações`
e `Modelo do laboratório, Spring Boot com JAR executável`:

```markdown
# Empacotamento: JAR executável contra WAR em servidor de aplicações

| Aspecto | Modelo do capítulo, Java EE + servidor de aplicações | Modelo do laboratório, Spring Boot com JAR executável |
|---|---|---|
| Instalação | Instala e administra JBoss ou WebSphere à parte | Nenhuma instalação: `java -jar` já sobe tudo |
| Empacotamento | WAR, só o código da aplicação | JAR, aplicação mais servidor embarcado |
| Portabilidade | Depende do servidor de aplicações do ambiente de destino | Roda em qualquer máquina com a JVM 21 |
| Infraestrutura | O servidor de aplicações, via JTA, JNDI e EJB | O próprio Spring, via inversão de controle (Aula 12) |
```

### 3.6 Escrever a conclusão

Ao final de `docs/empacotamento.md`, um parágrafo respondendo por que a
indústria migrou do modelo do capítulo para o modelo do laboratório. O
parágrafo precisa cobrir:

1. O custo de instalar e administrar um servidor de aplicações em cada
   ambiente.
2. A agilidade de empacotar tudo junto para rodar em contêineres, prévia da
   Aula 19.
3. **Ao menos um serviço da Java EE** citado pelo nome, com o que faz o
   papel dele no laboratório.

Exemplo de conclusão que cumpre os três pontos (o aluno escreve com as
próprias palavras, não copia este parágrafo):

> A indústria migrou do modelo WAR mais servidor de aplicações porque
> instalar e administrar um JBoss ou WebSphere em cada ambiente, de
> desenvolvimento a produção, tem um custo operacional que o modelo de JAR
> executável elimina: o mesmo artefato que roda na máquina do desenvolvedor
> roda em produção, sem depender de um servidor pré-instalado e configurado
> à parte. Essa mesma vantagem é o que torna o empacotamento executável
> natural para contêineres, tema da Aula 19: um `Dockerfile` que copia o
> `.jar` e roda `java -jar` é toda a receita. Boa parte do que o JNDI
> resolvia na Java EE clássica, localizar e configurar a fonte de conexão
> com o banco de dados, hoje é o próprio Spring Boot autoconfigurando o
> `DataSource` a partir de `application.properties`, sem exigir um serviço
> de diretório externo ao servidor.

### 3.7 Conferir o `.gitignore`

Garantir que `target/` está listado no `.gitignore` do fork, para o `.jar`
gerado não ser commitado. O que vai para o fork é a comparação escrita, não
o binário.

### 3.8 Registrar a decisão

Em `docs/decisoes.md`, uma linha nova registrando a escolha de empacotamento
executável em vez de WAR, com a justificativa resumida em uma frase. Exemplo:

> Empacotamento: JAR executável com Spring Boot (não WAR em servidor de
> aplicações), porque o `.jar` já embarca o Tomcat e roda com `java -jar` em
> qualquer máquina com JVM 21, sem instalar e administrar um servidor à
> parte.

## 4. Entregável

No fork do aluno:

- O `.jar` executável rodando com `java -jar`, sem usar
  `./mvnw spring-boot:run`.
- A evidência de `GET /pedidos` colada no commit da aula.
- `docs/empacotamento.md`, com a tabela de quatro aspectos e a conclusão
  citando ao menos um serviço da Java EE com o equivalente no laboratório.
- `docs/decisoes.md` com a linha nova sobre o empacotamento.
- `target/` fora do commit.

## 5. Critérios de aceitação

| Critério | Evidência conferida na correção |
|---|---|
| A aplicação responde a partir de `java -jar` | `GET /pedidos` respondendo, sem qualquer processo de `./mvnw spring-boot:run` ativo |
| A tabela cobre os quatro aspectos mínimos | `docs/empacotamento.md` com instalação, empacotamento, portabilidade e infraestrutura |
| A conclusão cita um serviço da Java EE | Parágrafo final de `docs/empacotamento.md` nomeando o serviço (JTA, JNDI ou EJB) e o equivalente no laboratório |
| `target/` está fora do commit | `.gitignore` do fork lista `target/`, e `git log --stat` da aula não traz nenhum `.jar` |
| A decisão está registrada | Linha nova em `docs/decisoes.md` explicando a escolha |
| O commit da aula existe | `git log` do fork mostra o commit `docs(empacotamento): compara o JAR executável do laboratório com o modelo WAR do capítulo` |

## 6. Commit e push esperados

```bash
git add docs/empacotamento.md docs/decisoes.md
git commit -m "docs(empacotamento): compara o JAR executável do laboratório com o modelo WAR do capítulo"
git push
```
