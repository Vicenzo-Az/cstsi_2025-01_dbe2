# src/examples/exemplo_02_autoload_psr4.py
import sys
from pathlib import Path
from unidecode import unidecode  # pip install unidecode

# Configurar caminhos
BASE_DIR = Path(__file__).parents[2]
sys.path.append(str(BASE_DIR))

# Importar classes
from src.classes.atleta import Atleta
from src.classes.medico import Medico

def main():
    # Criar instâncias
    atl1 = Atleta("Pedro Geromel", 36, 1.83, 75)
    med1 = Medico("Paulo Paixão", "CRM-122343", "Fisioterapeuta")

    # Chamar métodos
    atl1.show_imc()
    med1.show_imc()

    # Usar utilitário externo
    print(f"\nutil: {unidecode(med1.nome)}")

if __name__ == "__main__":
    main()