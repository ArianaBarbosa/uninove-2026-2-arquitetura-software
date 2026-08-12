# Laboratório da Aula 10: cliente SOAP para o parceiro legado, e a API REST documentada

Disciplina Arquitetura de Software, Uninove, Prof. José Romualdo. Roteiro dos
Ciclos 3 e 4 do encontro: a Rota Sul consome, por SOAP, um endpoint que simula
o parceiro legado dentro do próprio fork, e documenta a API REST de remessas
com springdoc-openapi.

## 0. O que chega pronto neste kit

Dois arquivos são andaime, não conteúdo da aula, e chegam prontos para o
aluno copiar:

| Arquivo | Onde entra no fork | Papel |
|---|---|---|
| [`src/main/resources/parceiro.xsd`](src/main/resources/parceiro.xsd) | `src/main/resources/parceiro.xsd` | Contrato do serviço: o que o parceiro espera receber e o que devolve |
| [`src/main/java/br/uni9/rotasul/parceiro/WebServiceConfig.java`](src/main/java/br/uni9/rotasul/parceiro/WebServiceConfig.java) | `src/main/java/br/uni9/rotasul/parceiro/WebServiceConfig.java` | Publica o `MessageDispatcherServlet` em `/ws/*` e expõe o WSDL a partir do XSD |

Escrever um XSD à mão e acertar os três beans de configuração do Spring Web
Services consumiria o laboratório inteiro e não ensinaria nada sobre objetos
remotos. O que ensina, e o que o aluno escreve hoje, são três peças: o
`@Endpoint` que atende, o cliente que chama, e o teste que prova. Todo o
código dos passos 3.4, 3.6 e 3.8 abaixo é o que o aluno escreve; os passos
3.1 (cópia do kit) e 3.5 (subir e olhar o WSDL gerado) usam os dois arquivos
prontos sem alteração.

## 1. O passo do case que esta aula resolve

Na Aula 09 cada aluno entregou `RemessaController`, respondendo
`GET /remessas/{id}` em JSON ou em XML conforme o cabeçalho `Accept`. A Rota
Sul já sabe falar dois formatos com quem pergunta em português, por assim
dizer, o mesmo protocolo HTTP que ela usa desde a Aula 06. A pergunta de hoje
é mais dura: e quando quem pergunta é um sistema mais antigo, que só fala um
protocolo específico, com regras próprias de envelope e assinatura?

A Rota Sul não tem um parceiro real para a turma acessar, então este
laboratório simula o parceiro legado dentro do próprio fork: um endpoint SOAP
simples, no pacote `br.uni9.rotasul.parceiro`, representando o sistema que a
transportadora parceira expõe. O cliente que a turma escreve na sequência é o
mesmo tipo de código que se escreveria para consumir um parceiro de verdade;
só o endereço muda.

## 2. Pré-requisitos

- **O fork da Aula 09**, com o contexto `expedicao` (`RemessaController`,
  `RemessaService`, `RemessaRepository`, `Remessa`) já commitado e empurrado.
- **Java 21 LTS** e **Maven** ativos, conferidos na Aula 01.
- **Os dois arquivos da seção 0**, copiados para as posições indicadas.
- **Três dependências novas no `pom.xml`**: `spring-boot-starter-web-services`,
  `wsdl4j` e `springdoc-openapi-starter-webmvc-ui`, mais o plugin
  `jaxb2-maven-plugin`, passos 3.2 e 3.9 abaixo.

## 3. Passo a passo

### 3.1 Instalar o kit e ler o contrato (Ciclo 3)

Copiar os dois arquivos da seção 0 para as posições correspondentes no fork,
e criar o pacote `br.uni9.rotasul.parceiro` com os subpacotes `endpoint` (o
parceiro simulado) e `client` (quem consome, do lado da Rota Sul). É o
primeiro contexto que se soma aos três da Aula 05 (`pedido`, `expedicao` e
`rastreamento`): acrescenta contexto novo ao lado dos existentes, nunca
renomeia os já fixados.

```
src/main/java/br/uni9/rotasul/
└── parceiro/
    ├── endpoint/
    └── client/
```

O `parceiro.xsd` do kit define os dois elementos do contrato:

