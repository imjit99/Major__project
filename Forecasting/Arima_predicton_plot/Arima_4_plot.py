import matplotlib.pyplot as plt
import numpy as np
<<<<<<< HEAD
=======

>>>>>>> 0b365cd3daead317d114aa298fb02b47af88497f
Dates = ['06-01', '06-02', '06-03', '06-04', '06-05', '06-06', '06-07', '06-08', '06-09', '06-10', '06-11', '06-12', '06-13', '06-14', '06-15', '06-16', '06-17', '06-18', '06-19', '06-20', '06-21', '06-22', '06-23', '06-24', '06-25', '06-26', '06-27', '06-28', '06-29', '06-30', '07-01', '07-02', '07-03', '07-04', '07-05', '07-06', '07-07', '07-08', '07-09', '07-10', '07-11', '07-12', '07-13', '07-14', '07-15', '07-16', '07-17', '07-18', '07-19', '07-20', '07-21', '07-22', '07-23', '07-24', '07-25', '07-26', '07-27', '07-28', '07-29', '07-30', '07-31']
Dates1 = ['06-01', '06-02', '06-03', '06-04', '06-05', '06-06', '06-07', '06-08', '06-09', '06-10', '06-11', '06-12', '06-13', '06-14', '06-15', '06-16', '06-17', '06-18', '06-19', '06-20', '06-21', '06-22', '06-23', '06-24', '06-25', '06-26', '06-27', '06-28', '06-29', '06-30']

ActualValue = np.array([508.70588235294116, 502.94117647058823, 410.1764705882353, 328.11764705882354, 498.1764705882353, 490.6470588235294, 495.1764705882353, 504.0, 502.29411764705884, 405.70588235294116, 327.3529411764706, 482.8235294117647, 491.7647058823529, 513.8823529411765, 508.8235294117647, 502.29411764705884, 408.1764705882353, 291.8235294117647, 462.94117647058823, 490.29411764705884, 498.11764705882354, 499.5882352941176, 509.3529411764706, 420.1764705882353, 312.1764705882353, 483.8235294117647, 489.5882352941176, 492.05882352941177, 491.4117647058824, 503.5882352941176]
)


PredictingValue = np.array([410.158686, 327.980498, 515.005297, 475.784684, 460.949201, 498.086316, 385.075262, 365.747048, 465.662756, 502.258096, 498.074620, 491.846347, 499.540123, 398.212930, 367.999681, 475.611924, 505.603016, 498.226888, 499.025170, 523.922662, 406.309453, 341.204029, 408.305154, 497.822385, 506.847921, 508.172929, 494.575482, 416.550656, 351.970493, 399.110873, 483.439014, 515.068946, 512.836319, 489.664709, 420.029657, 361.819183, 392.575760, 472.398835, 517.238112, 518.285690, 487.888785, 422.745156, 368.441190, 389.001472, 462.901608, 516.684829, 522.649134, 488.767300, 425.086037, 373.205239, 386.689462, 455.032562, 514.371077, 525.943751, 491.115851, 427.689805, 376.708105, 385.015310, 448.376554, 511.114922, 528.188774]
)

<<<<<<< HEAD
plt.plot(Dates1,ActualValue , label='Actual Value')
plt.plot(Dates,PredictingValue , label='Predicting Value')





=======
# for plotting the Actual values and the expected predictions
plt.plot(Dates1,ActualValue , label='Actual Value')
plt.plot(Dates,PredictingValue , label='Predicting Value')

>>>>>>> 0b365cd3daead317d114aa298fb02b47af88497f
plt.xlabel('Date')
plt.ylabel('Value')
plt.title('Actual vs Predicting Values (Clustering 4)')
plt.legend()
plt.xticks(rotation=60)

<<<<<<< HEAD
=======
# for vizualization
>>>>>>> 0b365cd3daead317d114aa298fb02b47af88497f
plt.show()