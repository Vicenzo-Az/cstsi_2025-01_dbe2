class ZagueiroMixin:
    """
    Mixin para habilidades específicas de zagueiros
    Implementação Pythonica do trait Zagueiro com verificações de estado
    """
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)  # Compatível com herança múltipla
        self._esta_com_bola = False

    @property
    def esta_com_bola(self) -> bool:
        """Indica se o jogador está com a posse de bola"""
        return self._esta_com_bola

    @esta_com_bola.setter
    def esta_com_bola(self, value: bool):
        """Define o estado de posse de bola"""
        self._esta_com_bola = value

    def cerca_adversario(self) -> str:
        """
        Executa marcação no adversário
        Só funciona SEM a posse de bola
        """
        if not self._esta_com_bola:
            return "Cerca o adversário."
        return "Erro: jogador com bola."

    def lancamento_longo(self) -> str:
        """
        Executa lançamento longo
        Só funciona COM a posse de bola
        """
        if self._esta_com_bola:
            return "Faz lançamento longo."
        return "Erro: jogador sem bola."

    def carrinho(self) -> str:
        """
        Executa dividida (carrinho)
        Só funciona SEM a posse de bola
        """
        if not self._esta_com_bola:
            return "Realiza carrinho na bola."
        return "Erro: jogador com bola."