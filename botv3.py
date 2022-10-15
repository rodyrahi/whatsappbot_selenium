import schedule
import time
import contact_save
import fuctions as funcs
from selenium.webdriver import Keys
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.options import Options
import os
import sys

sys.setrecursionlimit(10 ** 6)

funcs.validity = 30


def dec():
    print("-ve")
    funcs.validity -= 1


options = Options()
options.add_argument('--profile-directory=Person 1')
options.add_argument(
    "user-data-dir=C:\\Users\\home\\AppData\\Local\\Google\\Chrome\\User Data\\")  # Path to your chrome profile
driver = webdriver.Chrome(executable_path="C:\dev\chromedriver\chromedriver.exe", options=options)

driver.get('https://web.whatsapp.com')

# fp = webdriver.FirefoxProfile('/Users/<username>/Library/Application Support/Firefox/Profiles/')

# options = Options()
# options.add_argument('--profile-directory=Profile 6')
# options.add_argument(
#     "user-data-dir=C:\dev")
# fp = webdriver.FirefoxProfile(r'C:\Users\Home\AppData\Roaming\Mozilla\Firefox\Profiles\5p8s46q5.kamigo')
# driver = webdriver.Firefox(executable_path=GeckoDriverManager().install() , firefox_profile=fp)
# driver.get('https://web.whatsapp.com')

input("enter")


def element(url):
    element = driver.find_element(By.XPATH , url)
    return element

def get_contact():
    contact = element('//*[@id="main"]/header/div[2]/div/div').text
    contact = contact.split()
    contact = contact[-2] + contact[-1]
    contact_save.contacts = contact
    if contact_save.new_contact():
        driver.execute_script('''window.open("https://www.google.com", "_blank")''')






def get_name_no():
    # contact = element('//*[@id="main"]/header/div[2]/div/div').click()
    contact_url = '//*[@id="main"]/header/div[2]/div/div/span'
    name_url = '//*[@id="app"]/div/div/div[5]/span/div/span/div/div/section/div[1]/div[2]/div'
    close_url = '//*[@id="app"]/div/div/div[5]/span/div/span/div/header/div/div[1]/button'


    contact_box = driver.find_element(By.XPATH, contact_url)
    if contact_box:
        contact_box.click()
        sleep(0.5)
    name_box = driver.find_element(By.XPATH, name_url)
    if name_box:
        name_box = name_box.text
        name_box = name_box.split()
        name = name_box[0].split("~")[1]
    close = driver.find_element(By.XPATH, close_url)
    if close:
        close.click()
    if name:
        return name
    else:
        name = "person"
        return name

    # print(name_box)

class questions():

    def __init__(self, message):
        self.message = message

    def send(self):
        xpath_input = '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]'
        input_box = driver.find_elements(By.XPATH, xpath_input)
        for x in self.message:
            sleep(1)
            input_box[0].send_keys(x + Keys.ENTER)
        sleep(1)
        get_element()

    def send_next(self):
        xpath_input = '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]'
        input_box = driver.find_elements(By.XPATH, xpath_input)
        for x in self.message:
            sleep(1)
            input_box[0].send_keys(x + Keys.ENTER)





