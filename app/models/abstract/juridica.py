from app.models.abstract.pessoa import Pessoa
from abc import ABC
from app.models.endereco import Endereco

class Jurida(ABC, Pessoa):
    def __init__(self, cnpj: str, inscricaoEstadual: str, id: str, nome: str, telefone: str, email: str, endereco:Endereco ):
        super().__init__(id, nome, telefone, email, endereco)

        self.cnpj = cnpj
        self.inscricaoEstadual = inscricaoEstadual