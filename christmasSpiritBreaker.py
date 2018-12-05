#!/usr/bin/python3
import sys
import os

def prnthelp():
    print("Welcome to the Christmas Spirit Breaker user guide\nPlease refer to the Github page for detailed setup instructions")
    print("\nList of commands:\nwhatsapp or -w ---> launches CSB in WhatsApp mode\nmessenger or -m ---> launches CSB in Messenger mode\nsms or -s ---> launches CSB in SMS mode")
    print("help or -h or man ---> Launches user guide\nupdate ---> Updates CSB from the github repo")

if str(sys.argv[1]) == "whatsapp" or str(sys.argv[1]) == "-w":
    print("WHATSAPP MODE")
    os.system("python whatsappCSB.py")
elif str(sys.argv[1]) == "messenger" or str(sys.argv[1]) == "-m":
    print("MESSENGER MODE")
    os.system("python messengerCSB.py")
elif str(sys.argv[1]) == "sms" or str(sys.argv[1]) == "-s":
    print("SMS MODE")
    os.system("python smsCSB.py")
elif str(sys.argv[1]) == "help" or str(sys.argv[1]) == "-h" or str(sys.argv[1]) == "man":
    prnthelp()
elif str(sys.argv[1]) == "update":
    os.system("git pull")
else:
    print("Invalid arguments\nRun python christmasSpiritBreaker.py -h to look at the commands manual")