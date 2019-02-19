# -*- coding: utf-8 -*-
import random

def newTime(customTimeInterval):
    randTimeHour = random.randint(
        int(customTimeInterval[0][0:2]), int(customTimeInterval[1][0:2]))
    if int(randTimeHour) == int(customTimeInterval[1][0:2]):
        randTimeMinute = random.randint(0, int(customTimeInterval[1][3:5]))
    elif int(randTimeHour) == int(customTimeInterval[0][0:2]):
        randTimeMinute = random.randint(int(customTimeInterval[1][3:5]), 59)
    else:
        randTimeMinute = random.randint(0, 59)
    return str(str(randTimeHour).zfill(2) + ":" + str(randTimeMinute).zfill(2))