class Cliente:
    
    _ultimo_id = 0 
    
    def __init__(self, nome, tipo):
        Cliente._ultimo_id += 1
        self.id = Cliente._ultimo_id
        self.nome = nome
        self.tipo = tipo