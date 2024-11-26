from app.models.abstract.fisica import Fisica
from abc import ABC
from app.models.endereco import Endereco
from app.models.enums.sexo import Sexo
from app.models.enums.setor import Setor

class Funcionario(ABC, Fisica):
    def __init__(self, cpf: str, rg: str, matricula: str, setor: Setor, salario: float, dataDeNascimento: str, estadoCivil: str, sexoNome: Sexo, sexoSigla: Sexo, id: str, nome: str, telefone: str, email: str, endereco: Endereco):
        super().__init__(dataDeNascimento, estadoCivil, sexoNome, sexoSigla, id, nome, telefone, email, endereco)

        self.cpf = cpf
        self.rg = rg
        self.matricula = matricula
        self.setor = setor
        self.salario = salario