from numbers import Real
from typing import Optional, Union

class Atacante:
    def __init__(self, nome: str, idade: int, altura: float, peso: float):
        self._nome = nome
        self._idade = idade
        self._altura = altura
        self._peso = peso
        self._imc: Optional[float] = None
        self.calc_imc()

    @property
    def nome(self) -> str:
        return self._nome

    @property
    def idade(self) -> int:
        return self._idade

    @property
    def altura(self) -> float:
        return self._altura

    @altura.setter
    def altura(self, value: float) -> None:
        self._altura = value
        self.calc_imc()

    @property
    def peso(self) -> float:
        return self._peso

    @peso.setter
    def peso(self, value: float) -> None:
        self._peso = value
        self.calc_imc()

    def calc_imc(self) -> None:
        """Calcula o IMC com tratamento de erros"""
        try:
            if self._altura is None or self._peso is None:
                raise ValueError("Erro: defina peso e altura primeiro!")
            
            if self._altura <= 0:
                raise ValueError("Altura deve ser maior que zero!")
                
            self._imc = self._peso / (self._altura ** 2)
            
        except ValueError as e:
            print(f"Erro no cálculo do IMC: {e}")
            raise
        except Exception as e:
            print(f"Erro inesperado: {e}")
            raise

    def show_imc(self) -> None:
        """Exibe o IMC formatado"""
        if self._imc is not None:
            print(f"\nO IMC do {self._nome} é: {self._imc:.2f}")

    def __setattr__(self, name: str, value: Union[Real, str, list, tuple]) -> None:
        """Permite definir IMC com lista [peso, altura]"""
        if name == 'imc':
            if isinstance(value, (list, tuple)) and len(value) == 2:
                peso, altura = value
                if peso > altura:
                    super().__setattr__('_imc', peso / (altura ** 2))
                else:
                    print("Erro: o primeiro valor deve ser o peso.")
            else:
                print("Erro: esperado um array [peso, altura]")
        else:
            super().__setattr__(name, value)

    def __str__(self) -> str:
        """Representação em string formatada"""
        components = [
            f"\n===Dados do {self.__class__.__name__}===",
            f"\nNome: {self._nome}",
            f"\nIdade: {self._idade}" if self._idade else "",
            f"\nPeso: {self._peso}",
            f"\nAltura: {self._altura}",
            f"\nIMC: {self._imc:.3f}" if self._imc is not None else ""
        ]
        return "".join(components)

# Exemplo de uso
if __name__ == "__main__":
    try:
        jogador = Atacante("Ronaldo", 35, 1.83, 85)
        print(jogador)
        jogador.show_imc()
        
        # Testando setters
        jogador.altura = 1.85
        jogador.peso = 87
        print("\nApós atualização:")
        print(jogador)
        jogador.show_imc()
        
        # Testando atribuição direta de IMC
        jogador.imc = [90, 1.85]
        print("\nApós definir IMC diretamente:")
        print(jogador)
        
    except Exception as e:
        print(f"Erro crítico: {e}")