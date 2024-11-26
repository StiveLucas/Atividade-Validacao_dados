from app.models.abstract.funcionario import Funcionario
from app.models.enums.estado_civil import EstadoCivil
from app.models.endereco import Endereco
from app.models.enums.sexo import Sexo
from app.models.enums.setor import Setor

class Engenheiro(Funcionario):
    def __init__(self, crea: str, cpf: str, rg: str, matricula: str, setor: Setor, salario: float, dataDeNascimento: str, estadoCivil: EstadoCivil, sexoNome: Sexo, sexoSigla: Sexo, id: str, nome: str, telefone: str, email: str, endereco: Endereco):
        super().__init__(cpf, rg, matricula, setor, salario, dataDeNascimento, estadoCivil, sexoNome, sexoSigla, id, nome, telefone, email, endereco)

        self.crea = crea

    def __str__(self):
        return(

            f"\nEngenheiro: \nId: {self.id} \nNome: {self.nome} \nTelefone: {self.telefone} \nEmail: {self.email} "
            f"\nData de Nascimento: {self.dataDeNascimento} \nSexo: {self.sexoNome} / {self.sexoSigla}"
            f"\nCREA: {self.crea} \nCPF: {self.cpf} \nRG: {self.rg} \nMatricula: {self.matricula}"
            f" \nEstado Civil: {self.estadoCivil} \nSetor: {self.setor} \nEndereço do Engenheiro: {self.endereco}"
        )