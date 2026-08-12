# Laboratório da Aula 12: configuração explícita por perfil, `dev` e `prod`

Disciplina Arquitetura de Software, Uninove, Prof. José Romualdo. Roteiro dos
Ciclos 3 e 4 do encontro: inversão de controle na prática, com injeção de
dependência explícita e dois perfis de ambiente subindo com beans distintos.

## 0. O que chega pronto neste kit

Um arquivo é correção, não o conteúdo que a aula ensina, e chega pronto para
o aluno copiar:

| Arquivo | Onde entra no fork | Papel |
|---|---|---|
| [`src/main/java/br/uni9/rotasul/pedido/service/PedidoServicePadrao.java`](src/main/java/br/uni9/rotasul/pedido/service/PedidoServicePadrao.java) | `pedido/service/PedidoServicePadrao.java` (substitui a versão da Aula 07) | `@Profile` ampliado de `"padrao"` para `{"padrao", "dev", "prod"}` |

**Por que `PedidoServicePadrao` precisa mudar hoje.** Os perfis `dev` e
`prod` de hoje são perfis de ambiente: eles decidem qual `NotificadorDeOcorrencia`
sobe, não dizem nada sobre qual `PedidoService` usar. Mas `PedidoServicePadrao`,
desde a Aula 07, só está registrado como bean sob `@Profile("padrao")`, e
`PedidoServiceComAnaliseDeRisco` só sob `@Profile("risco")`. `PedidoController`
pede `PedidoService` no construtor sem nenhuma restrição de perfil: ele existe
em toda subida da aplicação. O passo 3.7 abaixo mostra o efeito exato: sem
este ajuste, `./mvnw spring-boot:run -Dspring-boot.run.profiles=dev` (o
critério de aceitação de hoje) falha com
`UnsatisfiedDependencyException: No qualifying bean of type 'PedidoService'`,
porque nem `"padrao"` nem `"risco"` batem com `"dev"`. Isso não é o mesmo
mecanismo das quebras anteriores (Aulas 07, 10 e 11): não é uma assinatura
que muda, é dois perfis com propósitos diferentes (escolha de implementação
contra escolha de ambiente) usando o mesmo mecanismo do Spring sem terem sido
desenhados juntos. O ajuste é o menor possível: ampliar a lista de perfis de
`PedidoServicePadrao`, sem tocar `PedidoServiceComAnaliseDeRisco`, que continua
exclusivo do perfil `"risco"`.

Todo o código dos passos 3.1 a 3.6 e 3.8 a 3.12 abaixo é o que o aluno
escreve; o passo 3.7 usa o arquivo pronto, copiando-o sem alteração.

## 1. O passo do case que esta aula resolve

Na Aula 11 cada aluno entregou dois padrões de projeto: Strategy no cálculo
de frete, com `CalculadoraDeFrete`, `FreteRotaPropria` e
`FreteTransportadoraParceira`, e Factory Method na criação de `Ocorrencia`,
com `OcorrenciaCreator` e seus dois criadores concretos. Ali quem decidia
qual estratégia usar era o próprio código da Rota Sul, uma linha de `if`
dentro do serviço. Hoje o Spring assume essa decisão: a interface
`NotificadorDeOcorrencia` ganha duas implementações, `NotificadorDeOcorrenciaConsole`
para o perfil `dev` e `NotificadorDeOcorrenciaWebhookSimulado` para o perfil
`prod`, escolhidas pelo container em tempo de subida, por métodos `@Bean` na
classe `NotificacaoConfig`. Ninguém no código da Rota Sul escreve o `if` que
decide qual das duas sobe: é exatamente a inversão de controle que dá nome à
aula.

O laboratório de hoje abre a camada `service` do contexto `rastreamento`,
que a Aula 11 abriu só com `domain`.

**`NotificadorDeOcorrencia.notificar(...)` ainda não é chamado por ninguém.**
Isso é deliberado: o objetivo de hoje é a configuração por perfil, provada
por log, não o fluxo completo de notificação. O passo 3.11 explica quando
essa chamada real entra.

## 2. Pré-requisitos

- **O fork da Aula 11**, com `CalculadoraDeFrete`, `FreteRotaPropria`,
  `FreteTransportadoraParceira`, `CalculoDeFreteService`,
  `CalculoDeFreteConfig` e a hierarquia de `OcorrenciaCreator`, já commitados
  e empurrados.
