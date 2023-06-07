from matplotlib import pyplot as plt
from Constant.constant import *

""" According to the elbow method for difining the number of the clusters(k) = 6 (soft DTW) 
Sillouhette score = 0.720
"""


""".............cluster 0 .........."""

"""
data_02 = [x / max(data_02) for x in data_02]
data_14 = [x / max(data_14) for x in data_14]
data_16 = [x / max(data_16) for x in data_16]
data_18 = [x / max(data_18) for x in data_18]
data_30 = [x / max(data_30) for x in data_30]
data_31 = [x / max(data_31) for x in data_31]
data_38 = [x / max(data_38) for x in data_38]
data_45 = [x / max(data_45) for x in data_45]
data_47 = [x / max(data_47) for x in data_47]
data_49 = [x / max(data_49) for x in data_49]


avg_data = [sum(data)/len(data) for data in zip(data_02, data_14, data_16, data_18, data_30, data_31, data_38, data_45 ,data_47 , data_49)]
avg_data = [x / max(avg_data) for x in avg_data]


plt.plot(days, data_02, label='02')
plt.plot(days, data_14, label='14')
plt.plot(days, data_16, label='16')
plt.plot(days, data_18, label='18')
plt.plot(days, data_30, label='30')
plt.plot(days, data_31, label='31')
plt.plot(days, data_38, label='38')
plt.plot(days, data_45, label='45')
plt.plot(days, data_47, label='47')
plt.plot(days, data_49, label='49')

plt.plot(days, avg_data, color='black', label='avg_data')
plt.ylim(0,1)
plt.legend()
plt.show()

"""

""".............cluster 1 .........."""
"""
data_15 = [x / max(data_15) for x in data_15]
data_49 = [x / max(data_50) for x in data_50]

avg_data = [sum(data)/len(data) for data in zip(data_15, data_50)]
avg_data = [x / max(avg_data) for x in avg_data]

plt.plot(days, data_15, label='15')
plt.plot(days, data_50, label='50')

plt.plot(days, avg_data, color='black', label='avg_data')
plt.ylim(0,1)
plt.legend()
plt.show()

"""


""".............cluster 2 .........."""
"""
data_01 = [x / max(data_01) for x in data_01]
data_09 = [x / max(data_09) for x in data_09]
data_23 = [x / max(data_23) for x in data_23]
data_27 = [x / max(data_27) for x in data_27]
data_29 = [x / max(data_29) for x in data_29]
data_39 = [x / max(data_39) for x in data_39]
data_41 = [x / max(data_41) for x in data_41]
data_48 = [x / max(data_48) for x in data_48]

avg_data = [sum(data)/len(data) for data in zip(data_01, data_09, data_23, data_27, data_29, data_39, data_41, data_48)]
avg_data = [x / max(avg_data) for x in avg_data]

plt.plot(days, data_01, label='01')
plt.plot(days, data_09, label='09')
plt.plot(days, data_23, label='23')
plt.plot(days, data_27, label='27')
plt.plot(days, data_29, label='29')
plt.plot(days, data_39, label='39')
plt.plot(days, data_41, label='41')
plt.plot(days, data_48, label='48')

plt.plot(days, avg_data, color='black', label='avg_data')
plt.ylim(0,1)
plt.legend()
plt.show()
"""

""".............cluster 3 .........."""
"""
data_06 = [x / max(data_06) for x in data_06]
data_10 = [x / max(data_10) for x in data_10]
data_17 = [x / max(data_17) for x in data_17]
data_20 = [x / max(data_20) for x in data_20]
data_21 = [x / max(data_21) for x in data_21]
data_28 = [x / max(data_28) for x in data_28]
data_33 = [x / max(data_33) for x in data_33]
data_35 = [x / max(data_35) for x in data_35]

avg_data = [sum(data)/len(data) for data in zip(data_06, data_10, data_17, data_20, data_21, data_28, data_33, data_35)]
avg_data = [x / max(avg_data) for x in avg_data]

plt.plot(days, data_06, label='06')
plt.plot(days, data_10, label='10')
plt.plot(days, data_17, label='17')
plt.plot(days, data_20, label='20')
plt.plot(days, data_21, label='21')
plt.plot(days, data_28, label='28')
plt.plot(days, data_33, label='33')
plt.plot(days, data_35, label='35')

plt.plot(days, avg_data, color='black', label='avg_data')
plt.ylim(0,1)
plt.legend()
plt.show()

"""

