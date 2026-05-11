# 05 — Roadmap por estágios

Este roadmap não é uma lista linear.

Ele organiza o projeto por estados de maturidade.

---

# Estágio 0 — 🧱 Alinhar verdade operacional

## Objetivo

Eliminar confusão entre docs, comandos antigos e runtime atual.

## Resultado esperado

Todos sabem:

- qual entrypoint usar;
- qual health usar;
- quais docs vencem;
- quais testes são obrigatórios.

## Obrigatório

- ✅ `docs/current/` como fonte canônica.
- ✅ Entry point oficial documentado.
- ✅ Health `/healthz` documentado.
- 🔵 Release checklist seguido.

## Paralelo

- Criar status board visual.
- Mapear riscos.
- Simplificar docs para leitura rápida.

## Critério para avançar

```text
Backend sobe localmente + health canônico responde + docs atuais não contradizem o fluxo.
```

## Risco principal

⚠️ Usar comando antigo e validar a coisa errada.

---

# Estágio 1 — 👤 Provar tenant/auth local

## Objetivo

Conseguir um ambiente local onde rotas protegidas possam ser testadas.

## Resultado esperado

Existe um tenant e um staff/token para smoke.

## Obrigatório

- Tenant local conhecido.
- Staff/token local validado.
- Header tenant definido.
- DB local ou fixture mínima.

## Opcional

- Script de seed completo.
- Múltiplos tenants de demo.

## Paralelo

- UX/copy do dashboard.
- Design cockpit.
- Docs de troubleshooting.

## Critério para avançar

```text
Uma rota staff protegida responde com tenant/token válidos.
```

## Risco principal

⚠️ Bloquear em auth antes de provar o fluxo principal.

---

# Estágio 2 — 🗂️ Provar CRM core mínimo

## Objetivo

Garantir que serviços, locais e clientes existem como base de booking.

## Resultado esperado

O sistema tem dados operacionais mínimos.

## Obrigatório

- Serviço ativo.
- Local ativo.
- Tenant associado.
- Cliente ou dados mínimos de contacto.

## Opcional

- Catálogo completo de serviços.
- Multi-location avançado.
- Importação de clientes.

## Paralelo

- Empty states.
- UI de ativação rápida.
- Checklist de dados mínimos.

## Critério para avançar

```text
É possível identificar “este negócio oferece este serviço neste local”.
```

## Risco principal

⚠️ Criar onboarding bonito sem dados reais suficientes.

---

# Estágio 3 — 📅 Provar appointment/prebooking

## Objetivo

Criar a primeira marcação/prebooking válida ponta-a-ponta.

## Resultado esperado

Existe uma marcação/prebooking com tenant, serviço, hora e estado.

## Obrigatório

- Regras mínimas de horário/disponibilidade.
- Serviço/local válidos.
- Criação de appointment ou prebooking.
- Teste/smoke documentado.

## Opcional

- Gestão avançada de conflitos.
- Reagendamento.
- Cancelamento refinado.

## Paralelo

- Dashboard mostra próximos appointments.
- Estado visual de marcação.
- Copy de confirmação.

## Critério para avançar

```text
Uma marcação/prebooking real é criada e aparece numa superfície operacional.
```

## Risco principal

⚠️ Duplicar regras entre public booking, CRM staff e assistant.

---

# Estágio 4 — 🌍 Primeiro fluxo público funcional

## Objetivo

Permitir que alguém marque pelo link público.

## Resultado esperado

`/book/{slug}` funciona minimamente.

## Obrigatório

- Slug público resolve tenant.
- Serviços públicos carregam.
- Horários/disponibilidade aparecem.
- Confirmação cria appointment/prebooking.
- Estado de sucesso/erro claro.

## Opcional

- Visual premium completo.
- Analytics de booking.
- Personalização de marca.

## Paralelo

- Melhorias visuais.
- Mobile-first review.
- Estados vazios e erros.

## Critério para avançar

```text
Cliente consegue completar um booking sem intervenção manual.
```

## Risco principal

⚠️ Link público existir mas não concluir marcação.

---

# Estágio 5 — 🚀 Onboarding ativa primeiro valor

## Objetivo

Levar o negócio do zero até link público funcional.

## Resultado esperado

Pessoa configura o mínimo sem se perder.

## Obrigatório

- Etapas curtas.
- Uma decisão por tela.
- Serviços/locais ativados sem formulário gigante.
- Slug validado inline.
- Readiness claro.

## Opcional

- Personalização avançada.
- Sugestões inteligentes por segmento.
- Wizard visual sofisticado.

## Paralelo

- Melhorar dashboard de readiness.
- Revisar copy curta.
- Reduzir carga cognitiva.

## Critério para avançar

```text
Novo negócio chega a um link funcional com fricção baixa.
```

## Risco principal

⚠️ Onboarding virar backoffice administrativo.

---

# Estágio 6 — 🤖 Assistant prebooking confiável

## Objetivo

Permitir que conversas usem dados CRM e criem/preparem prebookings.

## Resultado esperado

TheOne e chatbot1 trabalham juntos sem misturar responsabilidades.

## Obrigatório

- `CHATBOT_SERVICE_BASE_URL` correto.
- Proxy `/api/chatbot/message` validado.
- Proxy `/api/chatbot/reset` validado.
- Prebooking assistant testado.
- Tenant/client mapping claro.

## Opcional

- UI avançada de conversa.
- Histórico detalhado.
- Automação completa de confirmação.

## Paralelo

- Mostrar estado assistant no dashboard.
- Trace/correlação.
- Evidence de smoke.

## Critério para avançar

```text
Mensagem/intent sai do dashboard/conversa e chega à superfície CRM sem quebrar tenant.
```

## Risco principal

⚠️ Colocar lógica conversacional dentro do TheOne.

---

# Estágio 7 — 🧭 Cockpit visual operacional

## Objetivo

Fazer o dashboard mostrar o que fazer agora.

## Resultado esperado

Staff ou builder abre o dashboard e entende estado em segundos.

## Obrigatório

- Bloco `🔥 Agora`.
- Bloco `🔴 Bloqueado`.
- Bloco `🔵 Pode já`.
- Bloco `⚡ Paralelo`.
- Bloco `✅ Feito`.
- Bloco `⚠️ Risco`.

## Opcional

- Drag/drop.
- Histórico visual de progresso.
- Gráficos avançados.

## Paralelo

- Design polish.
- Labels curtas.
- Mobile layout.

## Critério para avançar

```text
A próxima ação é óbvia sem ler documento longo.
```

## Risco principal

⚠️ Dashboard bonito mas sem decisão.

---

# Estágio 8 — 🧪 Release e hardening

## Objetivo

Garantir que o que existe é estável o suficiente para merge/release.

## Resultado esperado

Testes, build, docs e riscos estão registrados.

## Obrigatório

- Health passa.
- Testes relevantes passam.
- Frontend build passa se UI foi tocada.
- Docs atualizadas.
- Evidência sem secrets.
- Rollback surface documentado.

## Opcional

- Testes e2e completos.
- Observability avançada.
- CI mais rigoroso.

## Paralelo

- Docs de troubleshooting.
- Auditoria de UX.
- Performance review.

## Critério para avançar

```text
Mudança pode entrar em main sem depender de memória pessoal.
```

## Risco principal

⚠️ Fazer merge com comportamento funcional sem evidência mínima.
