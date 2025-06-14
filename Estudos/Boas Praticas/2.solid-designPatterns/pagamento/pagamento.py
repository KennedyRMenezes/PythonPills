from abc import ABC, abstractmethod

class Pagamento(ABC):

    # sem necessidade de um construtor

    @abstractmethod
    def processar(self, valor):
        pass