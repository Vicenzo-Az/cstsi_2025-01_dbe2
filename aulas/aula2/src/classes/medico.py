from pessoa import Pessoa
from typing import Optional

class Medico(Pessoa):
    def __init__(self, 
                 nome: str, 
                 crm: str, 
                 especialidade: str, 
                 idade: Optional[int] = None, 
                 altura: float = 1.0, 
                 peso: float = 1.0):
        """
        Inicializa um médico com:
        - nome: Nome completo
        - crm: Número do CRM
        - especialidade: Área de atuação
        - idade: Opcional
        - altura: Padrão 1.0m
        - peso: Padrão 1.0kg
        """
        super().__init__(nome, idade, peso, altura)
        self._crm = crm
        self._especialidade = especialidade
        self.calc_imc()  # Calcula o IMC automaticamente

    @property
    def crm(self) -> str:
        """Número de registro no CRM"""
        return self._crm

    @property
    def especialidade(self) -> str:
        """Especialidade médica"""
        return self._especialidade

    def __str__(self) -> str:
        """Representação em string formatada"""
        components = [
            f"\n=== Dados de {self.__class__.__name__} ===",
            f"\nHerança: {Pessoa.__name__}",
            "\nAtributos:",
            f"\nIMC: {self.imc:.2f}" if self.imc else "\nIMC: Não calculado",
            f"\n\tNome: {self.nome}",
            f"\n\tIdade: {self.idade}" if self.idade else "",
            f"\n\tEspecialidade: {self.especialidade}",
            f"\n\tCRM: {self.crm}\n"
        ]
        return "".join(filter(None, components))