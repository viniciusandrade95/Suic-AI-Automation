# 🧭 TheOne Project Map

Pasta de documentação visual para transformar o `theone` num mapa de execução por capítulos, checkpoints, dependências, riscos e próximos passos.

Esta pasta foi desenhada para leitura rápida, com foco em TDAH severo:

- pouco texto por bloco;
- muitos símbolos funcionais;
- títulos curtos;
- decisões visíveis;
- separação clara entre `AGORA`, `BLOQUEADO`, `PODE JÁ`, `PARALELO`, `FEITO` e `RISCO`.

## Começa aqui

| Ficheiro | Para quê serve |
|---|---|
| [`00-START-HERE.md`](./00-START-HERE.md) | Mapa de 30 segundos para abrir antes de qualquer trabalho. |
| [`01-PROJECT-OVERVIEW.md`](./01-PROJECT-OVERVIEW.md) | O que é o TheOne e quais são os blocos principais. |
| [`02-VISUAL-COCKPIT-BLUEPRINT.md`](./02-VISUAL-COCKPIT-BLUEPRINT.md) | Como o dashboard visual deve parecer e funcionar. |
| [`03-EPICS-AND-CHECKPOINTS.md`](./03-EPICS-AND-CHECKPOINTS.md) | Capítulos, checkpoints, critérios e dependências. |
| [`04-DEPENDENCY-MAP.md`](./04-DEPENDENCY-MAP.md) | O que desbloqueia o quê. |
| [`05-ROADMAP-STAGES.md`](./05-ROADMAP-STAGES.md) | Roadmap por estágios, não por lista infinita. |
| [`06-NEXT-ACTION-RECOMMENDATION-RULES.md`](./06-NEXT-ACTION-RECOMMENDATION-RULES.md) | Regras para escolher o próximo passo. |
| [`07-TDAH-VISUAL-RULES.md`](./07-TDAH-VISUAL-RULES.md) | Regras cognitivas obrigatórias para reduzir confusão. |
| [`08-FRONTEND-DESIGN-DIRECTION.md`](./08-FRONTEND-DESIGN-DIRECTION.md) | Direção visual Apple-grade Plainline Editorial Cockpit. |
| [`09-ENGINEERING-RUNBOOK.md`](./09-ENGINEERING-RUNBOOK.md) | Como validar sem inventar runtime novo. |
| [`10-RISK-REGISTER.md`](./10-RISK-REGISTER.md) | Riscos, gargalos e decisões em aberto. |
| [`11-STATUS-BOARD-TEMPLATE.md`](./11-STATUS-BOARD-TEMPLATE.md) | Template visual para status semanal/diário. |
| [`12-MAIN-MERGE-NOTE.md`](./12-MAIN-MERGE-NOTE.md) | Nota de commit/merge pretendida para `main`. |

## Regra central

O dashboard não deve ser uma lista gigante.

Ele deve responder em menos de 30 segundos:

```text
Onde estamos?
O que faço agora?
O que está bloqueado?
O que pode andar em paralelo?
O que já foi feito?
Qual é o maior risco?
```

## Ordem de leitura recomendada

1. `00-START-HERE.md`
2. `03-EPICS-AND-CHECKPOINTS.md`
3. `04-DEPENDENCY-MAP.md`
4. `02-VISUAL-COCKPIT-BLUEPRINT.md`
5. `06-NEXT-ACTION-RECOMMENDATION-RULES.md`

## Fonte de verdade

Esta pasta é uma camada visual/operacional.

Quando houver conflito:

1. Código atual do repo vence.
2. `docs/current/` vence esta pasta.
3. Esta pasta organiza execução, foco e próximos passos.
