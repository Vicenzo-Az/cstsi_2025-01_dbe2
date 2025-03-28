import sys

class Pessoa:
    def __init__(self, nome, idade, altura=0.0, peso=0):
        self.nome = nome
        self.idade = idade
        self.altura = altura
        self.peso = peso
        
    def __del__(self):
        print(f"\n{self.nome} foi destruído!!", end='')

# Criando instâncias
pessoa_um = Pessoa("Gill", 36)
pessoa_dois = Pessoa("Vera", 60, 1.55, 89)
pessoa_tres = Pessoa('Fulano', 24)

# Função para simular o var_dump
def var_dump(obj):
    print(f"Objeto {obj.__class__.__name__}:")
    for attr, value in vars(obj).items():
        print(f"  {attr}: {repr(value)} ({type(value).__name__})")

var_dump(pessoa_tres)
sys.exit()  # Equivalente ao die do PHP

# O código abaixo não será executado (equivalente ao PHP)
pessoa_tres = None
var_dump(pessoa_um, pessoa_dois)