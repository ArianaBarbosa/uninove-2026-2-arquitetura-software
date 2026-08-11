# ADR-003: Cópia em vez de symlink

**Data:** 11/08/2026
**Status:** Aceita
**Decisores:** Prof. José Romualdo

## Contexto

O acervo de Desenvolvimento Web compartilha seis arquivos com o acervo da FIAP
por symlink relativo (`tools/check_slides.py`, `tools/scaffold_labs.py`,
`.claude/settings.json`, `.claude/agents/construtor-aulas.md`,
`.claude/agents/revisor-slides.md`, `docs/referencia/SKILL-fiap.md`),
documentados na ADR-003 daquele repositório. Esse arranjo causou um incidente
de produção, registrado na ADR-006 do acervo de Desenvolvimento Web: o
workflow de publicação usava `actions/upload-pages-artifact@v3` com
`path: '.'`, empacotando o repositório inteiro, e essa action monta o
artefato com `tar --dereference --hard-dereference`, que precisa seguir todo
symlink até um arquivo real. No runner do GitHub Actions,
`actions/checkout@v4` traz apenas o próprio repositório: o alvo dos seis
symlinks, que só existe na máquina local do professor, não está ali. Os links
ficam quebrados (dangling), e o `tar` aborta com código de saída 1 ao tentar
dereferenciá-los. O primeiro push que continha os seis symlinks reproduziu
essa falha em produção e derrubou a publicação do site daquele acervo.

Este acervo, de Arquitetura de Software, tem quatro validadores
(`check_slides.py`, `check_decks.py`, `check_canto_coral.py`,
`check_portal.py`) e um tema (`uninove-theme.css`, `uninove-print.css`) que se
originam do mesmo código-base do acervo de Desenvolvimento Web.

## Decisão

Os quatro validadores e o tema deste acervo são cópias dos arquivos-fonte do
acervo de Desenvolvimento Web, não symlinks para o repositório irmão.

## Motivações

O incidente registrado na ADR-006 do acervo de Desenvolvimento Web é evidência
empírica direta do risco: um symlink relativo para um repositório irmão que só
existe localmente quebra o empacotamento do GitHub Pages assim que chega ao
runner, de forma silenciosa até o primeiro push. Este acervo está, em relação
a Desenvolvimento Web, na mesma posição relativa em que Desenvolvimento Web
está em relação à FIAP; o mesmo padrão de risco se repetiria.

Além do risco de symlink quebrado, os validadores deste acervo precisam
divergir do original de qualquer forma: não há regra de resolução de turma
nem de data-por-arquivo (ADR-002), e a regra nova, de reprovar data escrita à
mão, é específica deste acervo. Um symlink que precisa ser sobrescrito com
conteúdo diferente do arquivo original deixa de ser um symlink útil.

## Riscos conhecidos

- **Correção de bug em validador não se propaga sozinha entre os acervos.**
  Uma correção feita no `check_decks.py` de Desenvolvimento Web, por exemplo,
  precisa ser reaplicada manualmente aqui, caso se aplique.
  - **Mitigação:** nenhuma automática. É uma consequência aceita, listada
    abaixo como negativa, e não um risco a mitigar, dado que o objetivo desta
    decisão é justamente cortar a dependência entre os dois acervos.

## Consequências

### Positivas

- Este acervo é autônomo: nenhum arquivo dele depende da presença, do caminho
  ou do conteúdo do repositório de Desenvolvimento Web em tempo de build ou de
  publicação.
- O incidente do `tar --dereference` da ADR-006 de Desenvolvimento Web não
  pode se repetir aqui, porque não existe symlink algum no repositório: o
  passo `find _site -type l` do workflow de publicação, herdado como rede de
  segurança, nunca encontra nada para falhar.
- Os validadores podem divergir livremente do original (regra invertida de
  data, ausência de regra de turma) sem exigir nenhum mecanismo de
  sobrescrita.

### Negativas

- Correção de bug ou melhoria feita num validador de um dos três acervos
  (Desenvolvimento Web, FIAP ou este) não se propaga automaticamente para os
  outros dois; precisa ser identificada e reaplicada manualmente, acervo por
  acervo.
- Ao longo do tempo, os quatro validadores e o tema deste acervo podem
  divergir silenciosamente do original em pontos além dos intencionais, sem
  nenhum mecanismo automático de detecção de divergência.

## ADRs relacionadas

- ADR-002: sem resolução de turma e sem data no deck
