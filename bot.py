import send_mail
from selenium.webdriver import Keys
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import random
from flask import Flask



validity = int(random.randint(0,1000000000000))

options = Options()
options.add_argument('--profile-directory=Profile 6')
options.add_argument(
    "user-data-dir=C:\\Users\\home\\AppData\\Local\\Google\\Chrome\\User Data\\")  # Path to your chrome profile
driver = webdriver.Chrome(executable_path="C:\dev\chromedriver\chromedriver.exe", options=options)

driver.get('https://web.whatsapp.com')

print(validity)
send_mail.send_mail(validity)

input("enter")

def bot_stop(message):
    if str(message) in "admin-start":
        get_element()
    else:
        sleep(3)
        lastmessage = driver.find_elements(By.CLASS_NAME, "_1Gy50")
        message = lastmessage[-1].text
        message = message.lower()
        bot_stop(message)





def send_message(message):

    # geting input
    answers = [
        'hey there please type "place order" to place a order',
        """ Not recognised !!  
        please type "hi" to get started """,
        'please chose a way of placing order type "home" for home delivery ',
        'thanks for placing order',
        'bot started',
    ]
    intro = [
        'hi',
        'hey',
        'hello',
        'hii',

    ]
    commands = [
        'place order',
        'home',

    ]

    xpath_input = '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]'
    input_box = driver.find_elements(By.XPATH, xpath_input)




    if str(message) in str(intro):

        input_box[0].send_keys(answers[0] + Keys.ENTER)
        sent = True
        get_element()

    elif message in str(commands[0]):
        input_box[0].send_keys(answers[2] + Keys.ENTER)
        sent = True
        get_element()

    elif message in str(commands[1]):
        input_box[0].send_keys(answers[3] + Keys.ENTER)
        sent = True
        get_element()

    elif str(message) in str(answers):
        print("msg" + answers[0])
        print("match")
        get_element()

    elif str(message) in "admin-start":
        input_box[0].send_keys(answers[4] + Keys.ENTER)
        get_element()

    elif str(message) in "admin-stop":
        input_box[0].send_keys("bot stoped " + Keys.ENTER)
        bot_stop(message)


    else:
        input_box[0].send_keys(answers[1] + Keys.ENTER)
        sent = True
        sleep(1)





def get_element():
    # finding green dot
    greendot = driver.find_elements(By.CLASS_NAME, "_1pJ9J")
    if (greendot):
        greendot[-1].click()
        get_message()
    else:
        get_message()


def get_message():
    # message

    lastmessage = driver.find_elements(By.CLASS_NAME, "_1Gy50")
    message = lastmessage[-1].text
    message = message.lower()

    print(message)

    if (message):
        sleep(2)
        send_message(message)
        get_element()


get_element()