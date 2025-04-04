class ToquesDeBolaMixin:
    """
    Mixin para habilidades de toques de bola
    Implementação Pythonica do trait ToquesDeBola
    """
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)  # Importante para herança múltipla
        self._esta_com_bola = False

    @property
    def esta_com_bola(self) -> bool:
        """Indica se o jogador está com posse de bola"""
        return self._esta_com_bola

    @esta_com_bola.setter
    def esta_com_bola(self, value: bool):
        """Define o estado de posse de bola"""
        self._esta_com_bola = value

    def um_dois_curto(self) -> str:
        """Executa um passe curto (disponível sempre)"""
        return "Realiza passe um dois curto."

    def lancamento(self) -> str:
        """Tenta um lançamento (requer posse de bola)"""
        return "Faz lançamento." if self._esta_com_bola else "Erro, jogador sem bola."

    def cruzamento(self) -> str:
        """Tenta um cruzamento (requer posse de bola)"""
        return "Faz um cruzamento." if self._esta_com_bola else "Erro, jogador sem bola."