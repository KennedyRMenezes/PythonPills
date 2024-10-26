from datetime import datetime, timedelta
import random
from Media import *
from User import *

class Library():

    all_users = []

    def __init__(self, name: str, address: str, birth: str, phone_num: str):
        self.name = name
        self.address = address
        self.birth = birth
        self.phone_num = phone_num

        self.catalog = []
        self.list_of_borrowed = []

    def register_user(self, name, age):
        library_number =  random.randint(10**6, 10**7 - 1)
        user = User(name, age, library_number)
        self.all_users.append(user)

    def list_users(self):
        print(f"{'Name'.ljust(20)} | {'Library Number'.ljust(20)}\n")
        for user in self.all_users:
            print(f"{user.name.ljust(20)} | {str(user.library_num).ljust(20)}")

    def return_date(self, days):
        return_date=datetime.now()+timedelta(days=days)
        return return_date

    def borrow_item(self, item, user):

        if item.get_quantity() == 0:
            print("This item can't be borrow")
            return
        
        back_date = ""
        if isinstance(user, Professor):
            back_date = self.return_date(10)
        else:
            back_date = self.return_date(7)

        item.set_quantity(item.get_quantity() - 1)

        borrow = {"obj": item, "date": back_date}

        user.borrow(borrow)
        item.list_consultants(user)
        self.list_of_borrowed.append(borrow)

    def borrowed(self):
        result = ""
        print(f"Livros da {self.name} que estão atualmente emprestados: ")
        for item in self.list_of_borrowed:
            print(f"{item['obj'].title}")
        return result
        

    def return_item(self, item_to_remove, user):

        item_to_remove.set_quantity(item_to_remove.get_quantity() + 1)

        user.old_consults(item_to_remove)

        for item in self.list_of_borrowed:
            if item["obj"] == item_to_remove:
                self.list_of_borrowed.remove(item)


    def add_item(self, media):
        self.catalog.append(media)

    def return_catalog(self, obj):
        print("\n","="*30)
        print(f"Catalogo da {obj.name}\n")

        print(f"{'Item'.ljust(20)} | {'Autor'.ljust(20)} | {'Tipo'.ljust(10)} | {'Quantidade'.ljust(10)}\n")
        for item in obj.catalog:
            print(f"{item.title.ljust(20)} | {item.autor.ljust(20)} | {item.__class__.__name__.ljust(10)} | {str(item.get_quantity()).ljust(10)}")
        print("\n\n")

    def list_catalog(self, obj=None):
        
        if obj:
            self.return_catalog(obj)
        else:
            self.return_catalog(self)
