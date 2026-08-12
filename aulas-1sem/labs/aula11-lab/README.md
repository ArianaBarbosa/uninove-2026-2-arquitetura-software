# Laboratório da Aula 11: Strategy no cálculo de frete, Factory Method na criação de `Ocorrencia`

Disciplina Arquitetura de Software, Uninove, Prof. José Romualdo. Roteiro dos
Ciclos 3 e 4 do encontro: dois padrões de projeto do catálogo GoF entram no
código da Rota Sul, cada um com teste JUnit. Nenhum endpoint novo nasce hoje.

## 0. O que chega pronto neste kit

Seis arquivos são andaime ou correção, não o conteúdo que a aula ensina, e
chegam prontos para o aluno copiar:

| Arquivo | Onde entra no fork | Papel |
|---|---|---|
| [`src/main/java/br/uni9/rotasul/pedido/domain/Pedido.java`](src/main/java/br/uni9/rotasul/pedido/domain/Pedido.java) | `pedido/domain/Pedido.java` (substitui a versão da Aula 06) | Já com o atributo `regiao` e o construtor de três argumentos que o Strategy de hoje usa |
| [`src/test/java/br/uni9/rotasul/pedido/service/PedidoServiceTest.java`](src/test/java/br/uni9/rotasul/pedido/service/PedidoServiceTest.java) | `pedido/service/PedidoServiceTest.java` (substitui a versão da Aula 06) | Chamada ao construtor de `Pedido` corrigida para três argumentos |
| [`src/test/java/br/uni9/rotasul/pedido/service/PedidoServiceContratoTest.java`](src/test/java/br/uni9/rotasul/pedido/service/PedidoServiceContratoTest.java) | `pedido/service/PedidoServiceContratoTest.java` (substitui a versão da Aula 07) | Chamada ao construtor de `Pedido` corrigida para três argumentos |
| [`src/main/java/br/uni9/rotasul/rastreamento/domain/Ocorrencia.java`](src/main/java/br/uni9/rotasul/rastreamento/domain/Ocorrencia.java) | `rastreamento/domain/Ocorrencia.java` | Produto abstrato do Factory Method |
| [`src/main/java/br/uni9/rotasul/rastreamento/domain/OcorrenciaAtraso.java`](src/main/java/br/uni9/rotasul/rastreamento/domain/OcorrenciaAtraso.java) | `rastreamento/domain/OcorrenciaAtraso.java` | Subclasse concreta do produto |
| [`src/main/java/br/uni9/rotasul/rastreamento/domain/OcorrenciaExtravio.java`](src/main/java/br/uni9/rotasul/rastreamento/domain/OcorrenciaExtravio.java) | `rastreamento/domain/OcorrenciaExtravio.java` | Subclasse concreta do produto |

**Por que a hierarquia de `Ocorrencia` vem pronta.** `Ocorrencia`,
`OcorrenciaAtraso` e `OcorrenciaExtravio` são herança simples, que a turma já
domina desde a Aula 06: uma classe abstrata com dois atributos e duas
subclasses que acrescentam um atributo cada. Não é o padrão que a aula
ensina. O padrão do dia, o Factory Method, mora em `OcorrenciaCreator` e nas
suas duas subclasses, no passo 3.8 abaixo: é ali que o aluno escreve código
novo. Digitar a hierarquia de produto não ensinaria nada sobre Factory
Method e consumiria tempo do laboratório.

**Por que `Pedido.java` e os dois testes vêm prontos.** O passo 3.2 de hoje
acrescenta `regiao` como terceiro parâmetro obrigatório do construtor de
`Pedido`. Trocar a assinatura de um construtor público quebra qualquer
chamada existente com dois argumentos, e duas já existem no fork desde antes
de hoje: `PedidoServiceTest` (Aula 06) e `PedidoServiceContratoTest` (Aula
07). Sem o ajuste, `./mvnw test` para de compilar o projeto inteiro, não só
os testes de hoje. O kit já entrega as duas classes corrigidas, para que a
suíte nasça verde e o critério de aceitação 6 (seção 5) seja honesto: o
aluno não precisa caçar, sob pressão de tempo, todo lugar do fork que chama
`new Pedido(...)`. `PedidoServiceTest` recebe um segundo ajuste, não ligado a
hoje: desde a Aula 07, `PedidoService` é uma interface, e a instanciação
usa `PedidoServicePadrao`, a implementação concreta que a substituiu naquela
aula.

