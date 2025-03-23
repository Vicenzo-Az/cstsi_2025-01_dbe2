# ● Implemente a classificação
# recomendada ao lado através de uma
# classe chamada IMC;

# ● A classe IMC deverá possuir os
# seguintes métodos estáticos:

# ● calc: recebe um objeto do tipo
# Paciente e retorna o valor de seu
# imc.

# ● classifica: recebe um objeto do tipo
# Paciente e retornar sua classificação
# como string de acordo com as
# faixas de imc da imagem ao lado.

class Paciente:
    def __init__(self, sexo, idade, peso, altura):
        self.sexo = sexo
        self.idade = idade
        self.peso = peso
        self.altura = altura

class IMC:
    @staticmethod
    def calc(paciente):
        return paciente.peso / (paciente.altura ** 2)

    @staticmethod
    def classifica(paciente):
        imc = IMC.calc(paciente)
        if paciente.sexo == 'F':
            idade = paciente.idade
            range_peso_normal = None

            if 19 <= idade <= 24:
                range_peso_normal = (19, 24)
            elif 25 <= idade <= 34:
                range_peso_normal = (20, 25)
            elif 35 <= idade <= 44:
                range_peso_normal = (21, 26)
            elif 45 <= idade <= 54:
                range_peso_normal = (22, 27)
            elif 55 <= idade <= 64:
                range_peso_normal = (23, 28)
            elif idade >= 65:
                range_peso_normal = (24, 29)

            if range_peso_normal:
                imc_min, imc_max = range_peso_normal
                if imc_min <= imc <= imc_max:
                    return "Peso Normal"

            # Classificação geral se não estiver em Peso Normal
            if imc < 18.5:
                return "Abaixo do peso"
            elif 18.5 <= imc < 25.0:
                return "Saudável"
            elif 25.0 <= imc < 30.0:
                return "Sobregoso"
            else:
                return "Obesidade"
        else:  # Para homens
            if imc < 18.5:
                return "Abaixo do peso"
            elif 18.5 <= imc < 25.0:
                return "Saudável"
            elif 25.0 <= imc < 30.0:
                return "Sobregoso"
            else:
                return "Obesidade"


# Criação de um paciente (sexo, idade, peso, altura)
paciente1 = Paciente('F', 25, 65, 1.70)
paciente2 = Paciente('M', 40, 80, 1.75)

# Cálculo e classificação do IMC
print(f"IMC paciente 1: {IMC.calc(paciente1):.2f}")  # Saída: 22.49
print(f"Classificação: {IMC.classifica(paciente1)}")  # Saída: Peso Normal

print(f"\nIMC paciente 2: {IMC.calc(paciente2):.2f}")  # Saída: 26.12
print(f"Classificação: {IMC.classifica(paciente2)}")   # Saída: Sobregoso