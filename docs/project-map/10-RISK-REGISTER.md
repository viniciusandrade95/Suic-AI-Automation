# 10 — Risk Register

Este ficheiro lista riscos ativos, impacto e ação de redução.

## Escala simples

| Nível | Significado |
|---|---|
| 🔴 Alto | Pode bloquear milestone ou gerar retrabalho grande. |
| 🟡 Médio | Pode atrasar ou confundir. |
| 🔵 Baixo | Deve ser monitorado, mas não bloqueia agora. |

## Riscos principais

| Risco | Nível | Impacto | Mitigação | Dono sugerido |
|---|---|---|---|---|
| Docs antigas contradizem docs atuais | 🔴 Alto | Testes errados, entrypoint errado, perda de tempo | Sempre começar por `docs/current/` | Engenharia |
| Tenant/token local indefinido | 🔴 Alto | Bloqueia smokes staff e assistant | Criar fixture/local auth claro | Engenharia |
| Dados seed insuficientes | 🔴 Alto | Booking público não fecha E2E | Criar tenant + serviço + local + slug de demo | Produto/Eng |
| Public booking sem confirmação real | 🔴 Alto | Link existe mas não entrega valor | Validar criação de appointment/prebooking | Eng/QA |
| Onboarding vira backoffice | 🟡 Médio | Aumenta fricção e abandono | Uma decisão por etapa, progress disclosure | UX/Product |
| Dashboard vira lista gigante | 🟡 Médio | Piora TDAH e foco diário | Usar cockpit visual com blocos limitados | UX/Product |
| Frontend continua genérico | 🟡 Médio | Baixa percepção premium | Aplicar Plainline Editorial direction | Design/FE |
| Integração chatbot mistura responsabilidades | 🔴 Alto | TheOne vira sistema conversacional | Manter boundary: CRM vs conversa | Eng |
| Sem trace/correlação | 🟡 Médio | Debug difícil | Registrar trace_id/política de correlação | Eng/QA |
| Merge sem build/testes | 🔴 Alto | Regressão invisível | Release checklist obrigatório | Eng/QA |
| Excesso de polish antes do núcleo | 🟡 Médio | Perda de tempo e dispersão | Priorizar desbloqueadores | Produto |
| Falta de estado vazio útil | 🔵 Baixo | Confusão em telas sem dados | Empty states com próxima ação | UX |

## Riscos de TDAH severo

| Risco cognitivo | Sintoma | Correção |
|---|---|---|
| Informação demais | Travar antes de começar | Bloco `🔥 AGORA` com 1 tarefa |
| Muitos estados | Não saber o que significa | Legenda fixa e curta |
| Progresso invisível | Sensação de nada feito | Bloco `✅ FEITO` sempre visível |
| Bloqueio sem explicação | Frustração | Mostrar “falta X” |
| Paralelo misturado com principal | Dispersão | Separar `⚡ PARALELO` |
| Texto longo | Leitura evitada | Frases curtas, símbolos e barras |

## Riscos por estágio

| Estágio | Risco principal | Sinal de alerta |
|---|---|---|
| Runtime | usar health/entrypoint antigo | `/health` em vez de `/healthz` |
| Auth | não ter token local | smokes manuais impossíveis |
| CRM | serviços/locais faltando | booking não tem opções |
| Booking | confirmação não cria registro | usuário acha que marcou, mas nada salva |
| Onboarding | formulário gigante | uma etapa exige muitos campos |
| Assistant | tenant/client errado | conversa afeta tenant incorreto |
| Dashboard | mostra tudo | usuário não vê o próximo passo |
| Release | sem evidência | “funciona na minha máquina” |

## Regra de contenção

No cockpit, mostrar no máximo 3 riscos ativos.

Os demais ficam neste ficheiro.

## Template de risco novo

```text
⚠️ Risco:
Nível:
Impacto:
Sinal de alerta:
Mitigação:
Checkpoint afetado:
Dono sugerido:
Data/revisão:
```
