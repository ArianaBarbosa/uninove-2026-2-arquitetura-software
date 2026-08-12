# Laboratório da Aula 05: os diagramas estruturais da Rota Sul

Disciplina Arquitetura de Software, Uninove, Prof. José Romualdo. Roteiro dos
Ciclos 3 e 4 do encontro: laboratório de modelagem estrutural, ainda sem
código de aplicação.

## 1. O passo do case que esta aula resolve

Na Aula 04 cada aluno entregou `docs/arquitetura-colaborativa.md` e os quatro
arquivos de `docs/arquitetura/`: `componentes.puml`/`.md` e
`implantacao.puml`/`.md`, os dois desenhados por intuição, sem checar contra
uma definição formal de UML. Este laboratório revisa o `componentes.puml`
contra três regras precisas e acrescenta dois diagramas novos: **classes do
domínio** e **pacotes**, os dois com a notação UML formal que o Ciclo 2 acabou
de explicar. O produto de hoje é `docs/arquitetura/dominio.puml` e
`dominio.md`, mais `docs/arquitetura/pacotes.puml` e `pacotes.md`. A Aula 06
transforma o diagrama de pacotes de hoje em pacotes Java de verdade.

> **Ainda sem código de aplicação.** O que se cobra hoje é a decisão: quais
> entidades existem, com quais atributos, e como o código vai se agrupar em
> pacotes. O comportamento das classes, os métodos, entra na Aula 06.

## 2. Pré-requisitos

- **O fork da Aula 01**, com `docs/arquitetura-colaborativa.md` e os quatro
  arquivos de `docs/arquitetura/` da Aula 04 já commitados e empurrados.
- Nenhuma instalação nova: os diagramas são texto puro, e a imagem é gerada
  por um serviço externo, não por ferramenta local.
- Ter em mãos a lista fixa das nove entidades do case: `Cliente`, `Pedido`,
  `Remessa`, `Volume`, `Rota`, `Veiculo`, `Motorista`, `Ocorrencia` e
  `Parceiro`. Esses nomes valem o semestre inteiro; ninguém inventa entidade
  fora da lista.

## 3. Passo a passo

### 3.1 Revisar o diagrama de componentes

Abrir `docs/arquitetura/componentes.puml`, da Aula 04, e conferir três coisas
que na semana passada podiam ter passado:

1. Toda interface declarada tem **nome de operação**, e não descrição de
   conteúdo: `receberPedidoValidado`, não "pedido validado".
2. Cada interface está ligada com `--` ao componente que a **oferece** e com
   `--(` ao que a **consome**, nunca o contrário.
3. Nenhum componente ficou sem interface: componente que não oferece nem
   consome nada é caixa solta, não é componente.

Corrigir o que for preciso e salvar por cima. O histórico do Git guarda a
versão anterior, e é ele que mostra a evolução do aluno; não é necessário
versionar as duas cópias.

### 3.2 Listar as classes do domínio

Escrever as nove entidades do case, cada uma com **no mínimo três atributos
tipados**. Sem métodos por enquanto: o comportamento entra na Aula 06, quando
as camadas aparecem.

| Entidade | Ideia de atributos |
|---|---|
| `Cliente` | id, nome, documento, telefone |
| `Pedido` | id, criadoEm, situação |
| `Remessa` | id, código de rastreio, previsão de entrega |
| `Volume` | id, peso, etiqueta |
| `Rota` | id, origem, destino, data de saída |
| `Veiculo` | id, placa, tipo, capacidade |
| `Motorista` | id, nome, CNH, telefone |
| `Ocorrencia` | id, tipo, quando foi registrada, descrição |
| `Parceiro` | id, razão social, área de cobertura |

### 3.3 Desenhar o diagrama de classes

Criar `docs/arquitetura/dominio.puml`, usando `class` e as associações da
UML. **Toda associação precisa de multiplicidade nas duas pontas.** Quatro
decisões que a turma precisa tomar explicitamente:

- Um `Pedido` gera uma ou várias `Remessa`?
- Uma `Remessa` tem quantos `Volume`?
- Uma `Ocorrencia` se liga ao `Volume`, à `Remessa` ou aos dois?
- O `Parceiro` se liga à `Remessa` ou ao `Volume` da última milha?

> **Não há gabarito único.** Há gabarito coerente: qualquer escolha vale,
> desde que o diagrama inteiro fique consistente com ela.

Esqueleto de partida com três das nove classes, para adaptar:

```
@startuml
title Classes do domínio da Rota Sul

class Pedido {
  +Long id
  +LocalDateTime criadoEm
  +String situacao
}

class Remessa {
  +Long id
  +String codigoRastreio
  +LocalDate previsaoEntrega
}

class Volume {
  +Long id
  +BigDecimal pesoKg
  +String etiqueta
}

Pedido "1" -- "1..*" Remessa
Remessa "1" -- "1..*" Volume
@enduml
```

Gabarito completo do professor, com as nove entidades e uma decisão coerente
para as quatro perguntas acima (`Ocorrencia` ligada tanto à `Remessa` quanto
ao `Volume`, e `Parceiro` ligado à `Remessa`):

