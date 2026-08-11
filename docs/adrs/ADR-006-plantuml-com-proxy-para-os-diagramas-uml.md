# ADR-006: PlantUML com proxy para os diagramas UML

**Data:** 11/08/2026
**Status:** Aceita
**Decisores:** Prof. José Romualdo

## Contexto

A disciplina exige diagramas UML de quatro naturezas ao longo do semestre:
componentes e implantação (Aula 04, arquitetura colaborativa da Rota Sul) e
classes e pacotes (Aula 05, diagramas estruturais). Os entregáveis são
arquivos versionados no fork do aluno e precisam ser legíveis diretamente no
GitHub, sem ferramenta externa nem passo de build.

A escolha da ferramenta de diagrama passou por três decisões sucessivas
durante a execução. O implementador da tarefa de construção da Aula 04
escolheu PlantUML. O controlador reverteu essa escolha para Mermaid, porque o
GitHub renderiza blocos ```mermaid``` nativamente em qualquer Markdown,
enquanto um `.puml` aparece como texto cru sem processamento adicional. Ao
implementar essa reversão, ficou evidente que o Mermaid só tem diagrama de
classes como notação UML nativa: componentes, implantação e pacotes não têm
suporte nativo e teriam que ser desenhados como fluxograma genérico, com uma
convenção de forma e cor inventada para simular a notação UML, numa
disciplina cujo objetivo, na Aula 05, é justamente ensinar a notação UML
formal. O professor reverteu a decisão de volta para PlantUML, resolvendo a
objeção original de renderização por meio do proxy oficial do `plantuml.com`,
que gera a imagem a partir do `.puml` cru hospedado no GitHub.

## Decisão

Os diagramas UML deste acervo são escritos em PlantUML e renderizados no
GitHub por meio do proxy oficial do `plantuml.com`, com a imagem embutida por
Markdown no arquivo `.md` irmão de cada `.puml`.

## Motivações

PlantUML tem suporte nativo às quatro notações que a disciplina precisa,
diagrama de componentes, de implantação, de classes e de pacotes, com a
sintaxe formal que a Aula 05 ensina. O Mermaid, alternativa considerada e
revertida, só oferece diagrama de classes nativamente; usá-lo para os outros
três tipos misturaria a ferramenta com a notação, obrigando a inventar uma
convenção de fluxograma para representar algo que a UML já define
formalmente, o oposto do que a Aula 05 se propõe a ensinar. O proxy do
`plantuml.com` resolve a única objeção real ao PlantUML, a ausência de
renderização nativa no GitHub: ele lê o `.puml` cru do repositório e devolve
uma imagem, embutida assim no `.md`:

```markdown
![Diagrama de componentes da Rota Sul](https://www.plantuml.com/plantuml/proxy?cache=no&src=https://raw.githubusercontent.com/SEU_USUARIO/uninove-2026-2-rota-sul/main/docs/arquitetura/componentes.puml)
```

O `src` aponta para o `raw` do próprio fork do aluno, e o `.puml` é
versionado ao lado do `.md`.

## Riscos conhecidos

- **A imagem depende de um serviço externo, o `plantuml.com`.** Se esse
  serviço ficar fora do ar, a imagem some do `.md`, ainda que o `.puml`-fonte
  continue correto e versionado.
  - **Mitigação:** nenhuma técnica automática. O `.puml` continua sendo a
    fonte da verdade, e a imagem pode ser regenerada por qualquer outra
    ferramenta PlantUML (local, IDE, `plantuml.jar`) a qualquer momento; o
    material declara essa dependência em voz alta em sala, para que a turma
    não trate a imagem embutida como garantida.
- **O proxy só consegue ler o `.puml` se o repositório do aluno for
  público.** Um fork marcado como privado quebra a renderização
  silenciosamente: o link da imagem aponta para um
  `raw.githubusercontent.com` que o proxy não consegue acessar.
  - **Mitigação:** o material diz explicitamente, no roteiro das Aulas 04 e
    05, que o fork precisa permanecer público para a imagem funcionar, na
    mesma linha da exigência já existente de porta pública no Codespaces da
    Aula 19.

## Consequências

### Positivas

- Os quatro tipos de diagrama UML que a disciplina precisa (componentes,
  implantação, classes, pacotes) são desenhados na notação formal e nativa
  da ferramenta, sem convenção inventada.
- A fonte (`.puml`) e a imagem renderizada ficam ambas versionadas e
  visíveis diretamente no GitHub, sem exigir instalação de ferramenta nem
  passo de build por parte do aluno.
- Os diagramas construídos durante a execução foram validados com
  `plantuml -syntax` e o proxy testado ponta a ponta com resposta HTTP 200,
  reduzindo o risco de armadilha de sintaxe não descoberta em sala.

### Negativas

- A renderização da imagem depende de disponibilidade de um serviço de
  terceiros fora do controle do acervo; uma queda do `plantuml.com` faz a
  imagem sumir de qualquer `.md` que a referencie, no fork de qualquer aluno.
- O aluno é obrigado a manter o repositório do fork público durante todo o
  semestre para que os diagramas continuem renderizando; um fork privado
  quebra a imagem sem erro visível além do link quebrado.
- A decisão trocou de rumo duas vezes durante a execução (PlantUML, depois
  Mermaid, depois PlantUML de novo), o que exigiu revalidar diagramas já
  escritos na primeira passagem antes de fechar a decisão final.

## ADRs relacionadas

- ADR-005: mapeamento 1 para 1 com a ordem do AVA
