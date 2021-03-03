import pandas as pd

file = 'data/DespesaSenado.csv'

data = pd.read_csv(file, encoding='latin-1', sep=';', skiprows=2)

print(data.head())
