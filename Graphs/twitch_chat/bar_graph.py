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
# plt.bar(pt['streamer'] ,pt['percent_postive'])
p1 = plt.bar(pt['streamer'], pt['percent_postive'],color = 'forestgreen' , label = 'Positive')
p2 = plt.bar(pt['streamer'], 100 - pt['percent_postive'], bottom = pt['percent_postive'], color = 'indianred', label = 'Negative')
plt.xticks(rotation=90)
plt.ylim([0,100])
plt.ylabel("Percent")
plt.xlabel("Streamers \n (low sub count -> high sub count)")
plt.legend(bbox_to_anchor=(1.04,1), borderaxespad=0)
plt.title("Chat Sentiment By Streamer")
plt.show()