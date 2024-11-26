from app.models.abstract.pessoa import Pessoa
from abc import ABC
from app.models.endereco import Endereco
from app.models.enums.sexo import Sexo
from app.models.enums.estado_civil import EstadoCivil

class Fisica(ABC, Pessoa):
    def __init__(self, dataDeNascimento: str, estadoCivil: EstadoCivil, sexoNome: Sexo, sexoSigla: Sexo, id: str, nome: str, telefone: str, email: str, endereco: Endereco):
        super().__init__(id, nome, telefone, email, endereco)

        self.dataDeNascimento = dataDeNascimento
        self.estadoCivil = estadoCivil
        self.sexoNome = sexoNome
        self.sexoSigla = sexoSigla