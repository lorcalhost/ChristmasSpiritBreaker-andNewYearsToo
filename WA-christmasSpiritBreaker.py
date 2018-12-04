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

print("A popup view of WhatsApp web will now open,\nScan the QR code in the page via your app\nDon't close the popup")
time.sleep(5)

driver = webdriver.Chrome('./chromedriver')
driver.get("https://web.whatsapp.com/")
wait = WebDriverWait(driver, 600)

def christmasMessage(hour, minute):
    #Sending Christmas message
    global driver
    for i in range(0, len(config.WA_christmas_contacts_list)):
        if WA_christmas_contacts_list_times[i][0] == hour and WA_christmas_contacts_list_times[i][1] == minute:
            msg = random.choice(config.christmas_messages)
            pyperclip.copy(msg) #Copies random message to clipboard
            x_arg = '//span[contains(@title,' + config.WA_christmas_contacts_list[i] + ')]'
            group_title = wait.until(EC.presence_of_element_located((By.XPATH, x_arg)))
            group_title.click()
            message = driver.find_elements_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')[0]
            message.send_keys(Keys.CONTROL, 'v') #Sends message from clipboard
            sendbutton = driver.find_elements_by_xpath('//*[@id="main"]/footer/div[1]/div[3]/button')[0]
            sendbutton.click() #Presses send button
            print("Message successfully sent to "+ config.WA_christmas_contacts_list[i])
    return

def newYearsMessage(hour, minute):
    #Sending New Year's message
    global driver
    for i in range(0, len(config.WA_newYears_contacts_list)):
        if WA_newYears_contacts_list_times[i][0] == hour and WA_newYears_contacts_list_times[i][1] == minute:
            msg = random.choice(config.newYears_messages)
            pyperclip.copy(msg) #Copies random message to clipboard
            x_arg = '//span[contains(@title,' + config.WA_newYears_contacts_list[i] + ')]'
            group_title = wait.until(EC.presence_of_element_located((By.XPATH, x_arg)))
            group_title.click()
            message = driver.find_elements_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')[0]
            message.send_keys(Keys.CONTROL, 'v') #Sends message from clipboard
            sendbutton = driver.find_elements_by_xpath('//*[@id="main"]/footer/div[1]/div[3]/button')[0]
            sendbutton.click() #Presses send button
            print("Message successfully sent to "+ config.WA_newYears_contacts_list[i])
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

WA_christmas_contacts_list_times = [[0]*2 for i in range(len(config.WA_christmas_contacts_list))]
WA_newYears_contacts_list_times = [[0]*2 for i in range(len(config.WA_christmas_contacts_list))]


for i in range(0, len(config.WA_christmas_contacts_list)):
    config.WA_christmas_contacts_list[i] = str('"' + config.WA_christmas_contacts_list[i] + '"')
    newTime = newRandTime(config.christmas_time_interval)
    WA_christmas_contacts_list_times[i][0] = int(newTime[0:2])
    WA_christmas_contacts_list_times[i][1] = int(newTime[3:5])

for i in range(0, len(config.WA_newYears_contacts_list)):
    config.WA_newYears_contacts_list[i] = str('"' + config.WA_newYears_contacts_list[i] + '"')
    newTime = newRandTime(config.christmas_time_interval)
    WA_newYears_contacts_list_times[i][0] = int(newTime[0:2])
    WA_newYears_contacts_list_times[i][1] = int(newTime[3:5])

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
    time.sleep(60) #Wait one minute to check if it's #morningtime
