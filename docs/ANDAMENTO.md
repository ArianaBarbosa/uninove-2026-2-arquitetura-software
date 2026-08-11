# Andamento do acervo

Este arquivo registra o estado do trabalho entre sessões. Deve ser o primeiro
documento lido ao abrir uma sessão nova neste repositório.

## Ordem de leitura ao abrir uma sessão

1. `CLAUDE.md`, na raiz do repositório (instruções gerais e armadilhas do trabalho).
2. `aulas-1sem/SKILL.md` (metodologia e padrão de construção de deck e kit).
3. Este arquivo, `docs/ANDAMENTO.md` (o que já está pronto, o que falta, pendências e decisões).

## Onde está cada coisa

| O quê | Onde |
|---|---|
| Repositório local | `/Users/joseromualdocostafilho/Projects/Uninove/2026/uninove-2026-2-arquitetura-software` |
| Remote | `git@github.com:josercf/uninove-2026-2-arquitetura-software.git`, branch `main` |
| Portal publicado | `https://josercf.github.io/uninove-2026-2-arquitetura-software/` |
| Acervo de referência (ACERVO_DW) | `/Users/joseromualdocostafilho/Projects/Uninove/2026/uninove-2026-2-desenvolvimento-web` |
| Ledger da execução | `.superpowers/sdd/2026-08-10-acervo-arquitetura-software/progress.md` |

## Concluído

**Task 1, bootstrap do repositório e publicação vazia.** Commit 75ab5e0 (verificado em bc6c078). Entregou `.gitignore`, `README.md`, `index.html`, `docs/ANDAMENTO.md` (este arquivo) e `.github/workflows/static.yml`. Repositório publicado com GitHub Pages. Pendência: os 18 PDFs do AVA estão em `pdf/` no disco, mas não foram commitados (ver Pendências do professor, item 1).

**Task 2, tema visual e assets.** Commit ea6c188. Copiados 47 arquivos CSS, JS e imagens do tema Uninove do acervo de Desenvolvimento Web. Cópia byte-idêntica confirmada; nenhum symlink, nenhum resíduo de turma.

**Task 3, plano de ensino.** Commits 85f1050 a 50b8fb9. Entregou `PLANO_DE_ENSINO.md` com 20 títulos de aulas (confirmados caractere a caractere contra cronograma), cronograma de 15 semanas, pesos de avaliação (totalizando 100 pontos), critérios do projeto final e referências bibliográficas. Seção 7.2 de frequência foi removida por conter regra inventada sem validação. Pendência: texto de frequência do regulamento institucional (ver Pendências do professor, item 2).

**Task 4, planejamento aula a aula das 20 aulas.** Commits 8c1320f a e324f92. Entregou `PLANEJAMENTO_AULA_A_AULA.md` com 6042 linhas, cabeçalho teórico e 20 seções minuto a minuto. Executada em quatro passagens (4a: Aulas 01-06, M1; 4b: Aulas 07-10, M2; 4c: Aulas 11-14, M3; 4d: Aulas 15-20, M4 e M5). Diagramas UML em PlantUML com proxy do plantuml.com. Laboratórios das Aulas 10 e 19 redimensionados (10 e 9 passos, respectivamente, contra limite de 12). Convenção de pacotes adotada: `br.uni9.rotasul.<contexto>.<camada>`. Modelo 3C ancorado em Pimentel e Fucks, não nos capítulos 02 e 03 do AVA (confirmado por leitura integral). Contrato herdado registrado (ver seção própria adiante).

**Task 5, metodologia de construção.** Commit 58cf204. Entregou `aulas-1sem/SKILL.md` com padrão completo de deck e kit para as 20 aulas. Documento contém descrição das 47 classes CSS do tema, avisos obrigatórios sobre desempenho e compatibilidade, e coerência confirmada contra plano de ensino e planejamento.

**Task 6, arquitetura de decisões.** Commit 1346ac1. Entregou seis ADRs em `docs/adrs/`:
- ADR-001: Stack Spring Boot no lugar de Jakarta EE.
- ADR-002: Sem resolução de turma e sem data no deck.
- ADR-003: Cópia em vez de symlink.
- ADR-004: Case Rota Sul e repositório esqueleto único.
- ADR-005: Mapeamento um-para-um com ordem do AVA.
- ADR-006: PlantUML com proxy para os diagramas UML (decisão do professor em 10/08/2026, registrada durante a execução da Task 4).

**Task 7, instruções de repositório.** Commit ac697e5. Entregou `CLAUDE.md` com onze armadilhas e avisos de consequência concreta para trabalho futuro neste repositório, incluindo mapeamento de chaves SSH, permissões, e comando de push.

## O que falta

**Tasks 8 a 11: Validadores e CI**

