import pandas as pd
import matplotlib.pyplot as plt
from pmdarima.arima import auto_arima
from statsmodels.tsa.seasonal import seasonal_decompose
from tbats import TBATS


dados = pd.read_excel(r"C:\Users\win\Code\Python_101\data\dados_vendas_google.xlsx", sheet_name="dados", index_col=0)

dados.sort_index(inplace=True)
dados.head()

plt.plot(dados['Índice do dia'], dados['Receita'])
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

arima_model = auto_arima(dados, start_p=0, d=1, start_q=0, start_P= 0, D=1, start_Q=0, max_P=5, max_D=5, max_Q=5, m=365, seasonal=True, trace=True)


from tbats import TBATS, BATS# Fit the model
estimator = TBATS(seasonal_periods=(7, 365.25))
model = estimator.fit(dados)# Forecast 365 days ahead
y_forecast = model.forecast(steps=12)
print(y_forecast)

plt.plot(y_forecast)