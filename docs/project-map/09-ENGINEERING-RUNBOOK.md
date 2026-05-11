# 09 — Runbook de engenharia e validação

Este ficheiro resume o que validar sem inventar runtime novo.

## Fonte de verdade operacional

Usar `docs/current/` como camada canônica.

Quando houver contradição, decidir assim:

```text
1. Código atual
2. docs/current/
3. docs/project-map/
4. docs antigas/históricas
```

## Runtime atual esperado

| Área | Estado esperado |
|---|---|
| Backend | FastAPI |
| Backend app assembly | `app/http/main.py` |
| Frontend | Next.js em `frontend/` |
| Health canônico | `/healthz` |
| Public booking | `/book/{slug}` frontend + `/public/book/{slug}` backend |
| Staff CRM | `/crm/*` |
| Assistant surfaces | `/crm/assistant/*` e `/api/chatbot/*` |

## Validação mínima por tipo de alteração

### Alterou backend geral

- Health local responde.
- Teste smoke API passa.
- Docs atuais continuam corretas.

### Alterou assistant/chatbot proxy

- Teste de chatbot API relevante passa.
- `CHATBOT_SERVICE_BASE_URL` está correto.
- Tenant/client mapping validado.
- Trace/correlação considerada.

### Alterou prebooking

- Teste de assistant prebook passa.
- Payload mínimo registrado sem secrets.
- Appointment/prebooking respeita tenant.

### Alterou public booking

- Teste de public booking passa.
- Slug público resolve tenant.
- Página pública mostra erro/sucesso claro.

### Alterou onboarding/readiness

- Teste de onboarding readiness passa.
- UI continua progressiva.
- Não virou formulário gigante.

### Alterou frontend

- Build passa.
- Lint passa quando aplicável.
- Checklist UX passa.
- Mobile avaliado.
- Não há regressão para admin-template look.

## Variáveis relevantes

| Variável | Por quê importa |
|---|---|
| `ENV` | ambiente atual |
| `APP_NAME` | identificação app |
| `DATABASE_URL` | persistência |
| `SECRET_KEY` | auth/security |
| `TENANT_HEADER` | isolamento por tenant |
| `CHATBOT_SERVICE_BASE_URL` | integração com chatbot1 |
| `CHATBOT_SERVICE_TIMEOUT_SECONDS` | timeout upstream |
| `CHATBOT_CLIENT_ID` | override opcional tenant/client |
| `ASSISTANT_CONNECTOR_HEADER` | segurança assistant connector |
| `ASSISTANT_CONNECTOR_TOKEN` | segurança assistant connector |

## O que não versionar

- secrets;
- tokens;
- `.env` real;
- logs com dados sensíveis;
- dumps de DB;
- outputs locais enormes;
- screenshots com informações privadas.

## Evidência mínima de PR

```text
✅ O que mudou
🧪 O que foi testado
⚠️ O que ficou a validar
🔁 Rollback surface
📎 Docs atualizadas
```

## Critério de “pronto o suficiente”

Um checkpoint está pronto o suficiente quando:

- funciona no fluxo mínimo;
- tem critério observável;
- não quebra dependências conhecidas;
- está documentado se afeta comportamento;
- foi validado com o teste/smoke relevante;
- não depende de memória pessoal para repetir.
