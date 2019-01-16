# -*- coding: utf-8 -*- 
"""
   _____ _          _     _                        _____       _      _ _   ____                 _             
  / ____| |        (_)   | |                      / ____|     (_)    (_) | |  _ \               | |            
 | |    | |__  _ __ _ ___| |_ _ __ ___   __ _ ___| (___  _ __  _ _ __ _| |_| |_) |_ __ ___  __ _| | _____ _ __ 
 | |    | '_ \| '__| / __| __| '_ ` _ \ / _` / __|\___ \| '_ \| | '__| | __|  _ <| '__/ _ \/ _` | |/ / _ \ '__|
 | |____| | | | |  | \__ \ |_| | | | | | (_| \__ \____) | |_) | | |  | | |_| |_) | | |  __/ (_| |   <  __/ |   
  \_____|_| |_|_|  |_|___/\__|_| |_| |_|\__,_|___/_____/| .__/|_|_|  |_|\__|____/|_|  \___|\__,_|_|\_\___|_|   
                                                        | |                                                    
                                                        |_|                                                    
"""
# CHOOSE IF YOU WANT THE PROGRAM TO WORK BOTH FOR CHRISTMAS AND NEW YEAR'S OR JUST ONE OF THEM
# Set to True to enable, False to disable
christmasModeEnabled = True # Change to False to disable Christmas mode
newYearsModeEnabled = True # Change to False to disable New Year's mode

# RUN DATE AND FREQUENCY SETUP   
# Setup Christmas and New Year's day/month:
christmas_day = 25
christmas_month = 12

newYears_day = 1
newYears_month = 1

# Setup date/time update frequency (in seconds):
updade_frequency = 60


# CUSTOM MESSAGES SETUP
# Put here your custom christmas messages, supports emojis:
christmas_messages = ["Merry christmas!", "I wish you a merry christmas", "Merry christmas to you and family", "I hate christmas but merry christmas either way"]
# Put here your custom New Year's messages, supports emojis:
newYears_messages = ["Happy New Year!", "Felice capodanno as the italians say", "I totally wrote this messages on my own"]

# CUSTOM TIMES SETUP
# Put here the time interval in which the Christmas messages should be sent, make sure hour is two digits:
christmas_time_interval = ["08:00", "23:59"]
# Put here the time interval in which the New Year's messages should be sent, make sure hour is two digits:
newYears_time_interval = ["00:00", "00:15"]

# FACEBOOK MESSENGER CONTACTS SETUP:
# Insert here the Facebook Messenger USERNAMES (Not names) of the people whom to send christmas messages:
christmas_usernames = ["lollocll", "markzuckerberg", "elonmusk", "santaclaus"]
# Insert here the Facebook Messenger USERNAMES (Not names) of the people whom to send new year's messages
newYears_usernames = ["lollocll", "markzuckerberg", "elonmusk", "santaclaus"]

# WHATSAPP AND SMS CONTACTS SETUP:
# Insert here the NAMES of the people whom to send christmas messages as they appear in your contacts list:
christmas_contact_names = ["John McAfee", "Tim Cook", "Elon Musk", "Person I Hate"]
# Insert here the NAMES of the people whom to send new year's messages as they appear in your contacts list:
newYears_contact_names = ["lollocll", "markzuckerberg", "elonmusk", "santaclaus"]
