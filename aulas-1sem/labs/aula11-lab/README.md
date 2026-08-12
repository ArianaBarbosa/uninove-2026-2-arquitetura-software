# Laboratório da Aula 11: Strategy no cálculo de frete, Factory Method na criação de `Ocorrencia`

Disciplina Arquitetura de Software, Uninove, Prof. José Romualdo. Roteiro dos
Ciclos 3 e 4 do encontro: dois padrões de projeto do catálogo GoF entram no
código da Rota Sul, cada um com teste JUnit. Nenhum endpoint novo nasce hoje.

## 1. O passo do case que esta aula resolve

Na Aula 10 cada aluno entregou o cliente SOAP em `br.uni9.rotasul.parceiro`,
consumindo o parceiro legado simulado, mais a API REST de `/remessas`
documentada pelo springdoc-openapi, fechando o Módulo 2. Hoje abre o Módulo 3,
Padrões e frameworks: a turma usa padrões de projeto desde a Aula 06 sem
nomeá-los (o próprio contrato `PedidoService` com duas implementações
trocáveis por perfil, e `PedidoServiceContratoTest` rodando a mesma suíte
contra as duas, já era uma aplicação de Template Method). Hoje dois padrões
novos entram no código de propósito: Strategy no cálculo do frete e Factory
Method na criação de `Ocorrencia`.

O Strategy entra nas camadas `domain` e `service` do contexto `pedido`. O
Factory Method abre o contexto `rastreamento`, reservado desde o diagrama de
pacotes da Aula 05 e, até hoje, sem nenhuma linha de código (a Aula 10 havia
acrescentado o pacote `parceiro`, fora do trio original `pedido`, `expedicao`
e `rastreamento`, para simular o parceiro legado por SOAP).

**`CalculoDeFreteService` fica paralelo ao fluxo de `PedidoService.registrar`
até a Aula 13.** Isso é deliberado: ligar o cálculo de frete ao registro de
pedido de verdade pede uma etapa de fluxo (calcular, decidir, gravar) que só
faz sentido depois que a Aula 13 trouxer a camada de apresentação. Hoje o
Strategy só precisa provar que calcula o valor certo, isolado, com teste.

## 2. Pré-requisitos

- **O fork da Aula 10**, com o contexto `parceiro` (`ParceiroEndpoint`,
  `ParceiroClient`, `ParceiroClientConfig`) e a API REST documentada por
  springdoc-openapi já commitados e empurrados.
- **Java 21 LTS** e **Maven** ativos, conferidos na Aula 01.
- **`Pedido`, `PedidoRepository`, `PedidoService`** da Aula 06/07, em
  `pedido.domain`, `pedido.repository` e `pedido.service`.
- Nenhuma dependência nova no `pom.xml`: os dois padrões de hoje são código de
  domínio e serviço puro, sem biblioteca externa.

## 3. Passo a passo

### 3.1 Criar o contrato da estratégia (Ciclo 3)

Em `pedido/domain`, criar a interface `CalculadoraDeFrete`, com um único
método. Sem anotação de framework: é domínio.

```java
package br.uni9.rotasul.pedido.domain;

import java.math.BigDecimal;

// O contrato do padrão Strategy: uma família de algoritmos de cálculo de
// frete, encapsulados cada um numa classe própria e intercambiáveis. Sem
// anotação de framework: é domínio, igual a Pedido.
public interface CalculadoraDeFrete {

    BigDecimal calcular(Pedido pedido);
}
```

### 3.2 Acrescentar a região ao `Pedido`

Em `pedido/domain/Pedido`, criado na Aula 06, acrescentar o atributo
`regiao`, do tipo `String`, com os valores possíveis `"PRINCIPAL"` e
`"ULTIMA_MILHA"`, mais o getter e o ajuste no construtor. É a primeira vez
que a classe `Pedido` muda desde que nasceu, e ela continua sem depender de
nada do Spring.

