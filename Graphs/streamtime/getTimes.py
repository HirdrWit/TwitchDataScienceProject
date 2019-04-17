#### get hours streamed, daily broadcast time, active days per week
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 

data = pd.read_csv('../../ScrapedTwitch/twitch.csv')

totHrs = data.Hours_Streamed
totDays = data.Days_Active
dailyHrs = data.Daily_Broadcast_Time
dpw = data.Active_Days_per_Week
followers = data.Followers_to_Date

plt.scatter(dpw,followers)
plt.ticklabel_format(style='plain',axis='y')
plt.title("Effect of Active Days per Week")
plt.xlabel("Active Days")
plt.ylabel("Followers")

plt.scatter(totHrs,followers)
plt.ticklabel_format(style='plain',axis='y')
plt.title("Effect of Total Hours Streamed")
plt.xlabel("Total Hours")
plt.ylabel("Followers")

plt.scatter(dailyHrs,followers)
plt.ticklabel_format(style='plain',axis='y')
plt.title("Effect of Hours Active per Day")
plt.xlabel("Daily Hours")
plt.ylabel("Followers")

plt.scatter(totDays,followers)
plt.ticklabel_format(style='plain',axis='y')
plt.title("Effect of Total Days Streamed")
plt.xlabel("Total Days")
plt.ylabel("Followers")

plt.scatter(dpw,totHrs,s=followers*.00001,c=(0,0,1))
plt.title("Active Days and Total Hours vs Followers")
plt.xlabel("Active Days")
plt.ylabel("Total Hours")

plt.scatter(dpw,dailyHrs,s=followers*.00001,c=(0,0,1))
plt.title("Active Days and Daily Hours vs Followers")
plt.xlabel("Active Days")
plt.ylabel("Daily Hours")