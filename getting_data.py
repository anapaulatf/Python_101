### useful: download and extract chinook sample DB
import urllib.request
import zipfile
from functools import partial
import os

chinook_url = 'http://www.sqlitetutorial.net/wp-content/uploads/2018/03/chinook.zip'
if not os.path.exists('chinook.zip'):
    print('downloading chinook.zip ', end='')
    with urllib.request.urlopen(chinook_url) as response:
        with open('chinook.zip', 'wb') as f:
            for data in iter(partial(response.read, 4*1024), b''):
                print('.', end='', flush=True)
                f.write(data)

zipfile.ZipFile('chinook.zip').extractall()
assert os.path.exists('chinook.db')


## Essa é a parte que o datacamp ensina: 
from sqlalchemy import create_engine
import pandas as pd
engine = create_engine('sqlite:///chinook.db')

table_names = engine.table_names()
print(table_names)

con = engine.connect()
rs = con.execute("SELECT * FROM albums")
df = pd.DataFrame(rs.fetchall())
df.columns = rs.keys() #assim aparece o nome das colunas
con.close()
print(df.head())

# para evitar o TRABALHO de fechar ou evitar ESQUECER de fechar:
with engine.connect() as con:
    rs2 = con.execute("SELECT * FROM artists")
    df2 = pd.DataFrame(rs2.fetchall())
    df2.columns = rs2.keys()
print(df2.head())

# Fazer em apenas uma linha
df3 = pd.read_sql_query("SELECT * FROM customers", engine)

# Linkando tabelas
df4 = pd.read_sql_query("SELECT Title, Name FROM albums INNER JOIN artists on albums.ArtistID = artists.ArtistId", engine)
print(df4.head())


###############################################
#-------------INTERMEDIATE COURSE-------------#
#---------GETTING DATA FROM THE WEB-----------#
###############################################
import matplotlib.pyplot as plt
import pandas as pd
from urllib.request import urlretrieve

# URL é Universal Resource Locator
url = "https://s3.amazonaws.com/assets.datacamp.com/production/course_1606/datasets/winequality-red.csv"
urlretrieve(url, "data/winequality-red.csv") #salva localmente o arquivo 
df = pd.read_csv("data/winequality-red.csv", sep=';') #ler o arquivo no formato de DataFrame 
print(df.head())

# Não é necessário salvar o arquivo localmente. Basta mandar busca-lo para poder ler
url = "https://s3.amazonaws.com/assets.datacamp.com/production/course_1606/datasets/winequality-red.csv"
df = pd.read_csv(url, sep=';')

pd.DataFrame.hist(df.iloc[:, 0:1])
plt.xlabel('fixed acidity (g(tartaric acid)/dm$^3$)')
plt.ylabel('count')
plt.show()


### HTTP request 
# HTTP significa HyperText Transfer Protocol (Application Protocol)
# Ao ir em um website, você envia um HTTP request: GET request
# urlretrieve() realiza um GET request 
# HTML - HyperText Markup Language

# GET request utilizando urllib
from urllib.request import urlopen, Request
url = "http://www.wikipedia.org/"
request = Request(url) #envia o request
response = urlopen(request) #retorna uma resposta (response) associado a um método read
html = response.read()
response.close()

# Será utilizado o 'requests' para realizar o request GET
import requests
url = "http://www.datacamp.com/teach/documentation"
r = requests.get(url) #envia o request e captura a resposta em uma única função
text = r.text #retorna o html como uma string 
print(text)


# BeautifulSoup
# Parse (analisa) and extract strutured data from HTML
from bs4 import BeautifulSoup
import requests
url = 'http://www.crummy.com/software/BeautifulSoup/'
r = requests.get(url)
html_doc = r.text
soup = BeautifulSoup(html_doc)
print(soup.prettify())
print(soup.title)
print(soup.get_text())

#extrair todas as url de todos os hiperlinks 
#encontre todas as tags 'a', que são aquelas que definem hyperlinks
for link in soup.find_all('a'):
    print(link.get('href'))

#######################################
#------INTRODUÇÃO A APIs E JSONs------#
#######################################

# API - Application Programming Interface
# Apresenta protocolos e rotinas para que dois programas possam se comunicar e interagir entre si

# JSON - JavaScript Object Notation
# Comunicação software para browser em tempo real 

# Open Movie Data Base API
import json
import requests

url = 'http://www.omdbapi.com/?i=tt3896198&apikey=3cf7a0a' #importa o request. o apikey é o MEU
r = requests.get(url) #envia o request para a url (seu API query) e recebe a resposta 
json_data = r.json() #built-in json decoder. retorna um dicionário.

for key, value in json_data.items(): 
    print(key + ':', value)

# este API KEY foi fornecido pelo datacamp. Depois, utiliza o argumento t para selecionar o título "the social network"
url = 'http://www.omdbapi.com/?apikey=72bc447a&t=the+social+network'
r = requests.get(url)
print(r.text)
json_data = r.json() #decodifica o arquivo em JSON em um dicionário
for key, value in json_data.items(): #printa cada par key-value existente em json_data 
    print(key + ':', value)

# Wikipedia API
url = "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&format=json&exintro=&titles=pizza"
r = requests.get(url) #pega o request, envia e recebe a resposta 
json_data = r.json() #decodifica os dados em JSON para um dicionário
pizza_extract = json_data['query']['pages']['24768']['extract']
print(pizza_extract)

# Twitter API

