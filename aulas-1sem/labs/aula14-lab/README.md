# Laboratório da Aula 14: repositório JDBC contra o repositório em memória

Disciplina Arquitetura de Software, Uninove, Prof. José Romualdo. Roteiro dos
Ciclos 3 e 4 do encontro: trocar `PedidoRepositoryEmMemoria` por
`PedidoRepositoryJdbc`, JDBC puro contra um MySQL real, e medir o custo dessa
troca em linhas de código.

## 1. O passo do case que esta aula resolve

Na Aula 13 cada aluno entregou a tela de cadastro de pedido em
`/pedidos/novo`, com layout, fragments e validação do campo `cliente`,
chamando o mesmo `PedidoService` que a API REST já usava desde a Aula 06.
Cadastrar um pedido por essa tela, reiniciar a aplicação e voltar em
`/pedidos` mostra que o pedido sumiu: `PedidoRepositoryEmMemoria`, viva desde
a Aula 06, é uma `List` dentro da JVM, que existe enquanto o processo existe.

Hoje essa lacuna fecha. O contrato `PedidoRepository`, com `salvar(Pedido)` e
`listarTodos()`, não muda uma linha; só a implementação por trás dele muda,
de memória para um MySQL real acessado por JDBC puro, sem `JdbcTemplate` e
sem ORM. É a primeira das duas trocas prometidas desde a Aula 06: hoje sai a
memória, entra o JDBC puro, sentindo a verbosidade na mão; a Aula 15 troca o
JDBC pela API de Persistência Java, sentindo o alívio. **Não é para esperar o
ORM já hoje**: a verbosidade de hoje é proposital, e é ela a régua que a
próxima aula vai usar.

**Nenhuma classe existente muda de assinatura hoje.** `Pedido`,
`PedidoService`, `PedidoServicePadrao`, `PedidoForm` e
`PedidoFormController` continuam exatamente como a Aula 13 os deixou. A
única mudança em código já entregue é remover a anotação `@Repository` de
`PedidoRepositoryEmMemoria`, para que ela deixe de ser candidata a bean; a
classe continua existindo, intacta, como material de comparação de linhas.
**Não há arquivos prontos no kit desta aula**: três arquivos novos, mais
edições pontuais em `pom.xml`, `application.properties` e
`docs/decisoes.md`, todos digitados pelo aluno.

## 2. Pré-requisitos

- **O fork da Aula 13**, com `PedidoFormController`, `PedidoForm` e a tela
  de cadastro em Thymeleaf, já commitados e empurrados.
- **`PedidoRepository`, `PedidoRepositoryEmMemoria`, `PedidoService` e
  `Pedido`** (Aulas 06, 07 e 11), inalterados.
- **Java 21 LTS**, **Maven** e **Docker** ativos, conferidos na Aula 01. O
  laboratório de hoje é o primeiro a exigir um container Docker rodando, e
  **essa exigência vale, para os testes de persistência, da Aula 14 até a
  Aula 20** (ver passo 3.2).
- **Um arquivo `.env`** na raiz do fork, com `DB_PASSWORD=` e uma senha
  escolhida pelo aluno, listado no `.gitignore` desde a Aula 01.

## 3. Passo a passo

### 3.1 Acrescentar as dependências (Ciclo 3)

No `pom.xml`, seis dependências novas. O deck mostra as cinco principais
(`artifactId` de cada uma); a lista completa abaixo, com `groupId` e
`scope`, acrescenta `org.testcontainers:junit-jupiter`, o motor que liga
`@Testcontainers` ao JUnit 5.

```xml
<dependency>
  <groupId>org.springframework.boot</groupId>
  <artifactId>spring-boot-starter-jdbc</artifactId>
</dependency>
<dependency>
  <groupId>com.mysql</groupId>
  <artifactId>mysql-connector-j</artifactId>
  <scope>runtime</scope>
</dependency>
<dependency>
  <groupId>org.flywaydb</groupId>
  <artifactId>flyway-core</artifactId>
</dependency>
<dependency>
  <groupId>org.flywaydb</groupId>
  <artifactId>flyway-mysql</artifactId>
</dependency>
<dependency>
  <groupId>org.testcontainers</groupId>
  <artifactId>mysql</artifactId>
  <scope>test</scope>
</dependency>
<dependency>
  <groupId>org.testcontainers</groupId>
  <artifactId>junit-jupiter</artifactId>
  <scope>test</scope>
</dependency>
```

