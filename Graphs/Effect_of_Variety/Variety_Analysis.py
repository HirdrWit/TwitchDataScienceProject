import numpy as np
import pandas as pd
import math

#Reading in our Twitch Data
datat=pd.read_csv('../../ScrapedTwitch/twitch.csv')
#Converting it to a DataFrame
datat = pd.DataFrame(data=datat)

#plotting total games streamed
%matplotlib inline
import matplotlib.pyplot as plt
plt.style.use('seaborn')
plt.figure()
plt.scatter(datat.Total_Games_Streamed,datat.Followers_to_Date)
plt.ticklabel_format(style='plain',axis='y')
plt.xlabel('Total Games Streamed')
plt.ylabel('Number of Followers to Date')
plt.title('Effect of Game Variety on Number of Followers')
plt.show()

#plotting Average Number of Games played per Stream
%matplotlib inline
import matplotlib.pyplot as plt
plt.style.use('seaborn')
plt.figure()
plt.scatter(datat['Average_Games/stream'],datat.Followers_to_Date)
plt.ticklabel_format(style='plain',axis='y')
plt.xlabel('Average Games Played per Stream')
plt.ylabel('Number of Followers to Date')
plt.title('Effect of Game Variety on Number of Followers')
plt.show()
