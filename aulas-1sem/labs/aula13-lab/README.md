# Laboratório da Aula 13: camada de apresentação em Thymeleaf

Disciplina Arquitetura de Software, Uninove, Prof. José Romualdo. Roteiro dos
Ciclos 3 e 4 do encontro: layout e fragments no Thymeleaf, o formulário de
cadastro de pedido, e a fronteira entre a validação de tela e a regra de
negócio que já existe desde a Aula 06.

## 1. O passo do case que esta aula resolve

Na Aula 12 cada aluno entregou `NotificadorDeOcorrencia`, com
`NotificadorDeOcorrenciaConsole` para o perfil `dev` e
`NotificadorDeOcorrenciaWebhookSimulado` para o perfil `prod`, ligados
explicitamente por `NotificacaoConfig`, e comprovou pelo log que o container
troca de implementação sozinho conforme o perfil ativo. Até ali, porém, a
Rota Sul inteira só devolvia JSON: nenhuma tela existia.

Hoje essa lacuna fecha. A tabela da Aula 06, que compara o capítulo com a
stack da Rota Sul, tinha a linha Visão dizendo "Thymeleaf, a partir da Aula
13" desde aquele primeiro encontro de código. O laboratório de hoje cumpre
essa promessa: uma tela de cadastro de pedido em `/pedidos/novo`, construída
com layout e fragments do Thymeleaf, cujo formulário chama exatamente o
mesmo `PedidoService` que a API REST já usa desde a Aula 06, sem que uma
linha de regra de negócio precise ser reescrita.

**Nenhuma classe existente muda de assinatura hoje.** Diferente das Aulas
07, 10, 11 e 12, o laboratório de hoje só acrescenta arquivos novos:
`Pedido`, `PedidoService`, `PedidoServicePadrao` e `CalculoDeFreteService`
continuam exatamente como a Aula 11 e a Aula 12 os deixaram. Não há kit de
arquivos prontos nesta aula: tudo o que o passo a passo abaixo pede é código
novo, sem sobrepor nem corrigir nada que já existia no fork.

## 2. Pré-requisitos

- **O fork da Aula 12**, com `NotificadorDeOcorrencia`, `NotificacaoConfig`
  e os dois perfis `dev`/`prod`, já commitados e empurrados.
- **`CalculoDeFreteService`** (Aula 11), com o método `calcular(Pedido)`,
  que hoje é chamado pela primeira vez num fluxo real, não só num teste
  isolado.
- **`PedidoService`, `PedidoServicePadrao` e `Pedido`** (Aulas 06, 07 e 11),
  inalterados.
- **Java 21 LTS** e **Maven** ativos, conferidos na Aula 01.

## 3. Passo a passo

### 3.1 Acrescentar as dependências (Ciclo 3)

No `pom.xml`, duas dependências novas.

```xml
<dependency>
  <groupId>org.springframework.boot</groupId>
  <artifactId>spring-boot-starter-thymeleaf</artifactId>
</dependency>
<dependency>
  <groupId>org.springframework.boot</groupId>
  <artifactId>spring-boot-starter-validation</artifactId>
</dependency>
```

`spring-boot-starter-thymeleaf` está fixada no contrato técnico desde a Aula
01 e é usada pela primeira vez hoje. `spring-boot-starter-validation` é
nova, necessária para `@NotBlank` e `@Valid` no formulário.

### 3.2 Criar o layout compartilhado

Em `src/main/resources/templates/fragments/layout.html`, dois fragments:
`cabecalho(titulo)`, com um `<h1>` mostrando o título recebido por parâmetro
e um menu com dois links, e `rodape`, com uma linha fixa identificando o
painel interno da Rota Sul.

```html
<!DOCTYPE html>
<html xmlns:th="http://www.thymeleaf.org">
<body>

<header th:fragment="cabecalho(titulo)">
  <h1 th:text="${titulo}">Titulo da pagina</h1>
  <nav>
    <a href="/pedidos">Pedidos (API)</a>
    <a href="/pedidos/novo">Novo pedido</a>
  </nav>
</header>

<footer th:fragment="rodape">
  <p>Painel interno da Rota Sul</p>
</footer>

</body>
</html>
```

Um link aponta para `/pedidos`, a API REST da Aula 06; o outro para
`/pedidos/novo`, a tela de hoje.

### 3.3 Criar o modelo de formulário

Em `pedido/web`, a classe `PedidoForm`, com os atributos `cliente`
(anotado `@NotBlank`), `descricao` (sem validação) e `regiao` (`String`,
com valor padrão `"PRINCIPAL"`, o mesmo atributo que a Aula 11 acrescentou a
`Pedido`).

