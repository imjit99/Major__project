import matplotlib.pyplot as plt
import numpy as np
Dates = ['06-01', '06-02', '06-03', '06-04', '06-05', '06-06', '06-07', '06-08', '06-09', '06-10', '06-11', '06-12', '06-13', '06-14', '06-15', '06-16', '06-17', '06-18', '06-19', '06-20', '06-21', '06-22', '06-23', '06-24', '06-25', '06-26', '06-27', '06-28', '06-29', '06-30', '07-01', '07-02', '07-03', '07-04', '07-05', '07-06', '07-07', '07-08', '07-09', '07-10', '07-11', '07-12', '07-13', '07-14', '07-15', '07-16', '07-17', '07-18', '07-19', '07-20', '07-21', '07-22', '07-23', '07-24', '07-25', '07-26', '07-27', '07-28', '07-29', '07-30', '07-31']
Dates1 = ['06-01', '06-02', '06-03', '06-04', '06-05', '06-06', '06-07', '06-08', '06-09', '06-10', '06-11', '06-12', '06-13', '06-14', '06-15', '06-16', '06-17', '06-18', '06-19', '06-20', '06-21', '06-22', '06-23', '06-24', '06-25', '06-26', '06-27', '06-28', '06-29', '06-30']

ActualValue = np.array([300.625, 298.125, 226.0, 192.5, 321.375, 314.375, 316.125, 331.125, 311.875, 221.25, 199.375, 317.5, 306.375, 322.0, 329.125, 323.75, 219.75, 181.375, 286.75, 308.5, 315.625, 316.625, 319.375, 227.0, 184.375, 305.0, 312.875, 300.75, 298.125, 310.125]
)


PredictingValue = np.array([300.516381, 298.042123, 236.004417, 221.603622, 321.425464, 294.695983, 317.056823, 296.624936, 213.917848, 217.3335, 291.027415, 302.675897, 307.826992, 337.676033, 319.873407, 226.357511, 219.464755, 292.828266, 313.439784, 309.026196, 340.134748, 330.120004, 238.002426, 203.98906, 252.849938, 296.342631, 317.719122, 345.666245, 328.637626, 256.30012, 214.511034, 238.659014, 279.485923, 316.061086, 346.186282, 332.66006, 271.507152, 224.979295, 229.87547, 265.075366, 309.189849, 344.380737, 337.51913, 285.6319, 235.656439, 225.560532, 252.729224, 299.413909, 340.072324, 341.72684, 298.716914, 246.998751, 224.858361, 242.566373, 288.120607, 333.455025, 344.359212, 310.575904, 259.011781, 227.233618, 234.738352]
)

plt.plot(Dates1,ActualValue , label='Actual Value')
plt.plot(Dates,PredictingValue , label='Predicting Value')





plt.xlabel('Date')
plt.ylabel('Value')
plt.title('Actual vs Predicting Values (Clustering 2)')
plt.legend()
plt.xticks(rotation=60)

plt.show()