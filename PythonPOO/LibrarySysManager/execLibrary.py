from Library import Library
from User import User

def cadastra_biblioteca():

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

def cadastra_livro(id):

    id_biblio = Library.query_library(id)

    if id_biblio:

        name = input("Insira o nome do livro: ")
        author = input("Insira o nome do autor do livro: ")
        pages = input("Insira a quantidade de páginas do livro: ")
        num_books = input("Insira a quantidade de livros a serem cadastrados: ")
        Library.register_book(id, name, author, pages, num_books)

        print("\n Livro inserido com sucesso!")

    else:
        print("ID inválido")

def cadastra_usuario():

    name = input("Insira o nome do usuario: ")
    age = input("Insira a data de nascimento(aaaa-mm-dd): ")
    address = input("Insira o endereço: ")

    User(name, age, address)


def lista_livros(id):

    Library.list_books(id)

    back = input("Presione qualquer tecla para voltar ao menu ")

    return back

def request_id():

    lib_id = int(input("\nInsira o ID da Biblioteca: "))

    return lib_id


if __name__ == "__main__":

    while True:

        menu_string = """
            
            1 - Cadastrar Biblioteca
            2 - Cadastrar Livro
            3 - Cadastrar Usuário
            4* - Listar o histórico de livros emprestados a um usuário
            5 - Listar livros de uma biblioteca
            6* - Buscar livro
            x - Encerrar
            
            """

        command_menu = input(menu_string)

        if command_menu == "1":
            cadastra_biblioteca()
        elif command_menu == "2":
            cadastra_livro(request_id())
        elif command_menu == "3":
            cadastra_usuario()
        elif command_menu == "4":
            empresta_livro(request_id())
        elif command_menu == '5':
            lista_livros(request_id())
        elif command_menu == "x":
            break
        else:
            print("Insira uma opção válida")

        