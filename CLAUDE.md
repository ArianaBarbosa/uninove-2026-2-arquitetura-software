# CLAUDE.md

Antes de qualquer outra coisa, leia `docs/ANDAMENTO.md`. Ele registra o estado
do trabalho entre sessões e diz o que já está pronto e o que falta. Ele pode
estar desatualizado em relação ao histórico real do `git log`: se os dois
divergirem, confie no repositório em disco e no `git log`, não na tabela de
`docs/ANDAMENTO.md`, e atualize o arquivo antes de seguir.

## O que é este repositório

Acervo didático da disciplina **Arquitetura de Software**, curso de graduação
da Universidade Nove de Julho (Uninove), semestre 2026.2, Prof. José
Romualdo. Site estático a ser publicado no GitHub Pages, sem build e sem
bundler: os decks Reveal.js carregam do jsDelivr por CDN e o tema é CSS puro.
Não há passo de compilação em nenhum ponto do repositório.

Este acervo é irmão do acervo de **Desenvolvimento Web**
(`uninove-2026-2-desenvolvimento-web`), do mesmo professor, e reaproveita o
tema visual e os validadores daquele repositório. Mas as semelhanças param na
estrutura: este acervo **não** tem duas turmas, **não** resolve data por
código e **não** tem seletor de turma no portal. Ver seção "Armadilhas
conhecidas" e a ADR-002 antes de assumir qualquer coisa herdada do acervo de
Desenvolvimento Web.

## Estado atual do repositório

Sete das 34 tarefas do plano de implementação estão fechadas (Tasks 1 a 7).
Existem hoje, de fato, em disco:

- O esqueleto do repositório e o workflow de publicação
  (`.github/workflows/static.yml`), publicando no GitHub Pages.
- O tema visual completo, em `aulas-1sem/assets/` (`css/uninove-theme.css`,
  `css/uninove-print.css`, `js/uninove-quiz.js`, `img/uninove-logo.png`,
  `img/code-bg.png`).
- `PLANO_DE_ENSINO.md`, na raiz.
- `PLANEJAMENTO_AULA_A_AULA.md`, na raiz, com as 20 seções e 6247 linhas.
- `aulas-1sem/SKILL.md`, a metodologia e o padrão de construção de deck e kit.
- Os seis ADRs em `docs/adrs/` (ADR-001 a ADR-006).
- A suíte `tests/` com `test_publicacao.py` e `test_tema.py`, 7 testes.

**Ainda não existem, apesar de citados no planejamento e no SKILL.md:**

- O diretório `tools/` inteiro, com os quatro validadores
  (`check_slides.py`, `check_decks.py`, `check_canto_coral.py`,
  `check_portal.py`). Nenhum comando que os invoque funciona hoje.
- `aulas-1sem/index.html`, o portal com os 20 cards de aula.
- `aulas-1sem/aulas/`, `aulas-1sem/labs/`: nenhum deck e nenhum kit de
  laboratório foi construído ainda.
- `.github/workflows/ci.yml`, o workflow de integração contínua descrito na
  seção 10.2 do `aulas-1sem/SKILL.md`. Só existe `static.yml`, o de
  publicação.

Antes de rodar qualquer comando da seção seguinte, confira se o arquivo que
ele invoca já existe. Rodar um validador inexistente não falha com uma
mensagem clara de "arquivo não encontrado" em todos os shells; verifique com
`ls tools/` primeiro.

## Comandos

```bash
# Preview local (quando existir conteúdo em aulas-1sem/, os decks vão usar
# caminhos relativos e vão precisar de HTTP, não de file://)
python3 -m http.server 8000

# Exportação de um deck em PDF, quando os decks existirem: abrir com
# ?print-pdf e imprimir do navegador
# http://localhost:8000/aulas-1sem/aulas/aula01.html?print-pdf

# Testes de repositório (workflow de publicação e tema visual). Funciona hoje.
python3 -m pytest tests/ -v

# Os quatro comandos abaixo AINDA NÃO FUNCIONAM: tools/ não existe neste
# repositório ainda (ver "Estado atual"). Listados aqui porque são o padrão
# definido em aulas-1sem/SKILL.md, seção 10, para quando tools/ for criado.

# Validação de layout dos decks (estouro de 1280x720 e sobreposição)
python3 tools/check_slides.py

# Validação estrutural dos decks (data escrita à mão, decor-coral, quiz,
# âncoras, sequência de rodapés e caminhos relativos)
python3 tools/check_decks.py

# Validação pixel a pixel do triângulo coral, o ponto cego do check_slides.py
python3 tools/check_canto_coral.py

# Validação do portal e dos links dos cards
python3 tools/check_portal.py
```

