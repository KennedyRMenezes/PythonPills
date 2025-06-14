from abc import ABC, abstractclassmethod

# Design Pattern: Template Method
class Pedido(ABC):

    def __init__(self, cliente, itens):
        self.cliente = cliente
        self.itens = itens
        self.status = "Criado!"
        

    @abstractclassmethod
    def calcular_total(self):
        pass