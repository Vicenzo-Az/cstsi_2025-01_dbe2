from classes.jogador import Jogador

class JogadorDefesa(Jogador):
    def __str__(self):
        base = super().__str__()
        return base.replace("Jogador", "Jogador de Defesa")