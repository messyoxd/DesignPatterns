import pandas as pd
import os

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


estados = (
    ('Acre','AC'),
    ('Alagoas','AL'),
    ('Amapá','AP'),
    ('Amazonas','AM'),
    ('Bahia','BA'),
    ('Ceará','CE'),
    ('Distrito Federal','DF'),
    ('Espírito Santo','ES'),
    ('Goiás','GO'),
    ('Maranhão','MA'),
    ('Mato Grosso','MT'),
    ('Mato Grosso do Sul','MS'),
    ('Minas Gerais','MG'),
    ('Pará','PA'),
    ('Paraíba','PB'),
    ('Paraná','PR'),
    ('Pernambuco','PE'),
    ('Piauí','PI', ),
    ('Rio de Janeiro','RJ'),
    ('Rio Grande do Norte','RN'),
    ('Rio Grande do Sul','RS'),
    ('Rondônia','RO'),
    ('Roraima','RR'),
    ('Santa Catarina','SC'),
    ('São Paulo','SP'),
    ('Sergipe','SE'),
    ('Tocantins','TO'))

times = (
        ("CE", "Ceará"),
        ("FOR", "Fortaleza"),
        ("FER", "Ferroviário"),)

cores = (
        ("VER", "Vermelho"),
        ("AZ", "Azul"),
        ("VERD", "Verde"))

dias = (
    ("1", "Segunda"),
    ("2", "Terça"),
    ("3", "Quarta"),
    ("4", "Quinta"),
    ("5", "Sexta"),
    ("6", "Sábado"),
    ("7", "Domingo"),)

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
        self._lista_de_pessoas = []
        self.cadastrar()

    def ler_arquivo(self):
        return pd.read_csv(self._path, encoding='utf8')

    def ler_labels(self):
        campos = []
        for item in self._df.columns.tolist():
            campos.append(item)
        return campos
    def checa_enumeration(self, dado, enum):
        for item in enum:
            if item[1] == dado:
                return item[0]
        return None
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
                if self._campos[j] == "Nome":
                    aux = self._df.iloc[i, j]
                    nome = ""
                    for parte in aux.split(" "):
                        nome += parte[0].upper() + parte[1:].lower()+" "
                    nome = nome[:-1]
                    pessoa_atributos[atributos[self._campos[j]]] = nome
                elif self._campos[j] == "Data de nascimento":
                    aux = self._df.iloc[i, j]
                    data = ""
                    for item in aux.split("/"):
                        data += item+"-"
                    data = data[:-1]
                    pessoa_atributos[atributos[self._campos[j]]] = data
                elif self._campos[j] == "Estado":
                    estado = self.checa_enumeration(self._df.iloc[i, j], estados)
                    if estado == None:
                        estado = "-"
                    pessoa_atributos[atributos[self._campos[j]]] = estado
                elif self._campos[j] == "Time favorito":
                    time = self.checa_enumeration(self._df.iloc[i, j], times)
                    if time == None:
                        time = "-"
                    pessoa_atributos[atributos[self._campos[j]]] = time
                elif self._campos[j] == "Cor favorita":
                    cor = self.checa_enumeration(self._df.iloc[i, j], cores)
                    if cor == None:
                        cor = "-"
                    pessoa_atributos[atributos[self._campos[j]]] = cor
                elif self._campos[j] == "Dia da entrevista":
                    dia = self.checa_enumeration(self._df.iloc[i, j], dias)
                    if dia == None:
                        dia = "-"
                    pessoa_atributos[atributos[self._campos[j]]] = dia
                elif self._campos[j] == "Comida favorita":
                    pessoa_atributos[atributos[self._campos[j]]] = self._df.iloc[i, j]
            # print(pessoa_atributos)
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
