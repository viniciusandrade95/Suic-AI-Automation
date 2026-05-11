# 03 — Epics e Checkpoints

Este documento transforma o TheOne em capítulos funcionais.

Cada capítulo tem:

- objetivo;
- dependências;
- checkpoints verificáveis;
- categoria;
- status sugerido;
- critério de conclusão;
- paralelismo.

## Estados usados

| Estado | Significado |
|---|---|
| ✅ Feito | Evidenciado ou já documentado. |
| 🟡 Parcial | Existe, mas falta validação/acabamento. |
| 🔵 Pronto | Pode começar sem bloquear por dependência direta. |
| 🔴 Bloqueado | Precisa de outro checkpoint antes. |
| ⚠️ A validar | Precisa confirmação no runtime/local atual. |

---

# Epic 1 — 🧱 Runtime e fonte canônica

## Objetivo

Garantir que todos usam o mesmo entrypoint, health, docs e regras operacionais.

## Por que existe

Sem uma fonte canônica, o projeto perde tempo com comandos antigos, endpoints errados e runbooks contraditórios.

## Precisa funcionar

- Backend sobe pelo entrypoint oficial.
- Health oficial responde.
- Docs atuais vencem docs antigas.
- Release checklist existe e é seguido.

## Pode ficar imperfeito

- Automação total de startup local.
- Seeds locais padronizadas.
- Scripts auxiliares avançados.

## Checkpoints

| Status | Checkpoint | Categoria | Depende de | Desbloqueia | Paralelo? | Critério de conclusão |
|---|---|---|---|---|---|---|
| ✅ | Docs canônicas em `docs/current/` | 🧱 Foundation | — | Tudo que depende de orientação correta | Sim | Índice e canonical state existem. |
| ✅ | Entry point oficial documentado | 🧱 Foundation | Docs canônicas | Runbook local, deploy, QA | Não | Usar `app_factory --factory`. |
| ✅ | Health oficial documentado | 🧱 Foundation | Docs canônicas | Smoke local | Não | `/healthz` documentado como canônico. |
| 🟡 | Variáveis mínimas locais | 🔓 Unlocker | Config atual | Local run, assistant smoke | Sim | Lista mínima definida; valores reais ainda podem variar. |
| ⚠️ | Tenant/token local de smoke | ⚠️ Risk | Auth fixture local | Testes manuais autenticados | Não | Existe fluxo claro para obter token e tenant. |
| 🔵 | Status board visual desta pasta | 🔓 Unlocker | Este docs pack | Dashboard de execução | Sim | `11-STATUS-BOARD-TEMPLATE.md` atualizado. |

---

# Epic 2 — 👤 Tenant, Auth e isolamento

## Objetivo

Garantir que cada negócio opera isolado e que staff autenticado acede às superfícies corretas.

## Precisa funcionar

- Tenant identificado por header configurado.
- Rotas staff protegidas.
- Rotas públicas resolvem tenant por slug seguro.
- Integração com chatbot usa tenant/client mapping claro.

## Checkpoints

| Status | Checkpoint | Categoria | Depende de | Desbloqueia | Paralelo? | Critério de conclusão |
|---|---|---|---|---|---|---|
| 🟡 | Header tenant definido | 🧱 Foundation | Runtime/envs | Staff CRM e assistant | Não | `TENANT_HEADER` claro e usado. |
| 🟡 | Staff auth validada | 🧱 Foundation | Auth atual | CRM protegido | Não | Staff consegue chamar rotas protegidas com token. |
| ⚠️ | Fixture local de tenant | ⚠️ Risk | DB/seed local | Smokes autenticados | Sim | Existe tenant local conhecido. |
| ⚠️ | Fixture local de staff token | ⚠️ Risk | Auth local | Smokes `/crm/*` e `/api/chatbot/*` | Sim | Existe processo documentado para token local. |
| 🔵 | Mapa tenant_id = client_id | 🔓 Unlocker | Integração chatbot | Assistant prebooking | Sim | Regra clara: tenant_id vira client_id salvo override. |

