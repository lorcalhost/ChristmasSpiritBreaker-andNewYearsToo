# -*- coding: utf-8 -*-
import random
import fbchat
from fbchat.models import ThreadType, Message


def fb(hour, minute, client, u, u_pwd, usernames, usernames_times, message_list):
    for i in range(0, len(usernames)):
        if usernames_times[i][0] <= hour and usernames_times[i][1] <= minute:
            friends = client.searchForUsers(usernames[i])
            friend = friends[0]
            msg = random.choice(message_list)
            sent = client.send(
                Message(msg), thread_id=friend.uid, thread_type=ThreadType.USER)
            if sent:
                print("Message successfully sent to {}" .format(friend))
                usernames_times[i][0] = 99
                usernames_times[i][1] = 99
            else:
                client = fbchat.Client(u, u_pwd)
                fb(hour, minute, client, u, u_pwd,
                   usernames, usernames_times, message_list)
    return
