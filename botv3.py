import schedule
import time
import fuctions as funcs
from selenium.webdriver import Keys
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import os
import sys

sys.setrecursionlimit(10 ** 6)

funcs.validity = 30


def dec():
    print("-ve")
    funcs.validity -= 1



options = Options()
options.add_argument('--profile-directory=Profile 6')
options.add_argument(
    "user-data-dir=C:\\Users\\home\\AppData\\Local\\Google\\Chrome\\User Data\\")  # Path to your chrome profile
driver = webdriver.Chrome(executable_path="C:\dev\chromedriver\chromedriver.exe", options=options)

driver.get('https://web.whatsapp.com')

input("enter")


class questions():
    def __init__(self, message):
        self.message = message

    def send(self):
        xpath_input = '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]'
        input_box = driver.find_elements(By.XPATH, xpath_input)
        input_box[0].send_keys(self.message + Keys.ENTER)
        sleep(1)
        get_element()

    def send_next(self):
        xpath_input = '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]'
        input_box = driver.find_elements(By.XPATH, xpath_input)
        input_box[0].send_keys(self.message + Keys.ENTER)


question_1 = questions(message=
                       """
                       Hey! Welcome to LeadsGuru :)
                       Get ready to learn how to make money online with a few quick steps..
                       My Name is “Aman”
                       Are You Ready ?
                       """)
question_2 = questions(message=
                       """
                       That's Great!!
                       Are you already into Affiliate Marketing/Web marketing?
                       """)
question_3 = questions(message=
                       """
                       That's Great! Which platform are you currently using?
                       1. BizGurukul
                       2. LeadsArk
                       3. Other
                       4. I am not in Affiliate Marketing Business
                       """)
question_4 = questions(message=
                       """
                       Ok Great !
                       How much Commission you are getting on your Platform ?
                       1. 50 % Plus
                       2. 75 % Plus
                       """)
question_5 = questions(message=
                       """
                       No worries, before we go ahead let me ask you which is a greater figure?
                       1. 10,000
                       2. 20,000

                       """)
question_6 = questions(message=
                       """
                       That's Very less..                       
                       Do you get total commission, daily in your bank account ?
                       YES or NO 
                       """)
question_7 = questions(message=
                       """
                       Do you Know? Your platform is taking advantage of your hard work.
                       LeadsGuru is giving More than 90% commission to its affiliate with Daily withdrawal.
                       Are you Excited to start Affiliate  Marketing with LeadsGuru ?
                       Type YES
                       """)
question_8 = questions(message=
                       """
                       Are you sure 10,000 is greater than 20,000?
                       """)
question_9 = questions(message=
                       """
                       Well, you know what? I can help you Earn that greater figure of 20,000 within a week? JOKES APART!
                       Are you ready for that cha-ching sound of money? Say YES
                       """)
question_10 = questions(message=
                        """
                       Now! PLEASE NOTE that this is not a get-rich-quick scheme or a magic pill.
                       However, if you work exactly according to our strategies you will make a very handsome amount. I promise. YES?

                       """)
question_11 = questions(message=
                        """
                       So, Affiliate marketing is an Online business in which anyone can promote or recommend products and earn commissions based on their sales.
                       """)
question_12 = questions(message=
                        """
                       But why you need to start Affiliate Marketing with LeadsGuru ?
                       You will get :
                        -90% Commission
                        -Same Day Payout
                        -2 Tier Passive Income
                        -You DO NOT need to Create Product
                        -Valuable Courses to Upgrade Skills
                        Shall we go ahead? Something interesting is waiting for you.YES?
                       """)
question_13 = questions(message=
                        """
                       LeadsGuru is one of the best Platform That Provides multiple Premium Courses and An Opportunity To Become financial Free by Joining as affiliate.
                       1. I would like to know about the courses.
                       2. I want to see Earning Proofs
                       """)
question_14 = questions(message=
                        """
                       Make a call on 99999999
                       """)
