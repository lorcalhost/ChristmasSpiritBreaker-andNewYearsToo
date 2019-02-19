# Christmas Spirit Breaker (and New Years Too)
##### "Are you tired of having to manually write and send christmas texts to everyone on christmas to mantain a good relationship with them? Do you want to be the annoying person who is the first one to send "Happy new year" messages to everyone on your contact list exactly at midnight? Do you want to be a bad boy this christmas season? I got you covered."  
  
Strongly inspired by my other project [RomanceBreaker](https://github.com/lorcalhost/RomanceBreaker/), introducing ***Christmas Spirit Breaker***, a python script which automatically sends a custom christmas/new year's greeting message, from a custom messages list, to your selected contacts you want to mantain good relationships with, at given time range on Facebook Messenger, WhatsApp, Telegram or via SMS. Time to be bad boys this christmas. *Work smarter, not Harder.*

### What you will gain:
  - More time spent with the new body pillow you just received for christmas.
  - More time spent stealing new year's champagne from people who are busy texting their friends.
  - Mantain those relationships with friends (if you don't send greetings on such events they will know you are not a true friend)
  - Magic

---
## [NEW] [YOU CAN FIND THE VIDEO INSTALLATION GUIDE HERE](https://youtu.be/yaC3OxaGJpI)
# Facebook Messenger:
### Installation on PC

Santa relies on reindeers for delivery, and so does Christmas Spirit Breaker rely on a few things, here is what to do to get them:  
- Python3 is needed get it from [here](https://www.python.org/downloads/)

###### For Linux:
Run these commands in your preferred terminal application  
```sh
sudo apt-get install python3-pip
pip3 install fbchat bs4 
git clone https://github.com/lorcalhost/ChristmasSpiritBreaker-andNewYearsToo.git
```
###### For Windows
- Also install git from [here](https://git-scm.com/download/win)
- Make sure you run all the commands from git
```sh
pip install fbchat bs4
git clone https://github.com/lorcalhost/ChristmasSpiritBreaker-andNewYearsToo.git
```

### Installation on Android 
From *Android* you will only be able to run the Facebook Messenger version, here are the instructions:
- First download and install [Termux from the Google Play Store](https://play.google.com/store/apps/details?id=com.termux)  
- Then run the following commands:   
- ```termux-setup-storage``` and allow storage access  
```sh
cd storage/downloads 
pkg install python3 git
pip3 install fbchat requests bs4 enum
git clone https://github.com/lorcalhost/ChristmasSpiritBreaker-andNewYearsToo.git
```
Please note that every time you restart your device, you will have to re run the commands in the *How to run* section

---

# Telegram:
### Installation on PC

Santa relies on reindeers for delivery, and so does Christmas Spirit Breaker rely on a few things, here is what to do to get them:  
- Python3 is needed get it from [here](https://www.python.org/downloads/)

###### For Linux:
Run these commands in your preferred terminal application  
```sh
sudo apt-get install python3-pip
pip3 install telethon bs4 
git clone https://github.com/lorcalhost/ChristmasSpiritBreaker-andNewYearsToo.git
```
###### For Windows
- Also install git from [here](https://git-scm.com/download/win)
- Make sure you run all the commands from git
```sh
pip install telethon bs4
git clone https://github.com/lorcalhost/ChristmasSpiritBreaker-andNewYearsToo.git
```

### Installation on Android 
From *Android* you will only be able to run the Facebook Messenger version, here are the instructions:
- First download and install [Termux from the Google Play Store](https://play.google.com/store/apps/details?id=com.termux)  
- Then run the following commands:   
- ```termux-setup-storage``` and allow storage access  
```sh
cd storage/downloads 
pkg install python3 git
pip install fbchat requests bs4 enum
git clone https://github.com/lorcalhost/ChristmasSpiritBreaker-andNewYearsToo.git
```
Please note that every time you restart your device, you will have to re run the commands in the *How to run* section

---

# WhatsApp and SMS
### Installation on PC

Santa relies on reindeers for delivery, and so does Christmas Spirit Breaker rely on a few things, here is what to do to get them:  
- Python3 is needed get it from [here](https://www.python.org/downloads/)
- Chrome Driver get it from [here](https://chromedriver.storage.googleapis.com/index.html?path=2.44/) and unzip in the ```ChristmasSpiritBreaker-andNewYearsToo``` folder
- If you want to setup SMS you will need to have [Google messages](https://play.google.com/store/apps/details?id=com.google.android.apps.messaging) on your Android phone

###### For Linux:
Run these commands in your preferred terminal application  
```sh
sudo apt-get install python3-pip xclip
sudo pip3 install selenium bs4 pyperclip
git clone https://github.com/lorcalhost/ChristmasSpiritBreaker-andNewYearsToo.git
```
###### For Windows
- Also install git from [here](https://git-scm.com/download/win)
- Make sure you run all the commands from git
```sh
pip install selenium bs4 pyperclip
git clone https://github.com/lorcalhost/ChristmasSpiritBreaker-andNewYearsToo.git
```
##### SMS mode is strongly not suggested, it's slow and buggy due to Google Messages nature

---

# How to run
First go to the program directory by typing in the terminal:
- From **PC:**  ```cd ChristmasSpiritBreaker-andNewYearsToo``` 
- From **Android:** ```cd storage/downloads/ChristmasSpiritBreaker-andNewYearsToo```  

Then run the script with the according argument:  
- For **WhatsApp version**: ```python3 christmasSpiritBreaker.py -w``` or ```python3 christmasSpiritBreaker.py whatsapp``` 
- For **Messenger version**: ```python3 christmasSpiritBreaker.py -m``` or ```python3 christmasSpiritBreaker.py messenger``` 
- For **SMS version**: ```python3 christmasSpiritBreaker.py -s``` or ```python3 christmasSpiritBreaker.py sms``` 
- For **Telegram version**: ```python3 christmasSpiritBreaker.py -t``` or ```python3 christmasSpiritBreaker.py telegram``` 

Also other arguments exist like:
- To open **user guide**: ```python3 christmasSpiritBreaker.py -h``` or ```python3 christmasSpiritBreaker.py help```  or ```python3 christmasSpiritBreaker.py man``` 
- To **update** the script: ```python3 christmasSpiritBreaker.py update```

**For *Android* users:** you will also need to press ```"ACQUIRE WAKELOCK"``` in the Termux notification to enable the script to run in the background withoutthe process being killed  
***Android right now only supports Facebook Messenger mode***

---

# Custom messages/contacts/times setup
***Android** users may want to edit the ```config.py``` file with their preferred text editing app as the file will be in the Downloads folder of their devices*   
  
Simply open the ```config.py``` file with your preferred text editing app and follow the instructions there, I think I made them clear enough   

If you don't want to use the bot for both christmas and new years you can disable the fatures individually by setting to ```False``` the lines
```python
christmasModeEnabled = True # Change to False to disable Christmas mode
newYearsModeEnabled = True # Change to False to disable New Year's mode
```
###### If you still cannot understand from the config.py file..
## Custom messages:


Replace the messages in between ```" "``` with your own custom messages, you can also add more custom messages by adding after the ```"``` of the last message a comma and a new message, always in between ```" "```s. 
If we want to add ```New custom message``` to the list below 
```python
christmas_messages = ["Merry christmas!"]
```
We just need to edit it like this:
```python
christmas_messages = ["Merry christmas!", "New custom message"]
```
## Custom contacts:
**Important:**
 - Make sure that if you are setting up **WhatsApp** contatcs or **SMS** contacts you are writing their names **as they appear in your phone's conatct list**  
 - If you are using **Messenger** use your contact's messenger **username**

Replace the contact names in between ```" "``` with your own custom contact names, you can also add more custom contacts by adding after the ```"``` of the last contact a comma and a new contacts, always in between ```" "```s. 
If we want to add ```Santa Claus``` to the list below 
```python
christmas_contact_names = ["John McAfee"]
```
We just need to edit it like this:
```python
christmas_contact_names = ["John McAfee", "Santa Claus"]
```
## Custom time range: 
The **christmas messages** will be sent on *December 25th*  
The **new years** messages will be sent on *January 1st*  

If we want to change the christmas time range we have to edit this line:
```python
christmas_time_interval = ["08:00", "23:59"]
```
If we want to change the new year's time range we have to edit this line:
```python
newYears_time_interval = ["00:00", "00:15"]
```

Make sure the **hour** is always **two digits**

## Telegram API setup
- Log in to your Telegram core: https://my.telegram.org.
- Go to ‘API development tools’ and fill out the form.
- Create an app
- You will get the `api_id` and `api_hash` parameters required for user authorization (to put in the config.py file).
---

**If you have any trouble with your setup feel free to message me on Telegram [@lorcalhost](https://t.me/lorcalhost)**
