import os

class Quartos:
    lista_de_quartos = []

    def __init__(self, andar, numero):
        self._andar = andar.title()
        self._numero = numero
        self._disponivel = True
        Quartos.lista_de_quartos.append(self)

    def __str__(self):
        return f"{str(self._numero).ljust(25)} |{self._andar.ljust(25)} |{str(self.disponivel).ljust(25)}"

    @property
    def disponivel(self):
        # Exibe disponibilidade com cores no terminal
        return "\033[32mDisponível\033[m" if self._disponivel else "\033[31mIndisponível\033[m"

    def mudando_disponibilidade(self):
        self._disponivel = not self._disponivel

    @classmethod
    def listar_quartos_disponiveis(cls):
        os.system("clear")
        print(f"{'Quarto'.ljust(25)} |{'Andar'.ljust(25)} |{'Disponibilidade'.ljust(25)}")
        for quarto in cls.lista_de_quartos:
            if quarto._disponivel:
                print(quarto)
        print("")

# Instanciação de quartos
quarto101 = Quartos("primeiro andar", 101)
quarto102 = Quartos("primeiro andar", 102)
Quartos.listar_quartos_disponiveis()