```
@startuml
title Classes do domínio da Rota Sul

class Cliente {
  +Long id
  +String nome
  +String documento
  +String telefone
}

class Pedido {
  +Long id
  +LocalDateTime criadoEm
  +String situacao
}

class Remessa {
  +Long id
  +String codigoRastreio
  +LocalDate previsaoEntrega
}

class Volume {
  +Long id
  +BigDecimal pesoKg
  +String etiqueta
}

class Rota {
  +Long id
  +String origem
  +String destino
  +LocalDate dataSaida
}

class Veiculo {
  +Long id
  +String placa
  +String tipo
  +BigDecimal capacidadeKg
}

class Motorista {
  +Long id
  +String nome
  +String cnh
  +String telefone
}

class Ocorrencia {
  +Long id
  +String tipo
  +LocalDateTime registradaEm
  +String descricao
}

class Parceiro {
  +Long id
  +String razaoSocial
  +String areaCobertura
}

Cliente "1" -- "0..*" Pedido : faz
Pedido "1" -- "1..*" Remessa : gera
Remessa "1" -- "1..*" Volume : contém
Remessa "0..*" -- "1" Rota : segue
Rota "1" -- "1" Veiculo : utiliza
Rota "1" -- "1" Motorista : conduzida por
Remessa "1" -- "0..*" Ocorrencia : registra
Volume "1" -- "0..*" Ocorrencia : registra
Parceiro "1" -- "0..*" Remessa : entrega na última milha
@enduml
```

### 3.4 Criar o `.md` irmão e conferir a imagem

Criar `docs/arquitetura/dominio.md`, no mesmo formato do passo 3.4 da Aula 04,
trocando o nome do arquivo para `dominio.puml`:

```markdown
# Classes do domínio da Rota Sul

![Diagrama de classes do domínio da Rota Sul](https://www.plantuml.com/plantuml/proxy?cache=no&src=https://raw.githubusercontent.com/SEU_USUARIO/uninove-2026-2-rota-sul/main/docs/arquitetura/dominio.puml)
```

Commitar, empurrar e abrir o `.md` na página do fork. As nove classes
precisam aparecer desenhadas, com os atributos dentro de cada caixa e a
multiplicidade nas pontas das associações.

> **Se der erro.** Um retângulo com texto de erro no lugar da imagem é
> sintaxe errada no `.puml`; nada aparecendo é caminho errado no `src` ou
> fork privado.

### 3.5 Desenhar o diagrama de pacotes

Criar `docs/arquitetura/pacotes.puml`. Aqui a notação é `package`, aninhada,
com **pelo menos uma classe dentro de cada pacote**, e a dependência entre
pacotes desenhada com a seta tracejada `..>`. A estrutura de hoje é a que a
Aula 06 vai criar de verdade no código, e por isso os nomes são fixados agora
e não mudam:

- **Contexto primeiro, camada depois:** `br.uni9.rotasul.<contexto>.<camada>`.
- **Contextos:** `pedido`, `expedicao`, `rastreamento`, os mesmos nomes dos
  componentes da Aula 04 e dos processos separados da Aula 19.
- **Camadas:** `web`, `service`, `repository` e `domain`, seguindo a
  convenção do framework em inglês, enquanto os nomes de domínio ficam em
  português.
- **Direção das dependências:** sempre de `web` para `service` e de
  `service` para `repository`, nunca ao contrário.

Esqueleto de partida, com o contexto `pedido` completo e os outros dois
abreviados, para adaptar:

```
@startuml
title Pacotes da Rota Sul

package "br.uni9.rotasul" {

  package "pedido" {
    package "pedido.web" as web {
      class PedidoController
    }
    package "pedido.service" as service {
      class PedidoService
    }
    package "pedido.repository" as repository {
      interface PedidoRepository
    }
    package "pedido.domain" as domain {
      class Pedido
    }
  }

  package "expedicao" {
    class RemessaService
  }

  package "rastreamento" {
    class OcorrenciaService
  }
}

web ..> service
service ..> repository
service ..> domain
repository ..> domain
@enduml
```

Gabarito completo do professor, com os três contextos inteiros, cada um com
as quatro camadas:

