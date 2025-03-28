class Pessoa:
    def __init__(self, nome, idade, peso=None, altura=None):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura

pessoa1 = Pessoa("João", 34)
pessoa2 = Pessoa("Maria", 24, 60, 1.6)

print(pessoa1.__dict__)  # Saída: {'nome': 'João', 'idade': 34, 'peso': None, 'altura': None}