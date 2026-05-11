# 02 — Blueprint do Cockpit Visual

## Objetivo

Criar um dashboard que funciona como cockpit de decisão.

Não é para mostrar tudo.

É para responder rápido:

```text
O que faço agora?
O que está bloqueado?
O que pode andar em paralelo?
O que já está feito?
Qual é o risco principal?
```

## Layout ideal

```text
┌─────────────────────────────────────────────────────────────┐
│ 🧭 THEONE PROJECT MAP                                       │
│ Progresso geral ██████░░░░ 60%   Estado: 🟡 Em construção   │
│ Próximo milestone: 🎯 Primeiro fluxo booking funcional      │
└─────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────┐
│ 🔥 AGORA                                                    │
│ Concluir X                                                  │
│ 🧠 Motivo: sem isto, Y não avança                           │
│ 🔓 Desbloqueia: A, B, C                                     │
│ ⚡ Paralelo possível: Z                                     │
└─────────────────────────────────────────────────────────────┘

┌──────────────────────┬──────────────────────┬──────────────┐
│ 🎯 CAPÍTULOS          │ 🔴 BLOQUEADO          │ 🔵 PODE JÁ    │
│ 🧱 Runtime ████░      │ Item travado          │ Item pronto   │
│ 🗂️ CRM ███░░         │ Falta dependência     │ Item pronto   │
│ 🌍 Booking ██░░░      │                       │               │
└──────────────────────┴──────────────────────┴──────────────┘

┌──────────────────────┬──────────────────────┬──────────────┐
│ ⚡ PARALELO           │ ✅ FEITO              │ ⚠️ RISCO      │
│ UI polish            │ Health docs           │ Auth local    │
│ Docs                 │ README base           │ Scope creep   │
└──────────────────────┴──────────────────────┴──────────────┘
```

## Bloco principal: 🔥 AGORA

Deve ser o maior.

### Conteúdo máximo

| Linha | Conteúdo |
|---|---|
| Título | `🔥 Fazer agora` |
| Ação | 1 tarefa curta e concreta |
| Motivo | 1 frase |
| Desbloqueia | 2-4 itens |
| Se ignorar | 1 risco |
| Paralelo | 1 alternativa útil |

### Exemplo

```text
🔥 AGORA
Validar health e entrypoint canônico

🧠 Motivo: evita seguir runbooks antigos.
🔓 Desbloqueia: QA local, release checklist, integração assistant.
⚠️ Se ignorar: risco de testar endpoint errado.
⚡ Paralelo: revisar visual do dashboard.
```

## Bloco: 🔴 BLOQUEADO

Mostrar só:

- o item travado;
- o motivo;
- a dependência que destrava.

Exemplo:

```text
🔴 Public booking smoke
Falta: tenant + booking_slug válido
Destrava: primeiro fluxo público ponta-a-ponta
```

## Bloco: 🔵 PODE FAZER JÁ

Tarefas prontas e sem ambiguidade.

Exemplo:

```text
🔵 Atualizar status board
🔵 Revisar copy curta do dashboard
🔵 Mapear dependências de onboarding
```

## Bloco: ⚡ PARALELO

Para dias em que o núcleo está travado.

Exemplo:

```text
⚡ Preparar design direction
⚡ Criar empty states
⚡ Consolidar checklist de QA
⚡ Normalizar linguagem visual
```

## Bloco: ✅ FEITO

Importante para dopamina visual.

Nunca esconder completamente.

Exemplo:

```text
✅ README com áreas atuais
✅ docs/current como camada canônica
✅ UX rules com direção Plainline
```

## Bloco: ⚠️ RISCO

Pequeno, mas visível.

Não pode virar uma lista de ansiedade.

Máximo recomendado: 3 riscos ativos.

## Estados visuais

| Estado | Visual sugerido | Texto máximo |
|---|---|---|
| ✅ Feito | verde discreto, check, baixa prioridade visual | nome curto |
| 🟡 Em andamento | amarelo suave, barra parcial | nome + progresso |
| 🔴 Bloqueado | vermelho/laranja, lock, dependência | nome + falta |
| 🔵 Pronto | azul/calmo, círculo aberto | nome curto |
| ⚡ Paralelo | raio, área lateral | nome curto |
| 🔥 Recomendado | destaque grande no topo | ação + motivo |
| ⚠️ Risco | warning, lista limitada | risco + impacto |

## Regra de densidade

```text
Uma tela = uma decisão principal.
Um bloco = uma pergunta.
Uma linha = uma ideia.
```

## Anti-padrões

Evitar:

- cards demais;
- texto longo dentro de cards;
- duas ações primárias competindo;
- percentuais sem contexto;
- ícones decorativos sem significado;
- usar cor diferente para o mesmo estado;
- mostrar roadmap inteiro no bloco AGORA;
- esconder bloqueios importantes.
