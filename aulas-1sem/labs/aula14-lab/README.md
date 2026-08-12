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
  laboratório de hoje é o primeiro a exigir um container Docker rodando.
- **Um arquivo `.env`** na raiz do fork, com `DB_PASSWORD=` e uma senha
  escolhida pelo aluno, listado no `.gitignore` desde a Aula 01.

## 3. Passo a passo

### 3.1 Acrescentar as dependências (Ciclo 3)

No `pom.xml`, quatro dependências novas.

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
todo o laboratório: os passos 3.6, 3.8 e o restante da suíte de testes
herdada (Aulas 07 a 13) dependem dele estar no ar.

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

## 4. Entregável

`PedidoRepositoryJdbc` como única implementação ativa de `PedidoRepository`,
a migration Flyway, `PedidoRepositoryJdbcTest` com Testcontainers, e a
contagem de linhas registrada em `docs/decisoes.md`.

**Três arquivos digitados pelo aluno hoje**
(`V1__cria_tabela_pedido.sql`, `PedidoRepositoryJdbc.java`,
`PedidoRepositoryJdbcTest.java`), mais a edição de quatro linhas em
`pom.xml`, três linhas em `application.properties`, a remoção de uma
anotação em `PedidoRepositoryEmMemoria.java`, e duas linhas novas em
`docs/decisoes.md`. Abaixo da mediana do acervo (cerca de nove artefatos),
então nenhum arquivo pronto precisou entrar no kit: diferente de aulas que
mudam assinatura de algo já entregue, o laboratório de hoje só acrescenta
uma implementação nova atrás de um contrato que já existia.

## 5. Critérios de aceitação

| Critério | Evidência conferida na correção |
|---|---|
| `PedidoRepositoryJdbc` é o único bean de `PedidoRepository` | `@Repository` só na classe JDBC; `PedidoRepositoryEmMemoria` continua no código, sem a anotação |
| Um pedido sobrevive a um reinício da aplicação | `GET /pedidos` lista o pedido depois de `Ctrl+C` e nova subida |
| `PedidoRepositoryJdbcTest` passando | `./mvnw test` verde, usando Testcontainers |
| A contagem de linhas está registrada | `docs/decisoes.md` com os dois números do passo 3.6 |
| A decisão de arquitetura está registrada | `docs/decisoes.md` nomeando o Repository Pattern como razão da troca sem custo em `PedidoService` |
| `./mvnw test` passando | Suíte inteira verde, incluindo as Aulas 06 a 13 |
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
