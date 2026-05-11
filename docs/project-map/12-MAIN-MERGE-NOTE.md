# 12 — Main merge note

## Intenção

Adicionar uma pasta de documentação visual e operacional em:

```text
docs/project-map/
```

## Objetivo da mudança

Criar uma camada de projeto que organiza o TheOne por:

- capítulos/epics;
- checkpoints;
- dependências;
- paralelismo;
- riscos;
- regras de próximo passo;
- cockpit visual para TDAH severo;
- direção frontend Plainline Editorial.

## Ficheiros adicionados

```text
docs/project-map/README.md
docs/project-map/00-START-HERE.md
docs/project-map/01-PROJECT-OVERVIEW.md
docs/project-map/02-VISUAL-COCKPIT-BLUEPRINT.md
docs/project-map/03-EPICS-AND-CHECKPOINTS.md
docs/project-map/04-DEPENDENCY-MAP.md
docs/project-map/05-ROADMAP-STAGES.md
docs/project-map/06-NEXT-ACTION-RECOMMENDATION-RULES.md
docs/project-map/07-TDAH-VISUAL-RULES.md
docs/project-map/08-FRONTEND-DESIGN-DIRECTION.md
docs/project-map/09-ENGINEERING-RUNBOOK.md
docs/project-map/10-RISK-REGISTER.md
docs/project-map/11-STATUS-BOARD-TEMPLATE.md
docs/project-map/12-MAIN-MERGE-NOTE.md
```

## Commit message sugerida

```text
docs: add visual project map and execution cockpit
```

## PR title sugerido

```text
docs: add TheOne project map and visual execution cockpit
```

## PR description sugerida

```text
Adds docs/project-map as a visual, ADHD-friendly execution layer for TheOne.

Includes:
- project overview;
- epics and checkpoints;
- dependency map;
- roadmap stages;
- next-action recommendation rules;
- visual cockpit blueprint;
- TDAH visual rules;
- frontend design direction;
- risk register;
- status board template.

No runtime code changed.
No backend/frontend implementation changed.
```

## Validação esperada

Como isto é documentação:

- conferir links internos;
- conferir que não contradiz `docs/current/`;
- confirmar que não inclui secrets;
- confirmar que a pasta é apenas `.md`.

## Regra de precedência

Esta pasta não substitui `docs/current/`.

Ela organiza execução visual.

Se houver conflito:

```text
código atual > docs/current/ > docs/project-map/ > docs antigas
```

## Status de merge

Este ficheiro está pronto para entrar em `main`, mas precisa de commit/merge por uma ferramenta com permissão de escrita no GitHub ou por commit local.
