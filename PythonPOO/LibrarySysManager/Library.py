
class Library():

    def __init__(self, name: str, address: str, birth: str, phone_num: str):
        self.name = name
        self.address = address
        self.birth = birth
        self.phone_num = phone_num

        self.catalog = []
        self.list_of_borrowed = []

    def borrow_item(self, item, user):

        if item.get_quantity() == 0:
            print("This item can't be borrow")
            return
        
        item.set_quantity(item.get_quantity() - 1)
        user.borrow(item)
        item.list_consultants(user)
        self.list_of_borrowed.append(item)

    def borrowed(self):
        result = ""
        for item in self.list_of_borrowed:
            print(f"{item.title}")
        return result
        

    def return_item(self, item, user):

        item.set_quantity(item.get_quantity() + 1)
        user.old_consults(item)
        self.list_of_borrowed.remove(item)


    def add_item(self, media):
        self.catalog.append(media)

    def list_catalog(self):
        print("\n","="*30)
        print(f"Catalogo da {self.name}\n")

        print(f"{'Item'.ljust(20)} | {'Autor'.ljust(20)} | {'Tipo'.ljust(10)}\n")
        for item in self.catalog:
            print(f"{item.title.ljust(20)} | {item.autor.ljust(20)} | {item.__class__.__name__.ljust(10)}")
        print("\n\n")
