# Laboratório da Aula 06: as três camadas da Rota Sul, primeiro código

Disciplina Arquitetura de Software, Uninove, Prof. José Romualdo. Roteiro dos
Ciclos 3 e 4 do encontro: primeiro laboratório de código de aplicação do
semestre.

## 1. O passo do case que esta aula resolve

Na Aula 05 cada aluno entregou `docs/arquitetura/pacotes.puml` e
`dominio.puml`, com os respectivos `.md` irmãos. O `pacotes.puml` desenhou os
três contextos (`pedido`, `expedicao`, `rastreamento`) e as quatro camadas de
cada um (`web`, `service`, `repository`, `domain`), com dependência tracejada
sempre de fora para dentro. Nenhuma linha de código existia dentro daquelas
caixas.

Este laboratório transforma o contexto `pedido` do `pacotes.puml` em código
Java de verdade: quatro classes, um teste JUnit 5, e a aplicação Spring Boot
respondendo em dois endpoints. É o primeiro laboratório do semestre que
produz código de aplicação; os cinco anteriores foram ambiente e modelagem.

> **Ainda sem Thymeleaf.** A camada de apresentação de hoje é a resposta em
> JSON do próprio `PedidoController`, anotado com `@RestController`. O
> `spring-boot-starter-thymeleaf` só entra na Aula 13, quando a camada de
> apresentação ganha uma tela HTML de verdade. Quem procurar uma view aqui
> não vai encontrar: a Visão de hoje é o JSON.

## 2. Pré-requisitos

- **O fork da Aula 01**, com `docs/arquitetura/pacotes.puml` e `dominio.puml`
  da Aula 05 já commitados e empurrados.
- **Java 21 LTS** e **Maven** ativos, conferidos na Aula 01.
- Nenhuma dependência nova no `pom.xml`: `spring-boot-starter-web`, que traz
  `@RestController` e o servidor embutido, já está no projeto desde o fork.

## 3. Passo a passo

### 3.1 Criar os pacotes

Dentro de `src/main/java/br/uni9/rotasul/`, criar quatro diretórios. Eles
correspondem um a um às caixas do `pacotes.puml` da Aula 05:

```
src/main/java/br/uni9/rotasul/
└── pedido/
    ├── domain/
    ├── repository/
    ├── service/
    └── web/
```

### 3.2 Escrever o domínio

Em `pedido/domain`, criar `Pedido`, com os atributos mínimos `id`, `cliente`,
`descricao` e `situacao`, construtor e getters. **Sem anotação de framework
nenhuma nesta classe**: o domínio não depende de Spring, e essa independência
vai importar na Aula 12, quando a injeção de dependência explícita entrar em
pauta.

```java
package br.uni9.rotasul.pedido.domain;

// Classe de domínio. Sem anotação de framework nenhuma: o domínio não
// depende de Spring, e essa independência vai importar na Aula 12, quando
// a injeção de dependência explícita entrar em pauta.
public class Pedido {

    private Long id;
    private final String cliente;
    private final String descricao;
    private String situacao;

    public Pedido(String cliente, String descricao) {
        this.cliente = cliente;
        this.descricao = descricao;
        this.situacao = "RECEBIDO";
    }

    public Long getId() {
        return id;
    }

    public void setId(Long id) {
        this.id = id;
    }

    public String getCliente() {
        return cliente;
    }

    public String getDescricao() {
        return descricao;
    }

    public String getSituacao() {
        return situacao;
    }

    public void setSituacao(String situacao) {
        this.situacao = situacao;
    }
}
```

### 3.3 Escrever o contrato de persistência

Em `pedido/repository`, criar a **interface** `PedidoRepository`, com dois
métodos: `salvar(Pedido)` e `listarTodos()`. Interface primeiro,
implementação depois: é a interface que permite trocar a implementação sem
tocar no serviço, o que vai acontecer quando o banco real entrar na Aula 14
(JDBC puro) e na Aula 15 (JPA).

```java
package br.uni9.rotasul.pedido.repository;

import java.util.List;

import br.uni9.rotasul.pedido.domain.Pedido;

// Interface primeiro, implementação depois: é ela que permite trocar a
// implementação sem tocar no serviço, o que vai acontecer quando o banco
// real entrar na Aula 14 (JDBC puro) e na Aula 15 (JPA).
public interface PedidoRepository {

    Pedido salvar(Pedido pedido);

    List<Pedido> listarTodos();
}
```

### 3.4 Escrever a implementação em memória

Ainda em `pedido/repository`, criar `PedidoRepositoryEmMemoria`, anotada com
`@Repository`, guardando os pedidos numa `List` e gerando o `id` com um
contador. O capítulo de hoje trata de camadas, não de persistência: trocar
esta classe por uma implementação com banco é exatamente o exercício da Aula
14, e depois da Aula 15. A separação de hoje é o que torna as duas trocas
baratas.

