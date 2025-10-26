import unittest
from Clientes.ClienteFactory import ClienteFactory
from Repositorio.Repositorio import Repositorio
from Descontos.DescontoNormal import DescontoNormal
from Descontos.DescontoVip import DescontoVip

class TestClientes(unittest.TestCase):

    def setUp(self):
        self.repositorio = Repositorio()

    def test_factory_e_repositorio(self):
        c1 = ClienteFactory.criar_cliente("normal", "John")
        c2 = ClienteFactory.criar_cliente("vip", "Carrie")

        self.repositorio.gravarCliente(c1)
        self.repositorio.gravarCliente(c2)

        self.assertEqual(len(self.repositorio.getTodosOsClientes()), 2)
        self.assertEqual(self.repositorio.getClientePorId(c1.id).nome, "John")
        self.assertEqual(self.repositorio.getClientePorId(c2.id).tipo, "VIP")

    def test_strategy_desconto(self):
        normal = ClienteFactory.criar_cliente("normal", "João")
        vip = ClienteFactory.criar_cliente("vip", "Maria")

        valor = 100
        desconto_normal = DescontoNormal()
        desconto_vip = DescontoVip()

        self.assertEqual(desconto_normal.calcular(valor), 10)  
        self.assertEqual(desconto_vip.calcular(valor), 60)       

if __name__ == "__main__":
    unittest.main()
