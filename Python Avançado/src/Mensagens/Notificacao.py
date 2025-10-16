class Notificacao:
    def __init__(self, mensagem):
        self.mensagem = mensagem
    
    def notificar(self, texto):
        self.mensagem.enviar_mensagem(texto)