# Plano de testes e demonstração

Os testes automatizados cobrem inserção, busca por ID existente e inexistente, ID duplicado, ID não positivo, pesquisa por título/categoria, ordenação, remoção de início/meio/fim, remoção inexistente, persistência CSV e lista vazia.

| Caso verificado | Resultado observado |
|---|---|
| Base inicial | Passou: cinco registros carregados no teste de menu. |
| ID inexistente | Passou: aplicação informa que não encontrou o registro. |
| Entrada de menu inválida (`abc`) | Passou: informa opção inválida e continua no menu. |
| ID duplicado e ID zero | Passou nos testes automatizados; lista não é alterada. |
| Pesquisa por título/categoria e termo sem resultado | Passou nos testes automatizados. |
| Lista vazia | Passou nos testes automatizados de busca, ordenação e remoção. |
| Insertion Sort | Passou: ordem alfabética conferida no teste automatizado e na execução do menu. |
| CSV | Passou: salvar e recarregar preserva IDs e títulos. |
| Remoção do início, meio e fim | Passou: testes automatizados confirmam remoção e lista vazia. |

Os detalhes de execução estão em `saida_testes.txt` e `saida_menu.txt`. Reproduza com:

```sh
python -m unittest discover -s testes -v
```

## Roteiro da demonstração

1. Mostrar o modelo `Servico`, a classe `No` e a lista `ListaServicos`.
2. Executar a aplicação e apontar os itens carregados do CSV.
3. Consultar por ID, pesquisar por título/categoria e mostrar uma pesquisa sem resultado.
4. Cadastrar um item e tentar repetir o ID para demonstrar validação.
5. Atualizar um registro, ordenar por título e excluir um registro.
6. Encerrar, reabrir e confirmar que as alterações permaneceram no CSV.
7. Explicar busca linear, Insertion Sort e a tabela Big-O.

Os testes de menu automatizados já cobrem opção inválida, consulta de ID inexistente, ordenação e encerramento. A gravação em vídeo deve demonstrar também o cadastro, atualização e exclusão pela interface. Não incluir dados pessoais reais; os dados de exemplo são fictícios.
