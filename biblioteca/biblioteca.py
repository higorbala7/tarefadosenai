from livro import Livro

class Biblioteca:
    def __init__(self):
        self.livros = []

    def adicionar_livro(self, livro):
        self.livros.append(livro)

    def emprestar_livro(self, titulo):
        for livro in self.livros:
            if livro.titulo == titulo:
                if livro.verificar_disponibilidade():
                    livro.alterar_status("Emprestado")
                    print(f"O livro '{titulo}' foi emprestado.")
                else:
                    print(f"Desculpe, o livro '{titulo}' está emprestado no momento.")
                return
        print(f"O livro '{titulo}' não foi encontrado na biblioteca.")

    def devolver_livro(self, titulo):
        for livro in self.livros:
            if livro.titulo == titulo:
                livro.alterar_status("Disponível")
                print(f"O livro '{titulo}' foi devolvido com sucesso.")
                return
        print(f"O livro '{titulo}' não foi encontrado na biblioteca.")

    def exibir_livros_disponiveis(self):
        print("Livros disponíveis na biblioteca:")
        for livro in self.livros:
            if livro.verificar_disponibilidade():
                print(f"- {livro.titulo} por {livro.autor} ({livro.ano_publicacao})")
