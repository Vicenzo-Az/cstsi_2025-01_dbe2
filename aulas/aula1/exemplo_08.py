class Pessoa:
    def __init__(self, nome, idade, altura=None, peso=None):
        self.nome = nome
        self.idade = idade
        self.altura = altura
        self.peso = peso
        self._imc = 0.0  # Atributo protegido

    def get_imc(self):
        return self._imc

class IMC:
    @staticmethod
    def to_string():
        return "Classe para cálculos de Índice de Massa Corporal"
    
    @staticmethod
    def calc(pessoa):
        if pessoa.altura is None or pessoa.peso is None:
            raise ValueError("Altura e peso devem ser informados")
        if pessoa.altura <= 0 or pessoa.peso <= 0:
            raise ValueError("Altura e peso devem ser valores positivos")
        
        pessoa._imc = pessoa.peso / (pessoa.altura ** 2)
    
    @staticmethod
    def classifica(pessoa):
        IMC.calc(pessoa)  # Calcula primeiro o IMC
        
        print(f"\nClassificação IMC de {pessoa.nome}: ", end='')
        if pessoa._imc < 18.5:
            print("Magreza")
        elif 18.5 <= pessoa._imc < 25:
            print("Normal")
        elif 25 <= pessoa._imc < 30:
            print("Sobrepeso")
        elif 30 <= pessoa._imc < 40:
            print("Obesidade")
        else:
            print("Obesidade Grave")

if __name__ == "__main__":
    print(f"\nClasse estática: {IMC.to_string()}\n")
    
    pessoa = Pessoa("Lucia", 60, 1.55, 89)
    
    try:
        IMC.classifica(pessoa)
        print(f"IMC da {pessoa.nome} é {pessoa.get_imc():.2f}")
    except ValueError as e:
        print(f"\nErro: {str(e)}")