from Clientes.ClienteNormal import ClienteNormal
from Clientes.ClienteVip import ClienteVip

class ClienteFactory:
    @staticmethod
    def criar_cliente(tipo, nome):
        if tipo == "normal":
            return ClienteNormal(nome)
        elif tipo == "vip":
            return ClienteVip(nome)
        else:
            raise ValueError("Tipo de cliente inválido")