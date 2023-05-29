import matplotlib.pyplot as plt
import numpy as np
Dates = ['06-01', '06-02', '06-03', '06-04', '06-05', '06-06', '06-07', '06-08', '06-09', '06-10', '06-11', '06-12', '06-13', '06-14', '06-15', '06-16', '06-17', '06-18', '06-19', '06-20', '06-21', '06-22', '06-23', '06-24', '06-25', '06-26', '06-27', '06-28', '06-29', '06-30', '07-01', '07-02', '07-03', '07-04', '07-05', '07-06', '07-07', '07-08', '07-09', '07-10', '07-11', '07-12', '07-13', '07-14', '07-15', '07-16', '07-17', '07-18', '07-19', '07-20', '07-21', '07-22', '07-23', '07-24', '07-25', '07-26', '07-27', '07-28', '07-29', '07-30', '07-31']
Dates1 = ['06-01', '06-02', '06-03', '06-04', '06-05', '06-06', '06-07', '06-08', '06-09', '06-10', '06-11', '06-12', '06-13', '06-14', '06-15', '06-16', '06-17', '06-18', '06-19', '06-20', '06-21', '06-22', '06-23', '06-24', '06-25', '06-26', '06-27', '06-28', '06-29', '06-30']

ActualValue = np.array([1067.375, 1017.25, 898.25, 753.25, 1060.5, 1064.875, 1069.25, 1074.375, 1049.125, 900.75, 783.625, 1051.875, 1032.0, 1025.25, 1050.5, 1079.625, 883.625, 762.125, 1017.5, 1051.875, 1065.875, 1033.0, 1046.625, 902.375, 777.75, 1027.625, 983.125, 1010.625, 1016.25, 1040.625]
)


PredictingValue = np.array([1055.695821, 986.09729, 986.011886, 906.163456, 1023.966259, 1000.847212, 1027.613774, 1073.883781, 831.447956, 829.795782, 1002.200195, 1086.685099, 1071.467506, 1096.541091, 1102.019334, 826.592787, 797.74732, 985.766969, 1065.679714, 1005.40057, 1045.643256, 1104.54674, 875.662947, 828.91358, 958.310443, 1080.885238, 1019.988341, 1095.888161, 1079.042456, 906.061239, 810.382343, 974.877268, 1042.932701, 1032.888345, 1092.845657, 1098.282375, 897.899228, 828.184423, 960.250715, 1032.346496, 1021.732948, 1109.255266, 1098.249004, 907.394891, 832.698424, 958.09702, 1010.997379, 1020.159011, 1115.452105, 1104.994043, 911.546062, 843.955303, 950.830036, 994.608877, 1014.443678, 1123.443939, 1107.938927, 919.549543, 853.660449, 945.770013, 976.988635]
)

# for plotting the Actual values and the expected predictions

plt.plot(Dates1,ActualValue , label='Actual Value')
plt.plot(Dates,PredictingValue , label='Predicting Value')

plt.xlabel('Date')
plt.ylabel('Value')
plt.title('Actual vs Predicting Values (Clustering 3)')
plt.legend()
plt.xticks(rotation=60)

# for vizualization
plt.show()