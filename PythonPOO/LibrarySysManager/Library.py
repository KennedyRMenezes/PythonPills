from Media import Book
from User import *
from Database import Database

class Library():

    db = Database()

    def __init__(self, name: str, address: str, birth: str, phone_num: str):
        self.name = name
        self.address = address
        self.birth = birth
        self.phone_num = phone_num

        self.catalog = []
        self.list_of_borrowed = []

        self.register_library()


    def register_library(self):
        
        query = "INSERT INTO Library (lib_name, lib_address, lib_birth, lib_tel) VALUES (%s, %s, %s, %s)"
        Library.db.make_query(query, self.name, self.address, self.birth, self.phone_num)

    @staticmethod
    def query_library(id):

        query = f"SELECT lib_name FROM Library WHERE lib_id = {id}"
        result = Library.db.make_query(query)
        return True if result else None
    
    @staticmethod
    def register_book(lib_id, name, author, pages, num):

        #TODO: Book.register_book(lib_id, name, author, pages, num)

        query = "INSERT INTO Book (lib_id, book_name, book_author, book_pages, book_qtd) VALUES (%s, %s, %s, %s, %s)"
        Library.db.make_query(query, lib_id, name, author, pages, num)

    def register_user(self, name, phone, address):
        pass

    @staticmethod
    def list_books(id):

        query = f"SELECT book_name, book_author, book_pages, book_qtd FROM book WHERE lib_id = {id}"
        _, books = Library.db.make_query(query)

        lj = 20

        print(f"\n{'Livro'.ljust(lj)}| {'Autor'.ljust(lj)}| {'Páginas'.ljust(lj)}| {'Quantidade'.ljust(lj)}")
        for i in books:
            print(f"{str(i[0]).ljust(lj)}| {str(i[1]).ljust(lj)}| {str(i[2]).ljust(lj)}| {str(i[3]).ljust(lj)}")
        print()
