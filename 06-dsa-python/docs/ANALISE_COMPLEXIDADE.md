# Análise de complexidade

Considere `n` como o número de registros; `m` como o tamanho do texto comparado.

| Operação | Implementação | Tempo | Espaço auxiliar |
|---|---|---:|---:|
| Inserir no fim | Percorre a lista para achar o último nó | O(n) | O(1), além do novo nó |
| Consultar por ID | Busca linear | O(n) | O(1) |
| Pesquisar título/categoria | Verifica cada registro e compara substrings | O(n × m) | O(k) para lista de resultados, sendo `k` o número encontrado |
| Atualizar | Busca linear e substituição dos campos do nó | O(n) | O(1) |
| Remover por ID | Busca linear e religação de referências | O(n) | O(1) |
| Percorrer/listar/contar | Visita cada nó | O(n) | O(1) para a iteração |
| Insertion Sort por título | Insere nós na lista já ordenada | O(n²) pior caso; O(n) melhor caso | O(1) |
| Resumo por categoria | Uma passagem com dicionário de contagem | O(n) médio | O(c), para `c` categorias |

A remoção é O(1) depois de localizar o nó, mas a operação completa inclui uma busca O(n). O Insertion Sort preserva os nós e não cria vetor auxiliar; sua complexidade quadrática é adequada ao catálogo pequeno do protótipo. Busca binária não foi usada, pois lista encadeada não oferece acesso aleatório eficiente.
