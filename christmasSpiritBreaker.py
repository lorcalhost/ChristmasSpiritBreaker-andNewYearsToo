# -*- coding: utf-8 -*- 
import time
import datetime
import fbchat
import random
from fbchat.models import *
from getpass import getpass

#GENERAL SETUP
christmasModeEnabled = True #Change to False to disable Christmas mode
newYearsModeEnabled = True #Change to False to disable New Year's mode

#CHRISTMAS SETUP
christmas_messages = ["Merry christmas!", "I wish you a merry christmas", "Merry christmas to you and family", "I hate christmas but merry christmas either way"]
christmas_time_interval = ["08:00", "23:59"]
christmas_contacts_list = ["lollocll", "markzuckerberg", "elonmusk", "santaclaus"]

#NEW YEAR'S SETUP
newYears_messages = ["Happy New Year!", "Felice capodanno as the italians say", "I totally wrote this messages on my own"]
newYears_time_interval = ["00:00", "00:15"]
newYears_contacts_list = ["lollocll", "markzuckerberg", "elonmusk", "santaclaus"]

#REAL PROGRAM BEGINS, NO MORE SETUP FROM HERE ON

#Getting username & pwd
username = input("Username: ")
passwrd = getpass()
client = fbchat.Client(username, passwrd)

def christmasMessage(hour, minute):
    #Sending Christmas message
    global client
    for i in range(0, len(christmas_contacts_list)):
        if christmas_contacts_list_times[i][0] == hour and christmas_contacts_list_times[i][1] == minute:
            friends = client.searchForUsers(christmas_contacts_list[i])
            friend = friends[0]
            msg = random.choice(christmas_messages)
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
    for i in range(0, len(newYears_contacts_list)):
        if newYears_contacts_list_times[i][0] == hour and newYears_contacts_list_times[i][1] == minute:
            friends = client.searchForUsers(newYears_contacts_list[i])
            friend = friends[0]
            msg = random.choice(newYears_messages)
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

christmas_contacts_list_times = [[0]*2 for i in range(len(christmas_contacts_list))]
newYears_contacts_list_times = [[0]*2 for i in range(len(christmas_contacts_list))]

    #Reassuring users the script actually works
    if(christmasModeEnabled):
        print("Christmas messages setup correctly, They will be sent on December 25th in the time interval " + christmas_time_interval[0] + " " + christmas_time_interval[1])
    if(newYearsModeEnabled):
        print("New Year's messages setup correctly, They will be sent on January 1st in the time interval " + christmas_time_interval[0] + " " + christmas_time_interval[1])

while True:
    if (christmasModeEnabled):
        if (int(datetime.datetime.today().day) == 25) and (int(datetime.datetime.today().month) == 12):
            christmasMessage(int(datetime.datetime.today().hour), int(datetime.datetime.today().minute))
    if (newYearsModeEnabled):
        if (int(datetime.datetime.today().day) == 1) and (int(datetime.datetime.today().month) == 1):
            newYearsMessage(int(datetime.datetime.today().hour), int(datetime.datetime.today().minute))        
    time.sleep(60) #Wait one minute to check if it's #morningtime