Todo o código dos passos 3.2 a 3.6, 3.8, 3.9 e 3.10 abaixo é o que o aluno
escreve; os passos 3.1 e 3.7 usam os seis arquivos prontos, copiando-os sem
alteração.

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
- **Os seis arquivos da seção 0**, copiados para as posições indicadas.
- Nenhuma dependência nova no `pom.xml`: os dois padrões de hoje são código de
  domínio e serviço puro, sem biblioteca externa.

## 3. Passo a passo

### 3.1 Instalar o kit da camada `pedido` (Ciclo 3)

Copiar os três primeiros arquivos da seção 0 para as posições
correspondentes no fork, substituindo os que já existem:
`pedido/domain/Pedido.java`, `pedido/service/PedidoServiceTest.java` e
`pedido/service/PedidoServiceContratoTest.java`.

> **Mudar a assinatura de um construtor público tem custo.** `Pedido` é
> domínio, usado por toda a Rota Sul; qualquer código externo que já
> chamasse `new Pedido(cliente, descricao)`, com dois argumentos, deixa de
> compilar assim que `regiao` vira o terceiro parâmetro obrigatório. É
> exatamente o que aconteceu aqui: `PedidoServiceTest`, da Aula 06, e
> `PedidoServiceContratoTest`, da Aula 07 (o mesmo arquivo que o slide 4 de
> hoje projeta na tela, a propósito de Template Method), chamavam o
> construtor de duas posições. Mudar um contrato público sempre exige
> revisitar quem depende dele; hoje o kit já traz essa revisão pronta, mas
> em um sistema maior, ou num contrato exposto fora do próprio time, esse
> levantamento de impacto é trabalho real, e às vezes grande.

### 3.2 Criar o contrato da estratégia

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

`Pedido` já chegou pronto no passo 3.1, com o atributo `regiao` que o
Strategy de hoje usa para decidir qual estratégia aplicar; os valores
possíveis são `"PRINCIPAL"` e `"ULTIMA_MILHA"`.

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

### 3.7 Criar o contexto `rastreamento` e instalar a hierarquia de produtos (Ciclo 4)

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

Em seguida, copiar os três últimos arquivos da seção 0 para
`rastreamento/domain/`: `Ocorrencia.java`, `OcorrenciaAtraso.java` e
`OcorrenciaExtravio.java`. `Ocorrencia` é a classe abstrata com os
atributos `codigoRastreio` e `registradaEm` (`LocalDateTime`) e o método
abstrato `String getTipo()`; `OcorrenciaAtraso` acrescenta `horasDeAtraso`
e devolve `"ATRASO"`; `OcorrenciaExtravio` acrescenta
`ultimaLocalizacaoConhecida` e devolve `"EXTRAVIO"`. É herança simples, o
"produto" do Factory Method que o passo 3.8 constrói.

### 3.8 Escrever a hierarquia de criadores, o Factory Method

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

### 3.9 Testar o Factory Method

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

### 3.10 Registrar as duas decisões

Em `docs/decisoes.md`, duas linhas novas:

> Cálculo de frete: Strategy, porque a fórmula precisa variar por pedido, em
> tempo de execução (frota própria na rota principal, transportadora
> parceira na última milha).

> Criação de `Ocorrencia`: Factory Method, porque o código que recebe a
> ligação do atendente não deve conhecer as subclasses concretas
> (`OcorrenciaAtraso`, `OcorrenciaExtravio`).

## 4. Entregável

**Chega pronto no kit** (seção 0), copiado para o fork sem alteração:

- `Pedido` (Aula 06), acrescido do atributo `regiao` e do construtor de três
  argumentos.
