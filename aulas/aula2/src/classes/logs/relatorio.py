from typing import List
from abc import ABC
from src.classes.abstracts.pessoa import Pessoa  # Assuming abstract Pessoa class exists

class Relatorio:
    def __init__(self):
        self._pessoas: List[Pessoa] = []  # Type-hinted list of Pessoa objects

    def add(self, pessoa: Pessoa) -> None:
        """Adds a person to the report
        Args:
            pessoa: A Pessoa object or any of its subclasses
        """
        self._pessoas.append(pessoa)

    def log(self, pessoa: Pessoa) -> None:
        """Logs person's information
        Args:
            pessoa: A Pessoa object to be logged
        """
        print("\n\nlog:\n" + str(pessoa))  # Calls __str__ method

    def imprime(self) -> None:
        """Prints the complete report"""
        print("\n### RELATORIO ###")
        for pessoa in self._pessoas:
            self.log(pessoa)
        print("\n#############")

    # Pythonic alternative method names
    def print_report(self) -> None:
        """Alternative English name for imprime()"""
        self.imprime()