""".............cluster 4 .........."""
"""
data_04 = [x / max(data_04) for x in data_04]
data_05 = [x / max(data_05) for x in data_05]
data_07 = [x / max(data_07) for x in data_07]
data_08 = [x / max(data_08) for x in data_08]
data_11 = [x / max(data_11) for x in data_11]
data_12 = [x / max(data_12) for x in data_12]
data_13 = [x / max(data_13) for x in data_13]
data_22 = [x / max(data_22) for x in data_22]
data_25 = [x / max(data_25) for x in data_25]
data_32 = [x / max(data_32) for x in data_32]
data_34 = [x / max(data_34) for x in data_34]
data_36 = [x / max(data_36) for x in data_36]
data_37 = [x / max(data_37) for x in data_37]
data_40 = [x / max(data_40) for x in data_40]
data_42 = [x / max(data_42) for x in data_42]
data_43 = [x / max(data_43) for x in data_43]
data_46 = [x / max(data_46) for x in data_46]

avg_data = [sum(data)/len(data) for data in zip(data_04, data_05, data_07, data_08, data_11, data_12, data_13, data_22, data_25, data_32, data_34, data_36, data_37, data_40, data_42, data_43, data_46)]
avg_data = [x / max(avg_data) for x in avg_data]

plt.plot(days, data_04, label='04')
plt.plot(days, data_05, label='05')
plt.plot(days, data_07, label='07')
plt.plot(days, data_08, label='08')
plt.plot(days, data_11, label='11')
plt.plot(days, data_12, label='12')
plt.plot(days, data_13, label='13')
plt.plot(days, data_22, label='22')
plt.plot(days, data_25, label='25')
plt.plot(days, data_32, label='32')
plt.plot(days, data_34, label='34')
plt.plot(days, data_36, label='36')
plt.plot(days, data_37, label='37')
plt.plot(days, data_40, label='40')
plt.plot(days, data_42, label='42')
plt.plot(days, data_43, label='43')
plt.plot(days, data_46, label='46')

plt.plot(days, avg_data, color='black', label='avg_data')
plt.ylim(0,1)
plt.legend()
plt.show()
"""

""".............cluster 5 .........."""
"""
data_00 = [x / max(data_00) for x in data_00]
data_03 = [x / max(data_03) for x in data_03]
data_19 = [x / max(data_19) for x in data_19]
data_24 = [x / max(data_24) for x in data_24]
data_26 = [x / max(data_26 )for x in data_26]
data_44 = [x / max(data_44) for x in data_44]

avg_data = [sum(data)/len(data) for data in zip(data_00, data_03, data_19, data_24, data_26, data_44)]
avg_data = [x / max(avg_data) for x in avg_data]

plt.plot(days, data_00, label='00')
plt.plot(days, data_03, label='03')
plt.plot(days, data_19, label='19')
plt.plot(days, data_24, label='24')
plt.plot(days, data_26, label='26')
plt.plot(days, data_44, label='44')

plt.plot(days, avg_data, color='black', label='avg_data')
plt.ylim(0,1)
plt.legend()
plt.show()

"""

"""<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>"""

""" According to the elbow method for difining the number of the clusters(k) = 6 (DTW) 
Sillouhette score = 0.727
"""
""".............cluster 0 .........."""
"""
data_02 = [x / max(data_02) for x in data_02]
data_16 = [x / max(data_16) for x in data_16]
data_18 = [x / max(data_18) for x in data_18]
data_38 = [x / max(data_38) for x in data_38]
data_45 = [x / max(data_45) for x in data_45]
data_47 = [x / max(data_47) for x in data_47]
data_49 = [x / max(data_49) for x in data_49]

avg_data = [sum(data)/len(data) for data in zip(data_02, data_16, data_18, data_38, data_45 ,data_47 , data_49)]
avg_data = [x / max(avg_data) for x in avg_data]


plt.plot(days, data_02, label='02')
plt.plot(days, data_16, label='16')
plt.plot(days, data_18, label='18')
plt.plot(days, data_38, label='38')
plt.plot(days, data_45, label='45')
plt.plot(days, data_47, label='47')
plt.plot(days, data_49, label='49')

plt.plot(days, avg_data, color='black', label='avg_data')
plt.ylim(0,1)
plt.legend()
plt.show()

"""


""".............cluster 1 .........."""
"""
data_01 = [x / max(data_01) for x in data_01]
data_09 = [x / max(data_09) for x in data_09]
data_23 = [x / max(data_23) for x in data_23]
data_27 = [x / max(data_27) for x in data_27]
data_29 = [x / max(data_29) for x in data_29]
data_39 = [x / max(data_39) for x in data_39]
data_41 = [x / max(data_41) for x in data_41]
data_48 = [x / max(data_48) for x in data_48]

avg_data = [sum(data)/len(data) for data in zip(data_01, data_09, data_23, data_27, data_29, data_39, data_41, data_48)]
avg_data = [x / max(avg_data) for x in avg_data]

plt.plot(days, data_01, label='01')
plt.plot(days, data_09, label='09')
plt.plot(days, data_23, label='23')
plt.plot(days, data_27, label='27')
plt.plot(days, data_29, label='29')
plt.plot(days, data_39, label='39')
plt.plot(days, data_41, label='41')
plt.plot(days, data_48, label='48')

plt.plot(days, avg_data, color='black', label='avg_data')
plt.ylim(0,1)
plt.legend()
plt.show()
"""

