
class User():

    def __init__(self, name, age, library_num):
        self.name = name
        self.age = age
        self.library_num = library_num

        self.list_of_borrowed = []
        self.list_old_consults = []

    def borrow(self, item):
        self.list_of_borrowed.append(item)

    def old_consults(self, item):
        self.list_of_borrowed.remove(item)
        self.list_old_consults.append(item)

    def borrowed(self):
        result = ""
        for item in self.list_of_borrowed:
            print(f"{item.title}")
        return result
