from abc import ABC, abstractmethod
from typing import Optional

class Pessoa(ABC):
    """Abstract base class representing a person.
    Equivalent to PHP's abstract Pessoa class with additional Pythonic features.
    """
    
    def __init__(self, 
                 nome: str, 
                 idade: Optional[int], 
                 peso: Optional[float] = None, 
                 altura: Optional[float] = None):
        """Initialize person attributes"""
        self._nome = nome
        self._idade = idade
        self._peso = peso
        self._altura = altura

    @property
    def nome(self) -> str:
        """Person's name"""
        return self._nome

    @property
    def idade(self) -> Optional[int]:
        """Person's age"""
        return self._idade

    @property
    def peso(self) -> Optional[float]:
        """Person's weight"""
        return self._peso

    @property
    def altura(self) -> Optional[float]:
        """Person's height"""
        return self._altura

    @abstractmethod
    def __str__(self) -> str:
        """Abstract method for string representation (replaces __toString)"""
        pass

    def __del__(self):
        """Destructor (replaces __destruct)"""
        print(f"\n{self._nome} foi destruído!")

    def __getattr__(self, name: str):
        """Handle attribute access (similar to __get)"""
        if name in {'_nome', '_idade', '_peso', '_altura'}:
            return object.__getattribute__(self, name)
        raise AttributeError(f"'{self.__class__.__name__}' object has no attribute '{name}'")