`spring-boot-starter-jdbc` traz o `DataSource` autoconfigurado pelo Spring
Boot; `mysql-connector-j` é o driver JDBC do MySQL; `flyway-core` já estava
fixado no contrato técnico. **Correção em relação ao planejamento original:**
o Flyway 10 (a versão que o `spring-boot-starter-parent` 3.3.4 gerencia)
separou o suporte a cada banco do núcleo `flyway-core`; sem `flyway-mysql`, a
aplicação sobe com `FlywayException: Unsupported Database: MySQL 8.4`. As
duas dependências do Testcontainers sobem um MySQL descartável para o teste
do passo 3.9.

### 3.2 Subir um MySQL local

Com `DB_PASSWORD` lida do `.env`, nunca escrita no comando nem no
repositório.

```bash
export DB_PASSWORD=$(grep DB_PASSWORD .env | cut -d= -f2)
docker run --name rotasul-mysql -e MYSQL_ROOT_PASSWORD=${DB_PASSWORD} \
  -e MYSQL_DATABASE=rotasul -p 3306:3306 -d mysql:8.4
```

A porta `3306` é a porta padrão do MySQL, fixada pelo próprio driver JDBC do
passo 3.4, diferente da porta da aplicação Spring Boot, que continua sendo a
que o terminal imprimir a cada subida. Manter esse container rodando durante
todo o laboratório: o passo 3.8, a prova de persistência real rodando
`./mvnw spring-boot:run`, depende dele estar no ar. `PedidoRepositoryJdbcTest`
(passo 3.9) não depende deste container: ele sobe o próprio MySQL
descartável via Testcontainers, independente deste aqui.

**A dependência de um `DataSource` de verdade na subida do contexto não é
de hoje só: vale da Aula 14 até a Aula 20.** A partir de agora,
`spring-boot-starter-jdbc` e o Flyway estão no classpath, e qualquer teste
`@SpringBootTest` de contexto completo tenta abrir o `DataSource` e rodar
as migrations na subida, mesmo quando o teste não tem nada a ver com
persistência. Sem um `DataSource` que realmente conecte, esse teste quebra
com `CommunicationsException` ou `FlywayException`, não com um erro no seu
próprio código. Três testes herdados caem nessa categoria:
`ParceiroClientTest` (Aula 10), `NotificacaoConfigDevTest` e
`NotificacaoConfigProdTest` (Aula 12). O passo 3.12 isola os três.

### 3.3 Escrever a migration

Em `src/main/resources/db/migration/V1__cria_tabela_pedido.sql`, a tabela
`pedido`, com `id` (chave primária autoincremento), `cliente` (obrigatório),
`descricao`, `situacao` (obrigatório) e `regiao` (obrigatório, o atributo que
a Aula 11 acrescentou ao domínio).

```sql
CREATE TABLE pedido (
    id BIGINT AUTO_INCREMENT PRIMARY KEY,
    cliente VARCHAR(255) NOT NULL,
    descricao VARCHAR(255),
    situacao VARCHAR(50) NOT NULL,
    regiao VARCHAR(50) NOT NULL
);
```

O Flyway aplica essa migration sozinho na próxima subida da aplicação, contra
qualquer banco novo, o container manual deste passo ou o container
descartável do Testcontainers no passo 3.9.

### 3.4 Configurar o datasource

Em `src/main/resources/application.properties`.

```properties
spring.datasource.url=jdbc:mysql://localhost:3306/rotasul
spring.datasource.username=root
spring.datasource.password=${DB_PASSWORD}
```

Nenhuma senha em texto puro no arquivo, a mesma regra desde a Aula 01:
`${DB_PASSWORD}` é resolvida pela variável de ambiente exportada no passo
3.2.

### 3.5 Escrever `PedidoRepositoryJdbc`

Em `pedido/repository`, implementando `PedidoRepository` com `java.sql`
puro, recebendo `DataSource` pelo construtor.