---

# Epic 3 — 🗂️ CRM Core

## Objetivo

Sustentar a verdade operacional: clientes, serviços, locais e dados que alimentam booking/assistant.

## Precisa funcionar

- Cliente existe e é consultável.
- Serviço existe, tem duração/preço e estado ativo.
- Local existe e pertence ao tenant.
- Regras não duplicam lógica de appointment.

## Checkpoints

| Status | Checkpoint | Categoria | Depende de | Desbloqueia | Paralelo? | Critério de conclusão |
|---|---|---|---|---|---|---|
| 🟡 | Serviços ativos | 🧱 Foundation | Tenant/auth | Booking público, onboarding | Não | Serviço ativo com duração/preço válido. |
| 🟡 | Locais ativos | 🧱 Foundation | Tenant/auth | Booking público, appointments | Não | Local ativo disponível para marcação. |
| 🟡 | Clientes | 🧱 Foundation | Tenant/auth | CRM staff, appointment history | Sim | Cliente pode ser criado/listado por tenant. |
| 🔵 | Estado vazio útil para CRM | ✨ Enhancement | UI rules | Clareza do staff | Sim | Tela diz o que falta e próxima ação. |
| ⚠️ | Dados seed locais | ⚠️ Risk | DB local | Smokes rápidos | Sim | Serviços/locais/clientes de demo disponíveis. |

---

# Epic 4 — 📅 Appointments e regras de marcação

## Objetivo

Permitir criação e gestão de marcações/prebookings sem duplicar regras.

## Precisa funcionar

- Criar appointment/prebooking válido.
- Validar serviço, local, horário e tenant.
- Evitar conflitos ou dados inválidos.
- Alimentar dashboard e assistant.

## Checkpoints

| Status | Checkpoint | Categoria | Depende de | Desbloqueia | Paralelo? | Critério de conclusão |
|---|---|---|---|---|---|---|
| 🟡 | Modelo de appointment | 🧱 Foundation | CRM core | Booking e dashboard | Não | Appointment tem tenant, serviço, cliente/hora/status. |
| 🟡 | Regras de disponibilidade | 🔓 Unlocker | Serviços + locais | Public booking | Não | Horários válidos aparecem e inválidos não passam. |
| 🟡 | Criação staff CRM | 🔓 Unlocker | Auth + CRM | Operação interna | Sim | Staff cria marcação no CRM. |
| ⚠️ | Prebooking assistant | 🔓 Unlocker | Assistant contract | Conversa → CRM | Sim | `/crm/assistant/prebook` validado por teste/smoke. |
| 🔵 | Timeline/status visual | ✨ Enhancement | Appointment data | Dashboard mais claro | Sim | Status aparecem com símbolos, não texto longo. |

---

# Epic 5 — 🌍 Public Booking MVP

## Objetivo

Permitir que um cliente marque pelo link público `/book/{slug}`.

## Precisa funcionar

- Slug público resolve tenant.
- Página pública carrega serviços/locais/horários.
- Cliente escolhe horário e confirma.
- API pública cria marcação/prebooking seguro.

## Checkpoints

| Status | Checkpoint | Categoria | Depende de | Desbloqueia | Paralelo? | Critério de conclusão |
|---|---|---|---|---|---|---|
| 🟡 | Booking slug | 🧱 Foundation | Tenant settings | Link público | Não | Slug válido resolve tenant. |
| 🟡 | API pública por slug | 🔓 Unlocker | Slug + CRM core | Página `/book/{slug}` | Não | Dados públicos retornam sem header tenant. |
| 🟡 | UI pública simples | 🔓 Unlocker | API pública | Primeiro booking real | Sim | Cliente entende serviço/horário/confirmar. |
| ⚠️ | Confirmação de booking | 🎯 Milestone | Appointment rules | MVP booking completo | Não | Marcação criada e feedback visível. |
| 🔵 | Estado de erro público | ✨ Enhancement | UI pública | Confiança | Sim | Erro mostra próxima ação sem jargão. |

