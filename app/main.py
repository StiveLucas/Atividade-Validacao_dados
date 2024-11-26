import os
from app.models.endereco import Endereco
from app.models.enums.setor import Setor
from app.models.enums.sexo import Sexo
from app.models.enums.estado_civil import EstadoCivil
from app.models.enums.unidade_federativa import UnidadeFederativa
from app.models.engenheiro import Engenheiro
from app.models.medico import Medico
from app.models.advogado import Advogado
from app.models.cliente import Cliente
from app.models.prestacao_servico import PrestacaoServico

#A Atividade está incompleta.


engenheiro = Engenheiro("123", "111-111-11", "16-954-890",
                         "909.764.985", Setor.ENGENHARIA.nome, 4500, "02/04/2006",
                         EstadoCivil.CASADO.nome, Sexo.MASCULINO.nome, Sexo.MASCULINO.sigla,
                         "666-999-444", "Lucas", "71-907689", "@gmail.com",
                         Endereco("Perto do rio", "333", "Nenhum", "40391286", "Salvador", UnidadeFederativa.BAHIA.nome, UnidadeFederativa.BAHIA.sigla )
                        
                         
                         )

medico = Medico("344", "467.865.870-98", "16.6767-890.66", "345.642.897.987-99", 
                Setor.SAUDE.nome, 3500, "09/07/1990", EstadoCivil.SEPARADO.nome, Sexo.MASCULINO.nome,
                Sexo.MASCULINO.sigla, "566.8998", "Thiago", "71453-96598", "@hotmail.com",
                Endereco("Perto da praça", "445", "Nenhum", "4074379", "Salvador", UnidadeFederativa.BAHIA.nome, UnidadeFederativa.BAHIA.sigla)
                
                )

advogado = Advogado("3453", "490-765-897-90", "56.647-855-90", "566.998.567-63",
                     Setor.JURIDICO.nome, 56700, "23/12/2000", EstadoCivil.VIUVO.nome, 
                     Sexo.FEMININO.nome, Sexo.FEMININO.sigla, "6788.764-90", "Ana", "73975970", 
                     "@outllok.com",
                     Endereco("Perto do Banco", "231", "Nenhum", "324689", "Salvador", UnidadeFederativa.BAHIA.nome, UnidadeFederativa.BAHIA.sigla)
                         )

cliente = Cliente("5677", "09/09/1997", EstadoCivil.SOLTEIRO.nome, Sexo.MASCULINO.nome, 
                  Sexo.MASCULINO.sigla, "456758.47", "Davi", "75997-7667", "@Gmail.com",
                  Endereco("Perto do Lago", "213", "Nenhum", "7887546", "Salvador", UnidadeFederativa.BAHIA.nome, UnidadeFederativa.BAHIA.sigla)
                  )

pretacao_servico = PrestacaoServico()