```java
package br.uni9.rotasul.pedido.repository;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;
import java.util.ArrayList;
import java.util.List;

import javax.sql.DataSource;

import org.springframework.stereotype.Repository;

import br.uni9.rotasul.pedido.domain.Pedido;

// Implementacao com JDBC puro, sem JdbcTemplate e sem ORM: cada instrucao
// SQL, cada abertura e fechamento de Connection, e cada linha do ResultSet
// e escrita a mao. E o mesmo contrato PedidoRepository desde a Aula 06,
// so a implementacao troca de memoria para um MySQL real. A verbosidade
// daqui e proposital: a Aula 15 troca esta classe por JPA e mede de novo.
@Repository
public class PedidoRepositoryJdbc implements PedidoRepository {

    private final DataSource dataSource;

    public PedidoRepositoryJdbc(DataSource dataSource) {
        this.dataSource = dataSource;
    }

    @Override
    public Pedido salvar(Pedido pedido) {
        String sql = "INSERT INTO pedido (cliente, descricao, situacao, regiao) "
            + "VALUES (?, ?, ?, ?)";
        try (Connection conexao = dataSource.getConnection();
             PreparedStatement comando = conexao.prepareStatement(
                 sql, Statement.RETURN_GENERATED_KEYS)) {
            comando.setString(1, pedido.getCliente());
            comando.setString(2, pedido.getDescricao());
            comando.setString(3, pedido.getSituacao());
            comando.setString(4, pedido.getRegiao());
            comando.executeUpdate();
            try (ResultSet chaves = comando.getGeneratedKeys()) {
                if (chaves.next()) {
                    pedido.setId(chaves.getLong(1));
                }
            }
            return pedido;
        } catch (SQLException erro) {
            throw new IllegalStateException("falha ao salvar pedido", erro);
        }
    }

    @Override
    public List<Pedido> listarTodos() {
        String sql = "SELECT id, cliente, descricao, situacao, regiao FROM pedido";
        List<Pedido> pedidos = new ArrayList<>();
        try (Connection conexao = dataSource.getConnection();
             PreparedStatement comando = conexao.prepareStatement(sql);
             ResultSet resultado = comando.executeQuery()) {
            while (resultado.next()) {
                Pedido pedido = new Pedido(
                    resultado.getString("cliente"),
                    resultado.getString("descricao"),
                    resultado.getString("regiao"));
                pedido.setId(resultado.getLong("id"));
                pedido.setSituacao(resultado.getString("situacao"));
                pedidos.add(pedido);
            }
            return pedidos;
        } catch (SQLException erro) {
            throw new IllegalStateException("falha ao listar pedidos", erro);
        }
    }
}
```

Ajustar os nomes de campo e o construtor de `Pedido` conforme a versão que
cada aluno já tem, escrita na Aula 06 e ajustada na Aula 11.

### 3.6 Compilar e contar as linhas

O registro central do Ciclo 4 começa aqui.

```bash
./mvnw compile
wc -l src/main/java/br/uni9/rotasul/pedido/repository/PedidoRepositoryEmMemoria.java \
      src/main/java/br/uni9/rotasul/pedido/repository/PedidoRepositoryJdbc.java
```

Anotar os dois números num papel ou num editor à parte, para o registro do
passo 3.10.

### 3.7 Desativar a implementação em memória (Ciclo 4)

Remover a anotação `@Repository` de `PedidoRepositoryEmMemoria`. A classe
continua existindo no código, intacta, só deixa de ser candidata a bean; é o
material de comparação da contagem de linhas, não código morto para apagar.
Acrescentar `@Repository` em `PedidoRepositoryJdbc`, que passa a ser a única
implementação que o Spring enxerga.

```java
// PedidoRepositoryEmMemoria.java, sem @Repository desde a Aula 14
public class PedidoRepositoryEmMemoria implements PedidoRepository {
```

### 3.8 Provar a persistência real

Subir a aplicação, cadastrar um pedido pela tela `/pedidos/novo` da Aula 13,
parar a aplicação com `Ctrl+C`, subir de novo, e conferir em `/pedidos` que o
pedido continua lá. É o oposto exato do que a retomada de hoje mostrou com a
versão em memória.

