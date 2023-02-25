import pandas as pd
import matplotlib.pyplot as plt
from pmdarima.arima import auto_arima
from pyparsing import col
from statsmodels.tsa.seasonal import seasonal_decompose
from tbats import TBATS
import rpy2 as r
from rpy2.robjects.packages import importr


fpp2= importr("fpp2")


# Abrindo dados de vendas diárias
dados = pd.read_excel(r"C:\Users\win\Code\Projetos\Python_101\data\dados_vendas_google.xlsx", sheet_name="dados", parse_dates=['date'], index_col=0)
dados.head()

# Visualização inicial dos dados
plt.plot(dados)
plt.show()


ts_dicomposition = seasonal_decompose(dados.asfreq('MS'), model='additive')
trend_estimate = ts_dicomposition.trend
seasonal_estimate = ts_dicomposition.seasonal
residual_estimate = ts_dicomposition.resid




# Plotting the time series and it's components together
fig, axes = plt.subplots(4, 1, sharex=True, sharey=False)
fig.set_figheight(10)
fig.set_figwidth(20)
# First plot to the Original time series
axes[0].plot(dados, label='Original') 
axes[0].legend(loc='upper left');
# second plot to be for trend
axes[1].plot(trend_estimate, label='Trend')
axes[1].legend(loc='upper left');
# third plot to be Seasonality component
axes[2].plot(seasonal_estimate, label='Seasonality')
axes[2].legend(loc='upper left');
# last last plot to be Residual component
axes[3].plot(residual_estimate, label='Residuals')
axes[3].legend(loc='upper left');

plt.show()


from tbats import TBATS, BATS# Fit the model
estimator = TBATS(seasonal_periods=(7, 365.25))
model = estimator.fit(dados)# Forecast 365 days ahead
y_forecast = model.forecast(steps=12)
print(y_forecast)

plt.plot(y_forecast)