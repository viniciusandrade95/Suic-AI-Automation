# 06 — Regras de recomendação do próximo passo

O dashboard deve escolher o próximo passo por lógica de desbloqueio, não por opinião.

## Pergunta principal

```text
Qual é a menor ação que mais desbloqueia o projeto agora?
```

## Ordem de prioridade

1. 🔴 Destravar bloqueios críticos.
2. 🧱 Concluir fundações ausentes.
3. 🔓 Fazer tarefas que desbloqueiam mais checkpoints.
4. 🎯 Completar fluxo ponta-a-ponta.
5. 🧪 Reduzir risco com validação.
6. ⚡ Aproveitar trabalho paralelo útil.
7. ✨ Fazer melhorias/polish só depois.

## Pontuação visual sugerida

| Critério | Peso | Exemplo |
|---|---:|---|
| Está desbloqueado | +30 | Pode começar agora. |
| É foundation | +25 | Sem isto o resto fica frágil. |
| Desbloqueia 2+ itens | +20 | Serviço/local abre booking e onboarding. |
| Completa fluxo E2E | +20 | Primeiro booking funcional. |
| Reduz risco alto | +15 | Resolve auth local. |
| É rápido | +10 | Atualizar status board. |
| É apenas polish | -10 | Visual refinado sem impacto agora. |
| Está bloqueado | -999 | Não recomendar como ação direta. |

## Formato obrigatório da recomendação

```text
🔥 Fazer agora: [ação curta]
🧠 Motivo: [por que importa]
🔓 Desbloqueia: [2-4 itens]
⚠️ Se ignorar: [consequência]
⚡ Paralelo: [uma alternativa útil]
```

## Exemplos de recomendação

### Exemplo 1 — Runtime

```text
🔥 Fazer agora: validar health `/healthz`
🧠 Motivo: garante que o backend atual sobe pelo caminho correto.
🔓 Desbloqueia: release checklist, API smoke, integração assistant.
⚠️ Se ignorar: risco de testar endpoint/entrypoint antigo.
⚡ Paralelo: atualizar status board visual.
```

### Exemplo 2 — Booking

```text
🔥 Fazer agora: criar serviço + local de demo
🧠 Motivo: public booking e onboarding dependem de dados mínimos.
🔓 Desbloqueia: slug público, horários, primeiro booking.
⚠️ Se ignorar: UI pode parecer pronta mas sem fluxo real.
⚡ Paralelo: preparar empty states do booking público.
```

### Exemplo 3 — Assistant

```text
🔥 Fazer agora: validar tenant/client mapping
🧠 Motivo: sem isso chatbot1 pode falar com o cliente errado.
🔓 Desbloqueia: assistant prebooking, chatbot proxy, smoke com trace.
⚠️ Se ignorar: risco de integração insegura ou confusa.
⚡ Paralelo: criar visual de estado assistant no dashboard.
```

### Exemplo 4 — UI/TDAH

```text
🔥 Fazer agora: criar bloco `AGORA` no cockpit
🧠 Motivo: reduz sobrecarga e evita lista gigante.
🔓 Desbloqueia: foco diário, status board, priorização visual.
⚠️ Se ignorar: dashboard vira lista textual confusa.
⚡ Paralelo: definir legenda visual consistente.
```

## Regras para não recomendar

Não recomendar como ação principal:

- item bloqueado;
- polish que não destrava nada;
- tarefa vaga tipo “melhorar sistema”;
- tarefa sem critério de conclusão;
- tarefa que exige decisão ainda não tomada;
- refatoração sem risco claro.

## Como mostrar bloqueados

Um item bloqueado deve aparecer assim:

```text
🔴 Bloqueado: Public booking confirm
Falta: appointment/prebooking válido
Destrava quando: serviço + local + horário + tenant passarem smoke
```

## Como mostrar paralelos

Um item paralelo deve aparecer assim:

```text
⚡ Paralelo: design do bloco `Feito`
Motivo: não depende do backend e melhora dopamina visual.
Não bloqueia: booking MVP.
```

## Regra anti-TDAH overload

O dashboard só deve mostrar:

- 1 recomendação principal;
- até 3 bloqueios;
- até 5 tarefas prontas;
- até 5 tarefas paralelas;
- até 3 riscos.

Todo o resto fica em detalhe expandível.
