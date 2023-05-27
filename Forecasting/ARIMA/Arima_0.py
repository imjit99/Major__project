import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import warnings
from statsmodels.tsa.stattools import adfuller
from statsmodels.tsa.arima.model import ARIMA
import itertools
warnings.filterwarnings('ignore')
from sklearn.metrics import mean_squared_error
from sklearn.metrics import mean_absolute_error
from math import sqrt

file_path = r"C:\Users\jit24\OneDrive\Desktop\Major_project\Major__project\Forecasting\Average\0.csv"
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
# print(abs(df['new']))
adf1=adfuller(df['new'].dropna())
print('p is after:',adf1[1])
# # df['new'].plot()
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

model=ARIMA(train_section['data'],order=(5,0,3)).fit()
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

test_section['data'].mean()
rmse=sqrt(mean_squared_error(test_section['data'],FuturePrediction))
print(f"rmse score is {rmse}")
print(test_section['data'].mean())
mae = mean_absolute_error(test_section['data'], FuturePrediction)

print("MAE:", mae)

FuturePrediction.plot(legend=True,label="predicted")


start = len(train_section) #-20
end = len(train_section) # +40
future_prediction = model.predict(start=start, end=end, type='levels')

print("Future predictions:")
print(future_prediction)


"""
1     715.041011
2     701.309993
3     629.010087
4     685.117283
5     774.380911
6     710.926012
7     737.103104
8     760.149430
9     568.879572
10    543.679072
11    753.988973
12    798.244567
13    772.846143
14    772.703691
15    788.037840
16    568.029629
17    515.837776
18    701.072314
19    760.038900
20    747.181129
21    773.600771
22    781.320894
23    571.392268
24    531.527159
25    698.029590
26    783.502626
27    733.901849
28    785.705448
29    774.198386
30    591.780254
1    535.500968
2    701.553587
3    769.113258
4    726.889774
5    780.010720
6    779.139780
7    601.254285
8    546.386772
9    700.265852
10    760.017545
11    717.632506
12    776.433903
13    781.456829
14    610.956844
15    555.893762
16    700.230972
17    751.494140
18    709.543783
19    772.473126
20    783.186129
21    619.528185
22    565.076354
23    700.552242
24    744.037642
25    702.143623
26    768.521389
27    784.183324
28    627.227349
29    573.785406
30    701.248714
31    737.474190
"""