```java
package br.uni9.rotasul.pedido.web;

import jakarta.validation.constraints.NotBlank;

public class PedidoForm {

    @NotBlank(message = "Cliente e obrigatorio")
    private String cliente;

    private String descricao;

    private String regiao = "PRINCIPAL";

    public String getCliente() {
        return cliente;
    }

    public void setCliente(String cliente) {
        this.cliente = cliente;
    }

    public String getDescricao() {
        return descricao;
    }

    public void setDescricao(String descricao) {
        this.descricao = descricao;
    }

    public String getRegiao() {
        return regiao;
    }

    public void setRegiao(String regiao) {
        this.regiao = regiao;
    }
}
```

Diferente de `Pedido`, `PedidoForm` pode ter anotação de framework: ela
pertence à camada `web`, não ao domínio.

### 3.4 Escrever o controlador da tela

`PedidoFormController`, em `pedido/web`, anotado `@Controller`, não
`@RestController`, mapeado em `/pedidos/novo`. Recebe `PedidoService` e
`CalculoDeFreteService` pelo construtor. O método `GET` monta um
`PedidoForm` vazio, adiciona ao `Model` com o nome `pedidoForm` e devolve o
nome lógico da view, `"pedidos/formulario"`, sem o `.html`, resolvido pelo
Thymeleaf. O método `POST`, com a validação, entra no passo 3.7.

```java
package br.uni9.rotasul.pedido.web;

import java.math.BigDecimal;

import jakarta.validation.Valid;

import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.validation.BindingResult;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.ModelAttribute;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestMapping;

import br.uni9.rotasul.pedido.domain.Pedido;
import br.uni9.rotasul.pedido.service.CalculoDeFreteService;
import br.uni9.rotasul.pedido.service.PedidoService;

@Controller
@RequestMapping("/pedidos/novo")
public class PedidoFormController {

    private final PedidoService pedidoService;
    private final CalculoDeFreteService calculoDeFreteService;

    public PedidoFormController(PedidoService pedidoService, CalculoDeFreteService calculoDeFreteService) {
        this.pedidoService = pedidoService;
        this.calculoDeFreteService = calculoDeFreteService;
    }

    @GetMapping
    public String novo(Model model) {
        model.addAttribute("pedidoForm", new PedidoForm());
        return "pedidos/formulario";
    }

    // o metodo POST entra no passo 3.7
}
```

### 3.5 Escrever o template do formulário

Em `src/main/resources/templates/pedidos/formulario.html`, incluir o
cabeçalho e o rodapé com `th:replace`, e um `<form>` com
`th:object="${pedidoForm}"`.

```html
<!DOCTYPE html>
<html xmlns:th="http://www.thymeleaf.org">
<head>
  <meta charset="UTF-8">
  <title>Novo pedido</title>
</head>
<body>

<div th:replace="~{fragments/layout :: cabecalho(titulo='Novo pedido')}"></div>

<form th:action="@{/pedidos/novo}" th:object="${pedidoForm}" method="post">
  <div>
    <label for="cliente">Cliente</label>
    <input type="text" id="cliente" th:field="*{cliente}">
    <span th:if="${#fields.hasErrors('cliente')}" th:errors="*{cliente}">Erro</span>
  </div>
  <div>
    <label for="descricao">Descricao</label>
    <input type="text" id="descricao" th:field="*{descricao}">
  </div>
  <div>
    <label for="regiao">Regiao</label>
    <select id="regiao" th:field="*{regiao}">
      <option value="PRINCIPAL">PRINCIPAL</option>
      <option value="ULTIMA_MILHA">ULTIMA_MILHA</option>
    </select>
  </div>
  <button type="submit">Registrar pedido</button>
</form>

<div th:replace="~{fragments/layout :: rodape}"></div>

</body>
</html>
```

`th:field` escreve `name`, `id` e `value` sozinho, a partir do atributo de
`PedidoForm`; `th:errors` só aparece quando `#fields.hasErrors('cliente')`
for verdadeiro.

### 3.6 Subir e ver a tela

```bash
./mvnw spring-boot:run
```

Abrir `http://localhost:PORTA/pedidos/novo`, na porta que o terminal
imprimiu. Conferir que o cabeçalho, o formulário e o rodapé aparecem, mesmo
sem nenhuma folha de estilo: o laboratório de hoje é deliberadamente sem
CSS, o foco é a camada de apresentação, não o visual.

### 3.7 Escrever o `POST` com validação (Ciclo 4)

