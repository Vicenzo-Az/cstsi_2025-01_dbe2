
class Arbitro:
    def __init__(self, nome, idade, cargo, altura, peso):
        self.nome = nome
        self.idade = idade
        self.cargo = cargo
        self.altura = altura
        self.peso = peso
        self.calc_imc()

    def calc_imc(self):
        try:
            if (self.peso not 0) and (self.altura not 0):
                self.imc = self.peso / self.altura**2
        except:
            print('error')