```xml
<xs:element name="consultaEntregaRequest">
  <xs:complexType>
    <xs:sequence>
      <xs:element name="codigoRastreio" type="xs:string"/>
    </xs:sequence>
  </xs:complexType>
</xs:element>

<xs:element name="consultaEntregaResponse">
  <xs:complexType>
    <xs:sequence>
      <xs:element name="situacao" type="xs:string"/>
      <xs:element name="previsaoEntrega" type="xs:date"/>
    </xs:sequence>
  </xs:complexType>
</xs:element>
```

O XSD faz aqui o papel que o capítulo chamou de Descrição de Serviço na Aula
07: diz o que o Provedor espera receber e o que ele devolve.

### 3.2 Adicionar as dependências e o gerador de classes

No `pom.xml` do fork, dentro de `<dependencies>`:

```xml
<dependency>
  <groupId>org.springframework.boot</groupId>
  <artifactId>spring-boot-starter-web-services</artifactId>
</dependency>
<dependency>
  <groupId>wsdl4j</groupId>
  <artifactId>wsdl4j</artifactId>
</dependency>
<dependency>
  <groupId>org.glassfish.jaxb</groupId>
  <artifactId>jaxb-runtime</artifactId>
</dependency>
```

`spring-boot-starter-web-services` e `wsdl4j` já estão fixados no contrato
técnico da disciplina desde a Aula 01. `jaxb-runtime` entra porque o Java 21
não traz mais o módulo `java.xml.bind`; sem ele, o `Jaxb2Marshaller` do passo
3.6 não encontra implementação de JAXB no classpath.

E, dentro de `<build><plugins>`, o `jaxb2-maven-plugin`, **com a versão presa
na linha 3.x**:

```xml
<plugin>
  <groupId>org.codehaus.mojo</groupId>
  <artifactId>jaxb2-maven-plugin</artifactId>
  <version>3.2.0</version>
  <executions>
    <execution>
      <id>xjc</id>
      <goals><goal>xjc</goal></goals>
    </execution>
  </executions>
  <configuration>
    <sources><source>src/main/resources/parceiro.xsd</source></sources>
    <packageName>br.uni9.rotasul.parceiro.gerado</packageName>
  </configuration>
</plugin>
```

> **A versão precisa ser dita em voz alta, não só copiada.** A linha 2.x do
> plugin gera classes anotadas com `javax.xml.bind`, o pacote antigo; o
> Spring Boot 3.x sobre Java 21 usa `jakarta.xml.bind`, e o `Jaxb2Marshaller`
> do passo 3.6 simplesmente não reconhece as classes geradas pela linha
> antiga. O sintoma é um erro de contexto JAXB que não menciona versão
> nenhuma, e é o tipo de armadilha que trava um aluno por quarenta minutos.
> Sem `<version>` explícito, o Maven pode resolver a linha 2.x.

### 3.3 Gerar as classes Java do XSD

```bash
./mvnw generate-sources
```

Conferir em `target/generated-sources/jaxb/br/uni9/rotasul/parceiro/gerado/`
as classes `ConsultaEntregaRequest`, `ConsultaEntregaResponse` e
`ObjectFactory`, geradas automaticamente, sem uma linha escrita à mão. Abrir
uma das duas primeiras e conferir que os `import` são de
`jakarta.xml.bind.annotation`, e não de `javax`: é a confirmação, em cinco
segundos, de que a versão do passo 3.2 pegou.

Saída de referência, obtida gerando este mesmo gabarito com Java 21 e Maven
localmente (seção 7 do relatório desta tarefa detalha o ambiente): a classe
gerada começa assim, confirmando `jakarta.xml.bind`:

```java
package br.uni9.rotasul.parceiro.gerado;

import jakarta.xml.bind.annotation.XmlAccessType;
import jakarta.xml.bind.annotation.XmlAccessorType;
import jakarta.xml.bind.annotation.XmlElement;
import jakarta.xml.bind.annotation.XmlRootElement;
import jakarta.xml.bind.annotation.XmlType;
...
@XmlRootElement(name = "consultaEntregaRequest")
public class ConsultaEntregaRequest {
    @XmlElement(required = true)
    protected String codigoRastreio;
    // getters e setters gerados
}
```

