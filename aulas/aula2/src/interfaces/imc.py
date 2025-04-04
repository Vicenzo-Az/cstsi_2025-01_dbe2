from abc import ABC, abstractmethod

class IMC(ABC):
    """
    Interface para cálculo de IMC
    Padrão Python: Usamos ABC para interfaces com métodos abstratos
    """
    
    @abstractmethod
    def calc_imc(self) -> None:
        """Calcula o Índice de Massa Corporal"""
        pass
    
    @abstractmethod
    def show_imc(self) -> None:
        """Exibe o IMC formatado"""
        pass