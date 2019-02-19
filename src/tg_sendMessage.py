# -*- coding: utf-8 -*-
import random
from telethon import TelegramClient, events, sync


def tg(hour, minute, client, usernames, usernames_times, message_list):
    for i in range(0, len(usernames)):
        if usernames_times[i][0] <= hour and usernames_times[i][1] <= minute:
            msg = random.choice(message_list)
            sent = client.send_message(msg, usernames[i])
            if sent:
                print("Message successfully sent to {}" .format(usernames[i]))
                usernames_times[i][0] = 99
                usernames_times[i][1] = 99
            else:
                print("Error sending message to {}" .format(usernames[i]))
    return
