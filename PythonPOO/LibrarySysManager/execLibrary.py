from Library import Library


from Database import Database
db = Database()

def cadastraBiblioteca():

    while True:

        nome = input("Nome da Biblioteca: ")
        endereco = input("Endereço da Biblioteca: ")
        criacao = input("Insirada o ano de criação a Biblioteca: ")
        tel = input("Insira o telefone da Biblioteca: ")

        Library(nome, endereco, criacao, tel)

        sim_ou_nao = input("\nInserir nova Biblioteca? (S/N): ")
        print("\n")

        if sim_ou_nao == "S" or sim_ou_nao == "s":
            continue
        else:
            break

def cadastraLivro(id):

    #TODO: Receber ID da Biblioteca

    nome_biblio = Library.query_library(id)

    if nome_biblio:

        name = input("Insira o nome do livro: ")
        author = input("Insira o nome do autor do livro: ")
        pages = input("Insira a quantidade de páginas do livro: ")
        num_books = input("Insira a quantidade de livros a serem cadastrados: ")
        Library.register_book(id, name, author, pages, num_books)

        print("\n Livro inserido com sucesso!")

    else:
        print("ID inválido")


if __name__ == "__main__":

    while True:

        menu_string = """
            
            1 - Cadastrar Biblioteca
            2 - Cadastrar Livro
            3 - Cadastrar Usuário
            4* - Listar o histórico de livros emprestados a um usuário
            5* - Listar livros de uma biblioteca
            6* - Buscar livro
            x - Encerrar
            
            """

        command_menu = input(menu_string)
        

        if command_menu == "1":
            cadastraBiblioteca()
        elif command_menu == "2":
            lib_id = input("Insira o ID da Biblioteca: ")
            cadastraLivro(lib_id)
        elif command_menu == "x":
            break
        else:
            print("Insira uma opção válida")

        