Quando os quatro validadores existirem, nenhum substitui o outro: eles
conferem coisas diferentes. Os três de deck reportam o slide em **base 0**, a
mesma base de `Reveal.slide(i)`.

## As três camadas de conteúdo

1. **Planejamento, na raiz do repositório.** `PLANO_DE_ENSINO.md` (ementa,
   case, cronograma, avaliação) e `PLANEJAMENTO_AULA_A_AULA.md` (roteiro
   minuto a minuto das 20 aulas, mapeadas 1 para 1 com os 18 capítulos do AVA,
   ver ADR-005). São a fonte da verdade de títulos e escopo; decks e portal,
   quando construídos, seguem o que estiver aqui.
2. **Metodologia, em `aulas-1sem/SKILL.md`.** Descreve a espiral de conteúdo,
   o case Rota Sul, a estrutura do encontro de 150 minutos em quatro ciclos e
   o padrão de construção de decks e kits de laboratório. É o documento mais
   denso do repositório; leia antes de escrever qualquer deck.
3. **Materiais, em `aulas-1sem/`.** O portal (`index.html`, ainda não
   construído), os decks (`aulas/aulaXX.html`, ainda não construídos), os
   kits de laboratório (`labs/aulaXX-lab/`, ainda não construídos) e o tema
   visual (`assets/`, já pronto).

## O case Rota Sul

Todas as aulas e laboratórios constroem a **Rota Sul**, uma transportadora
fictícia de médio porte que evolui de um monólito conceitual, sem código de
aplicação nas Aulas 01 a 05, para uma aplicação Spring Boot em três camadas a
partir da Aula 06, e termina distribuída em quatro processos na Aula 19,
apresentada na Aula 20. Diferente de um laboratório por aula, existe um único
repositório-esqueleto, `josercf/uninove-2026-2-rota-sul`, que o aluno forka na
Aula 01 e evolui semana a semana; os diretórios em `aulas-1sem/labs/` são a
referência e o gabarito do professor para cada etapa, não repositórios à
parte. Ver ADR-004 para o raciocínio completo, e a seção 5 de
`aulas-1sem/SKILL.md` para o mini mundo, os atores, as entidades e o contrato
técnico (stack Java 21, Spring Boot 3.x, MySQL, Flyway, Thymeleaf).

## Anatomia do deck

Quando os decks forem construídos, cada `aulaXX.html` será autocontido, vai
medir exatamente 1280x720 e será inicializado com `center: false, margin: 0`.
A `section` do Reveal tem altura fixa: o conteúdo não rola, e o que não couber
quebra o slide visualmente sem lançar nenhum erro.

Ordem canônica de slides, em quatro ciclos de 35, 35, 35 e 25 minutos:

```
capa
título com AULA XX e o módulo, sem data
agenda com os horários dos quatro ciclos
ciclo 1                                                 19h30 às 20h05
ciclo 2                                                 20h05 às 20h40
quiz de fixação                                         20h40 às 20h50
ciclo 3 de laboratório                                  20h50 às 21h25
ciclo 4 de laboratório e entregável                     21h25 às 21h50
fechamento                                              21h50 às 22h00
referências da aula, com id="ref-slide"
encerramento com copyright
```

O slide de referências é canônico, entre o fechamento e o encerramento: é o
alvo das citações `[N]` dos títulos, e por isso leva `id="ref-slide"`.

Classes de slide: `cover-slide`, `title-slide`, `content-slide`,
`section-slide`, `quiz-slide`, `exercise-slide`, `end-slide`. `quiz-slide` e
`exercise-slide` não têm regras próprias de `.top-bar`, `.uninove-logo-header`
nem `.slide-footer`: por isso sempre se escreve `class="quiz-slide
content-slide"` e `class="exercise-slide content-slide"`.

