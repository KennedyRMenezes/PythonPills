from notificacao.notificacao import Notificacao

class NotificacaiSMS(Notificacao):

    def enviar_notificacao(self, cliente, mensagem):
        print(f"Enviando SMS para {cliente.nome}: {mensagem}")