from enum import Enum

class Sexo(Enum):
    MASCULINO = "Masculino", "M"
    FEMININO = "Feminino", "F"

    def __init__(self, nome: str, sigla: str):
        
        self.nome = nome
        self.sigla = sigla