- `PedidoServiceTest` (Aula 06) e `PedidoServiceContratoTest` (Aula 07),
  ajustados à nova assinatura do construtor de `Pedido`.
- `Ocorrencia`, `OcorrenciaAtraso` e `OcorrenciaExtravio`, em
  `rastreamento.domain`.

**O aluno escreve hoje:**

- `CalculadoraDeFrete`, `FreteRotaPropria` e `FreteTransportadoraParceira`,
  em `pedido.domain`.
- `CalculoDeFreteService`, em `pedido.service`, anotada `@Service`.
- `CalculoDeFreteServiceTest`, com os dois casos de região, passando.
- `OcorrenciaCreator`, `AtrasoOcorrenciaCreator` e
  `ExtravioOcorrenciaCreator`, em `rastreamento.domain`.
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
| `./mvnw test` passando | Suíte inteira verde, incluindo os dois testes de hoje e os testes das Aulas 06 e 07 que o kit já ajustou ao novo construtor de `Pedido` |
| O commit da aula existe | `git log` do fork mostra o commit `feat(padroes): aplica Strategy no calculo de frete e Factory Method na criacao de Ocorrencia` |

## 6. Commit e push esperados

```bash
git add src docs
git commit -m "feat(padroes): aplica Strategy no calculo de frete e Factory Method na criacao de Ocorrencia"
git push
```

## 7. Ambiente em que este gabarito foi verificado

Java 21 (`openjdk version "21.0.12"`) e Maven 3.9.16, com
`spring-boot-starter-parent` 3.3.4. Desta vez o gabarito montado para
verificação não isolou só o código novo de hoje: incluiu também `Pedido`,
`PedidoRepository`, `PedidoRepositoryEmMemoria`, a interface `PedidoService`
com as duas implementações da Aula 07 (`PedidoServicePadrao`,
`PedidoServiceComAnaliseDeRisco`) e as quatro classes de teste que dependem
do construtor de `Pedido` (`PedidoServiceTest`, `PedidoServiceContratoTest`
e as suas duas subclasses concretas), exatamente para confirmar que os seis
arquivos do kit (seção 0) fazem a suíte inteira do fork nascer verde, não só
o código de hoje isolado.

```
$ export JAVA_HOME=/opt/homebrew/opt/openjdk@21/libexec/openjdk.jdk/Contents/Home
$ export PATH="$JAVA_HOME/bin:$PATH"
$ java -version
openjdk version "21.0.12" 2026-07-21
$ mvn -version
Apache Maven 3.9.16, Java version: 21.0.12

$ mvn clean compile
BUILD SUCCESS   (sem warning nem erro)

$ mvn test
[INFO] Running br.uni9.rotasul.pedido.service.PedidoServiceTest
[INFO] Tests run: 2, Failures: 0, Errors: 0, Skipped: 0
[INFO] Running br.uni9.rotasul.pedido.service.PedidoServiceComAnaliseDeRiscoContratoTest
[INFO] Tests run: 2, Failures: 0, Errors: 0, Skipped: 0
[INFO] Running br.uni9.rotasul.pedido.service.CalculoDeFreteServiceTest
[INFO] Tests run: 2, Failures: 0, Errors: 0, Skipped: 0
[INFO] Running br.uni9.rotasul.pedido.service.PedidoServicePadraoContratoTest
[INFO] Tests run: 2, Failures: 0, Errors: 0, Skipped: 0
[INFO] Running br.uni9.rotasul.rastreamento.domain.OcorrenciaCreatorTest
[INFO] Tests run: 3, Failures: 0, Errors: 0, Skipped: 0
[INFO]
[INFO] Results:
[INFO]
[INFO] Tests run: 11, Failures: 0, Errors: 0, Skipped: 0
[INFO] BUILD SUCCESS
```

Os cinco testes de hoje (dois de `CalculoDeFreteServiceTest`, três de
`OcorrenciaCreatorTest`) mais os seis testes pré-existentes que o construtor
de `Pedido` afeta, todos verdes. `ps aux` confirmou que nenhum processo Java
ficou para trás.
