# src/examples/exemplo_05_traits.py
from src.traits.imc import IMCTrait

class Pessoa(IMCTrait):
    def __init__(self, nome: str, peso: float, altura: float):
        super().__init__()
        self._nome = nome
        self._peso = peso
        self._altura = altura

    @property
    def nome(self) -> str:
        return self._nome

    @property
    def peso(self) -> float:
        return self._peso

    @property
    def altura(self) -> float:
        return self._altura

def run_demo():
    """Demo function showing trait usage"""
    pessoa = Pessoa("Maria", 68.5, 1.65)
    pessoa.calc_imc()
    pessoa.show_imc()  # Output: IMC Maria: 25.16