No mesmo `PedidoFormController`, um método `POST` em `/pedidos/novo`,
recebendo `@Valid @ModelAttribute("pedidoForm") PedidoForm form` e
`BindingResult resultado`. Se `resultado.hasErrors()`, devolve de novo
`"pedidos/formulario"`, sem redirecionar, para o Thymeleaf reconstruir a
página com as mensagens de erro ao lado dos campos. Se não houver erro,
monta um `Pedido` a partir do `PedidoForm`, chama
`pedidoService.registrar(pedido)`, calcula o frete com
`calculoDeFreteService.calcular(pedido)`, e devolve a view
`"pedidos/confirmacao"`, com o pedido e o frete no `Model`.

```java
    @PostMapping
    public String registrar(@Valid @ModelAttribute("pedidoForm") PedidoForm form, BindingResult resultado,
            Model model) {
        if (resultado.hasErrors()) {
            return "pedidos/formulario";
        }

        Pedido pedido = new Pedido(form.getCliente(), form.getDescricao(), form.getRegiao());
        Pedido registrado = pedidoService.registrar(pedido);
        BigDecimal frete = calculoDeFreteService.calcular(registrado);

        model.addAttribute("pedido", registrado);
        model.addAttribute("frete", frete);
        return "pedidos/confirmacao";
    }
```

> **A validação de tela não substitui a regra de negócio.** `resultado.hasErrors()`
> antecipa, numa camada mais barata de errar, o mesmo problema que
> `PedidoServicePadrao.registrar` já recusa desde a Aula 06. Se
> `resultado.hasErrors()`, o método retorna antes de chamar
> `pedidoService.registrar`: nada é gravado. O passo 3.10 prova que a regra
> continua valendo mesmo fora da tela.

### 3.8 Escrever o template de confirmação

Em `templates/pedidos/confirmacao.html`, reaproveitando o cabeçalho e o
rodapé do mesmo jeito, mostrando o nome do cliente registrado e o valor do
frete calculado, com o texto "Frete calculado pela estratégia de
`regiao`", ligando visualmente o formulário de hoje ao Strategy da Aula 11.

```html
<!DOCTYPE html>
<html xmlns:th="http://www.thymeleaf.org">
<head>
  <meta charset="UTF-8">
  <title>Pedido confirmado</title>
</head>
<body>

<div th:replace="~{fragments/layout :: cabecalho(titulo='Pedido confirmado')}"></div>

<p>Cliente: <span th:text="${pedido.cliente}">Nome do cliente</span></p>
<p>Descricao: <span th:text="${pedido.descricao}">Descricao</span></p>
<p>Frete calculado pela estrategia de <span th:text="${pedido.regiao}">REGIAO</span>:
   R$ <span th:text="${frete}">0.00</span></p>

<div th:replace="~{fragments/layout :: rodape}"></div>

</body>
</html>
```

### 3.9 Testar a validação sem navegador

`PedidoFormControllerTest`, em
`src/test/java/br/uni9/rotasul/pedido/web/`, anotado
`@WebMvcTest(PedidoFormController.class)`, com `PedidoService` e
`CalculoDeFreteService` como `@MockBean`. Dois casos com `MockMvc`: um
`POST` para `/pedidos/novo` sem o parâmetro `cliente` devolve status 200 e a
view `pedidos/formulario` de novo, sem chamar `pedidoService.registrar`; um
`POST` com `cliente` preenchido devolve a view `pedidos/confirmacao` e chama
`pedidoService.registrar` exatamente uma vez.

