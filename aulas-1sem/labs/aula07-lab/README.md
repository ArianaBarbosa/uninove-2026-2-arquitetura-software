# Laboratório da Aula 07: contrato e implementações trocáveis por perfil

Disciplina Arquitetura de Software, Uninove, Prof. José Romualdo. Roteiro dos
Ciclos 3 e 4 do encontro: separação de contrato e implementação na camada de
serviço.

## 1. O passo do case que esta aula resolve

Na Aula 06 cada aluno entregou a primeira fatia em três camadas do pacote
`br.uni9.rotasul.pedido`: `PedidoController`, `PedidoService` como classe
concreta, a interface `PedidoRepository` e a implementação em memória
`PedidoRepositoryEmMemoria`. O repositório já tinha contrato separado de
implementação; o serviço, não. `PedidoService` era uma classe, e
`PedidoController` dependia diretamente dela.

Este laboratório aplica ao serviço a mesma lição que a Aula 06 já aplicou ao
repositório: `PedidoService` vira uma **interface**, com duas implementações
trocáveis por perfil do Spring, `PedidoServicePadrao` e
`PedidoServiceComAnaliseDeRisco`. O código de hoje não cria endpoint novo:
reorganiza o que já existe.

> **No vocabulário do capítulo de hoje (Arquitetura Orientada a Serviços,
> SOA).** A interface `PedidoService` é a Descrição de Serviço: o que o
> serviço faz e o que o Consumidor (`PedidoController`) precisa fornecer para
> usá-lo. Cada implementação concreta é um Provedor diferente por trás do
> mesmo contrato.

## 2. Pré-requisitos

- **O fork da Aula 01**, com o pacote `br.uni9.rotasul.pedido` da Aula 06 já
  commitado e empurrado: `PedidoController`, `PedidoService` (classe),
  `PedidoRepository` e `PedidoRepositoryEmMemoria`.
- **Java 21 LTS** e **Maven** ativos, conferidos na Aula 01.
- Nenhuma dependência nova no `pom.xml`: tudo o que este laboratório usa
  (`@Profile`, JUnit 5, AssertJ) já está disponível a partir do
  `spring-boot-starter-web` e do `spring-boot-starter-test`, presentes desde
  o fork.

## 3. Passo a passo

### 3.1 Extrair a interface

Em `pedido/service`, criar a interface `PedidoService` com as duas
assinaturas já existentes: `Pedido registrar(Pedido pedido)` e
`List<Pedido> listar()`. **Nenhuma anotação de framework na interface**: ela
é o contrato, não a implementação.

```java
package br.uni9.rotasul.pedido.service;

import java.util.List;

import br.uni9.rotasul.pedido.domain.Pedido;

// A interface é o contrato, não a implementação: nenhuma anotação de
// framework aqui. É a Descrição de Serviço do vocabulário de hoje, o que o
// Provedor faz e o que o Consumidor precisa fornecer para usá-lo.
public interface PedidoService {

    Pedido registrar(Pedido pedido);

    List<Pedido> listar();
}
```

### 3.2 Renomear a implementação atual

A classe `PedidoService` da Aula 06 passa a se chamar `PedidoServicePadrao` e
a implementar a interface `PedidoService`, mantendo o construtor que recebe
`PedidoRepository` e a regra de recusar pedido sem cliente. Anotar com
`@Service` e com `@Profile("padrao")`.

```java
package br.uni9.rotasul.pedido.service;

import java.util.List;

import org.springframework.context.annotation.Profile;
import org.springframework.stereotype.Service;

import br.uni9.rotasul.pedido.domain.Pedido;
import br.uni9.rotasul.pedido.repository.PedidoRepository;

// Provedor padrão da interface PedidoService, ativo no perfil "padrao". É a
// mesma classe PedidoService da Aula 06, renomeada e reclassificada como
// implementação de um contrato, não mais o contrato em si.
@Service
@Profile("padrao")
public class PedidoServicePadrao implements PedidoService {

    private final PedidoRepository pedidoRepository;

    public PedidoServicePadrao(PedidoRepository pedidoRepository) {
        this.pedidoRepository = pedidoRepository;
    }

    @Override
    public Pedido registrar(Pedido pedido) {
        if (pedido.getCliente() == null || pedido.getCliente().isBlank()) {
            throw new IllegalArgumentException("Pedido sem cliente informado é recusado.");
        }
        return pedidoRepository.salvar(pedido);
    }

    @Override
    public List<Pedido> listar() {
        return pedidoRepository.listarTodos();
    }
}
```