### 3.4 Escrever o endpoint que simula o parceiro

Em `parceiro/endpoint`, criar `ParceiroEndpoint`, anotado `@Endpoint`, com um
método anotado `@PayloadRoot` para o elemento `consultaEntregaRequest`,
recebendo `@RequestPayload ConsultaEntregaRequest` e devolvendo
`@ResponsePayload ConsultaEntregaResponse`. Regra simples para simular o
parceiro: se o `codigoRastreio` começar com `"RS"`, devolve situação
`EM_TRANSITO`; caso contrário, `DESCONHECIDO`.

```java
package br.uni9.rotasul.parceiro.endpoint;

import java.time.LocalDate;
import java.time.ZoneOffset;
import java.util.GregorianCalendar;

import javax.xml.datatype.DatatypeConfigurationException;
import javax.xml.datatype.DatatypeFactory;
import javax.xml.datatype.XMLGregorianCalendar;

import org.springframework.ws.server.endpoint.annotation.Endpoint;
import org.springframework.ws.server.endpoint.annotation.PayloadRoot;
import org.springframework.ws.server.endpoint.annotation.RequestPayload;
import org.springframework.ws.server.endpoint.annotation.ResponsePayload;

import br.uni9.rotasul.parceiro.gerado.ConsultaEntregaRequest;
import br.uni9.rotasul.parceiro.gerado.ConsultaEntregaResponse;

// Simula o parceiro legado dentro do próprio fork: quem chama este endpoint
// pelo /ws/parceiro.wsdl é exatamente o mesmo tipo de código que chamaria um
// parceiro de verdade, só o endereço muda.
@Endpoint
public class ParceiroEndpoint {

    private static final String NAMESPACE = "http://rotasul.uni9.br/parceiro";

    @PayloadRoot(namespace = NAMESPACE, localPart = "consultaEntregaRequest")
    @ResponsePayload
    public ConsultaEntregaResponse consultarEntrega(@RequestPayload ConsultaEntregaRequest request)
            throws DatatypeConfigurationException {
        ConsultaEntregaResponse response = new ConsultaEntregaResponse();

        String codigoRastreio = request.getCodigoRastreio();
        if (codigoRastreio != null && codigoRastreio.startsWith("RS")) {
            response.setSituacao("EM_TRANSITO");
        } else {
            response.setSituacao("DESCONHECIDO");
        }
        response.setPrevisaoEntrega(paraXmlGregorianCalendar(LocalDate.now().plusDays(3)));
        return response;
    }

    private XMLGregorianCalendar paraXmlGregorianCalendar(LocalDate data) throws DatatypeConfigurationException {
        GregorianCalendar calendario = GregorianCalendar.from(data.atStartOfDay(ZoneOffset.UTC));
        return DatatypeFactory.newInstance().newXMLGregorianCalendar(calendario);
    }
}
```

> **Por que `previsaoEntrega` precisa de `XMLGregorianCalendar`.** O XSD
> declara o campo como `xs:date`; o `jaxb2-maven-plugin` gera esse tipo Java
> para qualquer `xs:date` ou `xs:dateTime` do contrato, não `LocalDate`. A
> conversão acima, com `DatatypeFactory`, é o jeito padrão de produzir esse
> tipo a partir de um `LocalDate` da aplicação.

### 3.5 Subir e conferir o WSDL (Ciclo 4)

```bash
./mvnw spring-boot:run
```

```bash
# noutro terminal, trocando 8080 pela porta que o seu terminal imprimiu
curl http://localhost:8080/ws/parceiro.wsdl
```

O WSDL não foi escrito por ninguém: o `WebServiceConfig` do kit (seção 0) o
gera a partir do `parceiro.xsd`, e é esse documento que um parceiro real
publicaria para a Rota Sul consumir. Saída de referência (resumida), obtida
rodando este mesmo gabarito:

