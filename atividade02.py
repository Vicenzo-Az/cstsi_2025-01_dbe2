from dataclasses import dataclass
from datetime import date
from typing import Protocol
import locale

# Configurar localização para formatação monetária
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

# --- Protocolos para definir interfaces ---
class Funcionario(Protocol):
    def mostrar_salario(self) -> str: ...
    def mostrar_tempo_contrato(self) -> str: ...

class IMCProtocol(Protocol):
    peso: float
    altura: float
    idade: int
    sexo: str

# --- Mixin para cálculo de IMC ---
class CalculadoraIMC(IMCProtocol):
    """Fornece funcionalidades de cálculo e classificação de IMC"""
    
    @property
    def imc(self) -> float:
        return self.peso / (self.altura ** 2)
    
    def classificar_imc(self) -> str:
        if self.sexo == 'F':
            # Faixas específicas para mulheres
            if (19 <= self.idade <= 24 and 19 <= self.imc <= 24) or \
               (25 <= self.idade <= 34 and 20 <= self.imc <= 25) or \
               (35 <= self.idade <= 44 and 21 <= self.imc <= 26) or \
               (45 <= self.idade <= 54 and 22 <= self.imc <= 27) or \
               (55 <= self.idade <= 64 and 23 <= self.imc <= 28) or \
               (self.idade >= 65 and 24 <= self.imc <= 29):
                return "Peso Normal"
        
        # Classificação geral
        if self.imc < 18.5:
            return "Abaixo do peso"
        elif 18.5 <= self.imc < 25:
            return "Saudável"
        elif 25 <= self.imc < 30:
            return "Sobregoso"
        return "Obesidade"
    
    def imc_normal(self) -> bool:
        return self.classificar_imc() in ("Peso Normal", "Saudável")

# --- Modelos de dados ---
@dataclass
class Pessoa:
    nome: str
    idade: int
    sexo: str

@dataclass
class Atleta(Pessoa, CalculadoraIMC):
    peso: float
    altura: float
    salario: float
    data_contrato: date

    def mostrar_salario(self) -> str:
        return f"Salário: {locale.currency(self.salario, grouping=True)}"
    
    def mostrar_tempo_contrato(self) -> str:
        anos = date.today().year - self.data_contrato.year
        return f"Contrato de {anos} anos."

@dataclass
class Medico(Pessoa):
    salario: float
    data_contrato: date

    def mostrar_salario(self) -> str:
        return f"Salário: {locale.currency(self.salario, grouping=True)}"
    
    def mostrar_tempo_contrato(self) -> str:
        anos = date.today().year - self.data_contrato.year
        return f"Contrato de {anos} anos."

# --- Sistema de relatórios ---
class Relatorio:
    def __init__(self):
        self._registros: list[Pessoa] = []
    
    def adicionar(self, pessoa: Pessoa) -> None:
        self._registros.append(pessoa)
    
    def gerar(self) -> None:
        for pessoa in self._registros:
            print(f"\n=== Relatório para {pessoa.nome} ===")
            
            # Verificação por duck typing
            if all(hasattr(pessoa, m) for m in ['mostrar_salario', 'mostrar_tempo_contrato']):
                print(pessoa.mostrar_salario())
                print(pessoa.mostrar_tempo_contrato())
            
            # Informações específicas para Atletas
            if isinstance(pessoa, Atleta):
                print(f"IMC: {pessoa.imc:.1f}")
                print(f"Classificação: {pessoa.classificar_imc()}")
                print(f"IMC Normal: {'Sim' if pessoa.imc_normal() else 'Não'}")

# --- Exemplo de uso ---
if __name__ == "__main__":
    # Criando instâncias
    atleta = Atleta(
        nome="Mariana Oliveira",
        idade=28,
        sexo='F',
        peso=65,
        altura=1.70,
        salario=20000.00,
        data_contrato=date(2020, 3, 15)
    )

    medico = Medico(
        nome="Dr. Ricardo",
        idade=45,
        sexo='M',
        salario=35000.00,
        data_contrato=date(2017, 6, 1)
    )

    # Processando relatórios
    relatorio = Relatorio()
    relatorio.adicionar(atleta)
    relatorio.adicionar(medico)
    relatorio.gerar()