```java
package br.uni9.rotasul.pedido.domain;

// Classe de domínio. Sem anotação de framework nenhuma: o domínio não
// depende de Spring, e essa independência vai importar na Aula 12, quando
// a injeção de dependência explícita entrar em pauta. Primeira mudança
// desde que a classe nasceu na Aula 06: o atributo regiao, que o Strategy
// de hoje usa para decidir qual estratégia de frete aplicar.
public class Pedido {

    private Long id;
    private final String cliente;
    private final String descricao;
    private String situacao;
    private final String regiao;

    public Pedido(String cliente, String descricao, String regiao) {
        this.cliente = cliente;
        this.descricao = descricao;
        this.situacao = "RECEBIDO";
        this.regiao = regiao;
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

    public String getRegiao() {
        return regiao;
    }
}
```

> **Compatibilidade com quem já tinha `Pedido` na Aula 06/07.** O construtor
> ganha um terceiro parâmetro obrigatório. Qualquer código que ainda chame
> `new Pedido(cliente, descricao)` (duas posições) deixa de compilar; ajustar
> as chamadas existentes para informar a região é parte deste passo.

### 3.3 Escrever a primeira estratégia

`FreteRotaPropria implements CalculadoraDeFrete`, em `pedido/domain`, com
uma tarifa fixa de `new BigDecimal("15.00")` para qualquer pedido,
representando o custo da frota própria na rota principal.

```java
package br.uni9.rotasul.pedido.domain;

import java.math.BigDecimal;

// Primeira estratégia concreta: a frota própria na rota principal, com
// tarifa fixa.
public class FreteRotaPropria implements CalculadoraDeFrete {

    private static final BigDecimal TARIFA_BASE = new BigDecimal("15.00");

    @Override
    public BigDecimal calcular(Pedido pedido) {
        return TARIFA_BASE;
    }
}
```

### 3.4 Escrever a segunda estratégia

`FreteTransportadoraParceira implements CalculadoraDeFrete`, também em
`pedido/domain`, aplicando um adicional de 30% sobre a mesma tarifa base,
`new BigDecimal("15.00")` multiplicado por `new BigDecimal("1.30")`,
resultando em `19.50`, representando o repasse pago ao parceiro da última
milha.

```java
package br.uni9.rotasul.pedido.domain;

import java.math.BigDecimal;
import java.math.RoundingMode;

// Segunda estratégia concreta: a transportadora parceira na última milha,
// com um adicional de 30% sobre a mesma tarifa base da rota própria.
public class FreteTransportadoraParceira implements CalculadoraDeFrete {

    private static final BigDecimal TARIFA_BASE = new BigDecimal("15.00");
    private static final BigDecimal ADICIONAL_PARCEIRO = new BigDecimal("1.30");

    @Override
    public BigDecimal calcular(Pedido pedido) {
        // setScale ajusta 19.5000 (escala 4, de 2+2 casas na multiplicação)
        // para 19.50 (escala 2), o mesmo formato de dinheiro da outra
        // estratégia. Sem o ajuste de escala, o teste do passo 3.6 falharia:
        // BigDecimal.equals compara valor e escala, não só valor.
        return TARIFA_BASE.multiply(ADICIONAL_PARCEIRO).setScale(2, RoundingMode.HALF_UP);
    }
}
```

### 3.5 Escrever o contexto do Strategy

Em `pedido/service`, criar `CalculoDeFreteService`, anotada `@Service`,
recebendo `FreteRotaPropria` e `FreteTransportadoraParceira` pelo construtor
e guardando as duas. O método `calcular(Pedido pedido)` decide qual delas
chamar olhando `pedido.getRegiao()`: `"ULTIMA_MILHA"` usa a segunda,
qualquer outro valor usa a primeira. É o único ponto do código que conhece
as duas implementações concretas; todo o resto do sistema só vai conhecer a
interface `CalculadoraDeFrete` e o serviço.

