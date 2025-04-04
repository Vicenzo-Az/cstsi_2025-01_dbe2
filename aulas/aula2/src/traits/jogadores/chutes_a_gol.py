class ChutesAGolMixin:
    """Mixin que adiciona habilidades de chute ao gol
    Implementação Pythonica de trait com estado e métodos condicionais
    """
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)  # Importante para herança múltipla
        self.esta_com_bola = False  # Estado inicial

    def trivela(self) -> str:
        """Executa um chute de trivela se estiver com a bola"""
        return "Chuta de trivela." if self.esta_com_bola else ""

    def cavadinha(self) -> str:
        """Executa uma cavadinha se estiver com a bola"""
        return "Chuta de cavadinha." if self.esta_com_bola else ""

    def efeito_curva(self) -> str:
        """Executa um chute com efeito se estiver com a bola"""
        return "Chuta com efeito." if self.esta_com_bola else ""