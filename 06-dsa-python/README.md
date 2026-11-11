# Citizen Assist AI — Catálogo de serviços (DSA)

**Integrantes:** Ryan Luther Roque e João Guilherme Figueiredo — RM 572993 e 572697
**Turma:** 1CCR · **Linguagem:** Python

## Recorte

Catálogo de orientações ao cidadão sobre Tarifa Social de Energia, documentação e atendimento. É um protótipo acadêmico; não confirma benefícios nem substitui canais oficiais. Os cinco itens iniciais são exemplos de estrutura e devem ter conteúdo verificado em fontes oficiais antes de publicação.

## Requisitos demonstrados

- Lista simplesmente encadeada própria: classe `No` com registro e referência explícita ao próximo nó.
- Cadastro, consulta por ID, pesquisa por título/categoria, atualização, exclusão e listagem.
- Insertion Sort implementado por relink dos nós para ordenar títulos.
- CSV com ID único, validação de campos, persistência, indicadores por categoria e menu no terminal.

## Executar

Requer Python 3.10 ou superior. A partir desta pasta:

```sh
python main.py
```

Os dados são lidos e gravados em `dados/servicos.csv`. A interface é terminal e não requer bibliotecas externas.

## Testes

```sh
python -m unittest discover -s testes -v
```

Veja `docs/DOCUMENTACAO_TECNICA.md`, `docs/ANALISE_COMPLEXIDADE.md`, `testes/PLANO_DE_TESTES.md` e o registro gerado em `testes/saida_testes.txt`.