```java
package br.uni9.rotasul.pedido.service;

import java.math.BigDecimal;

import org.springframework.stereotype.Service;

import br.uni9.rotasul.pedido.domain.CalculadoraDeFrete;
import br.uni9.rotasul.pedido.domain.FreteRotaPropria;
import br.uni9.rotasul.pedido.domain.FreteTransportadoraParceira;
import br.uni9.rotasul.pedido.domain.Pedido;

// O "contexto" do padrão Strategy, na terminologia do GoF: guarda as duas
// estratégias e decide qual delas invocar a cada chamada, olhando um dado
// do próprio pedido. É o único ponto do código que conhece as duas
// implementações concretas; todo o resto do sistema só conhece a
// interface CalculadoraDeFrete e este serviço.
@Service
public class CalculoDeFreteService {

    private final CalculadoraDeFrete rotaPropria;
    private final CalculadoraDeFrete transportadoraParceira;

    public CalculoDeFreteService(FreteRotaPropria rotaPropria, FreteTransportadoraParceira transportadoraParceira) {
        this.rotaPropria = rotaPropria;
        this.transportadoraParceira = transportadoraParceira;
    }

    public BigDecimal calcular(Pedido pedido) {
        if ("ULTIMA_MILHA".equals(pedido.getRegiao())) {
            return transportadoraParceira.calcular(pedido);
        }
        return rotaPropria.calcular(pedido);
    }
}
```

> **Por que `CalculoDeFreteService` não entra em `PedidoService.registrar`
> hoje.** Ligar o cálculo ao fluxo de registro pede decidir onde o valor
> calculado é gravado e exibido, o que só faz sentido depois que a Aula 13
> trouxer a camada de apresentação. Até lá, o serviço fica pronto e testado,
> paralelo ao fluxo existente, pronto para ser chamado quando a hora chegar.

### 3.6 Testar o Strategy

`CalculoDeFreteServiceTest`, em
`src/test/java/br/uni9/rotasul/pedido/service/`, com dois casos: um
`Pedido` com `regiao` `"PRINCIPAL"` calcula `15.00`, e um `Pedido` com
`regiao` `"ULTIMA_MILHA"` calcula `19.50`.

```java
package br.uni9.rotasul.pedido.service;

import static org.junit.jupiter.api.Assertions.assertEquals;

import java.math.BigDecimal;

import org.junit.jupiter.api.Test;

import br.uni9.rotasul.pedido.domain.FreteRotaPropria;
import br.uni9.rotasul.pedido.domain.FreteTransportadoraParceira;
import br.uni9.rotasul.pedido.domain.Pedido;

class CalculoDeFreteServiceTest {

    private final CalculoDeFreteService service =
            new CalculoDeFreteService(new FreteRotaPropria(), new FreteTransportadoraParceira());

    @Test
    void calculaTarifaFixaParaPedidoDaRotaPrincipal() {
        Pedido pedido = new Pedido("Lojista Centro", "3 volumes", "PRINCIPAL");

        BigDecimal frete = service.calcular(pedido);

        assertEquals(new BigDecimal("15.00"), frete);
    }

    @Test
    void calculaTarifaComAdicionalParaPedidoDaUltimaMilha() {
        Pedido pedido = new Pedido("Lojista Bairro", "1 volume", "ULTIMA_MILHA");

        BigDecimal frete = service.calcular(pedido);

        assertEquals(new BigDecimal("19.50"), frete);
    }
}
```

```bash
./mvnw test
```

Saída de referência, obtida rodando este mesmo gabarito:

```
[INFO] Running br.uni9.rotasul.pedido.service.CalculoDeFreteServiceTest
[INFO] Tests run: 2, Failures: 0, Errors: 0, Skipped: 0
[INFO] BUILD SUCCESS
```

### 3.7 Criar o contexto `rastreamento` (Ciclo 4)

Dentro de `src/main/java/br/uni9/rotasul/`, criar `rastreamento/domain`. É
o primeiro código do terceiro contexto reservado desde o diagrama de
pacotes da Aula 05, ao lado de `pedido` e `expedicao`. A Aula 10 já havia
acrescentado o pacote `parceiro`, fora desse trio original, para simular o
parceiro legado por SOAP.

```
src/main/java/br/uni9/rotasul/
├── pedido/
├── expedicao/
├── parceiro/
└── rastreamento/
    └── domain/
```