### 3.3 Ajustar o controlador

Conferir que `PedidoController` passa a receber `PedidoService`, a
interface, no construtor, e não mais o tipo concreto. Se o controlador ainda
importar `PedidoServicePadrao` em algum lugar, é sinal de que a separação
não terminou.

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

// O controlador depende só da interface PedidoService, nunca de
// PedidoServicePadrao ou PedidoServiceComAnaliseDeRisco. Qual das duas o
// Spring injeta é decidido pelo perfil ativo, fora desta classe.
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

O texto do construtor não muda uma letra em relação à Aula 06:
`pedidoService` já era o nome do parâmetro. O que muda é o **tipo** que esse
nome designa, de `PedidoService` classe para `PedidoService` interface.

### 3.4 Configurar o perfil padrão

Em `src/main/resources/application.properties`, acrescentar:

```properties
spring.profiles.active=padrao
```

Sem essa linha, nenhum bean de `PedidoService` fica ativo, porque os dois
candidatos estão guardados por `@Profile`, e o Spring recusa subir sem um
deles disponível. Rodar `./mvnw spring-boot:run` e conferir que
`GET /pedidos` continua respondendo exatamente como na Aula 06.

### 3.5 Criar a segunda implementação

`PedidoServiceComAnaliseDeRisco`, também implementando `PedidoService`,
anotada `@Service` e `@Profile("risco")`, recebendo `PedidoRepository` pelo
mesmo construtor. Mantém a regra herdada, pedido sem cliente é recusado, e
acrescenta uma segunda: um conjunto fixo de lojistas bloqueados, e pedido de
um lojista bloqueado também é recusado.

```java
package br.uni9.rotasul.pedido.service;

import java.util.List;
import java.util.Set;

import org.springframework.context.annotation.Profile;
import org.springframework.stereotype.Service;

import br.uni9.rotasul.pedido.domain.Pedido;
import br.uni9.rotasul.pedido.repository.PedidoRepository;

// Segundo Provedor da mesma interface PedidoService, ativo no perfil
// "risco". Herda a regra de recusar pedido sem cliente e acrescenta a
// recusa de lojista bloqueado. A assinatura dos métodos é idêntica à de
// PedidoServicePadrao: é isso que torna as duas implementações trocáveis.
@Service
@Profile("risco")
public class PedidoServiceComAnaliseDeRisco implements PedidoService {

    private static final Set<String> LOJISTAS_BLOQUEADOS = Set.of("LOJISTA-BLOQUEADO");

    private final PedidoRepository pedidoRepository;

    public PedidoServiceComAnaliseDeRisco(PedidoRepository pedidoRepository) {
        this.pedidoRepository = pedidoRepository;
    }

    @Override
    public Pedido registrar(Pedido pedido) {
        if (pedido.getCliente() == null || pedido.getCliente().isBlank()) {
            throw new IllegalArgumentException("Pedido sem cliente informado é recusado.");
        }
        if (LOJISTAS_BLOQUEADOS.contains(pedido.getCliente())) {
            throw new IllegalArgumentException("Pedido de lojista bloqueado por análise de risco é recusado.");
        }
        return pedidoRepository.salvar(pedido);
    }

    @Override
    public List<Pedido> listar() {
        return pedidoRepository.listarTodos();
    }
}
```

A assinatura dos métodos é idêntica à da outra implementação: é exatamente
isso que faz das duas implementações trocáveis.

### 3.6 Escrever a suíte de contrato

Em `src/test/java/br/uni9/rotasul/pedido/service/`, criar a classe abstrata
`PedidoServiceContratoTest`, com um método `protected abstract PedidoService
criarServico()` e dois testes: `registraPedidoValidoEApareceNaListagem`, que
registra um pedido com cliente e confirma que ele aparece em `listar()`, e
`recusaPedidoSemClienteInformado`, que confirma a recusa. **Nenhum dos dois
testes sabe qual implementação está rodando**: eles testam apenas o
contrato.

