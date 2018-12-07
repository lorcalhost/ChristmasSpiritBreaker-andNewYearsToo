# -*- coding: utf-8 -*- 
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import sys
import datetime
import random
import pyperclip
import config

def christmasMessage(hour, minute):
    #Sending Christmas message
    global driver
    global christmas_contact_names_times
    for i in range(0, len(config.christmas_contact_names)):
        if christmas_contact_names_times[i][0] <= hour and christmas_contact_names_times[i][1] <= minute:
            try:
                pyperclip.copy(config.christmas_contact_names[i])
                searchbar = driver.find_elements_by_xpath('//*[@id="side"]/div[1]/div/label/input')[0]
                searchbar.click() #Click on searchbar
                searchbar.send_keys(Keys.CONTROL, 'v') #Search for contact for more speed
                msg = random.choice(config.christmas_messages)
                pyperclip.copy(msg) #Copies random message to clipboard
                x_arg = '//span[contains(@title,' + config.christmas_contact_names[i] + ')]'
                group_title = wait.until(EC.presence_of_element_located((By.XPATH, x_arg)))
                group_title.click()
                message = driver.find_elements_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')[0]
                message.send_keys(Keys.CONTROL, 'v') #Sends message from clipboard
                sendbutton = driver.find_elements_by_xpath('//*[@id="main"]/footer/div[1]/div[3]/button')[0]
                sendbutton.click() #Presses send button
                searchbar.click() #Click on searchbar
                searchbar.send_keys(Keys.CONTROL, 'a') #Select all
                searchbar.send_keys(Keys.DELETE) #Delete searchbar content
                print("Message successfully sent to "+ config.christmas_contact_names[i])

                christmas_contact_names_times[i][0] = 99
                christmas_contact_names_times[i][1] = 99
            except:
                print("Error sending message to "+ config.christmas_contact_names[i])
                pass
    return

def newYearsMessage(hour, minute):
    #Sending New Year's message
    global driver
    global newYears_contact_names_times
    for i in range(0, len(config.newYears_contact_names)):
        if newYears_contact_names_times[i][0] <= hour and newYears_contact_names_times[i][1] <= minute:
            try:
                pyperclip.copy(config.newYears_contact_names[i])
                searchbar = driver.find_elements_by_xpath('//*[@id="side"]/div[1]/div/label/input')[0]
                searchbar.click() #Click on searchbar
                searchbar.send_keys(Keys.CONTROL, 'v') #Search for contact for more speed
                msg = random.choice(config.newYears_messages)
                pyperclip.copy(msg) #Copies random message to clipboard
                x_arg = '//span[contains(@title,' + config.newYears_contact_names[i] + ')]'
                group_title = wait.until(EC.presence_of_element_located((By.XPATH, x_arg)))
                group_title.click()
                message = driver.find_elements_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')[0]
                message.send_keys(Keys.CONTROL, 'v') #Sends message from clipboard
                sendbutton = driver.find_elements_by_xpath('//*[@id="main"]/footer/div[1]/div[3]/button')[0]
                sendbutton.click() #Presses send button
                searchbar.click() #Click on searchbar
                searchbar.send_keys(Keys.CONTROL, 'a') #Select all
                searchbar.send_keys(Keys.DELETE) #Delete searchbar content
                print("Message successfully sent to "+ config.newYears_contact_names[i])

                newYears_contact_names_times[i][0] = 99
                newYears_contact_names_times[i][1] = 99
            except:
                print("Error sending message to "+ config.newYears_contact_names[i])
                pass
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

#MAIN

print("A popup view of WhatsApp web will now open,\nScan the QR code in the page via your app\nDon't close the popup")
time.sleep(5)

driver = webdriver.Chrome('./chromedriver')
driver.get("https://web.whatsapp.com/")
wait = WebDriverWait(driver, 600)

christmas_contact_names_times = [[0]*2 for i in range(len(config.christmas_contact_names))]
newYears_contact_names_times = [[0]*2 for i in range(len(config.newYears_contact_names))]


for i in range(0, len(config.christmas_contact_names)):
    config.christmas_contact_names[i] = str('"' + config.christmas_contact_names[i] + '"')
    newTime = newRandTime(config.christmas_time_interval)
    christmas_contact_names_times[i][0] = int(newTime[0:2])
    christmas_contact_names_times[i][1] = int(newTime[3:5])

for i in range(0, len(config.newYears_contact_names)):
    config.newYears_contact_names[i] = str('"' + config.newYears_contact_names[i] + '"')
    newTime = newRandTime(config.newYears_time_interval)
    newYears_contact_names_times[i][0] = int(newTime[0:2])
    newYears_contact_names_times[i][1] = int(newTime[3:5])

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