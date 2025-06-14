from notificacao.notificacao_email import NotificacaiEmail
from notificacao.notificacao_sms import NotificacaiSMS

class NotificacaoFacade:

    def __init__(self):
        self.notificacoes = [NotificacaiEmail(), NotificacaiSMS()]

    def enviar_notificacoes(self, cliente, mensagem):
        for notificacao in self.notificacoes:
            notificacao.enviar_notificacao(cliente, mensagem)
            