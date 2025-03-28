class Pessoa:
    def __init__(self, nome, idade, altura=0, peso=0):
        self.nome = nome
        self.idade = idade
        self.altura = altura
        self.peso = peso

# Criando instâncias
pessoa_um = Pessoa("Gill", 36)
pessoa_dois = Pessoa("Vera", 60, 1.55, 89)

print(pessoa_um.__dict__)  # {'nome': 'Gill', 'idade': 36, 'altura': 0, 'peso': 0}
print(pessoa_dois.__dict__) # {'nome': 'Vera', 'idade': 60, 'altura': 1.55, 'peso': 89}

# Função para simular o var_dump do PHP
# def var_dump(*objs):
#     for obj in objs:
#         print(f"Objeto {obj.__class__.__name__}:")
#         for attr, value in vars(obj).items():
#             print(f"  {attr}: {repr(value)} ({type(value).__name__})")
#         print()

# var_dump(pessoa_um, pessoa_dois)