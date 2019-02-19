# -*- coding: utf-8 -*-
from selenium_sendMessage import sms
import individualTimes
import os,sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import config
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import time
import datetime


print("A popup view of Android Messages web will now open,\nScan the QR code in the page via your app\nDon't close the popup")
time.sleep(5)

# Logging in
driver = webdriver.Chrome(
    '{}/chromedriver'.format(os.path.dirname(os.path.realpath('__file__'))))
driver.get("https://messages.android.com/")
wait = WebDriverWait(driver, 600)

# Setting up
if(config.christmasModeEnabled):
    christmas_names_times = individualTimes.custom(
        config.christmas_contact_names, config.christmas_time_interval)
    print("Christmas messages setup correctly, They will be sent on December 25th in the time interval {} {}" .format(
        config.christmas_time_interval[0], config.christmas_time_interval[1]))

if(config.newYearsModeEnabled):
    newYears_names_times = individualTimes.custom(
        config.newYears_contact_names, config.newYears_time_interval)
    print("New Year's messages setup correctly, They will be sent on January 1st in the time interval {} {}" .format(
        config.newYears_time_interval[0], config.newYears_time_interval[1]))

while True:
    today_day = int(datetime.datetime.today().day)
    today_month = int(datetime.datetime.today().month)
    today_hour = int(datetime.datetime.today().hour)
    today_minutes = int(datetime.datetime.today().minute)

    if (config.christmasModeEnabled):
        if (today_day == config.christmas_day) and (today_month == config.christmas_month):
            sms(today_hour, today_minutes, driver, wait, config.christmas_contact_names,
                christmas_names_times, config.christmas_messages)
    if (config.newYearsModeEnabled):
        if (today_day == config.newYears_day) and (today_month == config.newYears_month):
            sms(today_hour, today_minutes, driver, wait, config.newYears_contact_names,
                newYears_names_times, config.newYears_messages)
    # Wait one minute before checking again
    time.sleep(config.updade_frequency)
