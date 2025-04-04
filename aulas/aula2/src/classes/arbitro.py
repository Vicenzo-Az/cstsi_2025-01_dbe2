from numbers import Real
from typing import Optional, Union
from abc import ABC, abstractmethod
from classes.abstracts.pessoa import Pessoa

class IMC(ABC):
    @abstractmethod
    def calc_imc(self) -> None:
        pass
    
    @abstractmethod
    def show_imc(self) -> None:
        pass

class Arbitro(Pessoa, IMC):
    def __init__(self, 
                 nome: str, 
                 idade: int, 
                 cargo: str, 
                 altura: float, 
                 peso: float):
        super().__init__(nome, idade)
        self.cargo = cargo
        self._altura = altura
        self._peso = peso
        self._imc: Optional[float] = None
        self.calc_imc()

    @property
    def altura(self) -> float:
        return self._altura

    @altura.setter
    def altura(self, value: float) -> None:
        self._altura = value
        self.calc_imc()

    @property
    def peso(self) -> float:
        return self._peso

    @peso.setter
    def peso(self, value: float) -> None:
        self._peso = value
        self.calc_imc()

    def calc_imc(self) -> None:
        try:
            if self._altura is not None and self._peso is not None:
                self._imc = self._peso / (self._altura ** 2)
            else:
                raise ValueError("Erro: defina peso e altura primeiro!")
        except ZeroDivisionError:
            raise ValueError("Altura não pode ser zero!")
        except Exception as error:
            print(f"Erro: {error}")
            raise

    def show_imc(self) -> None:
        if self._imc is not None:
            print(f"\nO IMC do {self.cargo} {self.nome} é: {self._imc:.1f}")

    def __setattr__(self, name: str, value: Union[Real, str, list, tuple]) -> None:
        if name == 'imc':
            if isinstance(value, (list, tuple)) and len(value) == 2:
                peso, altura = value
                if peso > altura:
                    super().__setattr__('_imc', peso / (altura ** 2))
                else:
                    print("Erro: o primeiro valor deve ser o peso.")
            else:
                print("Erro: esperado um array [peso, altura]")
        else:
            super().__setattr__(name, value)

    def __str__(self) -> str:
        components = [
            f"\n===Dados do {self.__class__.__name__}===",
            f"\nNome: {self.nome}",
            f"\nIdade: {self.idade}" if self.idade else "",
            f"\nCargo: {self.cargo}",
            f"\nPeso: {self.peso}",
            f"\nAltura: {self.altura}",
            f"\nIMC: {self._imc:.3f}" if self._imc is not None else ""
        ]
        return "".join(components)

if __name__ == "__main__":
    try:
        arb = Arbitro("Carlos Silva", 42, "Árbitro FIFA", 1.80, 75)
        print(arb)
        arb.show_imc()
        
        # Teste de atualização
        arb.altura = 1.82
        arb.peso = 77
        print("\nApós atualização:")
        print(arb)
        arb.show_imc()
        
    except Exception as e:
        print(f"Erro crítico: {e}")