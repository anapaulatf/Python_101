# PYTHON AND STATISTICS FOR FINANCIAL ANALYSIS

# Pacotes utilizados:
# pandas
# numpy
# matplotlib
# statsmodels

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

fb = pd.read_csv('data/facebook.csv', index_col=0)
ms = pd.read_csv('data/microsoft.csv', index_col=0)

fb.head()
fb.index[0]
fb.index[-1] #último número
fb.columns
fb.shape #número de linhas e colunas

fb.tail() #últimas 5 linhas. você pode colocar o número desejado dentro dos parenteses
fb.describe() #algumas estatísticas básicas de distribuição


## SLICING DATA FRAME
# selection por label (.loc)
# selection por position (.iloc)

fb.loc['2015-01-02', 'Close']
fb.loc['2015-01-01':'2015-12-31', 'Close']

fb.iloc[1,3] #row, column
fb.iloc[624: , : ]


## PLOTTING DATA
fb.loc['2015-01-01':'2015-12-31', 'Close'].plot()
fb.loc['2016-01-01':'2016-12-31', 'Close'].plot()


## SELECIONANDO COLUNAS
fb['Close']

## Selecionando várias colunas
fb[['Open','Close']]


# CRIANDO COLUNAS NO DATAFRAME
fb['Price1'] = fb['Close'].shift(-1)
# shift(-1) coloca o preço de fechamento do dia seguinte. basicamente faz todas as linhas da coluna Close subir uma célula

fb['PriceDiff'] = fb['Price1'] - fb['Close']
fb['Return'] = fb['PriceDiff']/fb['Close']
fb.head()

# CRIANDO UMA COLUNA DE DIREÇÃO (list comprehension)
fb['Direction'] = [1 if fb.loc[ei, 'PriceDiff'] > 0 else -1 for ei in fb.index]

# MOVING AVERAGE
# moving average: aqui a gente está fazendo uma média simples entre os preços de fechamento de d(0), d(-1) e d(-2)
fb['Average3'] = (fb['Close'] + fb['Close'].shift(1) + fb['Close'].shift(2))/3
fb.head()

# moving average using .rolling()
# para os primeiros 40 dias

fb['MA40'] = fb['Close'].rolling(40).mean()

# para os primeiros 200 dias
fb['MA200'] = fb['Close'].rolling(200).mean()

# plotting moving AVERAGE
fb['Close'].plot()
fb['MA40'].plot()
fb['MA200'].plot()

####
####
#### RANDOM NUMBERS - SEMANA 2

dice = pd.DataFrame([1,2,3,4,5,6])
sum_of_dice = dice.sample(2, replace = True).sum().loc[0] # dice.sample(2) avisa que estão sendo jogados 2 dados
print(sum_of_dice) #os números jogados podem ser 5 e 3, 6 e 2, etc...

trial = 50   # vamos jogas os dados 50 vezes
result = [dice.sample(2, replace = True).sum().loc[0] for i in range(trial)]
result[:10]   # as 10 primeiras observações deste experimento

## Frequencia
freq = pd.DataFrame(result)[0].value_counts()
sort_freq = freq.sort_index()
sort_freq

sort_freq.plot(kind='bar', color='blue')

## Population sampling
data = pd.DataFrame()
data['Population'] = [47,48,85,20,19,13,72,16,50,60]
sample_no_replace = data['Population'].sample(5, replace=False)
sample_no_replace

## Sampling from a normal distribution
Fstsample = pd.DataFrame(np.random.normal(10,5,size=30))
print('sample mean is ', Fstsample[0].mean())
print('sample SD is ', Fstsample[0].std(ddof=1))



aapl = pd.read_csv("data/apple.csv", index_col=0) 
aapl.loc['2012-08-01':'2013-08-01', 'Close'].plot()

plt.gcf().autofmt_xdate()

