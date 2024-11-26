from app.models.abstract.juridica import Jurida
from app.models.endereco import Endereco

class Fornecedor(Jurida):
    def __init__(self, produto: str, cnpj: str, inscricaoEstadual: str, id: str, nome: str, telefone: str, email: str, endereco: Endereco):
        super().__init__(cnpj, inscricaoEstadual, id, nome, telefone, email, endereco)

        self.produto = produto

    def __str__(self):
        return(

            f"\nFornecedor:"
            f"\nID: {self.id} \nNome: {self.nome} \nTelefone: {self.telefone} \nEmail: {self.email}"
            f"\nCNPJ: {self.cnpj} \nInscrição Estadual: {self.inscricaoEstadual}"
            f"\nProduto: {self.produto}"
            f"\nEndereço do Fornecedor: {self.endereco}"
        )