question_1 = questions(message=[
    'Hey! Welcome to Leads Guru :)',
    'Get ready to learn how to make money online with a few quick steps..',
    'Hey I am Sugar :)',
    "What's your name ? "
])
question_2 = questions(message=[
    "That's Great!!",
    "Are you already into Affiliate Marketing/Web marketing?"
])
question_3 = questions(message=[

    "That's Great! Which platform are you currently using?",
    'To chose a Option use 1,2,3 or 4',
    '1. BizGurukul',
    '2. LeadsArk',
    '3. Other',
    '4. I am not in Affiliate Marketing Business'
])
question_4 = questions(message=[
    'Ok Great !',
    'How much Commission you are getting on your Platform ?',
    'To chose a Option use 1,2',
    '1. 50 % Plus',
    '2. 75 % Plus'
])
question_5 = questions(message=[
    'No worries, before we go ahead let me ask you which is a greater figure?',
    'To chose a Option use "1" or "2"',
    '1. 10,000',
    '2. 20,000'
])
question_6 = questions(message=[
    "That's Very less.. ",
    'Do you get total commission, daily in your bank account ?',
    'YES or NO'
])
question_7 = questions(message=[
    'Do you Know? Your platform is taking advantage of your hard work.',
    'Leads Guru is giving More than 90% commission to its affiliate with Daily withdrawal.',
    'Are you Excited to start Affiliate  Marketing with LeadsGuru ?',
    'Type YES'
])
question_8 = questions(message=[
    'Are you sure 10,000 is greater than 20,000?'
])
question_9 = questions(message=[
    'Well, you know what? I can help you Earn that greater figure of 20,000 within a week? JOKES APART!',
    'Are you ready for that cha-ching sound of money? Say YES'
])
question_10 = questions(message=[
    'Now! PLEASE NOTE that this is not a get-rich-quick scheme or a magic pill.',
    'However, if you work exactly according to our strategies you will make a very handsome amount. I promise. YES?'
])
question_11 = questions(message=[
    'So, Affiliate marketing is an Online business in which anyone can promote or recommend products and earn commissions based on their sales.'
])
question_12 = questions(message=[
    'But why you need to start Affiliate Marketing with Leads Guru ?',
    'You will get :',
    '-90% Commission',
    '-Same Day Payout',
    '-2 Tier Passive Income',
    '-You DO NOT need to Create Product',
    '-Valuable Courses to Upgrade Skills',
    'Shall we go ahead? Something interesting is waiting for you.YES?'
])
question_13 = questions(message=[
    'Leads Guru is one of the best Platform That Provides multiple Premium Courses and An Opportunity To Become financial Free by Joining as affiliate.',
    '1. I would like to know about the courses.',
    '2. I want to see Earning Proofs'
])
question_14 = questions(message=[
    'Make a call on 99999999'
])
question_15 = questions(message=[
    'Like to know about the courses.',
    'Courses with Pricing',
    'Say YES to Schedule call'
])
unrecognised = questions(message=[
    'Please Type "Hey" to get Started!',
])
stop_bot = questions(message=[
    'Bot is stopped'
])
start_bot = questions(message=[
    'bot-started'
])
validity = questions(message=[
    'your validity is over please re subscribe'
])
question_2a = questions(message=[
    'Nice Meeting you Mate :) ',
    'What do you Do ?'
])








def send_image():
    filepath = r'C:\Users\Home\Desktop\WhatsApp Ptt 2022-10-12 at 10.18.56 PM.ogg'
    image_url = '/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div/span[2]/div/div[1]/div[2]/div/span/div/div/ul/li[1]/button/input'
    attach_url = '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[1]/div[2]/div/div'
    send_button_url = '/html/body/div[1]/div/div/div[2]/div[2]/span/div/span/div/div/div[2]/div/div[2]/div[2]/div/div'
    attach_box = driver.find_element(By.XPATH, attach_url)
    attach_box.click()
    image_box = driver.find_element(By.XPATH, image_url)
    image_box.send_keys(filepath)
    sleep(1)
    send_button = driver.find_element(By.XPATH, send_button_url)
    send_button.click()
    sleep(1)
    question_15.send()


def last2nd_message():
    lastmessage = driver.find_elements(By.CLASS_NAME, 'message-out')

    if lastmessage:
        message = lastmessage[-1].text
        message = message.split()
        message = message[:-2]
        message = ' '.join(message)
        message = str(message.lower())
        print(message)

        return message
    else:
        unrecognised.send()


def last_message():
    lastmessage = driver.find_elements(By.CLASS_NAME, '_1Gy50')

    message = lastmessage[-1].text
    message = str(message.lower())

    return message