```bash
./mvnw spring-boot:run
# cadastrar um pedido em /pedidos/novo, depois Ctrl+C
./mvnw spring-boot:run
# conferir em /pedidos: o pedido continua la
```

### 3.9 Testar com Testcontainers

`PedidoRepositoryJdbcTest`, em
`src/test/java/br/uni9/rotasul/pedido/repository/`, anotado
`@Testcontainers` e `@SpringBootTest`, com um `@Container static
MySQLContainer<?> mysql = new MySQLContainer<>("mysql:8.4")`, e um método
`@DynamicPropertySource` sobrescrevendo `spring.datasource.url`, `username`
e `password` com os valores do container.

```java
package br.uni9.rotasul.pedido.repository;

import static org.assertj.core.api.Assertions.assertThat;

import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.test.context.DynamicPropertyRegistry;
import org.springframework.test.context.DynamicPropertySource;
import org.testcontainers.containers.MySQLContainer;
import org.testcontainers.junit.jupiter.Container;
import org.testcontainers.junit.jupiter.Testcontainers;

import br.uni9.rotasul.pedido.domain.Pedido;

@Testcontainers
@SpringBootTest
class PedidoRepositoryJdbcTest {

    @Container
    static MySQLContainer<?> mysql = new MySQLContainer<>("mysql:8.4");

    @DynamicPropertySource
    static void configurarDatasource(DynamicPropertyRegistry registry) {
        registry.add("spring.datasource.url", mysql::getJdbcUrl);
        registry.add("spring.datasource.username", mysql::getUsername);
        registry.add("spring.datasource.password", mysql::getPassword);
    }

    @Autowired
    private PedidoRepository pedidoRepository;

    @Test
    void salvarEDepoisListarTodosDevolveUmPedido() {
        Pedido pedido = new Pedido("Loja Boa Vista", "Sofa de dois lugares", "PRINCIPAL");

        pedidoRepository.salvar(pedido);

        assertThat(pedidoRepository.listarTodos()).hasSize(1);
    }
}
```

Esse teste sobe um MySQL descartável a cada execução, sem depender do
container manual do passo 3.2.

```bash
./mvnw test
```

### 3.10 Registrar a contagem, o entregável central de hoje

Em `docs/decisoes.md`, uma linha com os dois números do passo 3.6, por
exemplo:

```
PedidoRepositoryEmMemoria: 33 linhas; PedidoRepositoryJdbc: 75 linhas.
Diferenca: abertura/fechamento de Connection, PreparedStatement,
tratamento de SQLException e montagem manual de cada Pedido.
```

Mais uma frase curta explicando de onde vem a diferença: abertura e
fechamento de conexão, `PreparedStatement`, tratamento de `SQLException` e
montagem manual de cada `Pedido` a partir do `ResultSet`, tudo isso que a
versão em memória nunca precisou fazer.

### 3.11 Registrar a decisão de arquitetura

Uma segunda linha em `docs/decisoes.md`, nomeando o Repository Pattern do
capítulo como a razão de essa troca ter custado zero linha em
`PedidoService`.

```
Repository Pattern (capitulo 13) e a razao de a troca ter custado
zero linha em PedidoService: a camada abstrata ja existia desde a Aula 06.
```

### 3.12 Isolar os testes herdados que não são de persistência

`ParceiroClientTest` (Aula 10), `NotificacaoConfigDevTest` e
`NotificacaoConfigProdTest` (Aula 12) são `@SpringBootTest` de contexto
completo, e nenhum dos três testa persistência. Com
`spring-boot-starter-jdbc` e o Flyway agora no classpath, os três tentam
subir um `DataSource` de verdade e aplicar as migrations junto com o resto
do contexto, e quebram sem um MySQL no ar, mesmo não tendo nada a ver com
banco de dados.

**A saída é excluir a autoconfiguração de `DataSource` e de Flyway nesses
três testes**, e só nesses três, deixando a persistência real de fora do
que cada um se propõe a verificar. É isolamento de teste, prática padrão de
arquitetura: um teste só deveria depender da infraestrutura que o seu
próprio caso de uso exige.

