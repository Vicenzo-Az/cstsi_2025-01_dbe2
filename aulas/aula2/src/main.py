import sys
from pathlib import Path

# Configura caminhos
BASE_DIR = Path(__file__).parent.parent
sys.path.append(str(BASE_DIR))

# Imports após configurar o path
from src.classes.medico import Medico
from src.classes.atleta import Atleta
from src.classes.jogador import Jogador

def main():
    # Seu código existente
    med = Medico("Dr. Silva", "CRM/SP-123", "Cardiologia", 45, 1.75, 75)
    print(med)

if __name__ == "__main__":
    main()