def end():
    message = [
        "thanks for giving your time :)"
    ]
    xpath_input = '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]'
    input_box = driver.find_elements(By.XPATH, xpath_input)
    input_box[0].send_keys(message[0] + Keys.ENTER)

    get_element()


def send_message():
    get_contact()
    if not last_message() == last2nd_message():
        if not funcs.stop:
            if last_message() == "hey":

                funcs.fill = True

                question_1.send()

            elif last2nd_message() == question_1.message[-1].lower():
                if last_message():
                    question_2a.send_next()

            elif last2nd_message() == question_2a.message[-1].lower():
                if last_message():
                    funcs.fill = False
                    question_2.send()




            elif last2nd_message() == question_2.message[-1].lower():
                if last_message() == "yes":
                    question_3.send()
                if last_message() == "no":
                    question_5.send()

            elif last2nd_message() == question_10.message[-1].lower():
                if last_message() == "yes":
                    question_11.send_next()
                    question_12.send()


            # for answer to be yes----------------------------------------------------------
            elif last2nd_message() == question_3.message[-1].lower():
                if last_message() == "1" or last_message() == "2" or last_message() == "3":
                    question_4.send()
                if last_message() == "4":
                    question_5.send()

            elif last2nd_message() == question_4.message[-1].lower():
                if last_message() == "1" or last_message() == "2":
                    question_6.send()

            elif last2nd_message() == question_6.message[-1].lower():
                if last_message() == "yes" or last_message() == "no":
                    question_7.send()

            elif last2nd_message() == "type yes" and last_message() == "yes":

                question_12.send()

            # for answer to be no------------------------------------------------------------
            elif last2nd_message() == question_5.message[-1].lower():
                if last_message() == "1":
                    question_8.send_next()
                    question_9.send()
                if last_message() == "2":
                    question_9.send()
            elif last2nd_message() == question_9.message[-1].lower():
                if last_message() == "yes":
                    question_10.send()
                if last_message() == "no":
                    question_11.send_next()
                    question_12.send()

            elif last2nd_message() == question_12.message[-1].lower() and last_message() == "yes":
                question_13.send()
            elif last2nd_message() == question_13.message[-1].lower():
                if last_message() == "1":
                    sleep(1)
                    question_14.send()
                if last_message() == "2":
                    sleep(1)
                    send_image()
            # elif last2nd_message() == "courses with pricing" and last_message() == "yes" and last_message() == "yes":
            #
            #     question_14.send()
            elif last2nd_message() == question_15.message[-1].lower() and last_message() == "yes":
                question_14.send()


            # bot stop ----------------------------------------------------------------------------------
            elif last_message() == "admin-stop":
                stop_bot.send_next()
                funcs.stop = True
            else:
                print(funcs.fill)
                if funcs.fill:
                    print("fill")


                    question_2a.send()
                    # elif last2nd_message() == question_2a.message[-1].lower():
                    #     question_2.send()
                if not funcs.fill:
                    unrecognised.send()
                    get_element()

            sleep(1)
            get_element()

        else:
            if last_message() == "admin-start":
                start_bot.send_next()
                funcs.stop = False
                get_element()
            get_element()

    else:
        get_element()


def get_element():
    # finding green dot
    print(funcs.validity)

    if funcs.validity > 0:
        try:
            sleep(1)
            greendot = driver.find_elements(By.CLASS_NAME, "_1pJ9J")

            if (greendot):
                greendot[-1].click()
                sleep(1)

                send_message()

                # get_name_no()
            else:
                sleep(1)
                send_message()
        except:
            sleep(2)
            get_element()
    else:
        print("out")
        greendot = driver.find_elements(By.CLASS_NAME, "_1pJ9J")
        greendot[-1].click()
        message = last_message().split('-')
        print(message)

        if message == code:
            funcs.validity = int(message[2])

        sleep(10)
        get_element()


code = funcs.genrate_code()
print(code)
get_element()
sleep(1)
