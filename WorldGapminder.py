
# gapminder DATA
import pandas as pd
import matplotlib.pyplot as plt

from gapminder import gapminder
gapminder.head()


pd_gapminder = pd.DataFrame(gapminder)
type(pd_gapminder["country"])
help(pd.DataFrame)

pd_gapminder[['country']]
pd_gapminder[["country", "year", "pop"]]
albania = pd_gapminder.loc[12:23]


df = pd_gapminder.set_index('country')
df.head()
df_albania = df.loc["Albania"]
df_albania.head()

albania_pop = df.loc[["Albania"],["year","pop"]]

albania_pop = albania_pop.set_index("year")
plt.plot(albania_pop)
