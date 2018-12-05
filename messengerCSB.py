# -*- coding: utf-8 -*- 
import time
import datetime
import fbchat
import random
from fbchat.models import *
from getpass import getpass
import config

#Getting username & pwd
username = input("Username: ")
passwrd = getpass()
client = fbchat.Client(username, passwrd)

def christmasMessage(hour, minute):
    #Sending Christmas message
    global client
    for i in range(0, len(config.FB_christmas_contacts_list)):
        if FB_christmas_contacts_list_times[i][0] == hour and FB_christmas_contacts_list_times[i][1] == minute:
            friends = client.searchForUsers(config.FB_christmas_contacts_list[i])
            friend = friends[0]
            msg = random.choice(config.christmas_messages)
            sent = client.send(Message(msg), thread_id=friend.uid, thread_type=ThreadType.USER)
            if sent:
                print("Message successfully sent to "+ friend)
            else:
                global username
                global passwrd
                client = fbchat.Client(username, passwrd)
                christmasMessage(hour, minute)
    return

def newYearsMessage(hour, minute):
    #Sending New Year's message
    global client
    for i in range(0, len(config.FB_newYears_contacts_list)):
        if FB_newYears_contacts_list_times[i][0] == hour and FB_newYears_contacts_list_times[i][1] == minute:
            friends = client.searchForUsers(config.FB_newYears_contacts_list[i])
            friend = friends[0]
            msg = random.choice(config.newYears_messages)
            sent = client.send(Message(msg), thread_id=friend.uid, thread_type=ThreadType.USER)
            if sent:
                print("Message successfully sent to "+ friend)
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

FB_christmas_contacts_list_times = [[0]*2 for i in range(len(config.FB_christmas_contacts_list))]
FB_newYears_contacts_list_times = [[0]*2 for i in range(len(config.FB_christmas_contacts_list))]

for i in range(0, len(config.FB_christmas_contacts_list)):
    newTime = newRandTime(config.christmas_time_interval)
    FB_christmas_contacts_list_times[i][0] = int(newTime[0:2])
    FB_christmas_contacts_list_times[i][1] = int(newTime[3:5])

for i in range(0, len(config.FB_newYears_contacts_list)):
    newTime = newRandTime(config.christmas_time_interval)
    FB_newYears_contacts_list_times[i][0] = int(newTime[0:2])
    FB_newYears_contacts_list_times[i][1] = int(newTime[3:5])

#Reassuring users the script actually works
if(config.christmasModeEnabled):
    print("Christmas messages setup correctly, They will be sent on December 25th in the time interval " + config.christmas_time_interval[0] + " " + config.christmas_time_interval[1])
if(config.newYearsModeEnabled):
    print("New Year's messages setup correctly, They will be sent on January 1st in the time interval " + config.christmas_time_interval[0] + " " + config.christmas_time_interval[1])

while True:
    if (config.christmasModeEnabled):
        if (int(datetime.datetime.today().day) == 25) and (int(datetime.datetime.today().month) == 12):
            christmasMessage(int(datetime.datetime.today().hour), int(datetime.datetime.today().minute))
    if (config.newYearsModeEnabled):
        if (int(datetime.datetime.today().day) == 1) and (int(datetime.datetime.today().month) == 1):
            newYearsMessage(int(datetime.datetime.today().hour), int(datetime.datetime.today().minute))        
    time.sleep(60) #Wait one minute before checking again
