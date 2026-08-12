# Laboratório da Aula 09: `Remessa` em JSON e em XML, por negociação de conteúdo

Disciplina Arquitetura de Software, Uninove, Prof. José Romualdo. Roteiro dos
Ciclos 3 e 4 do encontro: nasce o contexto `expedicao`, e um único endpoint
responde em dois formatos, escolhidos pelo cabeçalho HTTP `Accept`.

## 1. O passo do case que esta aula resolve

Na Aula 08 cada aluno entregou o `.jar` executável rodando com `java -jar`,
mais `docs/empacotamento.md`, comparando esse modelo com o WAR do capítulo.
A aplicação já roda sozinha; a pergunta de hoje é sobre o que ela devolve
quando alguém pergunta algo a ela.

Este laboratório abre o segundo contexto do case, `expedicao`, já previsto
no `pacotes.puml` da Aula 05: `RemessaController`, `RemessaService`, a
interface `RemessaRepository` e a classe de domínio `Remessa`. O contexto
`pedido` da Aula 06 continua existindo, sem alteração; hoje o código novo
mora inteiro em `br.uni9.rotasul.expedicao`.

> **A pergunta central de hoje.** O capítulo apresenta XML e JSON como dois
> formatos de metadados, mas não explica como um mesmo endpoint escolhe
> entre eles: isso é técnica de HTTP e do framework web, posterior ao
> material. É a aplicação prática do princípio que o próprio capítulo já
> estabelece, que XML e JSON "podem ser usados como protocolos ou
> interfaces de comunicação": cabe ao sistema decidir qual usar para cada
> consumidor, e essa decisão é feita comparando o cabeçalho `Accept` da
> requisição com o que o endpoint declara que produz.

## 2. Pré-requisitos

- **O fork da Aula 08**, com o `.jar` executável e `docs/empacotamento.md`
  já commitados e empurrados. O contexto `pedido` (`PedidoController`, a
  interface `PedidoService` e as duas implementações) continua no fork,
  sem alteração.
- **Java 21 LTS** e **Maven** ativos, conferidos na Aula 01.
- **Uma dependência nova no `pom.xml`**: `jackson-dataformat-xml`, passo
  3.5 abaixo. Sem ela, o laboratório de hoje não funciona.

## 3. Passo a passo

### 3.1 Criar o pacote de expedição

Dentro de `src/main/java/br/uni9/rotasul/`, criar as quatro camadas do novo
contexto, seguindo a mesma convenção contexto primeiro, camada depois, do
`pacotes.puml` da Aula 05:

```
src/main/java/br/uni9/rotasul/
└── expedicao/
    ├── domain/
    ├── repository/
    ├── service/
    └── web/
```

### 3.2 Escrever o domínio

Em `expedicao/domain`, criar `Remessa`, com `id`, `codigoRastreio`,
`previsaoEntrega` e `situacao`.

```java
package br.uni9.rotasul.expedicao.domain;

import java.time.LocalDate;

import com.fasterxml.jackson.dataformat.xml.annotation.JacksonXmlRootElement;

// Domínio sem anotação de framework é a regra da Aula 06. Esta classe leva
// uma única exceção pontual: @JacksonXmlRootElement é anotação de
// serialização, não de persistência nem de web, e existe só porque, sem
// ela, a tag raiz do XML sairia "Remessa" (o nome da classe Java), em vez
// de "remessa", o nome de domínio em português que a Rota Sul usa em toda
// outra referência à entidade. A exceção fica registrada aqui e não vira
// regra geral: nenhuma outra anotação do Spring ou de persistência entra
// nesta classe.
@JacksonXmlRootElement(localName = "remessa")
public class Remessa {

    private Long id;
    private final String codigoRastreio;
    private final LocalDate previsaoEntrega;
    private String situacao;

    public Remessa(Long id, String codigoRastreio, LocalDate previsaoEntrega, String situacao) {
        this.id = id;
        this.codigoRastreio = codigoRastreio;
        this.previsaoEntrega = previsaoEntrega;
        this.situacao = situacao;
    }

    public Long getId() {
        return id;
    }

    public String getCodigoRastreio() {
        return codigoRastreio;
    }

    public LocalDate getPrevisaoEntrega() {
        return previsaoEntrega;
    }

    public String getSituacao() {
        return situacao;
    }

    public void setSituacao(String situacao) {
        this.situacao = situacao;
    }
}
```