- **`Ocorrencia`** (com `codigoRastreio`, `registradaEm` e `getTipo()`), em
  `rastreamento.domain`, entregue pela Aula 11.
- **Java 21 LTS** e **Maven** ativos, conferidos na Aula 01.
- **O arquivo da seção 0**, copiado para a posição indicada.
- Nenhuma dependência nova no `pom.xml`: `NotificadorDeOcorrencia` e as duas
  implementações não usam biblioteca externa, só o `Logger` do SLF4J, que já
  vem com `spring-boot-starter-web`.

## 3. Passo a passo

### 3.1 Criar o contrato de notificação (Ciclo 3)

Em `rastreamento/service`, criar a interface `NotificadorDeOcorrencia`, com
um único método. Nenhuma anotação de framework: como toda interface de
contrato do semestre, ela não sabe que o Spring existe.

```java
package br.uni9.rotasul.rastreamento.service;

import br.uni9.rotasul.rastreamento.domain.Ocorrencia;

public interface NotificadorDeOcorrencia {

    void notificar(Ocorrencia ocorrencia);
}
```

### 3.2 Escrever a implementação de dev

`NotificadorDeOcorrenciaConsole`, também em `rastreamento/service`, sem
anotação nenhuma, registrando no log, via `Logger` do SLF4J, uma linha com o
`codigoRastreio` e o `getTipo()` da ocorrência.

```java
package br.uni9.rotasul.rastreamento.service;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import br.uni9.rotasul.rastreamento.domain.Ocorrencia;

public class NotificadorDeOcorrenciaConsole implements NotificadorDeOcorrencia {

    private static final Logger log = LoggerFactory.getLogger(NotificadorDeOcorrenciaConsole.class);

    @Override
    public void notificar(Ocorrencia ocorrencia) {
        log.info("[DEV] ocorrencia {} do tipo {} registrada",
                ocorrencia.getCodigoRastreio(), ocorrencia.getTipo());
    }
}
```

### 3.3 Escrever a implementação de prod

`NotificadorDeOcorrenciaWebhookSimulado`, recebendo `urlWebhook` pelo
construtor, também sem anotação. O método `notificar` não faz chamada de
rede real, só registra no log a URL e o código de rastreio. É simulado de
propósito, pela mesma razão da Aula 10: a aula não pode depender de um
endpoint externo de verdade para funcionar em qualquer sala.

```java
package br.uni9.rotasul.rastreamento.service;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import br.uni9.rotasul.rastreamento.domain.Ocorrencia;

public class NotificadorDeOcorrenciaWebhookSimulado implements NotificadorDeOcorrencia {

    private static final Logger log = LoggerFactory.getLogger(NotificadorDeOcorrenciaWebhookSimulado.class);

    private final String urlWebhook;

    public NotificadorDeOcorrenciaWebhookSimulado(String urlWebhook) {
        this.urlWebhook = urlWebhook;
    }

    @Override
    public void notificar(Ocorrencia ocorrencia) {
        log.info("[PROD] enviaria POST para {} com a ocorrencia {}",
                urlWebhook, ocorrencia.getCodigoRastreio());
    }
}
```

### 3.4 Registrar os dois beans, explicitamente

Criar `NotificacaoConfig`, anotada `@Configuration`, em
`rastreamento/service`, com dois métodos `@Bean`: um devolvendo
`NotificadorDeOcorrenciaConsole` sob `@Profile("dev")`, outro devolvendo
`NotificadorDeOcorrenciaWebhookSimulado` sob `@Profile("prod")`, recebendo a
URL do webhook por `@Value`.

```java
package br.uni9.rotasul.rastreamento.service;

import org.springframework.beans.factory.annotation.Value;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.context.annotation.Profile;

@Configuration
public class NotificacaoConfig {

    @Bean
    @Profile("dev")
    public NotificadorDeOcorrencia notificadorDeOcorrenciaDev() {
        return new NotificadorDeOcorrenciaConsole();
    }

    @Bean
    @Profile("prod")
    public NotificadorDeOcorrencia notificadorDeOcorrenciaProd(
            @Value("${rotasul.webhook.parceiro-notificacao}") String urlWebhook) {
        return new NotificadorDeOcorrenciaWebhookSimulado(urlWebhook);
    }
}
```

