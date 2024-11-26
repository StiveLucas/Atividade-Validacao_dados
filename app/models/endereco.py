from app.models.enums.unidade_federativa import UnidadeFederativa

class Endereco():
    def __init__(self, logradouro: str, numero: str, 
                 complemento: str, cep: str, cidade: str, ufNome: UnidadeFederativa, 
                 ufSigla: UnidadeFederativa 
                 ):
        
        self.logradouro = logradouro
        self.numero = numero
        self.complemento = complemento
        self.cep = cep
        self.cidade = cidade
        self.ufNome = ufNome
        self.ufSigla = ufSigla

    def __str__(self):
        return(
            f"\nEndereço: \nLogradouro: {self.logradouro} \nNúmero: {self.numero} \nComplemento: {self.complemento}"
            f"\nCEP: {self.cep} \nCidade: {self.cidade} \nUf: {self.ufNome} / {self.ufSigla}"

        )

        