```
@startuml
title Pacotes da Rota Sul

package "br.uni9.rotasul" {

  package "pedido" {
    package "pedido.web" as pedidoWeb {
      class PedidoController
    }
    package "pedido.service" as pedidoService {
      class PedidoService
    }
    package "pedido.repository" as pedidoRepository {
      interface PedidoRepository
    }
    package "pedido.domain" as pedidoDomain {
      class Pedido
    }
  }

  package "expedicao" {
    package "expedicao.web" as expedicaoWeb {
      class RemessaController
    }
    package "expedicao.service" as expedicaoService {
      class RemessaService
    }
    package "expedicao.repository" as expedicaoRepository {
      interface RemessaRepository
    }
    package "expedicao.domain" as expedicaoDomain {
      class Remessa
    }
  }

  package "rastreamento" {
    package "rastreamento.web" as rastreamentoWeb {
      class OcorrenciaController
    }
    package "rastreamento.service" as rastreamentoService {
      class OcorrenciaService
    }
    package "rastreamento.repository" as rastreamentoRepository {
      interface OcorrenciaRepository
    }
    package "rastreamento.domain" as rastreamentoDomain {
      class Ocorrencia
    }
  }
}

pedidoWeb ..> pedidoService
pedidoService ..> pedidoRepository
pedidoService ..> pedidoDomain
pedidoRepository ..> pedidoDomain

expedicaoWeb ..> expedicaoService
expedicaoService ..> expedicaoRepository
expedicaoService ..> expedicaoDomain
expedicaoRepository ..> expedicaoDomain

rastreamentoWeb ..> rastreamentoService
rastreamentoService ..> rastreamentoRepository
rastreamentoService ..> rastreamentoDomain
rastreamentoRepository ..> rastreamentoDomain
@enduml
```

> **Duas armadilhas de sintaxe que já custaram tempo de aula.** `device` não
> aceita bloco com chaves: essa armadilha é da Aula 04 (diagrama de
> implantação), mas o hábito de esquecer volta aqui. E **`package` vazio ao
> lado de `class` solta no mesmo diagrama falha com "Use allowmixing"**: toda
> classe entra dentro do pacote a que pertence, nunca um `package { }` vazio
> ao lado de uma `class` declarada fora dele. Os dois esqueletos acima evitam
> a segunda armadilha porque nenhum pacote fica vazio.

Criar `docs/arquitetura/pacotes.md`, no mesmo formato do passo 3.4, trocando
`dominio.puml` por `pacotes.puml` no `src`:

```markdown
# Pacotes da Rota Sul

![Diagrama de pacotes da Rota Sul](https://www.plantuml.com/plantuml/proxy?cache=no&src=https://raw.githubusercontent.com/SEU_USUARIO/uninove-2026-2-rota-sul/main/docs/arquitetura/pacotes.puml)
```

### 3.6 Registrar a decisão

Acrescentar em `docs/decisoes.md`, criado na Aula 02, uma linha registrando a
convenção de pacotes escolhida, com a justificativa da direção das
dependências:

```markdown
| Escolha | Motivo |
|---|---|
| ... linhas das aulas anteriores ... | ... |
| Pacotes por br.uni9.rotasul.contexto.camada | Contexto primeiro isola pedido, expedicao e rastreamento; camada depois separa web, service, repository e domain, com dependência sempre de fora para dentro |
```

## 4. Entregável

No fork do aluno:

- `docs/arquitetura/dominio.puml` e `dominio.md`.
- `docs/arquitetura/pacotes.puml` e `pacotes.md`.
- `docs/arquitetura/componentes.puml`, da Aula 04, revisado e salvo por cima.
- Uma linha nova em `docs/decisoes.md`.

Tudo commitado e empurrado.

## 5. Critérios de aceitação

| Critério | Evidência conferida na correção |
|---|---|
| As nove entidades no diagrama de classes, com atributos tipados | `dominio.puml` declara as nove `class` da lista fixa, cada uma com três ou mais atributos |
| Todas as associações com multiplicidade nas duas pontas | `dominio.puml`, cada linha de associação traz `"..."` nas duas pontas |
| Pacotes com os três contextos e as quatro camadas | `pacotes.puml` declara `pedido`, `expedicao` e `rastreamento`, cada um com `web`, `service`, `repository` e `domain` |
| Dependências de `web` para `service` e de `service` para `repository` | `pacotes.puml`, setas `..>` apontando sempre de fora para dentro |
| As duas imagens novas aparecem na página do `.md` no fork | Abrir `dominio.md` e `pacotes.md` no GitHub e ver a imagem desenhada, sem retângulo de erro |
| Componentes da Aula 04 revisados, sem componente sem interface | `componentes.puml`, cada `component` ligado a pelo menos uma `interface` |
| Linha nova no inventário | `docs/decisoes.md` com uma linha a mais, referente à convenção de pacotes de hoje |
| O commit da aula existe no fork | `git log` do fork mostra o commit `docs(uml): formaliza classes do dominio e pacotes da Rota Sul` |

## 6. Commit e push esperados

```bash
git add docs/arquitetura docs/decisoes.md
git commit -m "docs(uml): formaliza classes do dominio e pacotes da Rota Sul"
git push
```

Conferir no navegador que as três imagens de `docs/arquitetura/` aparecem
desenhadas: `componentes.md`, `dominio.md` e `pacotes.md`. Se alguma não
aparecer, conferir nesta ordem: o fork está público, o caminho do `src` bate
com o caminho real do `.puml`, e o `.puml` não tem erro de sintaxe. Quem
receber erro de permissão no `git push` provavelmente está usando um `origin`
incorreto: corrigir com
`git remote set-url origin https://github.com/SEU_USUARIO/uninove-2026-2-rota-sul.git`
e repetir o push.
