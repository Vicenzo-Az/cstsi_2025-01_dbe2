class Pessoa:
    def __init__(self, nome, idade, altura=0.0, peso=0):
        self.nome = nome
        self.idade = idade
        self.altura = altura
        self.peso = peso
        self._imc = 0.0  # Atributo protegido
        print(f"\nObjeto {self.nome} construído!!!")

    def __del__(self):
        print(f"\n{self.nome} foi destruído!", end='')

    def calc_imc(self):
        # Verificação equivalente ao PHP (com a mesma lógica condicional)
        if not isinstance(self.altura, (int, float)) and not isinstance(self.peso, (int, float)):
            print(f"\nIMC {self.nome}: Erro, informe peso e altura corretamente.")
            return
        
        try:
            self._imc = self.peso / (self.altura ** 2)
            print(f"\nO IMC do {self.nome} é: {self._imc:.2f}")
        except TypeError:
            print("\nErro: valores inválidos para cálculo do IMC")
        except ZeroDivisionError:
            print("\nErro: altura não pode ser zero")

    @property
    def imc(self):
        return self._imc

class Funcionario(Pessoa):
    def __init__(self, nome, idade, altura=0.0, peso=0, salario=0):
        super().__init__(nome, idade, altura, peso)
        self._salario = salario  # Atributo protegido

    def ver_salario(self):
        print(f"\nSalario: {self._salario}")

class Professor(Funcionario):
    def __init__(self, nome, idade, altura=0.0, peso=0, salario=0, area='geral'):
        super().__init__(nome, idade, altura, peso, salario)
        self.area = area

    def area_atuacao(self):
        print(f"\nAtua na área: {self.area}")
        print(f"\nSeu imc é: {self._imc:.2f}")

def var_dump(*objs):
    print("\n====================VARDUMP DOS OBJETOS=============")
    for obj in objs:
        print(f"\nObjeto {obj.__class__.__name__}:")
        for attr, value in vars(obj).items():
            print(f"  {attr}: {repr(value)}")

# Criação dos objetos
pessoa_um = Pessoa("Joao", 35)
pessoa_dois = Pessoa("Lucia", 60, 1.55, 89)

pessoa_um.calc_imc()     # Gerará erro
pessoa_dois.calc_imc()   # Cálculo correto

pessoa_tres = Professor('Gill', 35, 1.55, 89, 5000)
pessoa_tres.calc_imc()    # Herdado de Pessoa
pessoa_tres.ver_salario() # Herdado de Funcionario
pessoa_tres.area_atuacao()# Específico de Professor

var_dump(pessoa_um, pessoa_dois, pessoa_tres)