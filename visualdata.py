###############################################
##------------------SEABORN------------------##
###############################################

# bibiliotecas
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns 


# abrindo dados 
paises = pd.read_csv(r"C:\Users\anapa\OneDrive\Dados\datacamp\countries-of-the-world.csv", index_col=0)
paises.head()
# analises iniciais dos dados
sns.scatterplot(x=paises['GDP ($ per capita)'], y=paises['Literacy (%)'])
plt.show()

plt.scatter(x=paises['GDP ($ per capita)'], y=paises['Literacy (%)'])
print(paises)


fig, ax = plt.subplots()
ax.scatter(paises['GDP ($ per capita)'], y=paises['Literacy (%)'])
plt.show()