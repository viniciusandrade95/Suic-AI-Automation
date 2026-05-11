# 04 — Mapa de dependências

Este mapa mostra o que precisa vir antes, o que pode andar em paralelo e onde estão os gargalos.

## Fluxo macro

```text
🧱 Runtime canônico
  ↓
👤 Tenant/Auth
  ↓
🗂️ CRM Core
  ↓
📅 Appointments / Booking rules
  ↓
🌍 Public Booking MVP
  ↓
🚀 Onboarding de primeira ativação
  ↓
🧭 Dashboard/Cockpit mostra progresso e próxima ação
```

## Integração assistant

```text
👤 Tenant/Auth
  ↓
🗂️ CRM Core
  ↓
📅 Appointment/Prebooking rules
  ↓
🤖 Assistant Prebooking
  ↓
chatbot1 usa TheOne como fonte CRM
```

## Frontend/UX em paralelo

```text
🎨 Design System
  ↘
   🧭 Dashboard/Cockpit visual
  ↗
07-TDAH visual rules
```

Esta frente pode avançar enquanto CRM/booking é validado, desde que não invente dados nem altere contratos.

## Dependências por bloco

| Para fazer | Antes precisa de | Desbloqueia |
|---|---|---|
| Smoke local backend | Runtime/envs | Release checklist, API tests |
| Staff CRM real | Tenant/auth | Customers/services/locations/appointments |
| Public booking | Services + locations + booking slug | Primeiro valor público |
| Onboarding readiness | Services + locations + slug | Ativação guiada |
| Assistant prebooking | Tenant/auth + appointments | Conversa cria prebooking |
| Dashboard cockpit | Dados operacionais + rules | Próxima ação visual |
| Frontend polish | UX rules + design direction | Menos admin genérico |
| Release seguro | Tests + build + docs current | Merge confiável |

## Gargalos prováveis

### 🔴 Gargalo 1 — Tenant/token local

Sem tenant e token válidos:

- staff CRM não faz smoke real;
- `/api/chatbot/*` não é validado manualmente;
- prebooking protegido fica difícil de provar.

### 🔴 Gargalo 2 — Dados seed locais

Sem serviço/local/slug de demo:

- public booking fica travado;
- onboarding readiness não fecha;
- appointment/prebooking não é validado ponta-a-ponta.

### 🔴 Gargalo 3 — Docs antigas vs estado atual

Se alguém usar `/health` ou target antigo, perde tempo.

O estado atual deve usar `/healthz` e entrypoint com `app_factory --factory`.

### 🔴 Gargalo 4 — UI com informação demais

Mesmo funcional, o dashboard falha se exigir leitura profunda.

Para TDAH severo, o sistema precisa mostrar estado por símbolo, cor e posição.

## O que pode andar em paralelo

| Frente paralela | Depende pouco de | Valor |
|---|---|---|
| Design direction | Backend | Melhora clareza e identidade |
| Status board docs | Runtime | Ajuda foco imediato |
| Copy curta | Backend | Reduz carga cognitiva |
| Empty states | Dados reais | Ajuda telas vazias |
| QA evidence template | Funcionalidades | Evita esquecimentos |
| Visual dashboard blueprint | APIs finais | Define cockpit antes da implementação |

## O que não bloqueia MVP

- visual final premium em todas as telas;
- analytics avançados;
- relatórios complexos;
- automações outbound completas;
- personalização profunda por tenant;
- animações ou microinterações refinadas.

## O que bloqueia MVP

- runtime local confuso;
- tenant/auth sem validação;
- serviço/local inexistente;
- booking slug inválido;
- appointment/prebooking sem regra;
- public booking sem confirmação;
- testes essenciais ignorados.

## Resumo rápido

```text
🔴 Gargalo atual provável: tenant/token + seed local.
🔓 Maior desbloqueador: serviço + local + slug + health correto.
⚡ Melhor paralelo: cockpit visual + UX rules + status board.
✨ Pode esperar: polish premium em telas secundárias.
🔥 Fazer agora: transformar cada milestone em checkpoint verificável.
```
