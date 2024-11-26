from enum import Enum

class EstadoCivil(Enum):
    CASADO = "Casado"
    SOLTEIRO = "Solteiro"
    VIUVO = "Viuvo"
    SEPARADO = "Separado"

    def __init__(self, nome: str):

        self.nome = nome