---

# Epic 6 — 🚀 Onboarding de primeira ativação

## Objetivo

Levar o negócio rapidamente ao primeiro link de booking funcional.

## Precisa funcionar

- Recolher o mínimo necessário.
- Ativar serviços/locais/settings sem formulário gigante.
- Validar slug/link público.
- Mostrar progresso de ativação.

## Checkpoints

| Status | Checkpoint | Categoria | Depende de | Desbloqueia | Paralelo? | Critério de conclusão |
|---|---|---|---|---|---|---|
| 🟡 | Etapas progressivas | 🔓 Unlocker | UX rules | Ativação simples | Sim | Cada etapa tem uma decisão principal. |
| ⚠️ | Serviços sem form pesado | ⚠️ Risk | CRM core + UX | Menos fricção | Sim | Sugestões aparecem como cards/ativar, não campos abertos. |
| ⚠️ | Slug com validação inline | 🔓 Unlocker | Tenant settings | Link público confiável | Não | Estados: carregando, disponível, indisponível, erro. |
| 🔵 | Readiness score | 🔓 Unlocker | Serviços/locais/slug | Dashboard de ativação | Sim | Mostra o que falta para publicar link. |
| 🔵 | Primeiro booking milestone | 🎯 Milestone | Public booking | Valor real do produto | Não | Negócio chega a link funcional. |

---

# Epic 7 — 🤖 Assistant Integration e prebooking

## Objetivo

Permitir que `chatbot1` use TheOne como verdade CRM para prebooking, sem misturar responsabilidades.

## Precisa funcionar

- TheOne expõe superfícies CRM/prebooking.
- TheOne chama `chatbot1` via `/api/chatbot/*` quando necessário.
- Tenant/client mapping é claro.
- Trace/correlação existe para debugging.

## Checkpoints

| Status | Checkpoint | Categoria | Depende de | Desbloqueia | Paralelo? | Critério de conclusão |
|---|---|---|---|---|---|---|
| 🟡 | Proxy `/api/chatbot/message` | 🔓 Unlocker | Auth + env chatbot | Chat no dashboard | Sim | Chamada passa do TheOne para chatbot1. |
| 🟡 | Proxy `/api/chatbot/reset` | 🔓 Unlocker | Auth + env chatbot | Reset operacional | Sim | Reset chega ao chatbot1. |
| ⚠️ | Prebooking assistant | 🔓 Unlocker | CRM/appointments | Conversa cria intenção de marcação | Não | Teste/smoke passa sem quebrar tenant. |
| ⚠️ | Trace ID/correlação | 🧪 Validation | Proxy/prebooking | Debug confiável | Sim | Trace aparece em evidência ou política. |
| 🔵 | Dashboard mostra estado assistant | ✨ Enhancement | APIs reais | Operação mais clara | Sim | Staff vê se assistant está pronto/bloqueado. |

---

# Epic 8 — 🧭 Staff Dashboard / Cockpit

## Objetivo

Fazer o dashboard responder perguntas operacionais sem leitura longa.

## Precisa funcionar

- Métricas essenciais.
- Próxima ação recomendada.
- Bloqueios e riscos visíveis.
- Itens feitos visíveis.
- Tarefas paralelas separadas.

## Checkpoints