```java
package br.uni9.rotasul.pedido.service;

import static org.assertj.core.api.Assertions.assertThat;
import static org.assertj.core.api.Assertions.assertThatThrownBy;

import org.junit.jupiter.api.Test;

import br.uni9.rotasul.pedido.domain.Pedido;

// Suíte de contrato: testa a interface PedidoService, nunca uma
// implementação específica. Cada subclasse concreta só precisa dizer qual
// implementação está sendo testada; os dois métodos abaixo rodam iguais
// para as duas.
abstract class PedidoServiceContratoTest {

    protected abstract PedidoService criarServico();

    @Test
    void registraPedidoValidoEApareceNaListagem() {
        PedidoService pedidoService = criarServico();
        Pedido pedido = new Pedido("Lojista Ana", "Duas caixas de peças automotivas");

        pedidoService.registrar(pedido);

        assertThat(pedidoService.listar())
                .hasSize(1)
                .first()
                .satisfies(registrado -> {
                    assertThat(registrado.getId()).isNotNull();
                    assertThat(registrado.getCliente()).isEqualTo("Lojista Ana");
                });
    }

    @Test
    void recusaPedidoSemClienteInformado() {
        PedidoService pedidoService = criarServico();
        Pedido pedido = new Pedido("", "Pedido sem cliente");

        assertThatThrownBy(() -> pedidoService.registrar(pedido))
                .isInstanceOf(IllegalArgumentException.class)
                .hasMessage("Pedido sem cliente informado é recusado.");

        assertThat(pedidoService.listar()).isEmpty();
    }
}
```

### 3.7 Estender a suíte para cada implementação

Duas classes concretas, `PedidoServicePadraoContratoTest` e
`PedidoServiceComAnaliseDeRiscoContratoTest`, cada uma implementando
`criarServico()` para devolver a sua própria implementação, com um novo
`PedidoRepositoryEmMemoria` a cada teste.

```java
package br.uni9.rotasul.pedido.service;

import br.uni9.rotasul.pedido.repository.PedidoRepositoryEmMemoria;

// Roda os dois testes da suíte de contrato contra PedidoServicePadrao, com
// um PedidoRepositoryEmMemoria novo a cada teste.
class PedidoServicePadraoContratoTest extends PedidoServiceContratoTest {

    @Override
    protected PedidoService criarServico() {
        return new PedidoServicePadrao(new PedidoRepositoryEmMemoria());
    }
}
```

```java
package br.uni9.rotasul.pedido.service;

import br.uni9.rotasul.pedido.repository.PedidoRepositoryEmMemoria;

// Roda os dois testes da suíte de contrato contra
// PedidoServiceComAnaliseDeRisco, com um PedidoRepositoryEmMemoria novo a
// cada teste. Os dois métodos herdados não sabem, e não precisam saber, que
// esta implementação também recusa lojista bloqueado.
class PedidoServiceComAnaliseDeRiscoContratoTest extends PedidoServiceContratoTest {

    @Override
    protected PedidoService criarServico() {
        return new PedidoServiceComAnaliseDeRisco(new PedidoRepositoryEmMemoria());
    }
}
```

```bash
./mvnw test
```

Os dois métodos da classe abstrata executam duas vezes, uma para cada
implementação: **as quatro execuções precisam passar.**

### 3.8 Confirmar a troca de perfil em tempo de execução

Subir a aplicação com o perfil `risco` e enviar, por `curl` ou pelo
navegador, um `POST /pedidos` com o cliente `LOJISTA-BLOQUEADO`. A resposta
precisa ser de recusa. Voltar a subir sem o parâmetro de perfil, que volta
para `padrao`, e enviar o mesmo pedido: a resposta precisa ser de sucesso.

```bash
./mvnw spring-boot:run -Dspring-boot.run.profiles=risco
# noutro terminal, trocando 8080 pela porta que o seu terminal imprimiu
curl -i -X POST http://localhost:8080/pedidos \
  -H "Content-Type: application/json" \
  -d '{"cliente":"LOJISTA-BLOQUEADO","descricao":"Pedido suspeito"}'
```

```bash
./mvnw spring-boot:run
# mesmo POST, agora sem o perfil risco
curl -i -X POST http://localhost:8080/pedidos \
  -H "Content-Type: application/json" \
  -d '{"cliente":"LOJISTA-BLOQUEADO","descricao":"Pedido suspeito"}'
```

Saída de referência, obtida rodando este mesmo gabarito com Java 21 e Maven
localmente (seção 5 do relatório desta tarefa detalha o ambiente):

