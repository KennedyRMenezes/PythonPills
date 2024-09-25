
class User():

    def __init__(self, name, age, library_num):
        self.name = name
        self.age = age
        self.library_num = library_num

        self.list_of_borrowed = []
        self.list_old_consults = []


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