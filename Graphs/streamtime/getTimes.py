#### get hours streamed, daily broadcast time, active days per week
import pandas as pd 
from mpl_toolkits import mplot3d
import numpy as np 
import matplotlib.pyplot as plt 

data = pd.read_csv('twitch.csv')

# print(data.columns)

totHrs = data.Hours_Streamed
dailyHrs = data.Daily_Broadcast_Time
dpw = data.Active_Days_per_Week

# print(totHrs[:5])
# print(dailyHrs[:5])
# print(dpw[:5])
# print(totHrs[0])

fig = plt.figure()
ax = plt.axes(projection='3d')
fig.show()