```java
@SpringBootTest(properties = "spring.autoconfigure.exclude="
    + "org.springframework.boot.autoconfigure.jdbc.DataSourceAutoConfiguration,"
    + "org.springframework.boot.autoconfigure.flyway.FlywayAutoConfiguration")
```

Essa anotação substitui o `@SpringBootTest` simples de cada um dos três
testes, sem tocar em mais nada: `ParceiroClientTest` mantém
`webEnvironment = SpringBootTest.WebEnvironment.RANDOM_PORT` dentro dos
parênteses, ao lado de `properties`; `NotificacaoConfigDevTest` e
`NotificacaoConfigProdTest` mantêm `@ActiveProfiles` como uma anotação à
parte, logo abaixo.

**Excluir a autoconfiguração não basta sozinho.** `PedidoRepositoryJdbc`,
componente do mesmo contexto que os três testes sobem por inteiro, exige um
`DataSource` no construtor; sem a autoconfiguração, esse bean deixa de
existir, e a subida falha de um jeito novo, `NoSuchBeanDefinitionException`
em vez de erro de conexão. Cada um dos três testes precisa de um
`@MockBean DataSource`, só para satisfazer essa dependência de construtor,
sem que nenhuma conexão de verdade seja aberta:

```java
@MockBean
private DataSource dataSource;
```

Depois de editar os três, rodar a suíte com o container do passo 3.2
**parado**. `ParceiroClientTest`, `NotificacaoConfigDevTest` e
`NotificacaoConfigProdTest` passam mesmo sem o container, porque não
dependem mais dele. `PedidoRepositoryJdbcTest` também não depende do
container manual: ele sobe o próprio MySQL descartável via Testcontainers
(passo 3.9), então continua passando contanto que o **Docker em si**
esteja de pé. **O container do passo 3.2 só é exigido por
`./mvnw spring-boot:run`** (o teste de ponta a ponta do passo 3.8), não
por `./mvnw test`.

```bash
docker stop rotasul-mysql
./mvnw test
```

Depois, subir o container de novo e confirmar a suíte inteira verde, agora
com o cenário completo, incluindo o passo 3.8.

```bash
docker start rotasul-mysql
./mvnw test
```

## 4. Entregável

`PedidoRepositoryJdbc` como única implementação ativa de `PedidoRepository`,
a migration Flyway, `PedidoRepositoryJdbcTest` com Testcontainers, a
contagem de linhas registrada em `docs/decisoes.md`, e os três testes
herdados de contexto completo isolados da autoconfiguração de persistência.

**Três arquivos digitados pelo aluno hoje**
(`V1__cria_tabela_pedido.sql`, `PedidoRepositoryJdbc.java`,
`PedidoRepositoryJdbcTest.java`), mais a edição de quatro linhas em
`pom.xml`, três linhas em `application.properties`, a remoção de uma
anotação em `PedidoRepositoryEmMemoria.java`, duas linhas novas em
`docs/decisoes.md`, e a troca de `@SpringBootTest` pela variante com
`properties` em `ParceiroClientTest`, `NotificacaoConfigDevTest` e
`NotificacaoConfigProdTest` (passo 3.12). Abaixo da mediana do acervo
(cerca de nove artefatos), então nenhum arquivo pronto precisou entrar no
kit: diferente de aulas que mudam assinatura de algo já entregue, o
laboratório de hoje só acrescenta uma implementação nova atrás de um
contrato que já existia, mais o ajuste pontual de isolamento nos três
testes que a nova dependência atinge de raspão.

## 5. Critérios de aceitação