> **Por que só esta classe tem anotação de framework no domínio.** A regra
> da Aula 06 continua valendo: o domínio não depende de Spring, nem de
> JPA, nem de nenhum framework de persistência ou de web. A exceção de hoje
> é estritamente sobre como o Jackson nomeia a tag raiz na serialização
> XML, uma preocupação que não existe em JSON (o JSON não tem "tag raiz").
> Se esta classe algum dia ganhar `@Entity` ou `@RestController`, isso
> quebra a regra; `@JacksonXmlRootElement` não quebra, porque não descreve
> nem persistência nem rota HTTP, só o nome de um elemento na
> serialização.

### 3.3 Escrever o repositório

Interface primeiro, implementação depois, a mesma convenção da Aula 06:

```java
package br.uni9.rotasul.expedicao.repository;

import br.uni9.rotasul.expedicao.domain.Remessa;

public interface RemessaRepository {

    Remessa buscarPorId(Long id);
}
```

```java
package br.uni9.rotasul.expedicao.repository;

import java.time.LocalDate;
import java.util.HashMap;
import java.util.Map;

import org.springframework.stereotype.Repository;

import br.uni9.rotasul.expedicao.domain.Remessa;

// Pré-carregada com remessas de exemplo, no mesmo espírito da
// PedidoRepositoryEmMemoria da Aula 06: o assunto de hoje é o formato da
// resposta, não a persistência.
@Repository
public class RemessaRepositoryEmMemoria implements RemessaRepository {

    private final Map<Long, Remessa> remessas = new HashMap<>();

    public RemessaRepositoryEmMemoria() {
        remessas.put(1L, new Remessa(1L, "RS-0001", LocalDate.of(2026, 8, 20), "EM_TRANSITO"));
        remessas.put(2L, new Remessa(2L, "RS-0002", LocalDate.of(2026, 8, 22), "AGUARDANDO_COLETA"));
        remessas.put(3L, new Remessa(3L, "RS-0003", LocalDate.of(2026, 8, 18), "ENTREGUE"));
    }

    @Override
    public Remessa buscarPorId(Long id) {
        return remessas.get(id);
    }
}
```

### 3.4 Escrever o serviço

`RemessaService`, anotado `@Service`, delegando ao repositório:

```java
package br.uni9.rotasul.expedicao.service;

import org.springframework.stereotype.Service;

import br.uni9.rotasul.expedicao.domain.Remessa;
import br.uni9.rotasul.expedicao.repository.RemessaRepository;

@Service
public class RemessaService {

    private final RemessaRepository remessaRepository;

    public RemessaService(RemessaRepository remessaRepository) {
        this.remessaRepository = remessaRepository;
    }

    public Remessa buscarPorId(Long id) {
        return remessaRepository.buscarPorId(id);
    }
}
```

### 3.5 Adicionar o módulo Jackson XML

No `pom.xml` do fork, dentro de `<dependencies>`:

```xml
<dependency>
  <groupId>com.fasterxml.jackson.dataformat</groupId>
  <artifactId>jackson-dataformat-xml</artifactId>
</dependency>
```

Sem ela, o Spring só tem o conversor de JSON disponível (o que já vem com
`spring-boot-starter-web`, via Jackson), e qualquer pedido de
`Accept: application/xml` recebe `406 Not Acceptable`. Com ela no
classpath, o Spring passa a ter um segundo conversor, `MappingJackson2XmlHttpMessageConverter`,
e escolhe entre os dois automaticamente.

### 3.6 Escrever o controlador

`RemessaController`, em `expedicao/web`, mapeado em `/remessas`, com
`GET /remessas/{id}` declarando os dois formatos que produz:

```java
package br.uni9.rotasul.expedicao.web;

import org.springframework.http.MediaType;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import br.uni9.rotasul.expedicao.domain.Remessa;
import br.uni9.rotasul.expedicao.service.RemessaService;

// O Spring escolhe sozinho entre os dois conversores, JSON e XML,
// comparando esta lista de "produces" com o header Accept da requisição.
// Um único endpoint, uma única URI: dois formatos de resposta, não dois
// recursos.
@RestController
@RequestMapping("/remessas")
public class RemessaController {

    private final RemessaService remessaService;

    public RemessaController(RemessaService remessaService) {
        this.remessaService = remessaService;
    }

    @GetMapping(value = "/{id}", produces = { MediaType.APPLICATION_JSON_VALUE, MediaType.APPLICATION_XML_VALUE })
    public Remessa buscarPorId(@PathVariable Long id) {
        return remessaService.buscarPorId(id);
    }
}
```

### 3.7 Subir e testar manualmente

```bash
./mvnw spring-boot:run
```

```bash
# noutro terminal, trocando 8080 pela porta que o seu terminal imprimiu
curl -H "Accept: application/json" http://localhost:8080/remessas/1
curl -H "Accept: application/xml" http://localhost:8080/remessas/1
```

Saída de referência, obtida rodando este mesmo gabarito com Java 21 e Maven
localmente (seção 6 do relatório desta tarefa detalha o ambiente):

```
$ curl -H "Accept: application/json" http://localhost:8080/remessas/1
{"id":1,"codigoRastreio":"RS-0001","previsaoEntrega":"2026-08-20","situacao":"EM_TRANSITO"}

$ curl -H "Accept: application/xml" http://localhost:8080/remessas/1
<remessa><id>1</id><codigoRastreio>RS-0001</codigoRastreio><previsaoEntrega>2026-08-20</previsaoEntrega><situacao>EM_TRANSITO</situacao></remessa>
```

Conferir três coisas: a tag raiz do XML é `<remessa>`, não `<Remessa>` (é a
anotação do passo 3.2 fazendo efeito); o conteúdo dos dois é o mesmo dado;
e `previsaoEntrega` sai como `"2026-08-20"` em JSON e `<previsaoEntrega>2026-08-20</previsaoEntrega>`
em XML, sem configuração extra de data em nenhum dos dois lados, porque o
Spring Boot já registra o suporte a `java.time` nos dois conversores.

> **Se testar um `Accept` que nenhum dos dois conversores produz** (por
> exemplo, `Accept: text/plain`), a resposta é `406 Not Acceptable`, o
> mesmo erro que qualquer pedido de XML recebia antes do passo 3.5.

### 3.8 Escrever o teste

Em `src/test/java/br/uni9/rotasul/expedicao/web/`, criar
`RemessaControllerTest`, anotada com `@WebMvcTest(RemessaController.class)`
e `MockMvc`, com dois métodos:

```java
package br.uni9.rotasul.expedicao.web;

import static org.mockito.Mockito.when;
import static org.springframework.test.web.servlet.request.MockMvcRequestBuilders.get;
import static org.springframework.test.web.servlet.result.MockMvcResultMatchers.content;
import static org.springframework.test.web.servlet.result.MockMvcResultMatchers.status;

import java.time.LocalDate;

import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.autoconfigure.web.servlet.WebMvcTest;
import org.springframework.boot.test.mock.mockito.MockBean;
import org.springframework.http.MediaType;
import org.springframework.test.web.servlet.MockMvc;

import br.uni9.rotasul.expedicao.domain.Remessa;
import br.uni9.rotasul.expedicao.service.RemessaService;

// @WebMvcTest sobe só a camada web, com o RemessaService trocado por um
// mock: o que este teste comprova é a negociação de conteúdo do
// controlador, não a regra do serviço nem a implementação do repositório.
@WebMvcTest(RemessaController.class)
class RemessaControllerTest {

    @Autowired
    private MockMvc mockMvc;

    @MockBean
    private RemessaService remessaService;

    @Test
    void respondeEmJsonQuandoOAcceptPedeJson() throws Exception {
        Remessa remessa = new Remessa(1L, "RS-0001", LocalDate.of(2026, 8, 20), "EM_TRANSITO");
        when(remessaService.buscarPorId(1L)).thenReturn(remessa);

        mockMvc.perform(get("/remessas/1").accept(MediaType.APPLICATION_JSON))
                .andExpect(status().isOk())
                .andExpect(content().contentType(MediaType.APPLICATION_JSON));
    }

    @Test
    void respondeEmXmlQuandoOAcceptPedeXml() throws Exception {
        Remessa remessa = new Remessa(1L, "RS-0001", LocalDate.of(2026, 8, 20), "EM_TRANSITO");
        when(remessaService.buscarPorId(1L)).thenReturn(remessa);

        mockMvc.perform(get("/remessas/1").accept(MediaType.APPLICATION_XML))
                .andExpect(status().isOk())
                .andExpect(content().contentType(MediaType.APPLICATION_XML));
    }
}
```

