class DriblesMixin:
    """
    Mixin que adiciona habilidades de drible
    Implementação Pythonica do trait Dribles com métodos condicionais
    """
    
    def __init__(self, *args, **kwargs):
        """Inicializa o estado do mixin"""
        super().__init__(*args, **kwargs)  # Importante para herança múltipla
        self._esta_com_bola = False  # Estado protegido

    @property
    def esta_com_bola(self) -> bool:
        """Indica se o jogador está com a bola (getter)"""
        return self._esta_com_bola

    @esta_com_bola.setter
    def esta_com_bola(self, value: bool):
        """Define se o jogador está com a bola (setter)"""
        self._esta_com_bola = value

    def elastico(self) -> str:
        """Executa o drible elástico (não requer posse de bola)"""
        return "Realiza elástico no adversário."

    def rolinho(self) -> str:
        """Executa o drible rolinho se estiver com a bola"""
        return "Faz o rolinho com a bola." if self._esta_com_bola else ""

    def pedala(self) -> str:
        """Executa a pedalada se estiver com a bola"""
        return "Faz a pedalada." if self._esta_com_bola else ""