from typing import Optional
from .jogador import Jogador
from ..traits.jogadores.chutes_a_gol import ChutesAGolMixin
from ..traits.jogadores.dribles import DriblesMixin

class JogadorAtacante(Jogador, ChutesAGolMixin, DriblesMixin):
    """Class representing an attacking soccer player.
    Combines player traits with specialized attacking skills.
    """
    
    def __init__(self, nome: str, idade: int, altura: float, peso: float):
        """
        Initialize an attacking player.
        
        Args:
            nome: Player's name
            idade: Player's age
            altura: Height in meters
            peso: Weight in kg
        """
        super().__init__(nome, idade, altura, peso)
        self._esta_com_bola = False  # Initialize trait state

    def __str__(self) -> str:
        """String representation of the attacking player"""
        saida = [
            f"Classe Parent: {super().__class__.__name__}",
            super().__str__(),
            f"\n===Atribuições do {self.__class__.__name__}"
        ]
        
        if self.esta_com_bola:
            saida.extend([
                "\n\nDribles:",
                f"\n{self.rolinho()}",
                f"\n{self.elastico()}",
                "\n\nChutes:",
                f"\n{self.cavadinha()}",
                f"\n{self.trivela()}"
            ])
        
        return "".join(saida)

    @property
    def esta_com_bola(self) -> bool:
        """Whether the player currently has the ball"""
        return self._esta_com_bola

    @esta_com_bola.setter
    def esta_com_bola(self, value: bool):
        """Set whether the player has the ball"""
        self._esta_com_bola = value