# src/examples/exemplo_01_spl_autoload.py
import sys
from pathlib import Path

# Configura caminhos
BASE_DIR = Path(__file__).parent.parent.parent
sys.path.append(str(BASE_DIR))

from src.classes.atletas import Atletas
from src.classes.atacante import Atacante

def main():
    # Cria instâncias
    atl1 = Atletas("Luizito", 36, 1.8, 80)
    atl2 = Atacante("Luiz Soarez", 36, 1.8, 80)

    # Exibe IMCs
    atl1.show_imc()
    atl2.show_imc()

if __name__ == "__main__":
    main()