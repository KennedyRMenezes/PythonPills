from datetime import datetime, timedelta
import random
import csv
from Media import Book
from User import *
import mysql.connector as con
from Database import Database

class Library():

    all_users = []

    def __init__(self, name: str, address: str, birth: str, phone_num: str):
        self.name = name
        self.address = address
        self.birth = birth
        self.phone_num = phone_num

        self.catalog = []
        self.list_of_borrowed = []

        self.register_library()


    def register_library(self):
        
        query = "INSERT INTO Library (lib_id, lib_name, lib_address, lib_birth, lib_tel) VALUES (%s, %s, %s, %s, %s)"
        Database.make_query(query, self.name, self.address, self.birth, self.phone_num)

    def query_library(self, id):
        
        query = f"SELECT lib_name FROM Library WHERE lib_id = {id}"

        result = Database.make_query(query)

        return True if result else None
    
    def register_book(self, lib_id, name, author, pages, num):

        #TODO: Book.register_book(lib_id, name, author, pages, num)

        query = "INSERT INTO Book (lib_id, book_name, book_author, book_pages, book_qtd) VALUES (%s, %s, %s, %s, %s)"

        Database.make_query(query, lib_id, name, author, pages, num)

    def register_user(self, name, age):
        pass