### 3.8 Escrever a hierarquia de produtos

Em `rastreamento/domain`, a classe abstrata `Ocorrencia`, com os atributos
`codigoRastreio` e `registradaEm` (`LocalDateTime`) e o método abstrato
`String getTipo()`. Duas subclasses: `OcorrenciaAtraso`, com o atributo
extra `horasDeAtraso` e `getTipo()` devolvendo `"ATRASO"`, e
`OcorrenciaExtravio`, com o atributo extra `ultimaLocalizacaoConhecida` e
`getTipo()` devolvendo `"EXTRAVIO"`.

```java
package br.uni9.rotasul.rastreamento.domain;

import java.time.LocalDateTime;

// Primeiro código do contexto rastreamento, reservado desde o diagrama de
// pacotes da Aula 05. O "produto" do padrão Factory Method: a hierarquia
// que OcorrenciaCreator decide qual subclasse instanciar. Sem anotação de
// framework, igual ao domínio de pedido e expedicao.
public abstract class Ocorrencia {

    private final String codigoRastreio;
    private final LocalDateTime registradaEm;

    protected Ocorrencia(String codigoRastreio, LocalDateTime registradaEm) {
        this.codigoRastreio = codigoRastreio;
        this.registradaEm = registradaEm;
    }

    public String getCodigoRastreio() {
        return codigoRastreio;
    }

    public LocalDateTime getRegistradaEm() {
        return registradaEm;
    }

    public abstract String getTipo();
}
```

```java
package br.uni9.rotasul.rastreamento.domain;

import java.time.LocalDateTime;

public class OcorrenciaAtraso extends Ocorrencia {

    private final int horasDeAtraso;

    public OcorrenciaAtraso(String codigoRastreio, LocalDateTime registradaEm, int horasDeAtraso) {
        super(codigoRastreio, registradaEm);
        this.horasDeAtraso = horasDeAtraso;
    }

    public int getHorasDeAtraso() {
        return horasDeAtraso;
    }

    @Override
    public String getTipo() {
        return "ATRASO";
    }
}
```

```java
package br.uni9.rotasul.rastreamento.domain;

import java.time.LocalDateTime;

public class OcorrenciaExtravio extends Ocorrencia {

    private final String ultimaLocalizacaoConhecida;

    public OcorrenciaExtravio(String codigoRastreio, LocalDateTime registradaEm, String ultimaLocalizacaoConhecida) {
        super(codigoRastreio, registradaEm);
        this.ultimaLocalizacaoConhecida = ultimaLocalizacaoConhecida;
    }

    public String getUltimaLocalizacaoConhecida() {
        return ultimaLocalizacaoConhecida;
    }

    @Override
    public String getTipo() {
        return "EXTRAVIO";
    }
}
```

### 3.9 Escrever a hierarquia de criadores, o Factory Method

Também em `rastreamento/domain`, a classe abstrata `OcorrenciaCreator`:

```java
package br.uni9.rotasul.rastreamento.domain;

import java.time.LocalDateTime;

// O padrão Factory Method: define o passo comum a toda ocorrência
// (registrar é final, valida o código de rastreio) e deixa para cada
// subclasse decidir qual produto concreto instanciar (criarOcorrencia,
// abstrato). O código que atende a ligação do atendente conhece só esta
// classe, nunca as subclasses de Ocorrencia diretamente.
public abstract class OcorrenciaCreator {

    public final Ocorrencia registrar(String codigoRastreio) {
        if (codigoRastreio == null || codigoRastreio.isBlank()) {
            throw new IllegalArgumentException(
                "codigo de rastreio e obrigatorio");
        }
        return criarOcorrencia(codigoRastreio, LocalDateTime.now());
    }

    protected abstract Ocorrencia criarOcorrencia(
        String codigoRastreio, LocalDateTime registradaEm);
}
```

O método `registrar` é final, de propósito: ele é o passo comum a toda
ocorrência, validar o código de rastreio antes de criar qualquer coisa. O
método `criarOcorrencia` é o Factory Method propriamente dito, abstrato,
deixado para cada subclasse decidir qual produto concreto instanciar.