A lista completa de blocos reutilizáveis, com o markup de cada um, está na
seção 6.3 de `aulas-1sem/SKILL.md`; não confie em nenhum resumo, confira
sempre no CSS real (`aulas-1sem/assets/css/uninove-theme.css`).

## Armadilhas conhecidas

- **Slide que estoura 720px não é detectável por `scrollHeight`**, porque a
  `section` do tema tem altura travada. O DOM não denuncia o estouro: a caixa
  simplesmente vaza visualmente sem lançar erro nem mudar `scrollHeight`. Só
  `tools/check_slides.py`, que mede geometria renderizada no navegador, pega
  isso. Inspeção visual isolada de um slide também não serve, porque o
  estouro pode não aparecer na resolução de tela de quem está olhando.

- **A `li` de `.quiz-options` é `display: flex` com `gap: 12px`.** Uma
  alternativa que contenha `<code>`, `<strong>` ou qualquer outro elemento
  inline no meio do texto precisa ter o texto inteiro envolvido em
  `<span class="option-text">`. Sem o `span`, o texto solto e o elemento
  inline viram itens de flex irmãos, e o `gap: 12px` do container abre um
  buraco de 12px de cada lado do elemento inline no lugar do espaço normal: a
  frase se parte visualmente na projeção. Alternativa de texto puro dispensa
  o `span`. **Nenhum validador cobre isso**, porque nada estoura nem se
  sobrepõe; é disciplina do autor do deck. Exemplo correto:

  ```html
  <li data-correct="false"><span class="option-letter">D</span><span class="option-text">Anota a interface num campo <code>@Autowired</code> e deixa o Spring resolver a implementação.</span></li>
  ```

- **Este acervo não tem resolução de turma.** Não existe `turmas.js`, não
  existe o atributo `data-data-da-aula`, não existe seletor de turma no
  portal, e nenhum deck exibe data. Diferente do acervo de Desenvolvimento
  Web, onde `check_decks.py` **exige** que `data-data-da-aula` bata com o
  número do encontro, o `check_decks.py` deste acervo (quando existir) faz o
  oposto: **reprova qualquer data escrita à mão** no corpo do deck, em
  `DD/MM/AAAA` ou por extenso. Ver ADR-002 para o raciocínio completo.

- **Os validadores em `tools/` e o tema em `aulas-1sem/assets/`, quando
  copiados, são cópias do acervo de Desenvolvimento Web, não symlinks.**
  Corrigir um bug num validador aqui não corrige o mesmo bug nos acervos
  irmãos (Desenvolvimento Web, FIAP); a correção precisa ser reaplicada
  manualmente, acervo por acervo, se também se aplicar a eles. Ver ADR-003.

- **Nenhum symlink pode existir neste repositório, em ponto nenhum.** O
  workflow de publicação (`.github/workflows/static.yml`) roda `find _site
  -type l` depois de montar o diretório de publicação e falha o build (exit
  1) se encontrar qualquer symlink. O motivo é o incidente descrito na
  ADR-003: `actions/upload-pages-artifact@v3` empacota com
  `tar --dereference`, que aborta ao tentar seguir um symlink cujo alvo não
  existe no runner. Este repositório resolve isso não tendo symlink nenhum,
  nunca corrigindo o `tar`; não recrie o padrão de symlink do acervo de
  Desenvolvimento Web aqui.

- **O remote deste repositório usa o host `github.com`**, que no
  `~/.ssh/config` do professor autentica como `canaldoovidio`
  (`IdentityFile ~/.ssh/id_ed25519`). Para publicar como `josercf`, o push
  precisa forçar a identidade correta:

  ```bash
  GIT_SSH_COMMAND='ssh -i /Users/joseromualdocostafilho/.ssh/id_ed25519_josercf -o IdentitiesOnly=yes -F /dev/null' git push
  ```

  Isso é **diferente** do acervo de Desenvolvimento Web, onde o remote usa o
  alias de host `github.com-josercf`, que já resolve para a identidade certa
  sozinho, e onde um `git push` simples basta. Aplicar o `GIT_SSH_COMMAND`
  acima no acervo de Desenvolvimento Web quebra o push por hostname não
  encontrado, porque `-F /dev/null` ignora o `~/.ssh/config` inteiro e o
  alias deixa de resolver.

