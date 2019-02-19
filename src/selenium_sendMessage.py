# -*- coding: utf-8 -*-
import random
import pyperclip
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


def wa(hour, minute, driver, wait, names, names_times, message_list):
    for i in range(0, len(names)):
        if names_times[i][0] <= hour and names_times[i][1] <= minute:
            try:
                quoted_username = str('"' + names[i] + '"')
                pyperclip.copy(names[i])
                searchbar = driver.find_elements_by_xpath(
                    '//*[@id="side"]/div[1]/div/label/input')[0]
                searchbar.click()  # Click on searchbar
                # Search for contact for more speed
                searchbar.send_keys(Keys.CONTROL, 'v')

                x_arg = '//span[contains(@title,' + quoted_username + ')]'
                group_title = wait.until(
                    EC.presence_of_element_located((By.XPATH, x_arg)))
                group_title.click()
                time.sleep(0.1)

                msg = random.choice(message_list)
                pyperclip.copy(msg)  # Copies random message to clipboard
                message = driver.find_elements_by_xpath(
                    '//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')[0]
                # Sends message from clipboard
                message.send_keys(Keys.CONTROL, 'v')
                time.sleep(0.1)

                sendbutton = driver.find_elements_by_xpath(
                    '//*[@id="main"]/footer/div[1]/div[3]/button')[0]
                sendbutton.click()  # Presses send button
                searchbar.click()  # Click on searchbar
                # Select searchbar content
                searchbar.send_keys(Keys.CONTROL, 'a')
                searchbar.send_keys(Keys.DELETE)  # Delete searchbar content
                print("Message successfully sent to {}" .format(names[i]))

                names_times[i][0] = 99
                names_times[i][1] = 99
            except:
                print("Error sending message to {}" .format(names[i]))
                pass
    return


def sms(hour, minute, driver, wait, names, names_times, message_list):
    for i in range(0, len(names)):
        if names_times[i][0] <= hour and names_times[i][1] <= minute:
            try:
                searchbar = driver.find_elements_by_xpath(
                    '//*[@id="yDmH0d"]/c-wiz/div/div/div/div/div/div[1]/div[3]/div/div[2]/div[3]')[0]
                searchbar.click()
                time.sleep(1)

                pyperclip.copy(names[i])
                newmessage = driver.find_element_by_xpath(
                    '//*[@id="yDmH0d"]/c-wiz/div/div/div/div/div/div[2]/div/div[2]/div/div[2]/div/div/div/div[1]/div/div[1]/input')
                newmessage.send_keys(Keys.CONTROL, 'v')
                time.sleep(5)

                newmessage.send_keys(Keys.ENTER)
                time.sleep(6.5)

                msg = random.choice(message_list)
                pyperclip.copy(msg)
                message = driver.find_elements_by_xpath(
                    '//*[@id="yDmH0d"]/c-wiz/div/div/div/div/div/div[2]/div/div[3]/div/div/div[3]/div[2]/div[1]/div/div[2]/div/div[1]')[0]
                message.send_keys(Keys.CONTROL, 'v')
                message.send_keys(Keys.ENTER)
                print("Message successfully sent to {}" .format(names[i]))

                names_times[i][0] = 99
                names_times[i][1] = 99
            except:
                print("Error sending message to {}" .format(names[i]))
                pass
    return
