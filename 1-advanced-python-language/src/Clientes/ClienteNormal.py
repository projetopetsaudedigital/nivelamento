from Clientes.Cliente import Cliente

class ClienteNormal(Cliente):
    
    def __init__(self, nome):
        super().__init__(nome, "Normal")