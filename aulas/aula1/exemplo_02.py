class Pessoa:
    def __init__(self):
        self.nome = None
        self.idade = None
        self.altura = None
        self.peso = None

# Criando as instâncias
pessoa_um = Pessoa()
pessoa_um.nome = "Gill"
pessoa_um.idade = 34

pessoa_dois = Pessoa()
pessoa_dois.nome = "Vera"
pessoa_dois.idade = 60
pessoa_dois.altura = 1.55
pessoa_dois.peso = 89

print(vars(pessoa_um))
print(vars(pessoa_dois))

# Função equivalente ao var_dump do PHP

# def var_dump(*objs):
#     for obj in objs:
#         print(f"Objeto {obj.__class__.__name__}:")
#         for attr, value in vars(obj).items():
#             print(f"  {attr}: {repr(value)} ({type(value).__name__})")
#         print()

# var_dump(pessoa_um, pessoa_dois)