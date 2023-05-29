import matplotlib.pyplot as plt
import numpy as np
Dates = ['06-01', '06-02', '06-03', '06-04', '06-05', '06-06', '06-07', '06-08', '06-09', '06-10', '06-11', '06-12', '06-13', '06-14', '06-15', '06-16', '06-17', '06-18', '06-19', '06-20', '06-21', '06-22', '06-23', '06-24', '06-25', '06-26', '06-27', '06-28', '06-29', '06-30', '07-01', '07-02', '07-03', '07-04', '07-05', '07-06', '07-07', '07-08', '07-09', '07-10', '07-11', '07-12', '07-13', '07-14', '07-15', '07-16', '07-17', '07-18', '07-19', '07-20', '07-21', '07-22', '07-23', '07-24', '07-25', '07-26', '07-27', '07-28', '07-29', '07-30', '07-31']
Dates1 = ['06-01', '06-02', '06-03', '06-04', '06-05', '06-06', '06-07', '06-08', '06-09', '06-10', '06-11', '06-12', '06-13', '06-14', '06-15', '06-16', '06-17', '06-18', '06-19', '06-20', '06-21', '06-22', '06-23', '06-24', '06-25', '06-26', '06-27', '06-28', '06-29', '06-30']

ActualValue = np.array([1520.0, 1508.5, 1111.5, 921.5, 1505.5, 1583.0, 1519.5, 1574.5, 1506.0, 1117.0, 967.0, 1470.0, 1472.0, 1501.0, 1535.5, 1467.5, 1127.0, 893.0, 1344.0, 1496.5, 1368.5, 1558.0, 1511.0, 1119.0, 993.0, 1492.5, 1440.5, 1422.5, 1430.5, 1463.0]
)


PredictingValue = np.array([1503.216005, 1426.370491, 1223.899143, 1187.292336, 1506.820279, 1400.588799, 1560.695268, 1591.782699, 1051.461778, 1017.133263, 1394.082753, 1569.296628, 1507.525972, 1605.498803, 1530.202349, 1010.858147, 1017.837581, 1342.530495, 1495.151986, 1434.552886, 1516.693553, 1528.634853, 1047.008344, 925.521659, 1320.97949, 1439.307071, 1352.186238, 1565.513155, 1539.229062, 1056.9062, 951.787585, 1306.165137, 1373.767199, 1344.304097, 1600.255671, 1550.81169, 1068.947227, 987.046188, 1286.357874, 1313.029151, 1334.49612, 1629.054474, 1556.283228, 1088.894671, 1024.91981, 1266.86483, 1254.341084, 1325.889045, 1648.737551, 1558.420423, 1113.954702, 1066.223044, 1246.868146, 1200.060171, 1317.141474, 1660.173559, 1556.746343, 1144.01011, 1109.403497, 1227.585308, 1150.647556]
)

plt.plot(Dates1,ActualValue , label='Actual Value')
plt.plot(Dates,PredictingValue , label='Predicting Value')





plt.xlabel('Date')
plt.ylabel('Value')
plt.title('Actual vs Predicting Values (Clustering 1)')
plt.legend()
plt.xticks(rotation=60)

plt.show()