As classes de implementação em si não precisam de nenhuma anotação de
framework: elas só implementam a interface, e é o método `@Bean` que as
registra. Só um dos dois métodos roda em cada subida, nunca os dois ao mesmo
tempo, porque só um perfil, `dev` ou `prod`, fica ativo de cada vez.

### 3.5 Criar os dois arquivos de propriedades por perfil

Em `src/main/resources`, `application-dev.properties`, vazio por enquanto, e
`application-prod.properties`, com a linha:

```properties
rotasul.webhook.parceiro-notificacao=https://parceiro.rotasul.exemplo/webhook
```

É a segunda metade da "configuração por perfil" do entregável de hoje: não
só o bean muda, a propriedade também muda, e só o perfil `prod` precisa
saber o endereço do parceiro.

### 3.6 Comprovar por log

Acrescentar, ainda em `NotificacaoConfig`, um terceiro `@Bean`,
`logarNotificadorAtivo`, do tipo `CommandLineRunner`, que registra no log,
ao subir, qual `NotificadorDeOcorrencia` o container injetou:

```java
    @Bean
    @Profile({"dev", "prod"})
    public CommandLineRunner logarNotificadorAtivo(NotificadorDeOcorrencia notificador) {
        return args -> log.info("Notificador ativo: {}", notificador.getClass().getSimpleName());
    }
```

> **Este `@Bean` precisa de `@Profile({"dev", "prod"})`, e não pode ficar sem
> restrição nenhuma.** O construtor pede `NotificadorDeOcorrencia`, e esse
> tipo só tem bean registrado nos perfis `dev` e `prod` (passo 3.4). Se este
> método não levasse `@Profile`, ele tentaria ser criado em **qualquer**
> subida da aplicação, inclusive no perfil `padrao` (o perfil ativo por
> padrão desde a Aula 07) e no perfil `risco`, onde não existe nenhum
> `NotificadorDeOcorrencia` para injetar. O resultado seria
> `UnsatisfiedDependencyException` toda vez que alguém rodasse `./mvnw test`
> ou `./mvnw spring-boot:run` sem escolher `dev` nem `prod` de propósito, e a
> suíte inteira do fork pararia de fechar verde. A lição: um `@Bean` sem
> `@Profile` precisa que toda a sua dependência exista em qualquer perfil
> ativo; se a dependência só existe em alguns perfis, o bean também precisa
> da mesma restrição.

### 3.7 Instalar o ajuste em `PedidoServicePadrao` (Ciclo 4)

Copiar o arquivo da seção 0 para `pedido/service/PedidoServicePadrao.java`,
substituindo o que já existe.

> **Um segundo ponto de fiação que só o contexto Spring inteiro expõe.**
> `PedidoController`, desde a Aula 06, pede `PedidoService` no construtor sem
> nenhuma restrição de perfil: ele existe em toda subida da aplicação. Mas,
> desde a Aula 07, `PedidoServicePadrao` só é bean sob `@Profile("padrao")`,
> e `PedidoServiceComAnaliseDeRisco` só sob `@Profile("risco")`. Os perfis
> `dev` e `prod` de hoje são perfis de ambiente, escolhendo o notificador de
> ocorrência; eles não dizem nada sobre qual `PedidoService` usar, mas também
> não coincidem com `"padrao"` nem com `"risco"`. Sem este ajuste,
> `./mvnw spring-boot:run -Dspring-boot.run.profiles=dev` falha com
> `UnsatisfiedDependencyException: No qualifying bean of type 'PedidoService'`
> ao montar `PedidoController`, porque nenhum dos dois provedores bate com
> `"dev"`. A correção amplia a lista de `@Profile` de `PedidoServicePadrao`
> para `{"padrao", "dev", "prod"}`, sem tocar
> `PedidoServiceComAnaliseDeRisco`, que continua exclusivo de `"risco"`.
> Diferente das quebras das Aulas 07, 10 e 11, aqui não é uma assinatura que
> muda: são dois eixos de perfil (qual implementação de negócio, qual
> ambiente) que nunca tinham sido combinados antes de hoje.

### 3.8 Subir com o perfil `dev`

```bash
./mvnw spring-boot:run -Dspring-boot.run.profiles=dev
```

Conferir, no log de inicialização, a linha:

