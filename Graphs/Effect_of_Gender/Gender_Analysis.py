import numpy as np
import pandas as pd
import math

#Reading in our Twitch Data
datat=pd.read_csv('../../ScrapedTwitch/twitch.csv')
#Converting it to a DataFrame
datat = pd.DataFrame(data=datat)
#Creating new variables to store the Avg number followers by Category
avgf=datat.Followers_to_Date[(datat['Category']=='female')].mean()
avgm=datat.Followers_to_Date[(datat['Category']=='male')].mean()
avgc=datat.Followers_to_Date[(datat['Category']=='corporation')].mean()
avgg=datat.Followers_to_Date[(datat['Category']=='group')].mean()
#Creating a new table to hold the Avg follower by category values
avg = {'Category': ['male','female','corporation','group'], 'Avg_Followers': [avgm,avgf,avgg,avgc]}
#Converting it to a dataframe
avgfoll = pd.DataFrame(data=avg)

#plotting avg_followers data - bar
%matplotlib inline
import matplotlib.pyplot as plt
plt.style.use('seaborn-dark')
plt.figure()
plt.bar(avgfoll.Category,avgfoll.Avg_Followers, color=['steelblue','darkorange','forestgreen','indianred'])
plt.xlabel('Category')
plt.ylabel('Average Number of Followers')
plt.title('Effect of Type of Streamer on Number of Followers')
#overlaying the actual values on top
plt.text(-0.25,653000,'651,445')
plt.text(.75,535000,'534,739')
plt.text(1.75,440000,'438,587')
plt.text(2.75,660000,'658,479')
plt.show()

#plotting num_followers data - scatte
%matplotlib inline
import matplotlib.pyplot as plt
import seaborn as sns
plt.style.use('seaborn-dark')
sns.lmplot( x="Streamer", y="Followers_to_Date", data=datat, fit_reg=False, hue='Category', legend=False)
plt.legend(loc='upper right')
plt.tick_params(axis='x', which='both', bottom=True, top=True, labelbottom=False)
plt.ylabel('Number of Followers to Date')
plt.ticklabel_format(style='plain',axis='y')
plt.title('Effect of Type of Streamer on Number of Followers')
plt.show()
