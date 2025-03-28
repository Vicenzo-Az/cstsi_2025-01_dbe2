class Pessoa:
    def __init__(self, nome: str, idade: int, peso: float = 0, altura: float = 0):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura
        self._imc = 0.0  # Atributo "privado" (convenção Python)
        print(f"\nObjeto {self.nome} construído!!!")

    def __del__(self):
        print(f"\n{self.nome} foi destruído!!", end='')

    def calc_imc(self):
        if self.peso <= 0 or self.altura <= 0:
            print("\nErro: configurar peso e altura primeiro!!")
            self._imc = 0.0
            return
        self._imc = self.peso / (self.altura ** 2)

    @property
    def imc(self):
        return self._imc

    def __getattr__(self, name):
        """Equivalente ao __get do PHP, mas só para atributos não existentes"""
        if name == 'imc':
            return self._imc
        raise AttributeError(f"Atributo {name} não existe")

# Função para simular o var_dump do PHP
def var_dump(*objs):
    for obj in objs:
        print(f"\nObjeto {obj.__class__.__name__}:")
        for attr, value in vars(obj).items():
            print(f"  {attr}: {repr(value)} ({type(value).__name__})")

# Criação dos objetos
pessoa_um = Pessoa("Gill", 36)
pessoa_dois = Pessoa("Vera", 60, 89, 1.55)

# Cálculo do IMC
pessoa_um.calc_imc()    # Gerará erro pois altura e peso são 0
pessoa_dois.calc_imc()  # Cálculo correto

# Saída formatada
print(f"\nO IMC do {pessoa_dois.nome} é {pessoa_dois.imc:.2f}")
print(f"\nIMC do {pessoa_um.nome}: {pessoa_um.imc:.2f}")

var_dump(pessoa_um, pessoa_dois)