from abc import ABC
from app.models.endereco import Endereco

class Pessoa(ABC):
    def __init__(self, id: str, nome: str, telefone: str, email: str, endereco: Endereco):

        self.id = id
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.endereco = endereco