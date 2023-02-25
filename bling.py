import requests
import json

apikey = 'eab3d65243c24585c5a0a31bd6d58086baa83fad43d45bef5b9c02d59b9bde5a3e66dcee'
url = "https://bling.com.br/Api/v2/produtos/page=1/json&apikey=eab3d65243c24585c5a0a31bd6d58086baa83fad43d45bef5b9c02d59b9bde5a3e66dcee"

r = requests.get(url)
json_data = r.json()

for key, value in json_data.items(): #printa cada par key-value existente em json_data 
    print(key + ':', value)


print(json_data['retorno']['produtos'])
