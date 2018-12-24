# -*- coding: utf-8 -*- 
import time
import datetime
import fbchat
import random
from fbchat.models import ThreadType, Message
from getpass import getpass
import config

#Getting username & pwd
username = input("Username: ")
passwrd = getpass()
client = fbchat.Client(username, passwrd)

def christmasMessage(hour, minute):
    #Sending Christmas message
    global client
    global christmas_usernames_times
    for i in range(0, len(config.christmas_usernames)):
        if christmas_usernames_times[i][0] <= hour and christmas_usernames_times[i][1] <= minute:
            friends = client.searchForUsers(config.christmas_usernames[i])
            friend = friends[0]
            msg = random.choice(config.christmas_messages)
            sent = client.send(Message(msg), thread_id=friend.uid, thread_type=ThreadType.USER)
            if sent:
                print("Message successfully sent to {}" .format(friend))
                christmas_usernames_times[i][0] = 99
                christmas_usernames_times[i][1] = 99
            else:
                global username
                global passwrd
                client = fbchat.Client(username, passwrd)
                christmasMessage(hour, minute)
    return

def newYearsMessage(hour, minute):
    #Sending New Year's message
    global client
    for i in range(0, len(config.newYears_usernames)):
        if newYears_usernames_times[i][0] <= hour and newYears_usernames_times[i][1] <= minute:
            friends = client.searchForUsers(config.newYears_usernames[i])
            friend = friends[0]
            msg = random.choice(config.newYears_messages)
            sent = client.send(Message(msg), thread_id=friend.uid, thread_type=ThreadType.USER)
            if sent:
                print("Message successfully sent to {}" .format(friend))
                newYears_usernames_times[i][0] = 99
                newYears_usernames_times[i][1] = 99
            else:
                global username
                global passwrd
                client = fbchat.Client(username, passwrd)
                newYearsMessage(hour, minute)
    return

def newRandTime(customTimeInterval):
    randTimeHour = random.randint(int(customTimeInterval[0][0:2]), int(customTimeInterval[1][0:2]))
    if int(randTimeHour) == int(customTimeInterval[1][0:2]):
        randTimeMinute = random.randint(0, int(customTimeInterval[1][3:5]))
    elif int(randTimeHour) == int(customTimeInterval[0][0:2]):
        randTimeMinute = random.randint(int(customTimeInterval[1][3:5]), 59)
    else:
        randTimeMinute = random.randint(0, 59)
    return str(str(randTimeHour).zfill(2) + ":" + str(randTimeMinute).zfill(2))

#Reassuring users the script actually works
if(config.christmasModeEnabled):
    christmas_usernames_times = [[0]*2 for i in range(len(config.christmas_usernames))]
    for i in range(0, len(config.christmas_usernames)):
        newTime = newRandTime(config.christmas_time_interval)
        christmas_usernames_times[i][0] = int(newTime[0:2])
        christmas_usernames_times[i][1] = int(newTime[3:5])
    print("Christmas messages setup correctly, They will be sent on December 25th in the time interval {} {}" .format(config.christmas_time_interval[0], config.christmas_time_interval[1]))

if(config.newYearsModeEnabled):
    newYears_usernames_times = [[0]*2 for i in range(len(config.newYears_usernames))]
    for i in range(0, len(config.newYears_usernames)):
        newTime = newRandTime(config.newYears_time_interval)
        newYears_usernames_times[i][0] = int(newTime[0:2])
        newYears_usernames_times[i][1] = int(newTime[3:5])
    print("New Year's messages setup correctly, They will be sent on January 1st in the time interval {} {}" .format(config.newYears_time_interval[0], config.newYears_time_interval[1]))

while True:
    if (config.christmasModeEnabled):
        if (int(datetime.datetime.today().day) == 25) and (int(datetime.datetime.today().month) == 12):
            christmasMessage(int(datetime.datetime.today().hour), int(datetime.datetime.today().minute))
    if (config.newYearsModeEnabled):
        if (int(datetime.datetime.today().day) == 1) and (int(datetime.datetime.today().month) == 1):
            newYearsMessage(int(datetime.datetime.today().hour), int(datetime.datetime.today().minute))        
    time.sleep(60) #Wait one minute before checking again
