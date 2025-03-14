from Library import Library

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

def cadastraLivro():

    #TODO: Receber ID da Bibliotec
    #TODO: Inserir livro "dentro" da Biblioteca

    pass



if __name__ == "__main__":

    menu_string = """
        
        1 - Cadastrar Biblioteca
        2 - Cadastrar Livro
        
        """

    command_menu = input(menu_string)
    

    if command_menu == "1":
        cadastraBiblioteca()
    elif command_menu == "2":
        lib_id = input("Insira o ID da Biblioteca")
    else:
        print("Insira uma opção válida")

        