from typing import Optional, Union
from numbers import Real

class Pessoa:
    def __init__(self, 
                 nome: str, 
                 idade: Optional[int], 
                 peso: Optional[float] = None, 
                 altura: Optional[float] = None):
        """Inicializa uma pessoa com os dados básicos"""
        # Atribuição direta para evitar recursão
        object.__setattr__(self, '_nome', nome)
        object.__setattr__(self, '_idade', idade)
        object.__setattr__(self, '_peso', peso)
        object.__setattr__(self, '_altura', altura)
        object.__setattr__(self, '_imc', None)

    @property
    def nome(self) -> str:
        return self._nome

    @nome.setter
    def nome(self, value: str) -> None:
        print(f"\nAlterando nome de {self._nome} para {value}...")
        self._nome = value

    @property
    def idade(self) -> Optional[int]:
        return self._idade

    @idade.setter
    def idade(self, value: Optional[int]) -> None:
        print(f"\nAlterando idade de {self._nome}...")
        self._idade = value

    @property
    def peso(self) -> Optional[float]:
        return self._peso

    @peso.setter
    def peso(self, value: Optional[float]) -> None:
        print(f"\nAlterando peso de {self._nome}...")
        self._peso = value
        self._imc = None  # Reseta o IMC quando o peso muda

    @property
    def altura(self) -> Optional[float]:
        return self._altura

    @altura.setter
    def altura(self, value: Optional[float]) -> None:
        print(f"\nAlterando altura de {self._nome}...")
        self._altura = value
        self._imc = None  # Reseta o IMC quando a altura muda

    @property
    def imc(self) -> Optional[float]:
        return self._imc

    def __del__(self):
        print(f"\n{self._nome} foi destruído!!!")

    def calc_imc(self) -> None:
        """Calcula o IMC se peso e altura estiverem definidos"""
        if self._peso is not None and self._altura is not None:
            self._imc = self._peso / (self._altura ** 2)
        else:
            print("Erro: defina peso e altura primeiro!")

    def show_imc(self) -> None:
        """Mostra o IMC formatado"""
        msg = f"\nIMC {self._nome}: "
        msg += f"{self._imc:.2f}" if self._imc is not None else "Erro: calcule o IMC primeiro"
        print(msg)

    def __str__(self) -> str:
        """Representação em string formatada"""
        components = [
            "\n===Dados da Pessoa===",
            f"\nNome: {self._nome}",
            f"\nIdade: {self._idade}" if self._idade is not None else "",
            f"\nPeso: {self._peso}" if self._peso is not None else "",
            f"\nAltura: {self._altura}" if self._altura is not None else "",
            f"\nIMC: {self._imc:.2f}" if self._imc is not None else ""
        ]
        return "".join(filter(None, components))