```xml
<wsdl:definitions ... targetNamespace="http://rotasul.uni9.br/parceiro">
  <wsdl:portType name="ParceiroPort">
    <wsdl:operation name="consultaEntrega">
      <wsdl:input message="tns:consultaEntregaRequest" name="consultaEntregaRequest"/>
      <wsdl:output message="tns:consultaEntregaResponse" name="consultaEntregaResponse"/>
    </wsdl:operation>
  </wsdl:portType>
  <wsdl:service name="ParceiroPortService">
    <wsdl:port binding="tns:ParceiroPortSoap11" name="ParceiroPortSoap11">
      <soap:address location="http://localhost:8080/ws"/>
    </wsdl:port>
  </wsdl:service>
</wsdl:definitions>
```

A operação `consultaEntrega`, o tipo da requisição e o tipo da resposta
aparecem sem nenhuma linha escrita à mão pelo aluno.

### 3.6 Escrever o cliente

Em `parceiro/client`, criar `ParceiroClient`, estendendo
`WebServiceGatewaySupport`, com o método `consultarEntrega(String
codigoRastreio)`:

```java
package br.uni9.rotasul.parceiro.client;

import org.springframework.ws.client.core.support.WebServiceGatewaySupport;

import br.uni9.rotasul.parceiro.gerado.ConsultaEntregaRequest;
import br.uni9.rotasul.parceiro.gerado.ConsultaEntregaResponse;

// O mesmo tipo de código que se escreveria para consumir um parceiro de
// verdade; só o endereço muda entre o parceiro simulado e um parceiro real.
public class ParceiroClient extends WebServiceGatewaySupport {

    public ConsultaEntregaResponse consultarEntrega(String codigoRastreio) {
        ConsultaEntregaRequest request = new ConsultaEntregaRequest();
        request.setCodigoRastreio(codigoRastreio);
        return (ConsultaEntregaResponse) getWebServiceTemplate().marshalSendAndReceive(request);
    }

    // A URI do parceiro não fica escrita dentro da classe: quem chama decide
    // para onde apontar, o que o teste do passo 3.7 precisa fazer contra a
    // porta aleatória do @SpringBootTest, e o que mudaria no dia em que o
    // parceiro deixasse de ser simulado.
    public void apontarPara(String uri) {
        getWebServiceTemplate().setDefaultUri(uri);
    }
}
```

E a classe de configuração que declara o `Jaxb2Marshaller` e o bean
`ParceiroClient`, lendo a URI padrão da propriedade `rotasul.parceiro.uri`:

```java
package br.uni9.rotasul.parceiro.client;

import org.springframework.beans.factory.annotation.Value;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.oxm.jaxb.Jaxb2Marshaller;

@Configuration
public class ParceiroClientConfig {

    @Bean
    public Jaxb2Marshaller marshaller() {
        Jaxb2Marshaller marshaller = new Jaxb2Marshaller();
        marshaller.setContextPath("br.uni9.rotasul.parceiro.gerado");
        return marshaller;
    }

    @Bean
    public ParceiroClient parceiroClient(Jaxb2Marshaller marshaller,
            @Value("${rotasul.parceiro.uri}") String uriPadrao) {
        ParceiroClient client = new ParceiroClient();
        client.setMarshaller(marshaller);
        client.setUnmarshaller(marshaller);
        client.apontarPara(uriPadrao);
        return client;
    }
}
```

Em `application.properties`:

```properties
rotasul.parceiro.uri=http://localhost:${server.port:8080}/ws
```

### 3.7 Testar o cliente

Em `src/test/java/br/uni9/rotasul/parceiro/client/`, criar
`ParceiroClientTest`, anotada `@SpringBootTest(webEnvironment =
SpringBootTest.WebEnvironment.RANDOM_PORT)`, com a porta injetada por
`@LocalServerPort` e o cliente apontado para ela antes da chamada:

