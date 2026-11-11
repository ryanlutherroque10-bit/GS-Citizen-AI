# Documentação técnica

## Modelo dos dados

`Servico` é uma dataclass com ID inteiro único, categoria, título, descrição, requisitos e local/canal. Cada campo textual é obrigatório. O CSV utiliza cabeçalho e `;` como delimitador, com suporte a acentos por UTF-8.

## Lista encadeada

A classe `No` armazena um `Servico` e uma referência `proximo`. `ListaServicos.inicio` aponta para o primeiro nó. Inserção percorre até o fim. A busca por ID percorre os nós sequencialmente. Remoção religa o nó anterior ao seguinte; quando remove o primeiro elemento, atualiza `inicio`. Python gerencia a liberação da memória quando nós deixam de ser referenciados.

## Algoritmos

`buscar_id` faz busca linear. `pesquisar` procura uma substring no título ou categoria, sem diferenciar maiúsculas/minúsculas. `ordenar_por_titulo` implementa Insertion Sort na lista: retira cada nó e o insere na posição correta da lista já ordenada. Não usa `sort`, `sorted` ou outro algoritmo pronto para ordenar registros.

## Menu e persistência

O menu fornece cadastro, consulta por ID, pesquisa por atributo, atualização, exclusão, listagem, ordenação, análise e encerramento. Erros de formato, campos vazios, ID duplicado, consultas sem resultado e lista vazia são tratados com mensagens. O CSV é salvo após alterações e ao encerrar. Caminho usado: `dados/servicos.csv` dentro da pasta do projeto.

## Escopo e cuidados

Os registros fornecidos são exemplos fictícios e não devem ser interpretados como orientação oficial. Antes de apresentar conteúdo ao público, confirmar fatos e documentos em fontes oficiais e registrar os links e as datas de consulta. O protótipo não coleta dados pessoais.
