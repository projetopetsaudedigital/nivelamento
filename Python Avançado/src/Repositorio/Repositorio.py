class Repositorio:
    def __init__(self):
        self._clientes = {}
    
    def getTodosOsClientes(self):
        return list(self._clientes.values())
    
    def getClientePorId(self, id):
        return self._clientes.get(id)
    
    def gravarCliente(self, cliente):
        self._clientes[cliente.id] = cliente