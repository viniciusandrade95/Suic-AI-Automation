# 08 — Direção visual do frontend

## Direção atual

```text
Apple-grade Plainline Editorial Cockpit
```

## O que isto significa

Interface:

- limpa;
- premium;
- precisa;
- flat, mas com presença;
- baixa carga cognitiva;
- sem cara de admin template genérico;
- com linhas, proporção e hierarquia fortes.

## Não fazer

- sombras pesadas;
- glow;
- glassmorphism;
- gradientes decorativos fortes;
- branco clínico dominante;
- azul SaaS genérico;
- cards flutuantes demais;
- ícones em bolhas decorativas;
- dashboard cheio de texto;
- duas ações primárias competindo.

## Fazer

- módulos estruturados por linhas;
- fundo bone/ivory quando apropriado;
- ink/graphite para autoridade;
- teal oxidado como acento controlado;
- botões flat e decididos;
- ícones monoline funcionais;
- labels curtas;
- hierarquia forte;
- área `AGORA` com destaque real;
- detalhes sob demanda.

## Paleta mental sugerida

| Token mental | Cor aproximada | Papel |
|---|---|---|
| Ink | `#111820` | autoridade, sidebar, texto forte |
| Graphite | `#1D252C` | superfícies escuras |
| Bone | `#F3F0E8` | fundo premium quente |
| Canvas | `#EDEAE1` | superfície geral |
| Line | `rgba(17,24,32,.14)` | divisores suaves |
| Line strong | `rgba(17,24,32,.28)` | linhas importantes |
| Muted teal | `#4FBDB5` | acento calmo |
| Deep teal | `#1F6F6A` | acento de autoridade |
| Sand | `#C6B896` | detalhe quente |

## Sidebar

Deve parecer peça de identidade, não menu genérico.

Regras:

- fundo ink ou graphite;
- sem gradiente decorativo;
- active state com linha/bracket;
- ícones finos e consistentes;
- menos “button pills” genéricos;
- labels curtas.

## Topbar

Regras:

- limpa;
- sólida;
- border-bottom clara;
- conta/user pill discreto;
- sem bolha visual pesada;
- sem ruído.

## Cards vs módulos

Evitar sensação de muitos cards soltos.

Preferir:

```text
módulos estruturados
frames
sections
linhas internas
slots medidos
```

## Métricas

Boas métricas:

```text
Hoje
12
marcações
```

Más métricas:

```text
Texto explicando em três linhas o que este número quer dizer e por que ele pode variar dependendo da operação...
```

## Botões

| Tipo | Visual |
|---|---|
| Primário | fundo ink, texto bone, flat, decidido |
| Secundário | outline limpo, texto ink |
| Ghost | texto + seta, sem caixa pesada |
| Destrutivo | separado, nunca dominante por defeito |

## Ícones

- monoline;
- stroke consistente;
- funcionais;
- não decorativos;
- não usar container preenchido sem necessidade.

## Regra AuDHD-friendly

Visual premium não pode virar ruído.

Premium aqui significa:

```text
menos distração
mais decisão
mais alinhamento
mais clareza
mais presença
menos ornamento
```

## Checklist visual por tela

- Existe uma ação principal clara?
- O bloco mais importante é visualmente dominante?
- O utilizador entende sem ler parágrafo?
- Há símbolos consistentes?
- O estado vazio orienta o próximo passo?
- Mobile continua curto?
- A tela evita admin-template look?
- Não há efeitos baratos substituindo hierarquia?