```bash
./mvnw test
```

Saída de referência, obtida rodando este mesmo gabarito:

```
[INFO] Tests run: 2, Failures: 0, Errors: 0, Skipped: 0 -- in br.uni9.rotasul.expedicao.web.RemessaControllerTest
[INFO] Tests run: 2, Failures: 0, Errors: 0, Skipped: 0
[INFO] BUILD SUCCESS
```

Os dois métodos precisam passar.

### 3.9 Registrar a decisão

Em `docs/decisoes.md`, uma linha nova explicando a escolha de um único
endpoint com negociação de conteúdo, em vez de dois endpoints separados,
um para cada formato. Exemplo:

> Formato de resposta de `/remessas/{id}`: um único endpoint com
> negociação de conteúdo pelo cabeçalho `Accept` (não dois endpoints, um
> `/remessas/{id}.json` e outro `/remessas/{id}.xml`), porque um único
> recurso deve ter uma única URI, princípio que a Aula 10, sobre REST, vai
> formalizar.

## 4. Entregável

No fork do aluno:

- O pacote `br.uni9.rotasul.expedicao`, com `domain`, `repository`,
  `service` e `web`.
- `Remessa`, com `@JacksonXmlRootElement(localName = "remessa")` como única
  anotação de framework no domínio.
- `RemessaRepository` (interface) e `RemessaRepositoryEmMemoria`.
- `RemessaService`.
- `RemessaController`, respondendo `GET /remessas/{id}` em JSON e em XML
  conforme o `Accept`.
- `pom.xml` com a dependência `jackson-dataformat-xml`.
- `RemessaControllerTest`, cobrindo os dois formatos.
- As duas evidências de `curl` (JSON e XML) coladas no commit ou em
  `docs/decisoes.md`.
- `docs/decisoes.md` com a linha nova sobre a negociação de conteúdo.

## 5. Critérios de aceitação

| Critério | Evidência conferida na correção |
|---|---|
| `Accept: application/json` devolve JSON | Saída do `curl` colada no commit, com `Content-Type: application/json` |
| `Accept: application/xml` devolve XML válido | Saída do `curl` colada no commit, com `Content-Type: application/xml` e a tag raiz `<remessa>` |
| Os dois formatos trazem os mesmos dados da `Remessa` | Comparação visual das duas saídas coladas |
| Nenhum endpoint duplicado por formato | Um único método `buscarPorId`, mapeado só em `GET /remessas/{id}`, no controlador |
| Nenhuma anotação de framework no domínio além da exceção documentada | `Remessa.java` só leva `@JacksonXmlRootElement`; nenhuma anotação de Spring ou de persistência |
| `./mvnw test` passando | Os dois métodos de `RemessaControllerTest` verdes |
| A decisão está registrada | Linha nova em `docs/decisoes.md` explicando a escolha de negociação de conteúdo |
| O commit da aula existe | `git log` do fork mostra o commit `feat(expedicao): remessa em JSON e em XML por negociação de conteúdo` |

## 6. Commit e push esperados

```bash
git add src/main/java/br/uni9/rotasul/expedicao src/test/java/br/uni9/rotasul/expedicao pom.xml docs
git commit -m "feat(expedicao): remessa em JSON e em XML por negociação de conteúdo"
git push
```