```
$ ./mvnw spring-boot:run -Dspring-boot.run.profiles=risco
...
The following 1 profile is active: "risco"
...
Started RotaSulApplication in 0.46 seconds

$ curl -i -X POST http://localhost:8080/pedidos \
  -H "Content-Type: application/json" \
  -d '{"cliente":"LOJISTA-BLOQUEADO","descricao":"Pedido suspeito"}'
HTTP/1.1 500
Content-Type: application/json

{"timestamp":"2026-08-12T06:12:27.623+00:00","status":500,"error":"Internal Server Error","path":"/pedidos"}

$ curl -i -X POST http://localhost:8080/pedidos \
  -H "Content-Type: application/json" \
  -d '{"cliente":"Lojista Ana","descricao":"Duas caixas"}'
HTTP/1.1 201
Content-Type: application/json

{"id":1,"cliente":"Lojista Ana","descricao":"Duas caixas","situacao":"RECEBIDO"}
```

```
$ ./mvnw spring-boot:run
...
The following 1 profile is active: "padrao"
...
Started RotaSulApplication in 0.51 seconds

$ curl -i -X POST http://localhost:8080/pedidos \
  -H "Content-Type: application/json" \
  -d '{"cliente":"LOJISTA-BLOQUEADO","descricao":"Pedido suspeito"}'
HTTP/1.1 201
Content-Type: application/json

{"id":2,"cliente":"LOJISTA-BLOQUEADO","descricao":"Pedido suspeito","situacao":"RECEBIDO"}
```

> **Sobre o `500` no perfil `risco`.** A `IllegalArgumentException` lançada
> pelo serviço ainda não tem um tratador de exceção dedicado no controlador,
> exatamente como já era o caso na Aula 06 para o cliente vazio. Isso é
> esperado hoje: os testes de contrato já comprovam a recusa no nível certo
> (o serviço), e converter a exceção de negócio num `400 Bad Request`
> arrumado é conteúdo que a disciplina só formaliza mais adiante. Não é bug
> do laboratório de hoje.

**Colar as duas evidências (recusa no perfil `risco`, sucesso no perfil
`padrao`) no corpo do commit da aula.**

### 3.9 Registrar a decisão

Em `docs/decisoes.md`, acrescentar uma linha explicando o padrão de
contrato mais implementações trocáveis por perfil, ligando ao vocabulário de
hoje: a interface é a Descrição de Serviço, e cada implementação é um
Provedor diferente por trás do mesmo contrato.

## 4. Entregável

No fork do aluno:

- A interface `PedidoService`, em `pedido/service`, sem anotação de
  framework.
- As duas implementações, `PedidoServicePadrao` (perfil `padrao`) e
  `PedidoServiceComAnaliseDeRisco` (perfil `risco`).
- A suíte de teste `PedidoServiceContratoTest` (classe abstrata) estendida
  por `PedidoServicePadraoContratoTest` e
  `PedidoServiceComAnaliseDeRiscoContratoTest`.
- `PedidoController` recebendo `PedidoService`, a interface, no construtor.
- `application.properties` com `spring.profiles.active=padrao`.
- As duas evidências de troca de perfil (recusa em `risco`, sucesso em
  `padrao`) coladas no commit ou em `docs/decisoes.md`.

## 5. Critérios de aceitação

| Critério | Evidência conferida na correção |
|---|---|
| `./mvnw test` passando | Quatro execuções verdes: os dois testes da suíte abstrata, duas vezes, uma por implementação |
| Nenhuma anotação de framework na interface | `PedidoService.java` sem `@Service`, `@Repository`, `@Profile` nem qualquer outra anotação do Spring |
| `PedidoController` depende só da interface | Nenhum import de `PedidoServicePadrao` nem de `PedidoServiceComAnaliseDeRisco` no controlador |
| As duas implementações são trocáveis | Assinatura idêntica dos métodos `registrar` e `listar` nas duas classes |
| Troca de perfil muda o comportamento observável | `POST` do lojista bloqueado recusado no perfil `risco`, aceito no perfil `padrao`, sem qualquer alteração no controlador |
| A decisão está registrada | Linha nova em `docs/decisoes.md` explicando o padrão |
| O commit da aula existe | `git log` do fork mostra o commit `feat(pedido): separa contrato PedidoService de duas implementações trocáveis por perfil` |

## 6. Commit e push esperados

```bash
git add src docs
git commit -m "feat(pedido): separa contrato PedidoService de duas implementações trocáveis por perfil"
git push
```
