# 11 — Status Board Template

Usa este ficheiro como painel diário/semanal.

Mantém curto.

---

# 🧭 TheOne Status Board

## Progresso geral

```text
████░░░░░░ 40%
```

Estado geral: 🟡 Em construção

Próximo milestone: 🎯 Primeiro fluxo booking funcional

---

# 🔥 AGORA

```text
Ação:
Motivo:
Desbloqueia:
Se ignorar:
Paralelo:
```

Exemplo:

```text
Ação: validar tenant/token local
Motivo: sem auth local, staff CRM e assistant smoke ficam travados
Desbloqueia: CRM protegido, chatbot proxy, prebooking
Se ignorar: testes manuais ficam inconclusivos
Paralelo: refinar cockpit visual
```

---

# 🔴 BLOQUEADO

| Item | Falta | Destrava |
|---|---|---|
| Public booking confirm | appointment/prebooking válido | Primeiro booking E2E |
| Chatbot smoke | token + tenant | Assistant integration |
| Onboarding readiness | slug validado | Link público |

---

# 🔵 PODE FAZER JÁ

| Item | Categoria | Critério |
|---|---|---|
| Atualizar docs de status | 🧪 Validation | Estado atual claro |
| Revisar labels do dashboard | ✨ Polish | Labels com 1-3 palavras |
| Mapear seed mínima | 🔓 Unlocker | Tenant + serviço + local + slug |

---

# ⚡ PARALELO

| Item | Por quê pode ser paralelo |
|---|---|
| Melhorar empty states | Não depende do backend completo |
| Definir linguagem visual de status | Ajuda cockpit sem alterar API |
| Criar checklist UX mobile | Pode ser usado em qualquer tela |

---

# ✅ FEITO

| Feito | Evidência |
|---|---|
| README aponta docs canônicas | README atual |
| `docs/current/` define estado canônico | CANONICAL_STATE |
| UX rules definem direção visual | FRONTEND_UX_RULES |

---

# ⚠️ RISCO

| Risco | Nível | Ação |
|---|---|---|
| Tenant/token local indefinido | 🔴 Alto | Criar fixture ou runbook auth |
| UI com texto demais | 🟡 Médio | Aplicar TDAH visual rules |
| Merge sem evidência | 🔴 Alto | Seguir release checklist |

---

# 🎯 Capítulos

| Capítulo | Progresso | Estado | Próxima ação |
|---|---|---|---|
| 🧱 Runtime | ████░ 80% | 🟡 | Validar local real |
| 👤 Tenant/Auth | ██░░░ 40% | ⚠️ | Token/tenant smoke |
| 🗂️ CRM Core | ███░░ 60% | 🟡 | Serviço+local seed |
| 📅 Appointments | ██░░░ 40% | 🟡 | Prebooking/appointment smoke |
| 🌍 Public Booking | ██░░░ 40% | 🟡 | Confirm E2E |
| 🚀 Onboarding | ██░░░ 40% | 🟡 | Readiness + slug inline |
| 🤖 Assistant | ██░░░ 40% | ⚠️ | Proxy + trace smoke |
| 🧭 Dashboard | █░░░░ 20% | 🔵 | Bloco `AGORA` |
| 🎨 Design | ███░░ 60% | 🟡 | Plainline pass |
| 🧪 QA/Release | ███░░ 60% | 🔵 | Evidence note |

---

# 🧠 Nota curta do dia

```text
Hoje não tentar fazer tudo.
Escolher 1 item foundation/unlocker.
Se bloquear, escolher 1 item paralelo.
Registrar o que foi feito.
```