```
Notificador ativo: NotificadorDeOcorrenciaConsole
```

Saída de referência, obtida rodando este mesmo gabarito:

```
INFO ... Starting RotaSulApplication using Java 21.0.12 ...
INFO ... The following 1 profile is active: "dev"
INFO ... Started RotaSulApplication in 1.036 seconds
INFO b.u.r.r.service.NotificacaoConfig : Notificador ativo: NotificadorDeOcorrenciaConsole
```

### 3.9 Subir com o perfil `prod`

Parar a aplicação (`Ctrl+C`) e subir de novo:

```bash
./mvnw spring-boot:run -Dspring-boot.run.profiles=prod
```

Conferir a linha:

```
Notificador ativo: NotificadorDeOcorrenciaWebhookSimulado
```

Saída de referência, obtida rodando este mesmo gabarito:

```
INFO b.u.r.r.service.NotificacaoConfig : Notificador ativo: NotificadorDeOcorrenciaWebhookSimulado
```

As duas capturas de log, `dev` e `prod`, são a evidência literal que o
entregável de hoje pede.

### 3.10 Testar os dois perfis

Duas classes de teste em
`src/test/java/br/uni9/rotasul/rastreamento/service/`:

```java
package br.uni9.rotasul.rastreamento.service;

import static org.junit.jupiter.api.Assertions.assertInstanceOf;

import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.test.context.ActiveProfiles;

@SpringBootTest
@ActiveProfiles("dev")
class NotificacaoConfigDevTest {

    @Autowired
    private NotificadorDeOcorrencia notificador;

    @Test
    void perfilDevInjetaONotificadorDeConsole() {
        assertInstanceOf(NotificadorDeOcorrenciaConsole.class, notificador);
    }
}
```

`NotificacaoConfigProdTest` é simétrico: `@ActiveProfiles("prod")`,
confirmando `instanceof NotificadorDeOcorrenciaWebhookSimulado`.

```bash
./mvnw test
```

Rodar as duas, sem que a suíte precise escolher perfil nenhum na linha de
comando: cada teste fixa o seu.

### 3.11 Deixar o gancho para a Aula 19

Ninguém chama `notificar(...)` de dentro de `OcorrenciaCreator` ainda, e está
certo que seja assim: hoje o objetivo é a configuração por perfil, não o
fluxo completo de notificação. A chamada real a `NotificadorDeOcorrencia`
entra quando os serviços da Rota Sul conversarem entre si de verdade, na
Aula 19.

### 3.12 Registrar a decisão

Em `docs/decisoes.md`, uma linha explicando a escolha de configuração
explícita por `@Configuration` em vez de `@Profile` direto na classe, e por
quê:

> Notificação de ocorrência: configuração explícita por `NotificacaoConfig`
> em vez de `@Profile` direto em `NotificadorDeOcorrenciaConsole` e
> `NotificadorDeOcorrenciaWebhookSimulado`, para concentrar a decisão de
> ambiente num único lugar, legível sem abrir cada implementação.

## 4. Entregável

**Chega pronto no kit** (seção 0), copiado para o fork sem alteração:

- `PedidoServicePadrao` (Aula 07), com `@Profile` ampliado para
  `{"padrao", "dev", "prod"}`.

**O aluno escreve hoje:**

- `NotificadorDeOcorrencia`, em `rastreamento.service`.
- `NotificadorDeOcorrenciaConsole` e `NotificadorDeOcorrenciaWebhookSimulado`,
  também em `rastreamento.service`.
- `NotificacaoConfig`, com os dois `@Bean` por perfil e o `CommandLineRunner`
  de log.
- `application-dev.properties` e `application-prod.properties`.
- `NotificacaoConfigDevTest` e `NotificacaoConfigProdTest`.
- `docs/decisoes.md` com a linha nova.

## 5. Critérios de aceitação

