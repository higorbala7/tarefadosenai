from biblioteca import Biblioteca

def exibir_menu():
    print("\nMenu:")
    print("1. Adicionar um livro")
    print("2. Emprestar um livro")
    print("3. Devolver um livro")
    print("4. Exibir todos os livros disponíveis")
    print("5. Sair")

def main():
    biblioteca = Biblioteca()

    while True:
        exibir_menu()
        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            titulo = input("Digite o título do livro: ")
            autor = input("Digite o nome do autor do livro: ")
            ano = input("Digite o ano de publicação do livro: ")
            livro = Livro(titulo, autor, ano)
            biblioteca.adicionar_livro(livro)
            print(f"O livro '{titulo}' foi adicionado à biblioteca.")

        elif escolha == "2":
            titulo = input("Digite o título do livro que deseja emprestar: ")
            biblioteca.emprestar_livro(titulo)

        elif escolha == "3":
            titulo = input("Digite o título do livro que deseja devolver: ")
            biblioteca.devolver_livro(titulo)

        elif escolha == "4":
            biblioteca.exibir_livros_disponiveis()

        elif escolha == "5":
            print("Saindo do programa...")
            break

        else:
            print("Opção inválida. Por favor, escolha novamente.")

if __name__ == "__main__":
    main()