- Task 8: `check_decks.py` adaptado para este acervo e suíte pytest dos validadores fundamentais (7 testes esperados).
- Task 9: `check_slides.py` e `check_canto_coral.py`, validadores de diagramas.
- Task 10: `check_portal.py` e verificação de coerência do planejamento contra as 20 aulas.
- Task 11: Configuração de CI com GitHub Actions.

**Tasks 12 a 34: Decks, kits de laboratório e publicação**

- Task 12: Portal publicado com 20 cards vinculados às aulas (conteúdo dinâmico).
- Tasks 13-33: Vinte decks (padrão-ouro + 19 de aula) e respectivos kits de laboratório, com testes e armadilhas registradas (20 pares).
- Task 34: Revisão final, correção de regredir na coerência, e publicação do acervo completo.

Arquivos que ainda não existem: `tools/` com validadores, Portal em `_site/` com 20 cards, 20 decks em `aulas-1sem/` e `aulas-2sem/`, 20 kits em `kits-*sem/`, e 20 conjuntos de testes.

## Pendências do professor

**1. Versionamento dos 18 PDFs do AVA**

Os PDFs estão em `pdf/001.pdf` até `pdf/018.pdf` no disco, mas não foram commitados. O classificador do harness bloqueou a tentativa três vezes sem contorno. Para adicionar os PDFs ao repositório, execute:

```bash
git add pdf/
git commit -m "chore: versionamento dos 18 PDFs do AVA"
git push
```

Estes arquivos não são publicados no GitHub Pages (excluídos do rsync do artefato), mas ficam versionados no repositório.

**2. Texto de frequência para o plano de ensino**

A Task 3 removeu a seção 7.2 de frequência, que continha uma regra institucional inventada. Se houver regulamento a registrar, forneça o texto correto, e uma Task futura inserirá em `PLANO_DE_ENSINO.md`.

## Decisões tomadas durante a execução

**PlantUML com proxy** (ADR-006, consolidada em 10/08/2026). Inicialmente escolhido Mermaid para os diagramas UML, mas o professor reverteu em favor de PlantUML com proxy do plantuml.com. Motivo: Mermaid renderiza nativamente no GitHub mas tem apenas diagrama de classes nativo; componentes, implantação e pacotes exigiam fluxogramas com notação inventada, incompatível com disciplina que ensina notação UML. PlantUML oferece diagrama completo de componentes e sintaxe UML pura. Limitações do proxy: é serviço externo, e o fork do aluno deve ser público para renderização funcionar. Ambas as restrições documentadas no cabeçalho do planejamento.

**Modelo 3C ancorado em Pimentel e Fucks.** A Task 4a confirmou que o modelo 3C não está nos capítulos 02 e 03 do AVA (leitura integral dos dois capítulos realizada). A origem é Pimentel e Fucks, citados na bibliografia do capítulo 02. Plano corrigido em 19a4f8c para deixar explícita a fonte.

**Convenção de pacotes:** `br.uni9.rotasul.<contexto>.<camada>`. Adotada na Task 4a, herdada pelas demais passagens (4b, 4c, 4d).

**Contexto `parceiro` na Aula 10 usa subpacotes `endpoint` e `client`.** Não segue web/service/repository/domain como os demais contextos, mas a decisão foi aceita e registrada. Quem escrever o kit da Aula 19 precisa conhecer esta estrutura.

## Contrato herdado dos kits de laboratório

Dois roteiros (Aulas 10 e 19) passaram a depender de arquivos que devem chegar prontos no kit, sob pena de o laboratório não caber no tempo aula (60 minutos).

**Task 23, kit da Aula 10:** O roteiro espera encontrar nos arquivos do fork do aluno:
- `parceiro.xsd`: esquema XML do serviço SOAP simulado.
- `WebServiceConfig.java`: configuração Spring-WS contract-first do parceiro.

**Task 32, kit da Aula 19:** O roteiro espera encontrar:
- `pom.xml` pai (multi-módulo com cuatro serviços: pedidos-service, expedicao-service, rastreamento-service, parceiro-service).
- Quatro `Dockerfile`: um por serviço.
- `compose.yaml`: orquestração Docker.
- Quatro arquivos `application.properties`, um por serviço, com valores distintos de `spring.flyway.table`:
  - `pedidos-service`: `_pedidos`
  - `expedicao-service`: `_expedicao`
  - `rastreamento-service`: `_rastreamento`
  - `parceiro-service`: valor será definido no roteiro.

Quem escrever o kit da Aula 19 deve ler o relatório de conclusão da Task 4 (arquivo `task-4-report.md` no ledger) para confirmar nomes de pacotes e estrutura dos três serviços principais que não são exercício de laboratório.
