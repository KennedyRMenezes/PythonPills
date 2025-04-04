class Media():

    def __init__(self, title: str, autor: str):

        self.title = title
        self.autor = autor
        self._quantity = 0

    # List of all users that consult the media
    def list_consultants(self, user):
        self.all_consultants.append(user)

    def set_quantity(self, qtt: int):
        self._quantity = qtt

    def get_quantity(self):
        return self._quantity
    
    def consults(self):
        result = ""
        print(f"Usuários que consultaram o livro {self.title}")
        for item in self.all_consultants:
            print(f"{item.name.ljust(20)} | {str(item.library_num).ljust(7)}")
        return result
    

class Book(Media):
    
    def __init__(self, 
                 title: str, 
                 autor: str, 
                 page_num: int):
        
        super().__init__(title, autor)
        self.page_nume = page_num
    
    def register_book(self, *args):
        pass

'''
class Revista(Media):

    def __init__(self, title: str, 
                 autor: str, publication_year: str, 
                 edition_num: int, periodicy: int, publisher: str):
        
        super().__init__(title, autor, publication_year)
        self.page_nume = edition_num
        self.isbn = periodicy
        self.publisher = publisher

class Jornal():
    pass

class Filme(Media):
    
    def __init__(self, title: str, 
                 autor: str, publication_year: str, duration: int, genre: str):
        super().__init__(title, autor, publication_year)
        super.duration = duration
        super.genre - genre
'''
