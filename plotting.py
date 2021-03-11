###############################
#----------INTRODUÇÃO---------#
###############################
import matplotlib.pyplot as plt
import pandas as pd

# para criar uma Figura e os Eixos do gráfico:
fig, ax = plt.subplots()
plt.show()

# vamos adicionar dados 
arquivo = pd.read_csv(r"C:\Users\anapa\OneDrive\Dados\datacamp\seattle_weather.csv")
arquivo1 = pd.read_csv(r"C:\Users\anapa\OneDrive\Dados\datacamp\austin_weather.csv")
seattle = pd.DataFrame(arquivo)

# com base nos dados utilizados no datacamp
seattle1 = pd.DataFrame(seattle[seattle['STATION']=='USW00094290']) #somente esta estação foi escolhida
dmeses = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dez'] #adicione uma coluna com os meses por escrito 
seattle1['MONTH'] = dmeses
seattle1.set_index('DATE') #data está como índice

austin = pd.DataFrame(arquivo1)
austin['MONTH'] = dmeses
austin.set_index('DATE')

# plotar dados de seattle e de austin
fig, ax = plt.subplots()
ax.plot(seattle1["MONTH"], seattle1["MLY-PRCP-NORMAL"])
ax.plot(austin["MONTH"], austin["MLY-PRCP-NORMAL"])
plt.show()

# customização dos gráficos
fig, ax = plt.subplots()
ax.plot(seattle1["MONTH"], seattle1["MLY-TAVG-NORMAL"], marker='v', linestyle='--', color='r')
ax.set_xlabel("Meses")
ax.set_ylabel("Temperatura Média em Fahrenheit")
plt.show()


# small multiples - útil para quando os dados são muitos e dificultam a visualização
fig, ax = plt.subplots(3,2) # 3 linhas e 2 colunas
plt.show()
ax.shape #neste caso, a variável ax torna-se um array de tamanho 3x2

ax[0,0].plot(seattle1["MONTH"], seattle1["MLY-PRCP-NORMAL"], color='b')
plt.show()

fig,ax = plt.subplots(2,1) #neste caso, só será necessário indicar um índice para acessar os elementos do array (conjunto)
ax[0].plot(seattle1["MONTH"], seattle1["MLY-PRCP-NORMAL"], color='b')
ax[0].plot(seattle1["MONTH"], seattle1["MLY-PRCP-25PCTL"], linestyle='--', color='b')
ax[0].plot(seattle1["MONTH"], seattle1["MLY-PRCP-75PCTL"], linestyle='--', color='b')
ax[1].plot(austin["MONTH"], austin["MLY-PRCP-NORMAL"], color='r')
ax[1].plot(austin["MONTH"], austin["MLY-PRCP-25PCTL"], linestyle='--', color='r')
ax[1].plot(austin["MONTH"], austin["MLY-PRCP-75PCTL"], linestyle='--', color='r')

ax[0].set_ylabel("Precipitação (em polegadas)")
ax[1].set_ylabel("Precipitação (em polegadas)")
ax[1].set_xlabel("Meses") #os dois gráficos possuem o mesmo eixo x
plt.show()

# no caso de possuírem o mesmo eixo y, rode isso ao determinar a configuração do gráficos 
fig, ax = plt.subplots(2,1, sharey=True)



###############################
#------SÉRIES TEMPORAIS-------#
###############################

# Para transformar o index em DateTimeIndex, use parse_dates (list) e index_col (string)
arquivo_ts = pd.read_csv(r"C:\Users\anapa\OneDrive\Dados\datacamp\climate_change.csv", parse_dates=["date"], index_col="date")
climate_change = pd.DataFrame(arquivo_ts)
climate_change.index


fig, ax = plt.subplots()
ax.plot(climate_change.index, climate_change['co2'])
plt.show()

fig, ax = plt.subplots()
ax.plot(climate_change.index, climate_change["relative_temp"])
ax.set_xlabel("Período")
ax.set_ylabel("Temperatura Relativa (Celsius)")
plt.show()

# Para selecionar um período:
fig, ax = plt.subplots()
anos90 = climate_change["1990-01-01":"1999-12-31"]
ax.plot(anos90.index, anos90["co2"])
ax.set_xlabel("Década de 1990")
ax.set_ylabel("CO2")
plt.show()


##### BARRAS DE ERROS #####
# Resumem a distribuição dos dados através de um número, como é o caso do desvio padrão
fig, ax = plt.subplots()

# Add Seattle temperature data in each month with error bars
ax.errorbar(seattle_weather["MONTH"], seattle_weather["MLY-TAVG-NORMAL"], yerr=seattle_weather["MLY-TAVG-STDDEV"])

# Add Austin temperature data in each month with error bars
ax.errorbar(austin_weather["MONTH"], austin_weather["MLY-TAVG-NORMAL"], yerr=austin_weather["MLY-TAVG-STDDEV"])

# Set the y-axis label
ax.set_ylabel("Temperature (Fahrenheit)")

plt.show()