# from Average import *
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import warnings
from statsmodels.tsa.stattools import adfuller
from statsmodels.tsa.arima.model import ARIMA
import itertools


warnings.filterwarnings('ignore')

"""enter your file path"""
file_path = r"C:\Users\jit24\OneDrive\Desktop\Major_project\Major__project\Forecasting\Average\3.csv"

df=pd.read_csv(file_path)
df.set_index('date',inplace=True)
print(df.head())

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



# Perform differencing to make the series stationary

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

""" for all combinations of (p,d,q) with the AIC and BIC values """
# print(AiC)
# print(BiC)

Best_aic_combination = min(AiC, key=lambda x: AiC[x])
min_aic_value = AiC[Best_aic_combination]

print(f"Minimum AIC: {min_aic_value}, Combination with Minimum AIC: {Best_aic_combination}")

Best_bic_combination = min(BiC, key= lambda y: BiC[y])
min_bic_value = BiC[Best_bic_combination]
print(f"Minimum AIC: {min_bic_value}, Combination with Minimum BIC: {Best_bic_combination}")


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


""" in start first 21 values i.e. 70% comes under the train_section and remaining 9 (30%) comes under test_section
To predict the vaalues for the next month i.e. July, we need to add 40 in the 'len(train_section)'. Similarly if we subtract 20 from the 'len(train_section)' it will show us from the previous 21 days."""
start = len(train_section) # -20
end = len(train_section)   +40
future_prediction = model.predict(start=start, end=end, type='levels')

print("Future predictions:")
print(future_prediction)


"""
These are the predictions we got afterwards  
1     1055.695821
2      986.097290
3      986.011886
4      906.163456
5     1023.966259
6     1000.847212
7     1027.613774
8     1073.883781
9      831.447956
10     829.795782
11    1002.200195
12    1086.685099
13    1071.467506
14    1096.541091
15    1102.019334
16     826.592787
17     797.747320
18     985.766969
19    1065.679714
20    1005.400570
21    1045.643256
22    1104.546740
23     875.662947
24     828.913580
25     958.310443
26    1080.885238
27    1019.988341
28    1095.888161
29    1079.042456
30     906.061239
1     810.382343
2     974.877268
3    1042.932701
4    1032.888345
5    1092.845657
6    1098.282375
7     897.899228
8     828.184423
9     960.250715
10    1032.346496
11    1021.732948
12    1109.255266
13    1098.249004
14     907.394891
15     832.698424
16     958.097020
17    1010.997379
18    1020.159011
19    1115.452105
20    1104.994043
21     911.546062
22     843.955303
23     950.830036
24     994.608877
25    1014.443678
26    1123.443939
27    1107.938927
28     919.549543
29     853.660449
30     945.770013
31     976.988635
"""