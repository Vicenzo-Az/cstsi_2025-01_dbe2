from numbers import Real
from typing import Optional, Union

class Atacante:
    def __init__(self, nome: str, idade: int, altura: float, peso: float):
        self.nome = nome
        self.idade = idade
        self.altura = altura
        self.peso = peso
        self._imc: Optional[float] = None
        self.calc_imc()

    def calc_imc(self) -> None:
        """Calcula o IMC com tratamento de erros"""
        try:
            if self.altura is not None and self.peso is not None:
                self._imc = self.peso / (self.altura ** 2)
            else:
                raise ValueError("Erro: defina peso e altura primeiro!")
        except Exception as error:
            print(f"Erro: {error}")
            raise

    def show_imc(self) -> None:
        """Exibe o IMC formatado"""
        if isinstance(self._imc, (int, float)):
            print(f"\nO IMC do {self.nome} é: {self._imc:.2f}")

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

    def __setattr__(self, name: str, value: Union[Real, str, list, tuple]) -> None:
        """Permite definir IMC com lista [peso, altura]"""
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
        """Representação em string formatada"""
        components = [
            f"\n===Dados do {self.__class__.__name__}===",
            f"\nNome: {self.nome}",
            f"\nIdade: {self.idade}" if self.idade else "",
            f"\nPeso: {self.peso}",
            f"\nAltura: {self.altura}",
            f"\nIMC: {self._imc:.3f}" if self._imc is not None else ""
        ]
        return "".join(components)