- **O `rsync` do workflow de publicação precisa excluir `_site`.** Sem essa
  exclusão, o próprio `mkdir -p _site` seguido do `rsync ./ _site/` copia o
  diretório `_site` para dentro de si mesmo. As doze exclusões obrigatórias
  (`.git`, `.github`, `.claude`, `tools`, `tests`, `docs`, `pdf`,
  `node_modules`, `.superpowers`, `shots`, `CLAUDE.md`, `_site`) estão
  fixadas em `tests/test_publicacao.py`; qualquer exclusão removida do
  workflow sem ser removida também da lista do teste quebra o teste, de
  propósito.

- **O `pdf/` fica fora do artefato do GitHub Pages, de propósito**, porque
  contém material de terceiro (os 18 capítulos do AVA, de autoria do Prof.
  Paulo Ricardo Batista Mesquita) que não deve ser redistribuído publicamente
  pelo site, apesar de o repositório em si ser público.

- **Os 18 PDFs em `pdf/` estão untracked e precisam de ação manual do
  professor.** A decisão de versioná-los foi tomada explicitamente (ver
  `docs/ANDAMENTO.md` e o ledger de execução em
  `.superpowers/sdd/2026-08-10-acervo-arquitetura-software/progress.md`),
  mas o commit foi bloqueado pelo classificador do harness em três
  tentativas e não foi contornado. Pendência aberta. O professor precisa
  rodar, a partir da raiz do repositório:

  ```bash
  git add pdf/
  git commit -m "docs(pdf): versiona os 18 capitulos do AVA"
  GIT_SSH_COMMAND='ssh -i /Users/joseromualdocostafilho/.ssh/id_ed25519_josercf -o IdentitiesOnly=yes -F /dev/null' git push
  ```

  Nenhum agente deve tentar `git add pdf/` de novo sem que o professor peça
  explicitamente; três tentativas já falharam.

- **A ferramenta de diagrama do case é PlantUML com proxy do
  `plantuml.com`, não Mermaid.** A decisão teve vaivém durante a execução:
  PlantUML, revertido para Mermaid, revertido de volta para PlantUML. Ver
  ADR-006 para o histórico completo. Duas armadilhas de sintaxe já custaram
  tempo de aula:
  - `device` não aceita bloco com chaves. `device "Nome" { ... }` falha de
    sintaxe. A forma correta é um `node` comum com o estereótipo
    `<<device>>`: `node "Nome" as apelido <<device>> { ... }`.
  - `package` vazio ao lado de `class` no mesmo diagrama falha com a
    mensagem "Use 'allowmixing'". Um pacote sem nenhuma classe dentro dele,
    ao lado de declarações de classe soltas, mistura dois modos de diagrama
    que o PlantUML não combina por padrão. A correção é sempre colocar as
    classes dentro do `package` a que pertencem, nunca deixar `package`
    decorativo vazio ao lado de `class`.

- **`docs/ANDAMENTO.md` pode estar desatualizado.** Na revisão feita para
  este documento, a tabela "Concluído / O que falta" ainda listava apenas a
  Task 1 como concluída, quando o `git log` já mostrava as Tasks 1 a 6
  fechadas. Confira sempre `git log --oneline` contra a tabela antes de
  assumir que ela reflete o estado real.

## Convenções editoriais

- Português do Brasil com acentuação completa.
- Nunca usar travessão em dash.
- Sem emojis em slides, títulos ou textos. O tom é profissional e direto, sem
  frase de efeito.
- Nenhuma data de encontro de aula em nenhum material (ver ADR-002).
- Preferir diagramas e imagens didáticas a paredes de texto.
- Referências numeradas ao longo dos slides e consolidadas em um slide final,
  com `id="ref-slide"`.
- Todo deck termina com o slide de copyright do Prof. José Romualdo.
- Commits em Conventional Commits, acentuados, com escopo pela aula quando
  fizer sentido: `feat(aula01): ...`, `fix(portal): ...`, `docs(adr): ...`.
