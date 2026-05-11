# TheOne Living Dashboard

Este repositório guarda a visão inicial, o mapa do projeto e os protótipos visuais do TheOne Living Dashboard.

O TheOne é pensado como um cockpit vivo para decisão semanal: mostra as 7 frentes gigantes da semana, destaca o estado central de AGORA / Broadway Signal, conversa com o operador através de chatbot e organiza a evolução numa timeline visual. A intenção não é criar um dashboard genérico de métricas, mas uma interface de decisão que ajude a perceber o que importa agora, o que está a avançar e qual deve ser o próximo movimento.

## Estado atual

Este repo ainda está em fase de mapa, documentação e protótipo visual.

Não há aqui uma app TheOne completa. Também não foi adicionada uma stack artificial só para parecer pronta. O conteúdo versionado nesta fase serve como base clara para o desenvolvimento local seguinte.

## Onde está a documentação

- `docs/project-map/` contém o mapa principal do projeto, visão, epics, dependências, riscos, roadmap e regras de execução.
- `docs/project-map/00-START-HERE.md` é o melhor ponto de entrada para ler a documentação.
- `docs/dashboard/` contém a documentação do cockpit visual e do dashboard conceptual.
- `docs/dashboard/week-01-living-cockpit-map.md` descreve o mapa visual da semana 01.

## Onde está o protótipo visual

Os protótipos HTML estão em:

- `prototypes/dashboard/theone-dashboard-visual-map.html`
- `prototypes/dashboard/theone-week-dashboard-visual-map.html`

Podem ser abertos diretamente no browser para rever a direção visual.

Os assets PNG/SVG do dashboard estão em:

- `docs/dashboard/assets/`

## Direção do produto

O TheOne Living Dashboard deve preservar estes princípios:

- 7 frentes gigantes da semana;
- zona central AGORA / Broadway Signal;
- chatbot que conversa com o dashboard;
- timeline inferior;
- estado visual vivo;
- futura camada visual tipo lava lamp;
- futuro avatar ou personagem;
- futura interface touchscreen;
- foco em decisão, não apenas métricas.

## Próximo passo recomendado

O próximo passo técnico recomendado é criar uma app local real, sem falsos módulos, com:

- frontend em Next.js;
- backend em FastAPI;
- Docker Compose para ambiente local;
- integração gradual a partir do mapa e dos protótipos já versionados.

Antes de construir, usar `docs/project-map/` e `docs/dashboard/` como fonte de intenção do produto.
