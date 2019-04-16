from bs4 import BeautifulSoup
import requests
import csv
import lxml
import time
def clean(s):
    s = str(s)
    s = s.replace("<span class=\"to-number\">","")
    s = s.replace("<span class=\"to-number-lg\">","")
    s = s.replace("<span>","")
    s = s.replace("</span>","")
    s = s.replace("<td>","")
    s = s.replace("</td>","")
    s = s.replace("<small>hrs</small>","")
    s = s.replace("<small>/stream</small>","")
    s = s.replace("<small>/hour</small>","")
    s = s.replace("<small>days</small>","")
    s = s.replace("\n","")
    return(s)
    

def main():
    file = open("streamers.txt","r") 
    with open('twitch.csv', mode='w', newline='') as csv_file:
        p_writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        p_writer.writerow(['Streamer','Hours_Streamed','Average_Viewers','Peek_Vierwers','Days_Active','Total_Games_Streamed','Daily_Broadcast_Time','Hours_Watched_Daily','Follower_Gained/stream','Views/stream','Followers_Gained/Hour','Followers_to_Date','Total_Views','Active_Days_per_Week','Average_Games/stream','Views/hour'])
      
    for streamer in file:
        streamer = clean(streamer)
         
        page = requests.get('https://twitchtracker.com/'+streamer+'/statistics')
        soup = BeautifulSoup(page.text, 'html.parser')

        x = soup.find_all('span', {'class': 'to-number'})
        z = soup.find_all('td')
        print("Scraping for : " + streamer)
        set1 = []
        set2 = []
        if(len(x)>0):
            for i in range(10):
                set1.append(clean(x[i])) #0
                
            for i in range(0,22):
                if(i%2 == 0):
                    set2.append(clean(z[i+1])) 
                    

            
            with open('twitch.csv', mode='a' , newline='') as csv_file:
                p_writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                p_writer.writerow([streamer,set1[0],set1[1],set1[2],set1[3],set1[4],set1[5],set1[6],set1[7],set1[8],set1[9],set2[0],set2[1],set2[5],set2[8],set2[9]])
            
if __name__== "__main__":
  main()