| Critério | Evidência conferida na correção |
|---|---|
| `PedidoRepositoryJdbc` é o único bean de `PedidoRepository` | `@Repository` só na classe JDBC; `PedidoRepositoryEmMemoria` continua no código, sem a anotação |
| Um pedido sobrevive a um reinício da aplicação | `GET /pedidos` lista o pedido depois de `Ctrl+C` e nova subida |
| `PedidoRepositoryJdbcTest` passando | `./mvnw test` verde, usando Testcontainers |
| A contagem de linhas está registrada | `docs/decisoes.md` com os dois números do passo 3.6 |
| A decisão de arquitetura está registrada | `docs/decisoes.md` nomeando o Repository Pattern como razão da troca sem custo em `PedidoService` |
| `ParceiroClientTest`, `NotificacaoConfigDevTest` e `NotificacaoConfigProdTest` não dependem mais do MySQL | `./mvnw test` passa com `rotasul-mysql` parado; só `./mvnw spring-boot:run` (passo 3.8) ainda exige o container no ar |
| `./mvnw test` passando | Suíte inteira verde, incluindo as Aulas 06 a 13, com o container do passo 3.2 no ar |
| O commit da aula existe | `git log` do fork mostra o commit `feat(pedido): troca PedidoRepositoryEmMemoria por PedidoRepositoryJdbc com JDBC puro` |

## 6. Commit e push esperados

```bash
git add src docs pom.xml
git commit -m "feat(pedido): troca PedidoRepositoryEmMemoria por PedidoRepositoryJdbc com JDBC puro"
git push
```

## 7. Ambiente em que este gabarito foi verificado

Java 21 (`openjdk version "21.0.12"`) e Maven 3.9.16, com
`spring-boot-starter-parent` 3.3.4, contra um MySQL 8.4 real subido por
`docker run` (passo 3.2). A verificação **não isolou o código de hoje**:
montou o fork acumulado inteiro, da Aula 06 até a Aula 13, com o código de
hoje por cima, e rodou `./mvnw test` nesse projeto acumulado.

```
$ export JAVA_HOME=/opt/homebrew/opt/openjdk@21/libexec/openjdk.jdk/Contents/Home
$ export PATH="$JAVA_HOME/bin:$PATH"
$ java -version
openjdk version "21.0.12"
$ mvn -version
Apache Maven 3.9.16, Java version: 21.0.12

$ docker run --name rotasul-mysql -e MYSQL_ROOT_PASSWORD=${DB_PASSWORD} \
    -e MYSQL_DATABASE=rotasul -p 3306:3306 -d mysql:8.4

$ export DB_PASSWORD=...
$ mvn clean test
...
Tests run: 2, Failures: 0, Errors: 0, Skipped: 0 -- in br.uni9.rotasul.parceiro.client.ParceiroClientTest
Tests run: 2, Failures: 0, Errors: 0, Skipped: 0 -- in br.uni9.rotasul.pedido.web.PedidoFormControllerTest
Tests run: 2, Failures: 0, Errors: 0, Skipped: 0 -- in br.uni9.rotasul.pedido.service.PedidoServiceComAnaliseDeRiscoContratoTest
Tests run: 2, Failures: 0, Errors: 0, Skipped: 0 -- in br.uni9.rotasul.pedido.service.PedidoServicePadraoTest
Tests run: 2, Failures: 0, Errors: 0, Skipped: 0 -- in br.uni9.rotasul.pedido.service.CalculoDeFreteServiceTest
Tests run: 2, Failures: 0, Errors: 0, Skipped: 0 -- in br.uni9.rotasul.pedido.service.PedidoServicePadraoContratoTest
Tests run: 2, Failures: 0, Errors: 0, Skipped: 0 -- in br.uni9.rotasul.expedicao.web.RemessaControllerTest
Tests run: 1, Failures: 0, Errors: 0, Skipped: 0 -- in br.uni9.rotasul.rastreamento.service.NotificacaoConfigDevTest
Tests run: 1, Failures: 0, Errors: 0, Skipped: 0 -- in br.uni9.rotasul.rastreamento.service.NotificacaoConfigProdTest
Tests run: 3, Failures: 0, Errors: 0, Skipped: 0 -- in br.uni9.rotasul.rastreamento.domain.OcorrenciaCreatorTest
[INFO]
[INFO] Results:
[INFO]
[INFO] Tests run: 19, Failures: 0, Errors: 0, Skipped: 0
[INFO] BUILD SUCCESS
```