| Status | Checkpoint | Categoria | Depende de | Desbloqueia | Paralelo? | Critério de conclusão |
|---|---|---|---|---|---|---|
| 🟡 | KPIs essenciais | 🔓 Unlocker | CRM/appointments | Visão operacional | Sim | Mostra hoje, próximos, clientes/booking status. |
| 🔵 | Bloco `🔥 Agora` | 🔓 Unlocker | Regras de recomendação | Decisão rápida | Sim | Uma ação principal aparece no topo. |
| 🔵 | Bloco `🔴 Bloqueado` | 🧪 Validation | Dependências mapeadas | Remoção de gargalos | Sim | Mostra dependência em falta. |
| 🔵 | Bloco `⚡ Paralelo` | ✨ Enhancement | Roadmap | Trabalho útil em dias travados | Sim | Mostra tarefas sem bloquear núcleo. |
| 🔵 | Bloco `✅ Feito` | ✨ Enhancement | Estado/progresso | Dopamina visual | Sim | Mostra conquistas sem poluir. |

---

# Epic 9 — 🎨 Frontend Design System e direção visual

## Objetivo

Tirar o produto de “admin genérico” e aproximar de um cockpit premium, claro e de baixa carga cognitiva.

## Direção

`Apple-grade Plainline Editorial Cockpit`

## Checkpoints

| Status | Checkpoint | Categoria | Depende de | Desbloqueia | Paralelo? | Critério de conclusão |
|---|---|---|---|---|---|---|
| ✅ | Direção visual definida | 🧱 Foundation | UX rules | Consistência UI | Sim | Plainline Editorial descrito em regra canônica. |
| 🟡 | Mist Blue foundation | 🧱 Foundation | Frontend setup | Componentes consistentes | Sim | Tokens/primitives existem. |
| 🔵 | Sidebar com identidade | ✨ Enhancement | Layout atual | Menos admin template | Sim | Sidebar ink/line markers/brackets. |
| 🔵 | Blocos estruturados por linhas | ✨ Enhancement | Dashboard atual | Mais presença sem sombra | Sim | Menos cards soltos, mais módulos. |
| 🔵 | Ícones monoline funcionais | ✨ Enhancement | UI inventory | Menos ruído | Sim | Ícones têm significado e stroke consistente. |
| 🔵 | Mobile-first review | 🧪 Validation | Tela final | Usabilidade real | Sim | Checklist mobile passou. |

---

# Epic 10 — 🧪 QA, evidência e release

## Objetivo

Evitar que progresso visual ou funcional entre sem validação mínima.

## Precisa funcionar

- Health local.
- Testes API relevantes.
- Build/lint frontend quando tocar UI.
- Migrations verificadas quando houver schema.
- Evidência sem secrets.

## Checkpoints

| Status | Checkpoint | Categoria | Depende de | Desbloqueia | Paralelo? | Critério de conclusão |
|---|---|---|---|---|---|---|
| ✅ | Release checklist canônico | 🧱 Foundation | docs/current | PRs seguros | Sim | Checklist existe e referencia testes certos. |
| 🔵 | Smoke local health | 🧪 Validation | Runtime | Confiança operacional | Não | `/healthz` retorna ok localmente. |
| 🔵 | API smoke mínimo | 🧪 Validation | DB/envs | Validação backend | Não | Testes relevantes passam. |
| 🔵 | Frontend build | 🧪 Validation | Frontend alterações | Merge seguro | Não | `npm run build` passa. |
| 🔵 | Evidence note | 🧪 Validation | Smoke/testes | Histórico de release | Sim | Resultado registrado sem secrets. |

---

## Resumo de desbloqueadores principais

| Desbloqueador | Abre |
|---|---|
| 🧱 Entry point + health corretos | QA local, release, integração. |
| 👤 Tenant/auth local | Smokes staff, chatbot proxy, CRM protegido. |
| 🗂️ Serviços + locais ativos | Public booking, onboarding, appointments. |
| 📅 Appointment/prebooking válido | Dashboard, assistant, primeiro valor real. |
| 🌍 Booking slug válido | Link público e onboarding completo. |
| 🧭 Bloco `🔥 Agora` | Decisão rápida e foco TDAH. |
| 🧪 Release checklist | Merge mais seguro. |
