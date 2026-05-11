# 01 — Visão geral do projeto

## 🎯 Objetivo central

Criar um sistema operacional simples e confiável para negócios pequenos de serviços.

O produto deve permitir que um negócio consiga:

- configurar serviços e locais;
- gerir clientes;
- gerir marcações;
- publicar um link de booking;
- receber pré-marcações vindas do assistente;
- acompanhar estado do negócio num dashboard;
- integrar com `chatbot1` sem misturar responsabilidades.

## 🧱 Blocos principais

| Bloco | Papel | Tipo |
|---|---|---|
| 🧱 Runtime e repo truth | Garantir que o sistema sobe, tem health e docs canônicas. | Fundação |
| 👤 Tenant/Auth | Isolamento por negócio e acesso staff. | Fundação |
| 🗂️ CRM Core | Clientes, serviços e locais. | Fundação |
| 📅 Appointments | Agenda, disponibilidade e marcações. | Desbloqueador |
| 🌍 Public Booking | Página pública `/book/{slug}` e APIs públicas. | Produto |
| 🚀 Onboarding | Levar negócio até primeiro link funcional. | Produto |
| 🤖 Assistant Integration | TheOne como fonte CRM para chatbot/prebooking. | Integração |
| 🧭 Staff Dashboard | Estado operacional, métricas e ações. | Cockpit |
| 🎨 Design System | Mist Blue / Plainline Editorial UI. | Experiência |
| 🧪 QA/Release | Testes, checklist, evidência e segurança. | Validação |

## 🔁 Fluxo principal do produto

```text
Tenant/Auth
  ↓
Serviços + locais + staff
  ↓
Disponibilidade / booking settings
  ↓
Link público de booking
  ↓
Cliente escolhe serviço e horário
  ↓
Appointment/prebooking criado
  ↓
Dashboard mostra estado e próxima ação
  ↓
Assistente pode consultar/criar prebooking com regras CRM
```

## 🔥 O núcleo que precisa funcionar

O MVP real depende de:

1. tenant identificado;
2. staff autenticado;
3. serviço ativo;
4. local configurado;
5. booking settings válidas;
6. link público funcional;
7. criação de appointment/prebooking;
8. dashboard que mostra o que aconteceu;
9. testes mínimos a passar.

## ⚡ O que pode avançar em paralelo

Estas frentes podem andar sem esperar tudo estar perfeito:

- refinamento visual do dashboard;
- design system e tokens;
- copy curta e estados vazios;
- docs de execução;
- QA checklists;
- integração visual com assistant cockpit;
- preparação de mensagens/outbound;
- mapeamento de riscos.

## ✨ O que é importante mas pode esperar

- visual premium completo em todas as telas;
- automações avançadas de outbound;
- analytics sofisticados;
- multi-location profundo;
- permissões granulares avançadas;
- relatórios financeiros complexos;
- personalização estética por tenant.

## ⚠️ Pontos sensíveis

| Risco | Por quê importa |
|---|---|
| Docs antigas vs docs atuais | Pode causar uso de entrypoint/health errado. |
| Tenant/auth local | Sem token/tenant válido, smokes reais ficam difíceis. |
| Frontend com cara de admin genérico | Diminui confiança e clareza. |
| Booking público incompleto | Bloqueia primeiro valor real do produto. |
| Integração com chatbot misturada | Pode quebrar fronteira entre CRM e conversa. |
| Excesso de texto | Piora uso para TDAH severo. |

## Regra de fronteira

```text
TheOne = verdade CRM, booking, tenant, appointments.
chatbot1 = conversa, routing, RAG, diálogo e workflow conversacional.
```

Não colocar lógica de conversa dentro do TheOne.

Não colocar regras persistentes de CRM dentro do chatbot1.
