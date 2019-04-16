# coding: cp1251 (only for russian keybord. if you from another country check your text encoding)
import socket, string, random, threading
from time import gmtime, strftime
 
#for connecting to twitch
HOST = "irc.twitch.tv"
NICK = "bob"
PORT = 6667
PASS = "oauth:j385auroytv80lxdsthdqnnta42xey"
 
#we need this
readbuffer = ""
MODT = False
mood = 0
 
#smiles
angry = " >( "
bigsmile = " :D "  
bored = " :z "
confused = " o_O "
cool = "  B)  "
heart = " <3 "
sad = " :( "
smile = " :) "
tongue = " :P "
surprised = " :o "
undecided = " :\ "
wink = " ;p "
winking =" ;) "
 
#connecting to twitch
s = socket.socket()
s.connect((HOST, PORT))
s.send("PASS " + PASS + "\r\n")
s.send("NICK " + NICK + "\r\n")
s.send("JOIN #ninja\r\n")
 
#sending message
def Send_message(message):
    s.send("PRIVMSG #YOURNICK :" + message + "\r\n")
 
# set timer (only once)
def time():
    Send_message("Commands: !time, etc")
 
#timer
t = threading.Timer(10.0, time)
t.start()    

while True:
    readbuffer = readbuffer + s.recv(1024)
    temp = string.split(readbuffer, "\n")
    readbuffer = temp.pop()
  
    for line in temp:
        #checks whether the message is PING because Twitch checks you (afk or not)
        if (line[0] == "PING"):
            s.send("PONG %s\r\n" % line[1])
        else:
            #splits the given string
            parts = string.split(line, ":")
 
            if "QUIT" not in parts[1] and "JOIN" not in parts[1] and "PART" not in parts[1]:
                try:
                    #sets the message variable to the actual message sent
                    message = parts[2][:len(parts[2]) - 1]
                except:
                    message = ""
                #sets the username variable to the actual username
                usernamesplit = string.split(parts[1], "!")
                username = usernamesplit[0]
               
                # works after twitch is done announcing stuff
                # (MODT = Message of the day)
                if MODT:
                    file1 = open("testfile.txt","a") 
                    print username + ": " + message 
                    file1.write(username + ": " + message + "\n" )
                    file1.close()
                    #here you can add your own commands
                    if message == "Hello":
                        Send_message("Hello " + username + cool)
                    if message == "How are you?":
                        mood = random.randint(3,6)
                        if mood == 3: Send_message("Nice, " + username  + smile)                        
                        elif mood == 4: Send_message("Fine, " + username  + tongue)
                        elif mood == 5: Send_message("Not bad, " + username  + bored)
                        elif mood == 6: Send_message("OK, " + username   + undecided)
                    if message == "!time":
                        Send_message(strftime("Now" + "%a, %d %b %Y %H:%M:%S", gmtime())+ "," + username)
               
                for l in parts:
                    if "End of /NAMES list" in l:
                        MODT = True