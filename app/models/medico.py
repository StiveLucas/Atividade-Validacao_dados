from app.models.abstract.funcionario import Funcionario
from app.models.enums.estado_civil import EstadoCivil
from app.models.endereco import Endereco
from app.models.enums.sexo import Sexo
from app.models.enums.setor import Setor

class Medico(Funcionario):
    def __init__(self, crm: str, cpf: str, rg: str, matricula: str, setor: Setor, salario: float, dataDeNascimento: str, estadoCivil: EstadoCivil, sexoNome: Sexo, sexoSigla: Sexo, id: str, nome: str, telefone: str, email: str, endereco: Endereco):
        super().__init__(cpf, rg, matricula, setor, salario, dataDeNascimento, estadoCivil, sexoNome, sexoSigla, id, nome, telefone, email, endereco)

        self.crm = crm

    def __str__(self):
        return(

            f"\nMédico: \nId: {self.id} \nNome: {self.nome} \nTelefone: {self.telefone} \nEmail: {self.email} "
            f"\nData de Nascimento: {self.dataDeNascimento} \nSexo: {self.sexoNome} / {self.sexoSigla}"
            f"\nCRM: {self.crm} \nCPF: {self.cpf} \nRG: {self.rg} \nMatricula: {self.matricula}"
            f" \nEstado Civil: {self.estadoCivil} \nSetor: {self.setor} \nEndereço do Médico: {self.endereco}"
        )