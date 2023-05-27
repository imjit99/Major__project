# from Average import *
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import warnings
from statsmodels.tsa.stattools import adfuller
from statsmodels.tsa.arima.model import ARIMA
import itertools

warnings.filterwarnings('ignore')

file_path = r"C:\Users\jit24\OneDrive\Desktop\Major_project\Major__project\Forecasting\Average\1.csv"
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

model=ARIMA(train_section['data'],order=(5,1,2)).fit()
print(model.aic) 

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


start = len(train_section) # -20
end = len(train_section)   # +40
future_prediction = model.predict(start=start, end=end, type='levels')

print("Future predictions:")
print(future_prediction)





"""
1     1503.216005
2     1426.370491
3     1223.899143
4     1187.292336
5     1506.820279
6     1400.588799
7     1560.695268
8     1591.782699
9     1051.461778
10    1017.133263
11    1394.082753
12    1569.296628
13    1507.525972
14    1605.498803
15    1530.202349
16    1010.858147
17    1017.837581
18    1342.530495
19    1495.151986
20    1434.552886
21    1516.693553
22    1528.634853
23    1047.008344
24     925.521659
25    1320.979490
26    1439.307071
27    1352.186238
28    1565.513155
29    1539.229062
30    1056.906200
1     951.787585
2    1306.165137
3    1373.767199
4    1344.304097
5    1600.255671
6    1550.811690
7    1068.947227
8     987.046188
9    1286.357874
10    1313.029151
11    1334.496120
12    1629.054474
13    1556.283228
14    1088.894671
15    1024.919810
16    1266.864830
17    1254.341084
18    1325.889045
19    1648.737551
20    1558.420423
21    1113.954702
22    1066.223044
23    1246.868146
24    1200.060171
25    1317.141474
26    1660.173559
27    1556.746343
28    1144.010110
29    1109.403497
30    1227.585308
31    1150.647556
"""