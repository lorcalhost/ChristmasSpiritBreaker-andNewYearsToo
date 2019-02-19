# -*- coding: utf-8 -*-
import randomTime

def custom(usernames, time_interval):
    usernames_times = [[0]*2 for i in range(len(usernames))]
    for i in range(0, len(usernames)):
        newTime = randomTime.newTime(time_interval)
        usernames_times[i][0] = int(newTime[0:2])
        usernames_times[i][1] = int(newTime[3:5])
    return usernames_times