question_15 = questions(message=
                        """
                       Like to know about the courses.
                       Courses with Pricing
                       Say YES to Schedule call
                       """)
unrecognised = questions(message=
                         """
                       Please Type "Hey" to get Started!
                       """)
stop_bot = questions(message=
                     """
                       Bot is stopped
                       """)
start_bot = questions(message=
                      """
                       bot-started
                       """)
validity = questions(message=
                     """
                       your validity is over please re subscribe
                       """)


def send_image():
    filepath = r'C:\Users\Home\Desktop\kamingo_icon.png'
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
    if not last_message() == last2nd_message():
        if not funcs.stop:
            if last_message() == "hey":
                sleep(1)
                question_1.send()
            elif last2nd_message() == "are you ready ?" and last_message() == "yes":
                sleep(1)
                question_2.send()
            elif last2nd_message() == "are you ready ?" and last_message() == "no":
                end()

            elif last2nd_message() == "are you already into affiliate marketing/web marketing?" and last_message() == "yes":
                sleep(1)
                question_3.send()
            elif last2nd_message() == "are you already into affiliate marketing/web marketing?" and last_message() == "no":
                sleep(1)
                question_5.send()

            # for answer to be yes----------------------------------------------------------
            elif last2nd_message() == "4. i am not in affiliate marketing business":
                if last_message() == "1" or last_message() == "2" or last_message() == "3":
                    sleep(1)
                    question_4.send()
                if last_message() == "4":
                    sleep(1)
                    question_5.send()

            elif last2nd_message() == "2. 75 % plus":
                if last_message() == "1" or last_message() == "2":
                    sleep(1)
                    question_6.send()

            elif last2nd_message() == "yes or no":
                if last_message() == "yes" or last_message() == "no":
                    sleep(1)
                    question_7.send()

            elif last2nd_message() == "type yes" and last_message() == "yes":
                sleep(1)
                question_12.send()

            # for answer to be no------------------------------------------------------------
            elif last2nd_message() == "2. 20,000":
                if last_message() == "1":
                    sleep(1)
                    question_8.send_next()
                    question_9.send()
                if last_message() == "2":
                    sleep(1)
                    question_9.send()
            elif last2nd_message() == "are you ready for that cha-ching sound of money? say yes" and last_message() == "yes":
                sleep(1)
                question_10.send()
            elif last2nd_message() == "however, if you work exactly according to our strategies you will make a very handsome amount. i promise. yes?" and last_message() == "yes":
                sleep(1)
                question_11.send_next()
                question_12.send()
            elif last2nd_message() == "shall we go ahead? something interesting is waiting for you.yes?" and last_message() == "yes":
                sleep(1)
                question_13.send()
            elif last2nd_message() == "2. i want to see earning proofs":
                if last_message() == "1":
                    sleep(1)
                    question_14.send()
                if last_message() == "2":
                    sleep(1)
                    send_image()
            elif last2nd_message() == "courses with pricing" and last_message() == "yes" and last_message() == "yes":
                sleep(1)
                question_14.send()
            elif last2nd_message() == "say yes to schedule call" and last_message() == "yes":
                question_14.send()


            # bot stop ----------------------------------------------------------------------------------
            elif last_message() == "admin-stop":
                stop_bot.send_next()
                funcs.stop = True
            else:
                unrecognised.send()
                sleep(1)
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
    schedule.every(1).seconds.do(dec)
    # finding green dot
    print(funcs.validity)

    if funcs.validity > 0:
        sleep(1)
        greendot = driver.find_elements(By.CLASS_NAME, "_1pJ9J")

        if (greendot):
            greendot[-1].click()
            sleep(1)
            send_message()
        else:
            sleep(1)
            send_message()
    else:
        print("out")
        message = last_message().split('-')
        message = message[1]

        if message == code:
            funcs.validity = int(message[2])

        sleep(10)
        get_element()


code = funcs.genrate_code()
print(code)
get_element()
sleep(2)
