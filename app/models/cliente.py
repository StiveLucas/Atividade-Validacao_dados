from app.models.abstract.fisica import Fisica
from app.models.enums.estado_civil import EstadoCivil
from app.models.enums.sexo import Sexo
from app.models.endereco import Endereco

class Cliente(Fisica):
    def __init__(self, protocoloDeAtendimento: str, dataDeNascimento: str, estadoCivil: EstadoCivil, sexoNome: Sexo, sexoSigla: Sexo, id: str, nome: str, telefone: str, email: str, endereco: Endereco):
        super().__init__(dataDeNascimento, estadoCivil, sexoNome, sexoSigla, id, nome, telefone, email, endereco)

        self.protocoloDeAtendimento = protocoloDeAtendimento

    def __str__(self):
        return(

            f"\nCliente: \nId: {self.id} \nNome: {self.nome} \nTelefone: {self.telefone} \nEmail: {self.email}"
            f"\nEstado Civil: {self.estadoCivil} \nSexo: {self.sexoNome} / {self.sexoSigla}"
            f"\nData de Nascimento: {self.dataDeNascimento} \nProtocolo de Atendimento: {self.protocoloDeAtendimento}"
            f"\nEndereço do Cliente: {self.endereco}"
        )