from Library import Library
from Media import *
from User import *


print("\n# ============ CADASTRANDO BIBLIOTECAS ============  #\n")

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

biMonteiroLobato = Library(
    "Biblioteca Monteiro Lobato",
    "Rua Gen. Jardim, 485",
    "1995",
    "(11) 3256-4122")

print("\n# CADASTRANDO LIVRO MARIO ============  #\n")

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
l2bma.set_quantity(3)


biMarioAndrade.add_item(l1bma)
biMarioAndrade.add_item(l2bma)

print("\n# CADASTRANDO LIVRO BSP ============  #\n")

l1bsp = Book("Dom Casmurro",
             "Machado de Assis",
             "1899",
             400,
             "978-8582850350",
             "Penguin-Companhia")
l1bsp.set_quantity(4)

l2bsp = Book("Angústia",
             "Graciliano Ramos",
             "1943",
             383,
             "978-8952850350",
             "Record")
l2bsp.set_quantity(1)


biSaoPaulo.add_item(l1bsp)
biSaoPaulo.add_item(l2bsp)

print("\n# ============ LISTA CATALOG BIBLIOTECAS ============  #\n")

biMarioAndrade.list_catalog()
biSaoPaulo.list_catalog()
biMonteiroLobato.list_catalog()

print("\n# ============ CADASTRANDO USUARIO ============  #\n")

biMarioAndrade.register_user("Kennedy Menezes", 26)

biSaoPaulo.register_user("Joaquim", 34)

biMonteiroLobato.register_user("Vivi", 31)

print("\n# ============ BSP vê BMA ============  #\n")

biSaoPaulo.list_catalog(biMarioAndrade)

print("\n# ============ BSP lista todos os usuarios ============  #\n")

biSaoPaulo.list_users()

print("\n# ============ BMA lista todos os usuarios ============  #\n")

biMarioAndrade.list_users()