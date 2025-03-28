class Pessoa:
    def __init__(self):
        self.nome = None
        self.idade = None
        self.altura = None
        self.peso = None

obj = Pessoa()
obj.nome = "Gill"
obj.idade = 34

print(obj.__dict__)  # Equivalente ao var_dump do PHP
print(vars(obj))  # Ou usando vars() para o mesmo resultado

# Se quiser uma saída mais detalhada (incluindo tipos), você pode usar este código:
# def var_dump(obj):
#     for attr, value in vars(obj).items():
#         print(f"{attr}: {value} ({type(value).__name__})")

# var_dump(obj)