| Critério | Evidência conferida na correção |
|---|---|
| Subir com o perfil `dev` mostra o notificador certo | `./mvnw spring-boot:run -Dspring-boot.run.profiles=dev`, log com `Notificador ativo: NotificadorDeOcorrenciaConsole` |
| Subir com o perfil `prod` mostra o notificador certo | `./mvnw spring-boot:run -Dspring-boot.run.profiles=prod`, log com `Notificador ativo: NotificadorDeOcorrenciaWebhookSimulado` |
| Os dois logs mostram classes diferentes | Comparação direta das duas linhas acima |
| `NotificacaoConfigDevTest` passando | `./mvnw test` verde, `instanceof NotificadorDeOcorrenciaConsole` |
| `NotificacaoConfigProdTest` passando | `./mvnw test` verde, `instanceof NotificadorDeOcorrenciaWebhookSimulado` |
| Nenhuma anotação de framework nas duas implementações | Inspeção de `NotificadorDeOcorrenciaConsole` e `NotificadorDeOcorrenciaWebhookSimulado`: nenhuma tem anotação; só `NotificacaoConfig` leva `@Configuration` |
| A decisão está registrada | `docs/decisoes.md` com a linha nova sobre configuração explícita |
| `./mvnw test` passando | Suíte inteira verde, incluindo os testes de hoje e os das Aulas 06 a 11 |
| O commit da aula existe | `git log` do fork mostra o commit `feat(rastreamento): configura NotificadorDeOcorrencia por perfil dev e prod, com injecao explicita` |

## 6. Commit e push esperados

```bash
git add src docs
git commit -m "feat(rastreamento): configura NotificadorDeOcorrencia por perfil dev e prod, com injecao explicita"
git push
```

## 7. Ambiente em que este gabarito foi verificado

Java 21 (`openjdk version "21.0.12"`) e Maven 3.9.16, com
`spring-boot-starter-parent` 3.3.4. A verificação **não isolou o código de
hoje**: montou o fork acumulado inteiro, da Aula 06 até a Aula 11 (`Pedido`,
`PedidoRepository`, `PedidoService` com as duas implementações da Aula 07,
`RemessaController` e `RemessaService` da Aula 09, `ParceiroClient` e
`ParceiroClientConfig` da Aula 10, `CalculoDeFreteService` e
`CalculoDeFreteConfig` e a hierarquia de `OcorrenciaCreator` da Aula 11), com
o código de hoje por cima, e rodou `./mvnw test` nesse projeto acumulado.

Essa verificação ampla é o que revelou as duas quebras documentadas nas
seções 0 e 3.6/3.7: nenhuma delas aparece isolando só o código novo de hoje,
porque a primeira só se manifesta quando o Spring monta o contexto inteiro
sob um perfil sem `NotificadorDeOcorrencia`, e a segunda só se manifesta
quando o Spring monta `PedidoController` sob um perfil sem `PedidoService`.

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
Tests run: 2, Failures: 0, Errors: 0, Skipped: 0 -- in br.uni9.rotasul.parceiro.client.ParceiroClientTest
Tests run: 2, Failures: 0, Errors: 0, Skipped: 0 -- in br.uni9.rotasul.expedicao.web.RemessaControllerTest
Tests run: 2, Failures: 0, Errors: 0, Skipped: 0 -- in br.uni9.rotasul.pedido.service.PedidoServiceComAnaliseDeRiscoContratoTest
Tests run: 3, Failures: 0, Errors: 0, Skipped: 0 -- in br.uni9.rotasul.rastreamento.domain.OcorrenciaCreatorTest
Tests run: 2, Failures: 0, Errors: 0, Skipped: 0 -- in br.uni9.rotasul.pedido.service.PedidoServicePadraoTest
Tests run: 2, Failures: 0, Errors: 0, Skipped: 0 -- in br.uni9.rotasul.pedido.service.PedidoServicePadraoContratoTest
Tests run: 1, Failures: 0, Errors: 0, Skipped: 0 -- in br.uni9.rotasul.rastreamento.service.NotificacaoConfigDevTest
Tests run: 1, Failures: 0, Errors: 0, Skipped: 0 -- in br.uni9.rotasul.rastreamento.service.NotificacaoConfigProdTest
[INFO]
[INFO] Results:
[INFO]
[INFO] Tests run: 17, Failures: 0, Errors: 0, Skipped: 0
[INFO] BUILD SUCCESS
```

Dezessete testes verdes: os dois de hoje mais os quinze acumulados desde a
Aula 06. `./mvnw spring-boot:run -Dspring-boot.run.profiles=dev` e depois
`=prod` também foram executados de ponta a ponta neste mesmo projeto, com a
saída exata mostrada nos passos 3.8 e 3.9. `ps aux` confirmou que nenhum
processo Java ficou para trás ao final da verificação.
