class Evento:
    def __init__(self, titulo, data, hora, local):
        self.titulo = titulo
        self.data = data
        self.hora = hora
        self.local = local

    def __str__(self):
        return f"Evento: {self.titulo}\nData: {self.data}\nHora: {self.hora}\nLocal: {self.local}\n"


class AgendaEventos:
    def __init__(self):
        self.eventos = []

    def adicionar_evento(self, evento):
        self.eventos.append(evento)

    def editar_evento(self, indice, evento):
        if 0 <= indice < len(self.eventos):
            self.eventos[indice] = evento
            print("Evento editado com sucesso.")
        else:
            print("Índice inválido. O evento não pôde ser editado.")

    def remover_evento(self, indice):
        if 0 <= indice < len(self.eventos):
            evento_removido = self.eventos.pop(indice)
            print(f"Evento '{evento_removido.titulo}' removido com sucesso.")
        else:
            print("Índice inválido. O evento não pôde ser removido.")

    def listar_eventos(self):
        print("Eventos cadastrados:")
        for indice, evento in enumerate(self.eventos):
            print(f"{indice + 1}. {evento}")


if __name__ == "__main__":
    
    agenda = AgendaEventos()

   
    evento1 = Evento("Reunião de equipe", "2024-04-10", "09:00", "Sala de reuniões")
    evento2 = Evento("Aniversário do CEO", "2024-05-15", "20:00", "Restaurante")
    evento3 = Evento("Apresentação do projeto", "2024-06-20", "14:30", "Auditório")
    agenda.adicionar_evento(evento1)
    agenda.adicionar_evento(evento2)
    agenda.adicionar_evento(evento3)

    agenda.listar_eventos()

    evento_editado = Evento("Apresentação do projeto atualizado", "2024-06-20", "14:30", "Auditório A")
    agenda.editar_evento(2, evento_editado)

    agenda.listar_eventos()

    agenda.remover_evento(1)

    agenda.listar_eventos()

# Ajuste