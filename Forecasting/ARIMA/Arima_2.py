# from Average import *
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import warnings
from statsmodels.tsa.stattools import adfuller
from statsmodels.tsa.arima.model import ARIMA
import itertools

warnings.filterwarnings('ignore')

file_path = r"C:\Users\i'm_jit99\Desktop\8sem\Forecasting\Average\2.csv"
df=pd.read_csv(file_path)
df.set_index('date',inplace=True)
print(df.head())
print("done")

#  ADf test to see if the date is stationary or not
def adfuller_test(data):
    result=adfuller(data)
    dftest = adfuller(data, autolag = 'AIC')

    labels = ['ADF Test Statistic','p-value','#Lags Used','Number of Observations Used']
    for value,label in zip(result,labels):
        print(label+' : '+str(value) )
    if result[1] <= 0.05:
        print("strong evidence against the null hypothesis(Ho), reject the null hypothesis. Data has no unit root and is stationary")
    else:
        print("weak evidence against null hypothesis, time series has a unit root, indicating it is non-stationary ")
    


     
adfuller_test(df['data'])


df['new']=df['data'].diff()
adfuller_test(df['new'].dropna())

# # Perform differencing to make the series stationary
# df['new_diff'] = df['new'].diff().dropna()


train_section=df.iloc[:21]
test_section=df.iloc[21:]
print(train_section.shape,test_section.shape)


p_values = range(0, 6)  # p values from 0 to 5
d_values = range(0, 3)  # d values from 0 to 2
q_values = range(0, 6)  # q values from 0 to 5

# Generate all possible combinations of p, d, and q values
all_combinations = list(itertools.product(p_values, d_values, q_values))


"""all the combinations
# list21= [(0, 0, 0), (0, 0, 1), (0, 0, 2), (0, 0, 3), (0, 0, 4), (0, 0, 5), (0, 1, 0), (0, 1, 1), (0, 1, 2), (0, 1, 3), (0, 1, 4), (0, 1, 5), (0, 2, 0), (0, 2, 1), (0, 2, 2), (0, 2, 3), (0, 2, 4), (0, 2, 5), (1, 0, 0), (1, 0, 1), (1, 0, 2), (1, 0, 3), (1, 0, 4), (1, 0, 5), (1, 1, 0), (1, 1, 1), (1, 1, 2), (1, 1, 3), (1, 1, 4), (1, 1, 5), (1, 2, 0), (1, 2, 1), (1, 2, 2), (1, 2, 3), (1, 2, 4), (1, 2, 5), (2, 0, 0), (2, 0, 1), (2, 0, 2), (2, 0, 3), (2, 0, 4), (2, 0, 5), (2, 1, 0), (2, 1, 1), (2, 1, 2), (2, 1, 3), (2, 1, 4), (2, 1, 5), (2, 2, 0), (2, 2, 1), (2, 2, 2), (2, 2, 3), (2, 2, 4), (2, 2, 5), (3, 0, 0), (3, 0, 1), (3, 0, 2), (3, 0, 3), (3, 0, 4), (3, 0, 5), (3, 1, 0), (3, 1, 1), (3, 1, 2), (3, 1, 3), (3, 1, 4), (3, 1, 5), (3, 2, 0), (3, 2, 1), (3, 2, 2), (3, 2, 3), (3, 2, 4), (3, 2, 5), (4, 0, 0), (4, 0, 1), (4, 0, 2), (4, 0, 3), (4, 0, 4), (4, 0, 5), (4, 1, 0), (4, 1, 1), (4, 1, 2), (4, 1, 3), (4, 1, 4), (4, 1, 5), (4, 2, 0), (4, 2, 1), (4, 2, 2), (4, 2, 3), (4, 2, 4), (4, 2, 5), (5, 0, 0), (5, 0, 1), (5, 0, 2), (5, 0, 3), (5, 0, 4), (5, 0, 5), (5, 1, 0), (5, 1, 1), (5, 1, 2), (5, 1, 3), (5, 1, 4), (5, 1, 5), (5, 2, 0), (5, 2, 1), (5, 2, 2), (5, 2, 3), (5, 2, 4), (5, 2, 5)]
# print(len(list21))
"""


AiC = {}
BiC = {}

for combination in all_combinations:
    p, d, q = combination

    try:
        # model = ARIMA(data, order=order).fit()
        model=ARIMA(train_section['data'],order=(combination)).fit()

        # print(f"Order {combination}: AIC = {model.aic}, BIC = {model.bic}")
    except:
        continue
    
    
    AiC[combination] = model.aic
    BiC[combination] = model.bic

# print(AiC)
# print(BiC)

Best_aic_combination = min(AiC, key=lambda x: AiC[x])
min_aic_value = AiC[Best_aic_combination]

print(f"Minimum AIC: {min_aic_value}, Combination with Minimum AIC: {Best_aic_combination}")

Best_bic_combination = min(BiC, key= lambda y: BiC[y])
min_bic_value = BiC[Best_bic_combination]
print(f"Minimum BIC: {min_bic_value}, Combination with Minimum BIC: {Best_bic_combination}")


print("<========================================>")

## model=ARIMA(train_section['data'],order=(5,2,4)).fit()
model=ARIMA(train_section['data'],order=(5,1,3)).fit()
print(model.aic) 

print(model.bic)
print(model.summary())





"""making prediction on the test cases"""

start=len(train_section)
end=len(train_section)+len(test_section)-1
FuturePrediction=model.predict(start=start,end=end,type='levels')
print(FuturePrediction)


from sklearn.metrics import mean_squared_error
from math import sqrt
test_section['data'].mean()
rmse=sqrt(mean_squared_error(test_section['data'],FuturePrediction))
print(f"rmse score is {rmse}")
# print(df['data'].mean())
print(test_section['data'].mean())

from sklearn.metrics import mean_absolute_error
mae = mean_absolute_error(test_section['data'], FuturePrediction)

print("MAE:", mae)

FuturePrediction.plot(legend=True,label="predicted")


plt.show()









