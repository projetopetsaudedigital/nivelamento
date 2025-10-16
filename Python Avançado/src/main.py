from Clientes.ClienteFactory import ClienteFactory
from Descontos.DescontoNormal import DescontoNormal
from Descontos.DescontoVip import DescontoVip
from Mensagens.Mensagem import Mensagem
from Mensagens.Notificacao import Notificacao
from Repositorio.Repositorio import Repositorio


repositorio = Repositorio()

mensagem = Mensagem()
notificador = Notificacao(mensagem)

clientes = [
    ClienteFactory.criar_cliente("normal", "Daisy"),
    ClienteFactory.criar_cliente("vip", "Adam"),
    ClienteFactory.criar_cliente("normal", "Tom")
]

for cliente in clientes:
    repositorio.gravarCliente(cliente)

for cliente in repositorio.getTodosOsClientes():
    if cliente.tipo == "VIP":
        estrategia = DescontoVip()
    else:
        estrategia = DescontoNormal()
    
    valor_original = 100
    valor_com_desconto = estrategia.calcular(valor_original)
    
    print(f"Cliente: {cliente.nome} | Tipo: {cliente.tipo} | Valor original: {valor_original} | Desconto: {valor_com_desconto}")
    notificador.notificar(f"Olá {cliente.nome}, seu valor de desconto é: {valor_com_desconto}")