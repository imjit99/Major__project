import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("dataset_Container/Bus_records03.csv")

""" Here, You can also change the dates according to you, date should be in the range of '2017-06-01' to '2017-06-30' """

df=df[df['RecordedAtTime'].str.split(' ').apply(lambda x:x[0]=='2017-06-16')]
df['RecordedAtTime']=pd.to_datetime(df['RecordedAtTime'],format='%Y-%m-%d %H:%M:%S')

"""for classifying into specific datetimes with the format of ( %H:%M:%S )"""

# #df['RecordedAtTime']=pd.to_datetime(df['RecordedAtTime'],format='%Y-%m-%d %H:%M:%S')
df=df.drop_duplicates()  # duplicate values will be dropped

"""creating three columns in the name of hour,minute and seconds"""

df['hour']=df['RecordedAtTime'].apply(lambda x: x.hour+1)
df['minutes']=df['RecordedAtTime'].apply(lambda x: x.minute)
df['seconds']=df['RecordedAtTime'].apply(lambda x: x.second)
print("length",len(df))

"""for calculating the movement for the whole day"""
# All_day_movement = [(df['hour'].value_counts()[1]),(df['hour'].value_counts()[2]),(df['hour'].value_counts()[3]),(df['hour'].value_counts()[4]),(df['hour'].value_counts()[5]),(df['hour'].value_counts()[6]),(df['hour'].value_counts()[7]),(df['hour'].value_counts()[8]),(df['hour'].value_counts()[9]),(df['hour'].value_counts()[10]),
# (df['hour'].value_counts()[11]),(df['hour'].value_counts()[12]),(df['hour'].value_counts()[13]),(df['hour'].value_counts()[14]),(df['hour'].value_counts()[15]),(df['hour'].value_counts()[16]),(df['hour'].value_counts()[17]),(df['hour'].value_counts()[18]),(df['hour'].value_counts()[19]),(df['hour'].value_counts()[20]),
# (df['hour'].value_counts()[21]),(df['hour'].value_counts()[22]),(df['hour'].value_counts()[23]),(df['hour'].value_counts()[24])]

# print("The movement of buses for the whole day is",sum(All_day_movement))


"""
day,data
2017-06-01,722
2017-06-02,705
2017-06-03,579
2017-06-04,589
2017-06-05,736
2017-06-06,746
2017-06-07,726
2017-06-08,730
2017-06-09,736
2017-06-10,558
2017-06-11,578
2017-06-12,727
2017-06-13,704
2017-06-14,705
2017-06-15,771
2017-06-16,758
2017-06-17,510
2017-06-18,566
2017-06-19,707
2017-06-20,744
2017-06-21,695
2017-06-22,731
2017-06-23,763
2017-06-24,576
2017-06-25,629
2017-06-26,713
2017-06-27,758
2017-06-28,696
2017-06-29,692
2017-06-30,729
"""