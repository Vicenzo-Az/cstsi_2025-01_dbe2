# src/classes/logs/static_relatorio.py
from ..atleta import Atleta as AtletaData

class StaticRelatorio:
    @staticmethod
    def log(atleta: AtletaData) -> None:
        """Loga informações do atleta formatadas
        Args:
            atleta: Instância de Atleta para registro
        """
        print(f"\nLog:\n{atleta}")