```java
package br.uni9.rotasul.pedido.repository;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.concurrent.atomic.AtomicLong;

import org.springframework.stereotype.Repository;

import br.uni9.rotasul.pedido.domain.Pedido;

// Implementação em memória. O capítulo de hoje trata de camadas, não de
// persistência: trocar esta classe por uma implementação com banco é o
// exercício da Aula 14 (JDBC puro) e, depois, da Aula 15 (JPA). A
// separação de hoje é o que torna as duas trocas baratas.
@Repository
public class PedidoRepositoryEmMemoria implements PedidoRepository {

    private final List<Pedido> pedidos = new ArrayList<>();
    private final AtomicLong contador = new AtomicLong(0);

    @Override
    public Pedido salvar(Pedido pedido) {
        pedido.setId(contador.incrementAndGet());
        pedidos.add(pedido);
        return pedido;
    }

    @Override
    public List<Pedido> listarTodos() {
        return Collections.unmodifiableList(pedidos);
    }
}
```

### 3.5 Compilar

```bash
./mvnw compile
```

Erro de compilação aqui é quase sempre pacote errado ou `import` faltando, e
é melhor descobrir agora do que no Ciclo 4.

### 3.6 Escrever o serviço

Em `pedido/service`, criar `PedidoService`, anotada com `@Service`,
recebendo `PedidoRepository` pelo construtor. Dois métodos: `registrar(Pedido)`,
que aplica a regra de negócio e delega ao repositório, e `listar()`, que
devolve a lista. **A regra mínima obrigatória: pedido sem cliente informado é
recusado**, com mensagem de erro em português.

```java
package br.uni9.rotasul.pedido.service;

import java.util.List;

import org.springframework.stereotype.Service;

import br.uni9.rotasul.pedido.domain.Pedido;
import br.uni9.rotasul.pedido.repository.PedidoRepository;

// A regra de negócio mora aqui, nunca no controlador. Recebe o
// repositório pelo construtor, sem framework de injeção de dependência
// explícito: isso é assunto da Aula 12.
@Service
public class PedidoService {

    private final PedidoRepository pedidoRepository;

    public PedidoService(PedidoRepository pedidoRepository) {
        this.pedidoRepository = pedidoRepository;
    }

    public Pedido registrar(Pedido pedido) {
        if (pedido.getCliente() == null || pedido.getCliente().isBlank()) {
            throw new IllegalArgumentException("Pedido sem cliente informado é recusado.");
        }
        return pedidoRepository.salvar(pedido);
    }

    public List<Pedido> listar() {
        return pedidoRepository.listarTodos();
    }
}
```

> **Quem quiser** acrescenta uma segunda regra tirada do seu próprio
> `docs/colaboracao.md`, da Aula 03.

### 3.7 Escrever o controlador

Em `pedido/web`, criar `PedidoController`, anotada com `@RestController` e
mapeada em `/pedidos`, com `GET` devolvendo a lista e `POST` recebendo o
pedido novo. **O controlador chama o serviço e não decide nada**: qualquer
`if` de negócio dentro dele reprova o critério de aceitação do dia.

```java
package br.uni9.rotasul.pedido.web;

import java.util.List;

import org.springframework.http.HttpStatus;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.ResponseStatus;
import org.springframework.web.bind.annotation.RestController;

import br.uni9.rotasul.pedido.domain.Pedido;
import br.uni9.rotasul.pedido.service.PedidoService;

// O controlador não decide nada de negócio: ele traduz requisição em
// chamada de método. Qualquer "if" de regra aqui reprova o critério de
// aceitação do dia.
@RestController
@RequestMapping("/pedidos")
public class PedidoController {

    private final PedidoService pedidoService;

    public PedidoController(PedidoService pedidoService) {
        this.pedidoService = pedidoService;
    }

    @GetMapping
    public List<Pedido> listar() {
        return pedidoService.listar();
    }

    @PostMapping
    @ResponseStatus(HttpStatus.CREATED)
    public Pedido registrar(@RequestBody Pedido pedido) {
        return pedidoService.registrar(pedido);
    }
}
```

> **Sobre o `Pedido` recebido no `POST`.** O Spring usa o único construtor
> público da classe (`Pedido(String cliente, String descricao)`) para montar
> o objeto a partir do JSON recebido, casando os nomes dos parâmetros com as
> chaves do corpo da requisição. Isso funciona porque o `spring-boot-starter-parent`
> já compila o projeto com a flag `-parameters` do `javac`, ativa por padrão
> desde as primeiras versões do Spring Boot 2. Nenhuma anotação extra é
> necessária no construtor.

### 3.8 Escrever o teste

Em `src/test/java/br/uni9/rotasul/pedido/service/`, criar
`PedidoServiceTest`, com JUnit 5 e no mínimo dois casos: um que registra um
pedido válido e confirma que ele aparece em `listar()`, e outro que registra
um pedido sem cliente e confirma que o serviço recusa. **O teste é do
serviço, não do controlador**, porque é no serviço que está a regra.

