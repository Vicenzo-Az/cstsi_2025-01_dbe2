from typing import Optional
from src.classes.pessoa import Pessoa

class ToquesDeBolaMixin:
    def __init__(self):
        self._esta_com_bola = False

    @property
    def esta_com_bola(self) -> bool:
        return self._esta_com_bola
    
    @esta_com_bola.setter
    def esta_com_bola(self, value: bool):
        self._esta_com_bola = value

    def um_dois_curto(self) -> str:
        return 'Relizou um um-dois curto!'
    
    def lancamento(self) -> str:
        return 'Realizou um lançamento longo!'


class Jogador(Pessoa, ToquesDeBolaMixin):
    def __init__(self, 
                 nome: str, 
                 idade: int, 
                 altura: float, 
                 peso: float):
        super().__init__(nome, idade, peso, altura)
        ToquesDeBolaMixin.__init__(self)
        self.calc_imc()

    @Pessoa.altura.setter
    def altura(self, value: float):
        super(Jogador, type(self)).altura.fset(self, value)
        self.calc_imc()

    @Pessoa.peso.setter
    def peso(self, value: float):
        super(Jogador, type(self)).peso.fset(self, value)
        self.calc_imc()

    def __setattr__(self, name: str, value):
        if name == 'imc':
            if isinstance(value, list) and len(value) == 2:
                peso, altura = value
                if peso > altura:
                    self._imc = peso / (altura ** 2)
                else:
                    print("Erro: o primeiro item deve ser o peso.")
            else:
                print("Erro: esperado um array [peso, altura]")
        else:
            super().__setattr__(name, value)

    def __str__(self) -> str:
        saida = [
            f"Classe Parent: {Pessoa.__name__}",
            f"\n===Dados do {self.__class__.__name__}===",
            f"\nNome: {self.nome}",
            f"\nIdade: {self.idade}" if self.idade else "",
            f"\nPeso: {self.peso}",
            f"\nAltura: {self.altura}",
            f"\nIMC: {self.imc:.3f}" if self.imc else ""
        ]

        if self.esta_com_bola:
            saida.extend([
                "\n\nPasses:",
                f"\n{self.um_dois_curto()}",
                f"\n{self.lancamento()}"
            ])

        return "".join(saida)