import pandas as pd
import os
from TratarCampos import TratarCampos
from NomeHandler import NomeHandler
from DataNascimentoHandler import DataNascimentoHandler
from EstadoHandler import EstadoHandler
from TimeFavoritoHandler import TimeFavoritoHandler
from CorFavoritaHandler import CorFavoritaHandler
from DiaHandler import DiaHandler
from ComidaHandler import ComidaHandler

class Pessoa:

    def __init__(self, nome, data_de_nascimento, estado,
                 time_favorito, cor_favorita, dia_da_entrevista,
                 comida_favorita):
            self._nome = nome
            self._data_de_nascimento = data_de_nascimento
            self._estado = estado
            self._time_favorito = time_favorito
            self._cor_favorita = cor_favorita
            self._dia_da_entrevista = dia_da_entrevista
            self._comida_favorita = comida_favorita
    def __str__(self):
        string="\nNome:"+self._nome+"\n"
        string+="Data de nascimento:"+self._data_de_nascimento+"\n"
        string+="Estado:"+self._estado+"\n"
        string+="Time favorito:"+self._time_favorito+"\n"
        string+="Cor Favorita:"+self._cor_favorita+"\n"
        string+="Dia da entrevista:"+self._dia_da_entrevista+"\n"
        string+="Comida Favorita:"+self._comida_favorita+"\n"
        return string

atributos = {
	"Nome": "nome",
	"Data de nascimento": "data_de_nascimento",
	"Estado": "estado",
    "Time favorito": "time_favorito",
	"Cor favorita": "cor_favorita",
	"Dia da entrevista": "dia_da_entrevista",
    "Comida favorita": "comida_favorita"
}


class Cadastrar:

    def __init__(self, path):
        self._path = path
        self._df = self.ler_arquivo()
        self._campos = self.ler_labels()
        self._tratarCampos = TratarCampos(
            NomeHandler(
                DataNascimentoHandler(
                    EstadoHandler(
                        TimeFavoritoHandler(
                            CorFavoritaHandler(
                                DiaHandler(
                                    ComidaHandler()
                                )
                            )
                        )
                    )
                )
            )
        )
        self._lista_de_pessoas = []
        self.cadastrar()

    def ler_arquivo(self):
        return pd.read_csv(self._path, encoding='utf8')

    def ler_labels(self):
        campos = []
        for item in self._df.columns.tolist():
            campos.append(item)
        return campos

    def printa_lista_de_pessoas(self):
        print("*******************")
        for pessoa in self._lista_de_pessoas:
            print(pessoa)
        print("*******************")

    def cadastrar(self):
        pessoa_atributos = {
			"nome": "",
			"data_de_nascimento": "",
			"estado": "",
            "time_favorito": "",
			"cor_favorita": "",
			"dia_da_entrevista": "",
            "comida_favorita": ""
		}
        for i in range(0, len(self._df.index)):
            for j in range(0, len(self._df.iloc[i].index)):
                pessoa_atributos[atributos[self._campos[j]]] = self._tratarCampos.handle(self._df.iloc[i, j], self._campos[j])

            pessoa = Pessoa(
				pessoa_atributos["nome"],
				pessoa_atributos["data_de_nascimento"],
				pessoa_atributos["estado"],
				pessoa_atributos["time_favorito"],
				pessoa_atributos["cor_favorita"],
				pessoa_atributos["dia_da_entrevista"],
				pessoa_atributos["comida_favorita"],
			)
            self._lista_de_pessoas.append(pessoa)
        self.printa_lista_de_pessoas()

current_directory = os.path.dirname(os.path.abspath(__file__))
arquivo_path = os.path.join(current_directory,"pessoas.csv")
cadastrador = Cadastrar(arquivo_path)
