import numpy as np
import pandas as pd
import math

# tf = '1_results.csv'

# pf = pd.read_csv(tf, sep=",")
tf=pd.read_csv('../../scrapedchat/1_results.csv')
#Converting it to a DataFrame
pf = pd.DataFrame(data=tf)
pt = pd.DataFrame()
pt = pf[::-1]
pt.head(5)
pt['percent_postive'].astype(float)

%matplotlib inline
import matplotlib.pyplot as plt
plt.style.use('seaborn-dark')
plt.figure()
# 
plt.scatter(pt['rank'] ,pt['percent_postive'])
plt.ticklabel_format(style='plain',axis='y')
plt.title("Chat Sentiment By Streamers Follower Rank")
plt.ylim([0,100])

plt.ylabel("Percent Positive")
plt.xlabel("Streamers Follower Rank")