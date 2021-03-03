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