```java
package br.uni9.rotasul.parceiro.client;

import static org.junit.jupiter.api.Assertions.assertEquals;

import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.web.server.LocalServerPort;

import br.uni9.rotasul.parceiro.gerado.ConsultaEntregaResponse;

// RANDOM_PORT é obrigatório: no modo padrão (MOCK) nenhum container servlet
// sobe, não existe porta aberta e a chamada SOAP não tem para onde ir.
@SpringBootTest(webEnvironment = SpringBootTest.WebEnvironment.RANDOM_PORT)
class ParceiroClientTest {

    @LocalServerPort
    int porta;

    @Autowired
    ParceiroClient parceiroClient;

    @Test
    void devolveEmTransitoParaCodigoDaRotaSul() {
        parceiroClient.apontarPara("http://localhost:" + porta + "/ws");
        ConsultaEntregaResponse resposta = parceiroClient.consultarEntrega("RS12345");
        assertEquals("EM_TRANSITO", resposta.getSituacao());
    }

    @Test
    void devolveDesconhecidoParaCodigoForaDoPadrao() {
        parceiroClient.apontarPara("http://localhost:" + porta + "/ws");
        ConsultaEntregaResponse resposta = parceiroClient.consultarEntrega("XX999");
        assertEquals("DESCONHECIDO", resposta.getSituacao());
    }
}
```

> **O `webEnvironment` não é detalhe de configuração.** No modo padrão de
> `@SpringBootTest`, que é `MOCK`, nenhum container servlet sobe, não existe
> porta aberta e a chamada SOAP não tem para onde ir: o teste falha com erro
> de conexão. `RANDOM_PORT` sobe o Tomcat embarcado numa porta livre, e
> `@LocalServerPort` diz qual foi. O cliente e o endpoint estão no mesmo
> processo, mas a chamada entre eles atravessa HTTP de verdade, como
> atravessaria contra um parceiro externo.

```bash
./mvnw test
```

Saída de referência, obtida rodando este mesmo gabarito:

```
[INFO] Running br.uni9.rotasul.parceiro.client.ParceiroClientTest
[INFO] Tests run: 2, Failures: 0, Errors: 0, Skipped: 0, Time elapsed: 1.465 s
[INFO] Results:
[INFO] Tests run: 2, Failures: 0, Errors: 0, Skipped: 0
[INFO] BUILD SUCCESS
```

### 3.8 Fechar a integração pelo lado REST

Acrescentar ao `RemessaController` da Aula 09 o método `GET
/remessas/{id}/situacao-parceiro`, que busca a `Remessa`, chama
`ParceiroClient.consultarEntrega` com o seu `codigoRastreio` e devolve o
resultado em JSON. É o ponto em que a integração se fecha: o dado que chegou
por SOAP sai por REST, para qualquer consumidor da Rota Sul.

```java
@RestController
@RequestMapping("/remessas")
public class RemessaController {

    private final RemessaService remessaService;
    private final ParceiroClient parceiroClient;

    public RemessaController(RemessaService remessaService, ParceiroClient parceiroClient) {
        this.remessaService = remessaService;
        this.parceiroClient = parceiroClient;
    }

    @GetMapping(value = "/{id}", produces = { MediaType.APPLICATION_JSON_VALUE, MediaType.APPLICATION_XML_VALUE })
    public Remessa buscarPorId(@PathVariable Long id) {
        return remessaService.buscarPorId(id);
    }

    @GetMapping("/{id}/situacao-parceiro")
    public ConsultaEntregaResponse situacaoNoParceiro(@PathVariable Long id) {
        Remessa remessa = remessaService.buscarPorId(id);
        return parceiroClient.consultarEntrega(remessa.getCodigoRastreio());
    }
}
```

Saída de referência do `curl`, obtida rodando este mesmo gabarito:

```
$ curl http://localhost:8080/remessas/1/situacao-parceiro
{"situacao":"EM_TRANSITO","previsaoEntrega":"2026-08-15T00:00:00.000+00:00"}
```

O `codigoRastreio` da remessa 1 é `RS-0001`, então o parceiro simulado
devolve `EM_TRANSITO`, exatamente a regra do passo 3.4.