""".............cluster 2 .........."""
"""
data_06 = [x / max(data_06) for x in data_06]
data_10 = [x / max(data_10) for x in data_10]
data_17 = [x / max(data_17) for x in data_17]
data_20 = [x / max(data_20) for x in data_20]
data_21 = [x / max(data_21) for x in data_21]
data_28 = [x / max(data_28) for x in data_28]
data_33 = [x / max(data_33) for x in data_33]
data_35 = [x / max(data_35) for x in data_35]

avg_data = [sum(data)/len(data) for data in zip(data_06, data_10, data_17, data_20, data_21, data_28, data_33, data_35)]
avg_data = [x / max(avg_data) for x in avg_data]

plt.plot(days, data_06, label='06')
plt.plot(days, data_10, label='10')
plt.plot(days, data_17, label='17')
plt.plot(days, data_20, label='20')
plt.plot(days, data_21, label='21')
plt.plot(days, data_28, label='28')
plt.plot(days, data_33, label='33')
plt.plot(days, data_35, label='35')

plt.plot(days, avg_data, color='black', label='avg_data')
plt.ylim(0,1)
plt.legend()
plt.show()

"""

""".............cluster 3 .........."""
"""
data_15 = [x / max(data_15) for x in data_15]
data_49 = [x / max(data_50) for x in data_50]

avg_data = [sum(data)/len(data) for data in zip(data_15, data_50)]
avg_data = [x / max(avg_data) for x in avg_data]

plt.plot(days, data_15, label='15')
plt.plot(days, data_50, label='50')

plt.plot(days, avg_data, color='black', label='avg_data')
plt.ylim(0,1)
plt.legend()
plt.show()

"""


""".............cluster 4 .........."""
"""
data_04 = [x / max(data_04) for x in data_04]
data_05 = [x / max(data_05) for x in data_05]
data_07 = [x / max(data_07) for x in data_07]
data_08 = [x / max(data_08) for x in data_08]
data_11 = [x / max(data_11) for x in data_11]
data_12 = [x / max(data_12) for x in data_12]
data_13 = [x / max(data_13) for x in data_13]
data_22 = [x / max(data_22) for x in data_22]
data_25 = [x / max(data_25) for x in data_25]
data_32 = [x / max(data_32) for x in data_32]
data_34 = [x / max(data_34) for x in data_34]
data_36 = [x / max(data_36) for x in data_36]
data_37 = [x / max(data_37) for x in data_37]
data_40 = [x / max(data_40) for x in data_40]
data_42 = [x / max(data_42) for x in data_42]
data_43 = [x / max(data_43) for x in data_43]
data_46 = [x / max(data_46) for x in data_46]

avg_data = [sum(data)/len(data) for data in zip(data_04, data_05, data_07, data_08, data_11, data_12, data_13, data_22, data_25, data_32, data_34, data_36, data_37, data_40, data_42, data_43, data_46)]
avg_data = [x / max(avg_data) for x in avg_data]

plt.plot(days, data_04, label='04')
plt.plot(days, data_05, label='05')
plt.plot(days, data_07, label='07')
plt.plot(days, data_08, label='08')
plt.plot(days, data_11, label='11')
plt.plot(days, data_12, label='12')
plt.plot(days, data_13, label='13')
plt.plot(days, data_22, label='22')
plt.plot(days, data_25, label='25')
plt.plot(days, data_32, label='32')
plt.plot(days, data_34, label='34')
plt.plot(days, data_36, label='36')
plt.plot(days, data_37, label='37')
plt.plot(days, data_40, label='40')
plt.plot(days, data_42, label='42')
plt.plot(days, data_43, label='43')
plt.plot(days, data_46, label='46')

plt.plot(days, avg_data, color='black', label='avg_data')
plt.ylim(0,1)
plt.legend()
plt.show()
"""

""".............cluster 5 .........."""
"""
data_00 = [x / max(data_00) for x in data_00]
data_03 = [x / max(data_03) for x in data_03]
data_14 = [x / max(data_14) for x in data_14]
data_19 = [x / max(data_19) for x in data_19]
data_24 = [x / max(data_24) for x in data_24]
data_26 = [x / max(data_26 )for x in data_26]
data_30 = [x / max(data_30 )for x in data_30]
data_31 = [x / max(data_31 )for x in data_31]
data_44 = [x / max(data_44) for x in data_44]

avg_data = [sum(data)/len(data) for data in zip(data_00, data_03, data_14, data_19, data_24, data_26, data_30, data_31, data_44)]
avg_data = [x / max(avg_data) for x in avg_data]

plt.plot(days, data_00, label='00')
plt.plot(days, data_03, label='03')
plt.plot(days, data_14, label='14')
plt.plot(days, data_19, label='19')
plt.plot(days, data_24, label='24')
plt.plot(days, data_26, label='26')
plt.plot(days, data_30, label='30')
plt.plot(days, data_31, label='31')
plt.plot(days, data_44, label='44')

plt.plot(days, avg_data, color='black', label='avg_data')
plt.ylim(0,1)
plt.legend()
plt.show()

"""