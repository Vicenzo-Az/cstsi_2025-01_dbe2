# src/traits/imc.py
from abc import abstractmethod
from typing import Optional

class IMCTrait:
    """
    Trait para cálculo de IMC (Equivalente ao trait PHP)
    Implementado como mixin class em Python
    """
    
    @property
    @abstractmethod
    def peso(self) -> Optional[float]:
        """Propriedade abstrata para peso (deve ser implementada)"""
        pass
    
    @property
    @abstractmethod
    def altura(self) -> Optional[float]:
        """Propriedade abstrata para altura (deve ser implementada)"""
        pass
    
    @property
    @abstractmethod
    def nome(self) -> str:
        """Propriedade abstrata para nome (deve ser implementada)"""
        pass

    def __init__(self, *args, **kwargs):
        """Inicialização segura para mixins"""
        super().__init__(*args, **kwargs)
        self._imc: Optional[float] = None

    def calc_imc(self) -> None:
        """Calcula o IMC e armazena no atributo _imc"""
        if self.peso is not None and self.altura is not None:
            self._imc = self.peso / (self.altura ** 2)
        else:
            print("Erro: defina peso e altura primeiro!")

    def show_imc(self) -> None:
        """Exibe o IMC formatado"""
        msg = f"\nIMC {self.nome}: "
        if self._imc is not None:
            msg += f"{self._imc:.2f}"
        else:
            msg += "Erro, calcule o IMC primeiro"
        print(msg)

    @property
    def imc(self) -> Optional[float]:
        """Propriedade para acesso ao IMC calculado"""
        return self._imc