> **O construtor de `RemessaController` ganha um parâmetro, e isso quebra
> quem o instanciava em teste.** `RemessaControllerTest`, entregue na Aula
> 09, sobe o contexto com `@WebMvcTest(RemessaController.class)` e troca
> `RemessaService` por um mock com `@MockBean`. Até aqui isso bastava: o
> controlador só recebia `RemessaService` no construtor. A partir de agora
> ele recebe `ParceiroClient` também, e o Spring não tem como montar o bean
> `RemessaController` dentro do contexto fatiado do `@WebMvcTest` sem que
> `ParceiroClient` também esteja disponível, como mock. Sem o ajuste
> abaixo, `./mvnw test` falha ao subir o contexto do teste, não por um
> `assertEquals` errado, mas porque o Spring não consegue instanciar o
> controlador. É a mesma lição da Aula 07 (interface no lugar de classe
> concreta) e da Aula 11 (parâmetro novo no construtor de `Pedido`): mudar
> a assinatura de algo que outro código já instancia é decisão de design
> com custo real, e o custo é ajustar quem depende da assinatura antiga.

Acrescentar ao `RemessaControllerTest` da Aula 09 o `@MockBean` de
`ParceiroClient`, ao lado do `@MockBean` de `RemessaService` que já existia:

```java
package br.uni9.rotasul.expedicao.web;

// ... imports já existentes do teste da Aula 09 ...

@WebMvcTest(RemessaController.class)
class RemessaControllerTest {

    @Autowired
    private MockMvc mockMvc;

    @MockBean
    private RemessaService remessaService;

    @MockBean
    private ParceiroClient parceiroClient;

    // os dois métodos de teste da Aula 09, respondeEmJsonQuandoOAcceptPedeJson
    // e respondeEmXmlQuandoOAcceptPedeXml, continuam exatamente como estavam
}
```

Nenhum dos dois métodos de teste muda: nenhum dos dois chama
`situacao-parceiro`, então nenhum precisa programar um retorno para
`parceiroClient`. O `@MockBean` sozinho já resolve a dependência que falta
para o contexto subir; sem ele o Spring lança
`UnsatisfiedDependencyException` na hora de criar o bean
`RemessaController`.

```bash
./mvnw test
```

Saída de referência, obtida rodando este mesmo gabarito:

```
[INFO] Running br.uni9.rotasul.expedicao.web.RemessaControllerTest
[INFO] Tests run: 2, Failures: 0, Errors: 0, Skipped: 0, Time elapsed: 0.612 s
[INFO] Results:
[INFO] Tests run: 2, Failures: 0, Errors: 0, Skipped: 0
[INFO] BUILD SUCCESS
```

### 3.9 Documentar a API e registrar a decisão

No `pom.xml`:

```xml
<dependency>
  <groupId>org.springdoc</groupId>
  <artifactId>springdoc-openapi-starter-webmvc-ui</artifactId>
</dependency>
```

Subir a aplicação e abrir `/swagger-ui/index.html` na porta que o terminal
imprimiu, conferindo que os endpoints de `/remessas` aparecem listados, com o
schema de `Remessa` gerado a partir das anotações Jackson da Aula 09. Saída
de referência de `/v3/api-docs`, confirmando os dois caminhos:

```
$ curl -s http://localhost:8080/v3/api-docs | python3 -c "import json,sys; print(list(json.load(sys.stdin)['paths'].keys()))"
['/remessas/{id}', '/remessas/{id}/situacao-parceiro']

$ curl -s -o /dev/null -w "%{http_code}\n" http://localhost:8080/swagger-ui/index.html
200
```

Em seguida, uma linha em `docs/decisoes.md`:

> Integração com o parceiro legado: simulada dentro do próprio fork, com um
> endpoint SOAP contract-first (`parceiro.xsd` + `@Endpoint`), porque a Rota
> Sul não tem um parceiro real disponível para a turma. O contrato XSD mais o
> endpoint reproduzem o mesmo tipo de código que se escreveria contra um
> parceiro de verdade; só o endereço mudaria.

## 4. Entregável

No fork do aluno:

- O pacote `br.uni9.rotasul.parceiro`, com `endpoint` e `client`, mais os
  dois arquivos do kit (`parceiro.xsd` e `WebServiceConfig.java`).
- `ParceiroEndpoint`, anotado `@Endpoint`, simulando o parceiro.
- `ParceiroClient` e `ParceiroClientConfig`, com a URI lida de
  `rotasul.parceiro.uri`.
- `ParceiroClientTest`, com `@SpringBootTest(webEnvironment = RANDOM_PORT)` e
  `@LocalServerPort`, passando.