```java
package br.uni9.rotasul.pedido.service;

import static org.assertj.core.api.Assertions.assertThat;
import static org.assertj.core.api.Assertions.assertThatThrownBy;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import br.uni9.rotasul.pedido.domain.Pedido;
import br.uni9.rotasul.pedido.repository.PedidoRepositoryEmMemoria;

// Teste do serviço, não do controlador: é no serviço que está a regra.
class PedidoServiceTest {

    private PedidoService pedidoService;

    @BeforeEach
    void configurar() {
        pedidoService = new PedidoService(new PedidoRepositoryEmMemoria());
    }

    @Test
    void registraPedidoValidoEApareceNaListagem() {
        Pedido pedido = new Pedido("Lojista Ana", "Duas caixas de peças automotivas");

        pedidoService.registrar(pedido);

        assertThat(pedidoService.listar())
                .hasSize(1)
                .first()
                .satisfies(registrado -> {
                    assertThat(registrado.getId()).isNotNull();
                    assertThat(registrado.getCliente()).isEqualTo("Lojista Ana");
                    assertThat(registrado.getSituacao()).isEqualTo("RECEBIDO");
                });
    }

    @Test
    void recusaPedidoSemClienteInformado() {
        Pedido pedido = new Pedido("", "Pedido sem cliente");

        assertThatThrownBy(() -> pedidoService.registrar(pedido))
                .isInstanceOf(IllegalArgumentException.class)
                .hasMessage("Pedido sem cliente informado é recusado.");

        assertThat(pedidoService.listar()).isEmpty();
    }
}
```

```bash
./mvnw test
```

Os dois casos precisam passar.

### 3.9 Subir e conferir

```bash
./mvnw spring-boot:run
```

A primeira linha de log a procurar é a que traz a porta. **Usar sempre a
porta que o terminal imprimiu**, nunca uma porta fixa decorada. Noutro
terminal, trocando `8080` pela porta real:

```bash
curl http://localhost:8080/pedidos

curl -X POST http://localhost:8080/pedidos \
  -H "Content-Type: application/json" \
  -d '{"cliente":"Lojista Ana","descricao":"Duas caixas de peças automotivas"}'

curl http://localhost:8080/pedidos
```

Saída de referência, obtida rodando este mesmo gabarito com Java 21 e Maven
localmente (seção 6 do relatório desta tarefa detalha o ambiente):

```
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

Colar a saída do `GET /pedidos` (a última chamada, com o pedido já
registrado) no corpo do commit desta aula ou numa seção nova de
`docs/decisoes.md`.

> **Se testar o cliente vazio.** `POST` com `"cliente":""` devolve
> `500 Internal Server Error`, porque a `IllegalArgumentException` lançada
> pelo serviço ainda não tem um tratador de exceção dedicado no controlador.
> Isso é esperado hoje: o `PedidoServiceTest` já comprova a regra no nível
> certo (o serviço), e converter a exceção de negócio num `400 Bad Request`
> arrumado é conteúdo que a disciplina só formaliza mais adiante, quando a
> camada web ganha tratamento de erro. Não é bug do laboratório de hoje.

## 4. Entregável

No fork do aluno:

- As quatro classes de produção: `Pedido`, `PedidoRepository`,
  `PedidoRepositoryEmMemoria`, `PedidoService`, `PedidoController` (cinco
  arquivos, quatro papéis: domínio, contrato de dados, implementação de
  dados, regra de negócio e controle contam como as "quatro classes" do
  entregável porque interface e implementação do repositório são as duas
  metades do mesmo passo 4).
- `PedidoServiceTest`, em `src/test`, com os dois casos passando.
- A aplicação subindo com `./mvnw spring-boot:run` e respondendo em
  `GET /pedidos` e `POST /pedidos`.
- A saída do `GET /pedidos` colada no commit ou em `docs/decisoes.md`.

## 5. Critérios de aceitação

| Critério | Evidência conferida na correção |
|---|---|
| As quatro classes nos pacotes corretos | `pedido/domain`, `pedido/repository` (duas classes), `pedido/service`, `pedido/web`, batendo com `pacotes.puml` da Aula 05 |
| Nenhuma regra de negócio dentro do controlador | `PedidoController` só chama `pedidoService.listar()` e `pedidoService.registrar(pedido)`, sem `if` de negócio |
| Nenhuma anotação de framework na classe `Pedido` | `Pedido.java` sem `@Service`, `@Repository`, `@RestController` nem `@Entity` |
| O teste passa | `./mvnw test` roda `PedidoServiceTest` com os dois casos verdes |
| A aplicação responde nos dois endpoints | `GET /pedidos` devolve lista JSON, `POST /pedidos` devolve `201` com o pedido criado |
| A saída do `GET` está registrada | Corpo do commit da aula ou seção nova em `docs/decisoes.md` |
| O commit da aula existe | `git log` do fork mostra o commit `feat(pedido): primeira fatia em três camadas com repositório em memória` |

## 6. Commit e push esperados

```bash
git add src docs
git commit -m "feat(pedido): primeira fatia em três camadas com repositório em memória"
git push
```
