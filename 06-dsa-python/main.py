"""Catálogo Citizen Assist AI com lista encadeada própria."""
from __future__ import annotations

import csv
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, Optional


ARQUIVO_DADOS = Path(__file__).parent / "dados" / "servicos.csv"
CAMPOS = ("id", "categoria", "titulo", "descricao", "requisitos", "local")


@dataclass
class Servico:
    id: int
    categoria: str
    titulo: str
    descricao: str
    requisitos: str
    local: str


class No:
    """Nó explícito: guarda um registro e uma referência ao próximo nó."""
    def __init__(self, dado: Servico):
        self.dado = dado
        self.proximo: Optional[No] = None


class ListaServicos:
    def __init__(self) -> None:
        self.inicio: Optional[No] = None

    def __iter__(self) -> Iterable[Servico]:
        atual = self.inicio
        while atual is not None:
            yield atual.dado
            atual = atual.proximo

    def __len__(self) -> int:
        return sum(1 for _ in self)

    def buscar_id(self, id_servico: int) -> Optional[No]:
        atual = self.inicio
        while atual is not None:
            if atual.dado.id == id_servico:
                return atual
            atual = atual.proximo
        return None

    def inserir(self, servico: Servico) -> None:
        if servico.id <= 0:
            raise ValueError("O ID deve ser positivo.")
        if self.buscar_id(servico.id):
            raise ValueError("Esse ID já está cadastrado.")
        novo = No(servico)
        if self.inicio is None:
            self.inicio = novo
            return
        atual = self.inicio
        while atual.proximo is not None:
            atual = atual.proximo
        atual.proximo = novo

    def remover(self, id_servico: int) -> bool:
        anterior = None
        atual = self.inicio
        while atual is not None and atual.dado.id != id_servico:
            anterior, atual = atual, atual.proximo
        if atual is None:
            return False
        if anterior is None:
            self.inicio = atual.proximo
        else:
            anterior.proximo = atual.proximo
        return True

    def pesquisar(self, termo: str) -> list[Servico]:
        termo = termo.casefold().strip()
        return [s for s in self if termo in s.titulo.casefold() or termo in s.categoria.casefold()]

    def ordenar_por_titulo(self) -> None:
        """Insertion Sort relinkando nós, sem criar vetor auxiliar."""
        ordenada: Optional[No] = None
        atual = self.inicio
        while atual is not None:
            proximo = atual.proximo
            chave = atual.dado.titulo.casefold()
            if ordenada is None or chave < ordenada.dado.titulo.casefold():
                atual.proximo = ordenada
                ordenada = atual
            else:
                cursor = ordenada
                while (cursor.proximo is not None and
                       cursor.proximo.dado.titulo.casefold() <= chave):
                    cursor = cursor.proximo
                atual.proximo = cursor.proximo
                cursor.proximo = atual
            atual = proximo
        self.inicio = ordenada

    def resumo_categorias(self) -> dict[str, int]:
        resumo: dict[str, int] = {}
        for servico in self:
            resumo[servico.categoria] = resumo.get(servico.categoria, 0) + 1
        return resumo

    @classmethod
    def carregar_csv(cls, caminho: Path = ARQUIVO_DADOS) -> "ListaServicos":
        lista = cls()
        if not caminho.exists():
            return lista
        with caminho.open("r", encoding="utf-8-sig", newline="") as arquivo:
            leitor = csv.DictReader(arquivo, delimiter=";")
            if leitor.fieldnames != list(CAMPOS):
                raise ValueError("Cabeçalho inválido no CSV; esperado: " + ";".join(CAMPOS))
            for numero, linha in enumerate(leitor, start=2):
                try:
                    servico = Servico(
                        id=int(linha["id"]), categoria=linha["categoria"].strip(),
                        titulo=linha["titulo"].strip(), descricao=linha["descricao"].strip(),
                        requisitos=linha["requisitos"].strip(), local=linha["local"].strip(),
                    )
                    if any(not getattr(servico, campo).strip() for campo in CAMPOS[1:]):
                        raise ValueError("campos de texto vazios")
                    lista.inserir(servico)
                except (ValueError, TypeError, KeyError) as erro:
                    raise ValueError(f"Registro inválido na linha {numero}: {erro}") from erro
        return lista

    def salvar_csv(self, caminho: Path = ARQUIVO_DADOS) -> None:
        caminho.parent.mkdir(parents=True, exist_ok=True)
        with caminho.open("w", encoding="utf-8", newline="") as arquivo:
            escritor = csv.DictWriter(arquivo, fieldnames=CAMPOS, delimiter=";", lineterminator="\n")
            escritor.writeheader()
            for s in self:
                escritor.writerow({campo: getattr(s, campo) for campo in CAMPOS})


