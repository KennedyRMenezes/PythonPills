from notificacao.notificacao import Notificacao

class NotificacaiEmail(Notificacao):

    def enviar_notificacao(self, cliente, mensagem):
        print(f"Enviando email para {cliente.nome}: {mensagem}")