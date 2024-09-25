from Library import Library
from Media import *
from User import *

bma = Library(
    "Biblioteca Mário de Andrade",
    "Rua da Consolação, 94",
    "1925",
    "(11)31509453")

book1 = Book("Dom Casmurro",
             "Machado de Assis",
             "1899",
             400,
             "978-8582850350",
             "Penguin-Companhia")
book1.set_quantity(4)

book2 = Book("Angústia",
             "Graciliano Ramos",
             "1943",
             383,
             "978-8952850350",
             "Record")
book2.set_quantity(1)


bma.add_item(book1)
bma.add_item(book2)

bma.list_catalog()

user1 = User("Kennedy Menezes",
             26,
             6598244)

bma.borrow_item(book2, user1)

print(user1.borrowed())
print(bma.borrowed())
print(book2.consults())

bma.return_item(book2, user1)

user2 = User("Joaquim", 34, 6598087)


print("\n\n")
bma.borrow_item(book2, user2)
bma.return_item(book2, user2)

user3 = User("Vivi", 31, 6598200)
bma.borrow_item(book2, user3)

print(book2.consults())