```java
package br.uni9.rotasul.rastreamento.domain;

import java.time.LocalDateTime;

public class AtrasoOcorrenciaCreator extends OcorrenciaCreator {

    private final int horasDeAtraso;

    public AtrasoOcorrenciaCreator(int horasDeAtraso) {
        this.horasDeAtraso = horasDeAtraso;
    }

    @Override
    protected Ocorrencia criarOcorrencia(String codigoRastreio, LocalDateTime registradaEm) {
        return new OcorrenciaAtraso(codigoRastreio, registradaEm, horasDeAtraso);
    }
}
```

```java
package br.uni9.rotasul.rastreamento.domain;

import java.time.LocalDateTime;

public class ExtravioOcorrenciaCreator extends OcorrenciaCreator {

    private final String ultimaLocalizacaoConhecida;

    public ExtravioOcorrenciaCreator(String ultimaLocalizacaoConhecida) {
        this.ultimaLocalizacaoConhecida = ultimaLocalizacaoConhecida;
    }

    @Override
    protected Ocorrencia criarOcorrencia(String codigoRastreio, LocalDateTime registradaEm) {
        return new OcorrenciaExtravio(codigoRastreio, registradaEm, ultimaLocalizacaoConhecida);
    }
}
```

### 3.10 Testar o Factory Method

`OcorrenciaCreatorTest`, em
`src/test/java/br/uni9/rotasul/rastreamento/domain/`, com três casos: `new
AtrasoOcorrenciaCreator(3).registrar("RS12345")` devolve uma instância de
`OcorrenciaAtraso` com `getTipo()` igual a `"ATRASO"`; `new
ExtravioOcorrenciaCreator("Galpao Osasco").registrar("RS99999")` devolve
uma instância de `OcorrenciaExtravio` com `getTipo()` igual a
`"EXTRAVIO"`; e chamar `registrar("")` em qualquer um dos dois criadores
lança `IllegalArgumentException`.

```java
package br.uni9.rotasul.rastreamento.domain;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertInstanceOf;
import static org.junit.jupiter.api.Assertions.assertThrows;

import org.junit.jupiter.api.Test;

class OcorrenciaCreatorTest {

    @Test
    void atrasoOcorrenciaCreatorRegistraUmaOcorrenciaDeAtraso() {
        OcorrenciaCreator creator = new AtrasoOcorrenciaCreator(3);

        Ocorrencia ocorrencia = creator.registrar("RS12345");

        assertInstanceOf(OcorrenciaAtraso.class, ocorrencia);
        assertEquals("ATRASO", ocorrencia.getTipo());
    }

    @Test
    void extravioOcorrenciaCreatorRegistraUmaOcorrenciaDeExtravio() {
        OcorrenciaCreator creator = new ExtravioOcorrenciaCreator("Galpao Osasco");

        Ocorrencia ocorrencia = creator.registrar("RS99999");

        assertInstanceOf(OcorrenciaExtravio.class, ocorrencia);
        assertEquals("EXTRAVIO", ocorrencia.getTipo());
    }

    @Test
    void registrarComCodigoDeRastreioVazioLancaExcecaoEmQualquerCreator() {
        OcorrenciaCreator atraso = new AtrasoOcorrenciaCreator(3);
        OcorrenciaCreator extravio = new ExtravioOcorrenciaCreator("Galpao Osasco");

        assertThrows(IllegalArgumentException.class, () -> atraso.registrar(""));
        assertThrows(IllegalArgumentException.class, () -> extravio.registrar(""));
    }
}
```

```bash
./mvnw test
```

Saída de referência, obtida rodando este mesmo gabarito:

```
[INFO] Running br.uni9.rotasul.rastreamento.domain.OcorrenciaCreatorTest
[INFO] Tests run: 3, Failures: 0, Errors: 0, Skipped: 0
[INFO] BUILD SUCCESS
```

### 3.11 Registrar as duas decisões

Em `docs/decisoes.md`, duas linhas novas:

> Cálculo de frete: Strategy, porque a fórmula precisa variar por pedido, em
> tempo de execução (frota própria na rota principal, transportadora
> parceira na última milha).

