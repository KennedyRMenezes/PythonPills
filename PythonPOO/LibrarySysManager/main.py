from Library import Library
from Media import *
from User import *

# ============ CADASTRANDO BIBLIOTECAS ============  #

biMarioAndrade = Library(
    "Biblioteca Mário de Andrade",
    "Rua da Consolação, 94",
    "1925",
    "(11) 3150-9453")

biSaoPaulo = Library(
    "Biblioteca de São Paulo",
    "Av. Cruzeiro do Sul, 2630",
    "1975",
    "(11) 2089-0800")

biSaoPaulo = Library(
    "Biblioteca Monteiro Lobato",
    "Rua Gen. Jardim, 485",
    "1995",
    "(11) 3256-4122")


# CADASTRANDO LIBRO MARIO ============  #

l1bma = Book("Dom Casmurro",
             "Machado de Assis",
             "1899",
             400,
             "978-8582850350",
             "Penguin-Companhia")
l1bma.set_quantity(4)

l2bma = Book("Angústia",
             "Graciliano Ramos",
             "1943",
             383,
             "978-8952850350",
             "Record")
l2bma.set_quantity(1)


biMarioAndrade.add_item(l1bma)
biMarioAndrade.add_item(l2bma)

# CADASTRANDO LIBRO BSP ============  #

l1bma = Book("Dom Casmurro",
             "Machado de Assis",
             "1899",
             400,
             "978-8582850350",
             "Penguin-Companhia")
l1bma.set_quantity(10)

l2bma = Book("Angústia",
             "Graciliano Ramos",
             "1943",
             383,
             "978-8952850350",
             "Record")
l2bma.set_quantity(1)


biMarioAndrade.add_item(l1bma)
biMarioAndrade.add_item(l2bma)


biMarioAndrade.list_catalog()

user1 = User("Kennedy Menezes",
             26,
             6598244)

biMarioAndrade.borrow_item(l2bma, user1)

print(user1.borrowed())
print(biMarioAndrade.borrowed())
print(l2bma.consults())

biMarioAndrade.return_item(l2bma, user1)

user2 = User("Joaquim", 34, 6598087)


print("\n\n")
biMarioAndrade.borrow_item(l2bma, user2)
biMarioAndrade.return_item(l2bma, user2)

user3 = User("Vivi", 31, 6598200)
biMarioAndrade.borrow_item(l2bma, user3)

print(l2bma.consults())