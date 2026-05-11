# 07 — Regras visuais para TDAH severo

## Objetivo

O projeto deve ser navegável sem exigir leitura profunda.

A pessoa deve conseguir olhar, reconhecer símbolos e decidir.

## Princípios obrigatórios

| Regra | Como aplicar |
|---|---|
| Uma decisão principal por tela | Bloco `🔥 AGORA` domina. |
| Pouco texto por bloco | Máximo 3-5 linhas. |
| Símbolo antes de texto | Estado visual vem primeiro. |
| Cor consistente | Mesmo estado = mesma cor sempre. |
| Detalhes escondidos | Expandir só quando necessário. |
| Progresso visível | Barras simples, não dashboards densos. |
| Feito sempre visível | Dopamina visual reduz sensação de caos. |
| Bloqueio sem drama | Mostrar dependência, não culpa. |
| Paralelo separado | Evita ficar parado quando o núcleo bloqueia. |
| Copy curta | Verbos diretos e labels pequenos. |

## Estrutura cognitiva ideal

```text
🔥 AGORA       = ação principal
🔴 BLOQUEADO   = impede avanço
🔵 PODE JÁ     = sem dependência
⚡ PARALELO    = adiantar sem travar
✅ FEITO       = progresso alcançado
⚠️ RISCO       = atenção limitada
```

## Limites por bloco

| Bloco | Máximo recomendado |
|---|---:|
| 🔥 Agora | 1 item |
| 🔴 Bloqueado | 3 itens |
| 🔵 Pode já | 5 itens |
| ⚡ Paralelo | 5 itens |
| ✅ Feito | 5 itens recentes |
| ⚠️ Risco | 3 riscos ativos |
| Capítulos visíveis | 6-8 no máximo por tela |

## Bom exemplo

```text
🔥 AGORA
Validar booking slug

🧠 Motivo: sem link público, onboarding não fecha.
🔓 Desbloqueia: página pública, primeiro booking, readiness.
```

## Mau exemplo

```text
Precisamos melhorar a camada de configuração do sistema para permitir que múltiplos fluxos operacionais possam evoluir com maior robustez e garantir uma arquitetura de dados coerente...
```

Problemas:

- longo;
- abstrato;
- sem ação;
- sem estado;
- sem critério.

## Labels recomendadas

Usar:

- `Fazer agora`
- `Falta isto`
- `Pronto`
- `Pode esperar`
- `Feito`
- `Risco`
- `Destrava`
- `Depende de`

Evitar:

- `Configuração avançada`
- `Pipeline operacional`
- `Payload`
- `Endpoint`
- `Módulo complexo`
- `Processo de estabilização`

## Tipografia e layout

| Elemento | Recomendação |
|---|---|
| Títulos | Grandes, curtos, com ícone. |
| Subtexto | Máximo 1 linha. |
| Descrições | Só em detalhe expandido. |
| Barras | Simples: `████░`. |
| Tabelas | Curtas, com no máximo 6 colunas visíveis. |
| Cards | Poucos e com função. |
| Linhas | Usar para estrutura, não decoração. |

## Cores sugeridas

| Estado | Cor mental | Uso |
|---|---|---|
| 🔥 Agora | forte/quente | foco máximo |
| ✅ Feito | verde discreto | progresso |
| 🟡 Em andamento | âmbar suave | atenção calma |
| 🔴 Bloqueado | vermelho/laranja | travado |
| 🔵 Pronto | azul/teal calmo | pode começar |
| ⚡ Paralelo | roxo/teal | energia lateral |
| ⚠️ Risco | âmbar/ink | cautela |

## Regra de scanning

A interface deve ser entendida nesta ordem:

```text
1. Ícone
2. Título
3. Estado
4. Progresso
5. Dependência
6. Detalhe opcional
```

## Perguntas que cada tela deve responder

- O que está acontecendo?
- O que preciso fazer?
- O que está impedindo?
- O que posso fazer sem pensar demais?
- O que já consegui?

## Legenda visual curta

| Símbolo | Significado | Uso no mapa |
|---|---|---|
| 🔥 | Fazer agora | Ação recomendada principal |
| ✅ | Feito | Já existe ou está validado |
| 🟡 | Em andamento / parcial | Existe, mas ainda precisa prova ou acabamento |
| 🔵 | Pronto para começar | Não está bloqueado |
| 🔴 | Bloqueado | Falta dependência anterior |
| ⚡ | Paralelo | Pode avançar sem travar o núcleo |
| 🧱 | Fundação | Sem isto o resto fica frágil |
| 🔓 | Desbloqueador | Ao concluir, abre outras frentes |
| 🎯 | Milestone | Marco de avanço visível |
| ⚠️ | Risco | Pode atrasar, quebrar ou confundir |
| ✨ | Melhoria | Ajuda, mas não bloqueia MVP |
| 👁️ | Verificação visual | Usar para revisar UI/UX |
| 🧪 | Validação | Teste, smoke, evidência ou checklist |