> Criação de `Ocorrencia`: Factory Method, porque o código que recebe a
> ligação do atendente não deve conhecer as subclasses concretas
> (`OcorrenciaAtraso`, `OcorrenciaExtravio`).

## 4. Entregável

No fork do aluno:

- `CalculadoraDeFrete`, `FreteRotaPropria` e `FreteTransportadoraParceira`,
  em `pedido.domain`.
- `Pedido` (Aula 06) acrescido do atributo `regiao`.
- `CalculoDeFreteService`, em `pedido.service`, anotada `@Service`.
- `CalculoDeFreteServiceTest`, com os dois casos de região, passando.
- `Ocorrencia`, `OcorrenciaAtraso` e `OcorrenciaExtravio`, em
  `rastreamento.domain`.
- `OcorrenciaCreator`, `AtrasoOcorrenciaCreator` e
  `ExtravioOcorrenciaCreator`, também em `rastreamento.domain`.
- `OcorrenciaCreatorTest`, com os três casos, passando.
- `docs/decisoes.md` com as duas linhas novas.

## 5. Critérios de aceitação

| Critério | Evidência conferida na correção |
|---|---|
| `CalculoDeFreteServiceTest` passando | `./mvnw test` verde, `"PRINCIPAL"` calcula `15.00` e `"ULTIMA_MILHA"` calcula `19.50` |
| `OcorrenciaCreatorTest` passando | `./mvnw test` verde, os três casos: `ATRASO`, `EXTRAVIO` e a exceção do código vazio |
| Nenhuma anotação de framework nas classes de domínio envolvidas | Inspeção de `Pedido`, `CalculadoraDeFrete`, `FreteRotaPropria`, `FreteTransportadoraParceira`, `Ocorrencia`, `OcorrenciaAtraso`, `OcorrenciaExtravio`, `OcorrenciaCreator`, `AtrasoOcorrenciaCreator` e `ExtravioOcorrenciaCreator`: nenhuma tem anotação; só `CalculoDeFreteService` leva `@Service` |
| Nenhuma classe fora de `pedido.domain`, `pedido.service` e `rastreamento.domain` instancia diretamente uma das quatro implementações concretas | Busca por `new FreteRotaPropria`, `new FreteTransportadoraParceira`, `new AtrasoOcorrenciaCreator` e `new ExtravioOcorrenciaCreator` fora desses três pacotes |
| As duas decisões estão registradas | `docs/decisoes.md` com as duas linhas novas, Strategy e Factory Method |
| `./mvnw test` passando | Suíte inteira verde, incluindo os dois testes de hoje |
| O commit da aula existe | `git log` do fork mostra o commit `feat(padroes): aplica Strategy no calculo de frete e Factory Method na criacao de Ocorrencia` |

## 6. Commit e push esperados

```bash
git add src docs
git commit -m "feat(padroes): aplica Strategy no calculo de frete e Factory Method na criacao de Ocorrencia"
git push
```

## 7. Ambiente em que este gabarito foi verificado

Java 21 (`openjdk version "21.0.12"`) e Maven 3.9.16, com
`spring-boot-starter-parent` 3.3.4. Todo o código deste `README.md` foi
montado como projeto Maven, compilado e testado: `mvn clean compile`
(`BUILD SUCCESS`) e `mvn test`, com os cinco testes verdes (dois de
`CalculoDeFreteServiceTest`, três de `OcorrenciaCreatorTest`):

```
[INFO] Running br.uni9.rotasul.pedido.service.CalculoDeFreteServiceTest
[INFO] Tests run: 2, Failures: 0, Errors: 0, Skipped: 0
[INFO] Running br.uni9.rotasul.rastreamento.domain.OcorrenciaCreatorTest
[INFO] Tests run: 3, Failures: 0, Errors: 0, Skipped: 0
[INFO]
[INFO] Results:
[INFO]
[INFO] Tests run: 5, Failures: 0, Errors: 0, Skipped: 0
[INFO] BUILD SUCCESS
```
