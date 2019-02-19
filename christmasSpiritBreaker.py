#!/usr/bin/python3
import sys
import os
import config

command = "python"
if config.currentOS is "Linux":
    command += "3"

def prnthelp():
    print("Welcome to the Christmas Spirit Breaker user guide\nPlease refer to the Github page for detailed setup instructions")
    print("\nList of commands:\nwhatsapp or -w ---> launches CSB in WhatsApp mode\nmessenger or -m ---> launches CSB in Messenger mode\nsms or -s ---> launches CSB in SMS mode")
    print("help or -h or man ---> Launches user guide\nupdate ---> Updates CSB from the github repo")
try:
    if str(sys.argv[1]) == "whatsapp" or str(sys.argv[1]) == "-w":
        print("WHATSAPP MODE")
        os.system("{} whatsappCSB.py" .format(command))
    elif str(sys.argv[1]) == "messenger" or str(sys.argv[1]) == "-m":
        print("MESSENGER MODE")
        os.system("{} messengerCSB.py" .format(command))
    elif str(sys.argv[1]) == "sms" or str(sys.argv[1]) == "-s":
        print("SMS MODE")
        os.system("{} smsCSB.py" .format(command))
    elif str(sys.argv[1]) == "help" or str(sys.argv[1]) == "-h" or str(sys.argv[1]) == "man":
        prnthelp()
    elif str(sys.argv[1]) == "update":
        os.system("git pull")
except:
    print("Invalid arguments\nTry running {} christmasSpiritBreaker.py -h to show the list of commands" .format(command))
