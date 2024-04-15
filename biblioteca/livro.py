class Livro:
    def __init__(self, titulo, autor, ano_publicacao):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_publicacao
        self.status = "Disponível"

    def verificar_disponibilidade(self):
        return self.status == "Disponível"

    def alterar_status(self, novo_status):
        self.status = novo_status
