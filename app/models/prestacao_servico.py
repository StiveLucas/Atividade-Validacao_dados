from app.models.abstract.juridica import Jurida
from app.models.endereco import Endereco

class PrestacaoServico(Jurida):
    def __init__(self, contratoInicial: str, contratoFinal: str, cnpj: str, inscricaoEstadual: str, id: str, nome: str, telefone: str, email: str, endereco: Endereco):
        super().__init__(cnpj, inscricaoEstadual, id, nome, telefone, email, endereco)

        self.contratoInicial = contratoInicial
        self.contratoFinal = contratoFinal

    def __str__(self):
        return(

            f"\nPrestação do Serviço:"
            f"\nID: {self.id} \nNome: {self.nome} \nTelefone: {self.telefone} \nEmail: {self.email}"
            f"\nCNPJ: {self.cnpj} \nInscrição Estadual: {self.inscricaoEstadual}"
            f"\nContrato Inicial: {self.contratoInicial} \nContrato Final: {self.contratoFinal}"
            f"\nEndereço da Prestação: {self.endereco}"
        )
