# -*- coding: utf-8 -*-
from tg_sendMessage import tg
from telethon import TelegramClient, events, sync
import individualTimes
import os,sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import config
import time
import datetime


# Create the client and connect
client = TelegramClient(config.telegram_username, config.tg_api_id, config.tg_api_hash)
client.start(config.telegram_phone, config.telegram_password)

# Setting up
if(config.christmasModeEnabled):
    christmas_usernames_times = individualTimes.custom(
        config.tg_christmas_usernames, config.christmas_time_interval)
    print("Christmas messages setup correctly, They will be sent on December 25th in the time interval {} {}" .format(
        config.christmas_time_interval[0], config.christmas_time_interval[1]))

if(config.newYearsModeEnabled):
    newYears_usernames_times = individualTimes.custom(
        config.tg_newYears_usernames, config.newYears_time_interval)
    print("New Year's messages setup correctly, They will be sent on January 1st in the time interval {} {}" .format(
        config.newYears_time_interval[0], config.newYears_time_interval[1]))

while True:
    today_day = int(datetime.datetime.today().day)
    today_month = int(datetime.datetime.today().month)
    today_hour = int(datetime.datetime.today().hour)
    today_minutes = int(datetime.datetime.today().minute)

    if (config.christmasModeEnabled):
        if (today_day == config.christmas_day) and (today_month == config.christmas_month):
            tg(today_hour, today_minutes, client, config.tg_christmas_usernames,
               christmas_usernames_times, config.christmas_messages)
    if (config.newYearsModeEnabled):
        if (today_day == config.newYears_day) and (today_month == config.newYears_month):
            tg(today_hour, today_minutes, client, config.tg_newYears_usernames,
               newYears_usernames_times, config.newYears_messages)
    # Wait one minute before checking again
    time.sleep(config.updade_frequency)
