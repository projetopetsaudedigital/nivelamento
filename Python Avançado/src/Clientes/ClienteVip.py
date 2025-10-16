from Clientes.Cliente import Cliente

class ClienteVip(Cliente):
    
    def __init__(self, nome):
        super().__init__(nome, "VIP")