import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from main import ListaServicos, Servico


def item(id_, titulo, categoria="Atendimento"):
    return Servico(id_, categoria, titulo, "Descrição", "Requisito", "Canal oficial")


class TestListaServicos(unittest.TestCase):
    def setUp(self):
        self.lista = ListaServicos()
        for s in (item(3, "Tarifa Social", "Direitos"), item(1, "Atendimento CRAS"), item(2, "Conta de energia", "Energia")):
            self.lista.inserir(s)

    def test_insercao_e_busca_por_id(self):
        self.assertEqual(len(self.lista), 3)
        self.assertEqual(self.lista.buscar_id(1).dado.titulo, "Atendimento CRAS")
        self.assertIsNone(self.lista.buscar_id(99))

    def test_rejeita_id_duplicado_e_nao_positivo(self):
        with self.assertRaises(ValueError): self.lista.inserir(item(1, "Duplicado"))
        with self.assertRaises(ValueError): self.lista.inserir(item(0, "Zero"))
        self.assertEqual(len(self.lista), 3)

    def test_pesquisa_por_titulo_ou_categoria_sem_case(self):
        self.assertEqual([s.id for s in self.lista.pesquisar("ENERGIA")], [2])
        self.assertEqual([s.id for s in self.lista.pesquisar("direitos")], [3])
        self.assertEqual(self.lista.pesquisar("inexistente"), [])

    def test_insertion_sort_por_titulo(self):
        self.lista.ordenar_por_titulo()
        self.assertEqual([s.titulo for s in self.lista], ["Atendimento CRAS", "Conta de energia", "Tarifa Social"])
        self.assertEqual([s.id for s in self.lista], [1, 2, 3])

    def test_remocao_inicio_meio_fim_e_nao_encontrado(self):
        self.assertTrue(self.lista.remover(3))
        self.assertTrue(self.lista.remover(1))
        self.assertTrue(self.lista.remover(2))
        self.assertFalse(self.lista.remover(99))
        self.assertEqual(len(self.lista), 0)
        self.assertIsNone(self.lista.inicio)

    def test_csv_persistencia(self):
        import tempfile
        with tempfile.TemporaryDirectory() as temp:
            caminho = Path(temp) / "servicos.csv"
            self.lista.salvar_csv(caminho)
            recarregada = ListaServicos.carregar_csv(caminho)
            self.assertEqual([(s.id, s.titulo) for s in recarregada], [(3, "Tarifa Social"), (1, "Atendimento CRAS"), (2, "Conta de energia")])

    def test_lista_vazia(self):
        vazia = ListaServicos()
        self.assertEqual(len(vazia), 0)
        self.assertIsNone(vazia.buscar_id(1))
        self.assertEqual(vazia.pesquisar("x"), [])
        vazia.ordenar_por_titulo()
        self.assertFalse(vazia.remover(1))


if __name__ == "__main__":
    unittest.main()