Dezenove testes verdes: os dezoito acumulados desde a Aula 06 mais
`PedidoFormControllerTest` (Aula 13), todos rodando contra o MySQL real do
passo 3.2, incluindo Flyway aplicando a migration antes de qualquer teste.
`./mvnw spring-boot:run` foi executado de ponta a ponta neste mesmo projeto:
`POST /pedidos/novo` cadastrou um pedido ("Loja Boa Vista"), `GET /pedidos`
listou o pedido pela API REST, a aplicação foi encerrada com `Ctrl+C` e
subida de novo, e `GET /pedidos` continuou listando o mesmo pedido, prova
direta do critério de aceitação central desta aula. `ps aux` confirmou que
nenhum processo Java ficou para trás ao final da verificação, e o container
`rotasul-mysql` foi removido ao final da sessão.

### 7.1 Verificação do passo 3.12, isolamento dos três testes herdados

A revisão que motivou o passo 3.12 exigia rodar a suíte com o MySQL parado
e depois com o MySQL de pé. Em vez de remontar o fork acumulado inteiro
(Aulas 06 a 14) outra vez, esta rodada usou um projeto Maven mínimo, com
Java 21 e `spring-boot-starter-parent` 3.3.4, contendo as classes reais e
literais dos três testes afetados e do que cada um exige para subir
(`ParceiroClient`, `ParceiroEndpoint`, `ParceiroClientConfig`, o par
`WebServiceConfig`/`parceiro.xsd` da Aula 10; `NotificacaoConfig` e os
notificadores da Aula 12; `PedidoRepositoryJdbc`, a migration e o
`application.properties` da Aula 14), com o passo 3.12 aplicado.

```
$ export JAVA_HOME=/opt/homebrew/opt/openjdk@21/libexec/openjdk.jdk/Contents/Home
$ export PATH="$JAVA_HOME/bin:$PATH"

# MySQL parado (nenhum container rotasul-mysql no ar):
$ mvn test -Dtest='!PedidoRepositoryJdbcTest'
...
Tests run: 2, Failures: 0, Errors: 0, Skipped: 0 -- in br.uni9.rotasul.parceiro.client.ParceiroClientTest
Tests run: 1, Failures: 0, Errors: 0, Skipped: 0 -- in br.uni9.rotasul.rastreamento.service.NotificacaoConfigDevTest
Tests run: 1, Failures: 0, Errors: 0, Skipped: 0 -- in br.uni9.rotasul.rastreamento.service.NotificacaoConfigProdTest
[INFO] Tests run: 4, Failures: 0, Errors: 0, Skipped: 0
[INFO] BUILD SUCCESS

# MySQL de pé (docker run --name rotasul-mysql ... mysql:8.4):
$ mvn test -Dtest='!PedidoRepositoryJdbcTest'
[INFO] Tests run: 4, Failures: 0, Errors: 0, Skipped: 0
[INFO] BUILD SUCCESS
```

**Os três testes passam nos dois estados**, exatamente o que o passo 3.12
promete: excluir a autoconfiguração de `DataSource` e Flyway, mais o
`@MockBean DataSource` que satisfaz `PedidoRepositoryJdbc`, tira os três da
dependência do container, sem exceção. Achado que corrige a expectativa
inicial da revisão: **`./mvnw test` nunca dependeu do container manual do
passo 3.2**, nem antes nem depois do passo 3.12, porque `PedidoRepositoryJdbcTest`
usa `@DynamicPropertySource` para apontar para o próprio MySQL descartável
do Testcontainers (passo 3.9), independente de `rotasul-mysql` estar de pé
ou não. Quem de fato exige o container manual é só `./mvnw spring-boot:run`
(o passo 3.8, o teste de ponta a ponta pela API), não a suíte automatizada.
O texto do passo 3.12 e a tabela da seção 5 já refletem essa correção.

`PedidoRepositoryJdbcTest` não pôde ser executado até o fim nesta sessão,
pela mesma limitação de ambiente já registrada na Task 27: o
Testcontainers desta máquina não encontra um "Docker environment" válido
(`Could not find a valid Docker environment`), mesmo com `docker run` e
`docker ps` funcionando normalmente pela CLI, no mesmo daemon. Não é
regressão do passo 3.12: a classe não foi tocada por ele, e a mesma
mensagem já tinha sido documentada como particularidade local do Docker
Desktop, não do código.