- `RemessaController` (da Aula 09) acrescido de `GET
  /remessas/{id}/situacao-parceiro` e do parâmetro `ParceiroClient` no
  construtor.
- `RemessaControllerTest` (da Aula 09) ajustado com o `@MockBean` de
  `ParceiroClient`, ao lado do `@MockBean` de `RemessaService` já existente.
- `pom.xml` com `spring-boot-starter-web-services`, `wsdl4j`,
  `jaxb-runtime`, `jaxb2-maven-plugin` (linha 3.x, versão presa) e
  `springdoc-openapi-starter-webmvc-ui`.
- `docs/decisoes.md` com a linha nova sobre o parceiro simulado.

## 5. Critérios de aceitação

| Critério | Evidência conferida na correção |
|---|---|
| `consultarEntrega("RS12345")` devolve `EM_TRANSITO` | `ParceiroClientTest` verde, com `@SpringBootTest(webEnvironment = RANDOM_PORT)` |
| Código fora do padrão `RS` devolve `DESCONHECIDO` | Segundo método de `ParceiroClientTest` verde |
| O WSDL está disponível | `/ws/parceiro.wsdl` respondendo, com a operação `consultaEntrega` |
| `jaxb2-maven-plugin` na linha 3.x | Classes geradas em `target/generated-sources/jaxb` importando `jakarta.xml.bind`, não `javax` |
| Swagger UI lista os endpoints de `/remessas` | `/swagger-ui/index.html` abrindo na porta do terminal, com os dois caminhos de `/remessas` em `/v3/api-docs` |
| `GET /remessas/{id}/situacao-parceiro` funcionando | Saída do `curl` colada no commit, com `situacao` vindo do parceiro simulado |
| Nenhuma URI de parceiro fixada dentro de `ParceiroClient` | A URI só entra por `apontarPara`, lida de `rotasul.parceiro.uri` no bean de configuração |
| `RemessaControllerTest`, da Aula 09, continua verde | `@MockBean` de `ParceiroClient` acrescentado ao lado do `@MockBean` de `RemessaService` |
| `./mvnw test` passando | Suíte inteira verde, incluindo os dois métodos de `ParceiroClientTest` e os dois de `RemessaControllerTest` |
| A decisão está registrada | Linha nova em `docs/decisoes.md` explicando o parceiro simulado |
| O commit da aula existe | `git log` do fork mostra o commit `feat(parceiro): consome o parceiro legado por SOAP e documenta a API REST com springdoc` |

## 6. Commit e push esperados

```bash
git add src pom.xml docs
git commit -m "feat(parceiro): consome o parceiro legado por SOAP e documenta a API REST com springdoc"
git push
```

## 7. Ambiente em que este gabarito foi verificado

Java 21 (`openjdk version "21.0.12"`) e Maven 3.9.16, com
`spring-boot-starter-parent` 3.3.4. Todo o código deste `README.md`, mais os
dois arquivos prontos da seção 0, foi montado como projeto Maven completo,
compilado, empacotado e executado: `mvn clean compile`, `mvn test` (2/2
testes verdes em `ParceiroClientTest`), `mvn clean package -DskipTests`,
`java -jar target/rota-sul-0.0.1-SNAPSHOT.jar`, com chamadas reais de `curl`
contra o WSDL, o endpoint SOAP bruto (envelope XML manual), `GET
/remessas/{id}`, `GET /remessas/{id}/situacao-parceiro` e o Swagger UI.
Nenhum processo ficou para trás depois dos testes manuais.

Essa verificação isolada, sozinha, não bastaria: `RemessaControllerTest`
pertence à camada `expedicao`, que a Aula 10 não recria, e só existe no
fork acumulado desde a Aula 09. Por isso este gabarito também foi conferido
no fork acumulado, com o código das Aulas 06 a 10 empilhado no mesmo
projeto Maven: `./mvnw test` roda a suíte inteira, incluindo
`RemessaControllerTest` com o `@MockBean` de `ParceiroClient` do passo 3.8,
e fica verde. É essa segunda verificação, não a primeira, que prova que o
laboratório de hoje não quebra o que a Aula 09 entregou.
