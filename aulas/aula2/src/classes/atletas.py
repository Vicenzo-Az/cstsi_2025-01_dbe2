from numbers import Real
from typing import Optional, Union

class Atletas:
    def __init__(self, nome: str, idade: int, altura: float, peso: float):
        # Inicialização direta SEM usar properties
        self._nome = nome
        self._idade = idade
        self._altura = altura  # Atributo privado
        self._peso = peso      # Atributo privado
        self._imc: Optional[float] = None
        self._calcular_imc()  # Método privado para cálculo inicial

    def _calcular_imc(self) -> None:
        """Método interno para cálculo seguro do IMC"""
        try:
            if self._altura and self._peso:
                self._imc = self._peso / (self._altura ** 2)
            else:
                raise ValueError("Altura e peso devem ser definidos!")
        except ZeroDivisionError:
            raise ValueError("Altura não pode ser zero!")
        except TypeError:
            raise ValueError("Valores inválidos para altura/peso!")

    @property
    def altura(self) -> float:
        return self._altura

    @altura.setter
    def altura(self, value: float) -> None:
        self._altura = value
        self._calcular_imc()

    @property
    def peso(self) -> float:
        return self._peso

    @peso.setter
    def peso(self, value: float) -> None:
        self._peso = value
        self._calcular_imc()

    def calc_imc(self) -> None:
        """Calcula o IMC com tratamento de erros"""
        try:
            if self._altura is not None and self._peso is not None:
                self._imc = self._peso / (self._altura ** 2)
            else:
                raise ValueError("Erro: defina peso e altura primeiro!")
        except Exception as error:
            print(f"Erro: {error}")
            raise

    def show_imc(self) -> None:
        """Exibe o IMC formatado"""
        if self._imc is not None:
            print(f"\nO IMC do {self._nome} é: {self._imc:.2f}")

    def __str__(self) -> str:
        """Representação em string formatada"""
        components = [
            f"\n===Dados do {self.__class__.__name__}===",
            f"\nNome: {self._nome}",
            f"\nIdade: {self._idade}" if self._idade else "",
            f"\nPeso: {self._peso}",
            f"\nAltura: {self._altura}",
            f"\nIMC: {self._imc:.3f}" if self._imc is not None else ""
        ]
        return "".join(components)