```java
package br.uni9.rotasul.pedido.web;

import static org.mockito.ArgumentMatchers.any;
import static org.mockito.Mockito.never;
import static org.mockito.Mockito.times;
import static org.mockito.Mockito.verify;
import static org.mockito.Mockito.when;
import static org.springframework.test.web.servlet.request.MockMvcRequestBuilders.post;
import static org.springframework.test.web.servlet.result.MockMvcResultMatchers.status;
import static org.springframework.test.web.servlet.result.MockMvcResultMatchers.view;

import java.math.BigDecimal;

import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.autoconfigure.web.servlet.WebMvcTest;
import org.springframework.boot.test.mock.mockito.MockBean;
import org.springframework.test.web.servlet.MockMvc;

import br.uni9.rotasul.pedido.domain.Pedido;
import br.uni9.rotasul.pedido.service.CalculoDeFreteService;
import br.uni9.rotasul.pedido.service.PedidoService;

@WebMvcTest(PedidoFormController.class)
class PedidoFormControllerTest {

    @Autowired
    private MockMvc mockMvc;

    @MockBean
    private PedidoService pedidoService;

    @MockBean
    private CalculoDeFreteService calculoDeFreteService;

    @Test
    void semClienteDevolveOMesmoFormularioComErroSemRegistrar() throws Exception {
        mockMvc.perform(post("/pedidos/novo")
                        .param("descricao", "Sofa de dois lugares")
                        .param("regiao", "PRINCIPAL"))
                .andExpect(status().isOk())
                .andExpect(view().name("pedidos/formulario"));

        verify(pedidoService, never()).registrar(any());
    }

    @Test
    void comClientePreenchidoRegistraEDevolveAConfirmacao() throws Exception {
        Pedido registrado = new Pedido("Loja Boa Vista", "Sofa de dois lugares", "PRINCIPAL");
        when(pedidoService.registrar(any())).thenReturn(registrado);
        when(calculoDeFreteService.calcular(any())).thenReturn(new BigDecimal("15.00"));

        mockMvc.perform(post("/pedidos/novo")
                        .param("cliente", "Loja Boa Vista")
                        .param("descricao", "Sofa de dois lugares")
                        .param("regiao", "PRINCIPAL"))
                .andExpect(status().isOk())
                .andExpect(view().name("pedidos/confirmacao"));

        verify(pedidoService, times(1)).registrar(any());
    }
}
```

```bash
./mvnw test
```

### 3.10 Confirmar a fronteira em voz alta

Com a aplicação no ar (passo 3.6), enviar, por `curl`, um `POST /pedidos`
(a API REST da Aula 06, não a tela de hoje) sem o campo `cliente`, e
conferir que o `PedidoService` recusa do mesmo jeito que recusaria vindo da
tela.

```bash
curl -X POST http://localhost:PORTA/pedidos \
  -H "Content-Type: application/json" \
  -d '{"descricao":"sem cliente","regiao":"PRINCIPAL"}'
```

Saída de referência, obtida rodando este mesmo gabarito:

```
HTTP/1.1 500 Internal Server Error
{"timestamp":"...","status":500,"error":"Internal Server Error","path":"/pedidos"}
```

É a prova de que a regra de negócio não migrou para o Thymeleaf, só ganhou
uma segunda porta de entrada na frente dela: `PedidoServicePadrao.registrar`
continua sendo quem recusa, e um `500` sem corpo tratado é exatamente o
comportamento herdado da Aula 06, sem `@ExceptionHandler` novo criado hoje.

### 3.11 Registrar as decisões

Em `docs/decisoes.md`, duas linhas: uma explicando a escolha de layout e
fragments em vez de repetir HTML em cada página, outra explicitando que a
validação de `PedidoForm` é responsabilidade da view, sem substituir a regra
de `PedidoService`.

```
Camada de apresentacao: layout e fragments do Thymeleaf em vez
de repetir cabecalho e rodape em cada pagina.

Validacao de PedidoForm e responsabilidade da view; nao substitui
a regra de PedidoServicePadrao, que continua recusando pedido
sem cliente em qualquer porta de entrada.
```

## 4. Entregável

`PedidoFormController`, `PedidoForm`, `templates/fragments/layout.html`,
`templates/pedidos/formulario.html` e `templates/pedidos/confirmacao.html`,
mais `PedidoFormControllerTest` e as duas linhas em `docs/decisoes.md`.

**Seis arquivos digitados pelo aluno hoje**, mais a edição de duas linhas
em `pom.xml` e duas linhas em `docs/decisoes.md`. Nenhum arquivo chega
pronto no kit desta aula: diferente das Aulas 10, 11 e 12, nenhuma
assinatura, tipo ou construtor já entregue muda hoje, então não há nada
para corrigir no fork acumulado.

## 5. Critérios de aceitação

| Critério | Evidência conferida na correção |
|---|---|
| `POST /pedidos/novo` sem `cliente` devolve a mesma tela com erro | Status 200, view `pedidos/formulario`, mensagem "Cliente e obrigatorio" ao lado do campo, nada registrado |
| `POST /pedidos/novo` com `cliente` registra e confirma | View `pedidos/confirmacao`, com o nome do cliente e o frete calculado no corpo |
| O frete mostrado vem do `CalculoDeFreteService` da Aula 11 | Texto "Frete calculado pela estrategia de PRINCIPAL" (ou `ULTIMA_MILHA`), com o valor de `FreteRotaPropria` ou `FreteTransportadoraParceira` |
| `PedidoFormControllerTest` passando | `./mvnw test` verde, os dois casos de `MockMvc` |
| A API REST continua recusando pedido sem cliente | `curl POST /pedidos` sem `cliente` devolve `500`, sem registrar nada, comprovando que a regra não saiu de `PedidoService` |
| As decisões estão registradas | `docs/decisoes.md` com as duas linhas novas |
| `./mvnw test` passando | Suíte inteira verde, incluindo as Aulas 06 a 12 |
| O commit da aula existe | `git log` do fork mostra o commit `feat(pedido): adiciona tela de cadastro em Thymeleaf com layout, fragments e validacao` |