def ler_inteiro(mensagem: str, input_fn=input) -> int:
    texto = input_fn(mensagem).strip()
    if not texto or not texto.isdecimal() or int(texto) <= 0:
        raise ValueError("Digite um inteiro positivo válido.")
    return int(texto)


def ler_texto(mensagem: str, input_fn=input) -> str:
    texto = input_fn(mensagem).strip()
    if not texto:
        raise ValueError("O campo não pode ficar vazio.")
    return texto


def exibir(servico: Servico) -> None:
    print(f"\nID: {servico.id}\nCategoria: {servico.categoria}\nTítulo: {servico.titulo}"
          f"\nDescrição: {servico.descricao}\nRequisitos: {servico.requisitos}\nLocal/canal: {servico.local}")


def cadastrar(lista: ListaServicos) -> None:
    item = Servico(
        ler_inteiro("ID único: "), ler_texto("Categoria: "), ler_texto("Título: "),
        ler_texto("Descrição: "), ler_texto("Requisitos: "), ler_texto("Local/canal: "),
    )
    lista.inserir(item)
    lista.salvar_csv()
    print("Serviço cadastrado.")


def menu() -> None:
    print("\n=== CITIZEN ASSIST AI | CATÁLOGO DE SERVIÇOS ===")
    print("1 Cadastrar | 2 Consultar por ID | 3 Pesquisar título/categoria")
    print("4 Atualizar | 5 Excluir | 6 Listar | 7 Ordenar por título")
    print("8 Análise | 0 Salvar e sair")


def executar() -> None:
    lista = ListaServicos.carregar_csv()
    print(f"{len(lista)} serviço(s) carregado(s) de {ARQUIVO_DADOS.name}.")
    while True:
        menu()
        opcao = input("Opção: ").strip()
        try:
            if opcao == "0":
                lista.salvar_csv()
                print("Dados salvos. Até logo!")
                return
            if opcao == "1":
                cadastrar(lista)
            elif opcao == "2":
                if not len(lista): print("Lista vazia.")
                else:
                    no = lista.buscar_id(ler_inteiro("ID: "))
                    exibir(no.dado) if no else print("Nenhum serviço encontrado para esse ID.")
            elif opcao == "3":
                if not len(lista): print("Lista vazia.")
                else:
                    termo = ler_texto("Buscar por título ou categoria: ")
                    resultados = lista.pesquisar(termo)
                    for item in resultados: exibir(item)
                    if not resultados: print("Nenhum resultado para essa busca.")
            elif opcao == "4":
                if not len(lista): print("Lista vazia.")
                else:
                    id_servico = ler_inteiro("ID a atualizar: ")
                    no = lista.buscar_id(id_servico)
                    if no is None: print("ID inexistente.")
                    else:
                        no.dado = Servico(id_servico, ler_texto("Categoria: "), ler_texto("Título: "),
                            ler_texto("Descrição: "), ler_texto("Requisitos: "), ler_texto("Local/canal: "))
                        lista.salvar_csv(); print("Serviço atualizado.")
            elif opcao == "5":
                if not len(lista): print("Lista vazia.")
                else:
                    id_servico = ler_inteiro("ID a excluir: ")
                    if lista.remover(id_servico): lista.salvar_csv(); print("Serviço excluído.")
                    else: print("ID inexistente; nada foi excluído.")
            elif opcao == "6":
                if not len(lista): print("Lista vazia.")
                else:
                    for item in lista: exibir(item)
            elif opcao == "7":
                if not len(lista): print("Lista vazia.")
                else:
                    lista.ordenar_por_titulo(); lista.salvar_csv()
                    for item in lista: print(f"{item.id} - {item.titulo}")
            elif opcao == "8":
                print(f"Total de serviços: {len(lista)}")
                for categoria, quantidade in sorted(lista.resumo_categorias().items()):
                    print(f"- {categoria}: {quantidade}")
                if not len(lista): print("Não há categorias para resumir.")
            else:
                print("Opção inválida.")
        except (ValueError, OSError) as erro:
            print(f"Não foi possível concluir: {erro}")


if __name__ == "__main__":
    executar()
