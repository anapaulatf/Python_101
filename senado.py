import pandas as pd
import json
import requests


url = 'https://dadosabertos.camara.leg.br/api/v2/deputados?ordenarPor=siglaPartido'
r = requests.get(url)

json_data = r.json()

json_data.keys()
json_extract = json_data['dados']
type(json_extract)

data = pd.DataFrame(json_extract)
data.head()
print(data.keys())