## 6. Commit e push esperados

```bash
git add src docs
git commit -m "feat(pedido): adiciona tela de cadastro em Thymeleaf com layout, fragments e validacao"
git push
```

## 7. Ambiente em que este gabarito foi verificado

Java 21 (`openjdk version "21.0.12"`) e Maven 3.9.16, com
`spring-boot-starter-parent` 3.3.4. A verificação **não isolou o código de
hoje**: montou o fork acumulado inteiro, da Aula 06 até a Aula 12
(`Pedido`, `PedidoRepository`, `PedidoService` com as duas implementações da
Aula 07, `RemessaController` e `RemessaService` da Aula 09, `ParceiroClient`
e `ParceiroClientConfig` da Aula 10, `CalculoDeFreteService` e
`CalculoDeFreteConfig` mais a hierarquia de `OcorrenciaCreator` da Aula 11,
`NotificadorDeOcorrencia` e `NotificacaoConfig` da Aula 12), com o código de
hoje por cima, e rodou `./mvnw test` nesse projeto acumulado.

```
$ export JAVA_HOME=/opt/homebrew/opt/openjdk@21/libexec/openjdk.jdk/Contents/Home
$ export PATH="$JAVA_HOME/bin:$PATH"
$ java -version
openjdk version "21.0.12"
$ mvn -version
Apache Maven 3.9.16, Java version: 21.0.12

$ mvn clean test
...
Tests run: 2, Failures: 0, Errors: 0, Skipped: 0 -- in br.uni9.rotasul.pedido.service.CalculoDeFreteServiceTest
Tests run: 2, Failures: 0, Errors: 0, Skipped: 0 -- in br.uni9.rotasul.expedicao.web.RemessaControllerTest
Tests run: 2, Failures: 0, Errors: 0, Skipped: 0 -- in br.uni9.rotasul.pedido.service.PedidoServiceComAnaliseDeRiscoContratoTest
Tests run: 2, Failures: 0, Errors: 0, Skipped: 0 -- in br.uni9.rotasul.parceiro.client.ParceiroClientTest
Tests run: 2, Failures: 0, Errors: 0, Skipped: 0 -- in br.uni9.rotasul.pedido.web.PedidoFormControllerTest
Tests run: 2, Failures: 0, Errors: 0, Skipped: 0 -- in br.uni9.rotasul.pedido.service.PedidoServicePadraoTest
Tests run: 2, Failures: 0, Errors: 0, Skipped: 0 -- in br.uni9.rotasul.pedido.service.PedidoServicePadraoContratoTest
Tests run: 3, Failures: 0, Errors: 0, Skipped: 0 -- in br.uni9.rotasul.rastreamento.domain.OcorrenciaCreatorTest
Tests run: 1, Failures: 0, Errors: 0, Skipped: 0 -- in br.uni9.rotasul.rastreamento.service.NotificacaoConfigProdTest
Tests run: 1, Failures: 0, Errors: 0, Skipped: 0 -- in br.uni9.rotasul.rastreamento.service.NotificacaoConfigDevTest
[INFO]
[INFO] Results:
[INFO]
[INFO] Tests run: 19, Failures: 0, Errors: 0, Skipped: 0
[INFO] BUILD SUCCESS
```

Dezenove testes verdes: os dois de hoje mais os dezessete acumulados desde
a Aula 06. `./mvnw spring-boot:run` também foi executado de ponta a ponta
neste mesmo projeto: `GET /pedidos/novo` devolveu o formulário (status
200), `POST /pedidos/novo` sem `cliente` devolveu o mesmo formulário com a
mensagem de erro, `POST /pedidos/novo` com `cliente` registrou o pedido e
devolveu a confirmação com o frete calculado (`R$ 15.00` para `PRINCIPAL`),
`GET /pedidos` listou o pedido pela API REST, e `POST /pedidos` sem
`cliente` devolveu `500`, sem registrar nada. `ps aux` confirmou que nenhum
processo Java ficou para trás ao final da verificação.
