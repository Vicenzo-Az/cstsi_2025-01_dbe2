from src.traits.imc import IMCTrait

class Atleta(IMCTrait):
    def __init__(self, nome: str, idade: int, altura: float, peso: float):
        self._nome = nome
        self._idade = idade
        self._altura = altura
        self._peso = peso
        self.calc_imc()

    @property
    def nome(self) -> str:
        return self._nome

    @property
    def idade(self) -> int:
        return self._idade

    @property
    def altura(self) -> float:
        return self._altura

    @property
    def peso(self) -> float:
        return self._peso

    def __str__(self):
        return (
            f"Atleta: {self.nome}\n"
            f"Idade: {self.idade}\n"
            f"Altura: {self.altura}m\n"
            f"Peso: {self.peso}kg\n"
            f"IMC: {self.imc:.2f}"
        )