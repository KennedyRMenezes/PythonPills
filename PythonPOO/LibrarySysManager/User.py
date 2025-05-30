from Database import Database

class User():

    db = Database()

    def __init__(self, name, birth, address):
        self.name = name
        self.birth = birth
        self.address = address

        self.list_of_borrowed = []
        self.list_old_consults = []

        self.register_library()

    def register_library(self):
        
        query = "INSERT INTO User (user_name, user_birth, user_address) VALUES (%s, %s, %s)"
        User.db.make_query(query, self.name, self.birth, self.address)


    def borrow(self, item):
        self.list_of_borrowed.append(item)

    def old_consults(self, item_to_remove):

        for item in self.list_of_borrowed:
            if item["obj"] == item_to_remove:
                self.list_of_borrowed.remove(item)
                
        self.list_old_consults.append(item)

    def borrowed(self):
        result = ""
        print(f"\nLivros que {self.name} pegou emprestado:")
        for item in self.list_of_borrowed:
            print(f"{item['obj'].title}")
        return result

class Professor(User):

    def __init__(self):
        super().__init__()