import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import warnings
from statsmodels.tsa.stattools import adfuller
from statsmodels.tsa.arima.model import ARIMA
import itertools


warnings.filterwarnings('ignore')

file_path = r"C:\Users\jit24\OneDrive\Desktop\Major_project\Major__project\Forecasting\Average\4.csv" 
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
print(abs(df['new']))
adf1=adfuller(df['new'].dropna())
print('p is after:',adf1[1])
# df['new'].plot()
adfuller_test(df['new'].dropna())

# Perform differencing to make the series stationary
df['new_diff'] = df['new'].diff().dropna()
adfuller_test(df['new_diff'].dropna())

# Handle missing or infinite values in the exogenous variable(s)
df = df.replace([np.inf, -np.inf], np.nan).dropna()



print(df.shape)

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

model=ARIMA(train_section['data'],order=(5,1,3)).fit()
print(model.aic) 
# """5,0,1 = 232/240"""
# print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
print(model.bic)

print(model.summary())


"""making prediction"""


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


start = len(train_section) #-20
end = len(train_section)  #+40
future_prediction = model.predict(start=start, end=end, type='levels')

print("Future predictions:")
print(future_prediction)


"""
1     410.158686
2     327.980498
3     515.005297
4     475.784684
5     460.949201
6     498.086316
7     385.075262
8     365.747048
9     465.662756
10    502.258096
11    498.074620
12    491.846347
13    499.540123
14    398.212930
15    367.999681
16    475.611924
17    505.603016
18    498.226888
19    499.025170
20    523.922662
21    406.309453
22    341.204029
23    408.305154
24    497.822385
25    506.847921
26    508.172929
27    494.575482
28    416.550656
29    351.970493
30    399.110873
1    483.439014
2    515.068946
3    512.836319
4    489.664709
5    420.029657
6    361.819183
7    392.575760
8    472.398835
9    517.238112
10    518.285690
11    487.888785
12    422.745156
13    368.441190
14    389.001472
15    462.901608
16    516.684829
17    522.649134
18    488.767300
19    425.086037
20    373.205239
21    386.689462
22    455.032562
23    514.371077
24    525.943751
25    491.115851
26    427.689805
27    376.708105
28    385.015310
29    448.376554
30    511.114922
31    528.188774
"""