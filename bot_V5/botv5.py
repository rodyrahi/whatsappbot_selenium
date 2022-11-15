from difflib import SequenceMatcher

import schedule
import time

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import contact_save
import fuctions as funcs
from selenium.webdriver import Keys
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from dateutil.parser import *
import gc

import os
import sys

sys.setrecursionlimit(10 ** 6)

funcs.validity = 30

contacts = []
filepath = os.getcwd()

user = os.getlogin()


def dec():
    print("-ve")
    funcs.validity -= 1


options = Options()
options.add_argument('--profile-directory=Person 1')
options.add_argument(
    "user-data-dir=C:\\Users\\" + user + "\\AppData\\Local\\Google\\Chrome\\User Data\\")  # Path to your chrome profile
# driver = webdriver.Chrome(executable_path="C:\dev\chromedriver\chromedriver.exe", options=options)
driver = webdriver.Chrome("C:\dev\chromedriver\chromedriver.exe", options=options)
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

intro = ['hey', 'hello', 'hi', 'hii', 'hola', 'heyy']


class Schedulecall():
    def __init__(self, m=None):
        self.message = m

    def send(self):
        try:
            url = 'https://web.whatsapp.com/send?phone=+918109204371+&text=' + get_contact() + ' ' + self.message
            driver.get(url)
            sleep(10)
            click_btn = driver.find_element(By.XPATH,'//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[2]/button')
            click_btn.click()
            sleep(1)

        except:
            sleep(1)
            funcs.find = True


def get_contact():
    element = driver.find_element(By.XPATH, '//*[@id="main"]/header/div[2]/div/div')
    contact = element.text
    return contact


class save_contact():

    def send(self):
        contact_save.insert_contact(get_contact())
        contact_save.contacts = get_contact()


class Questions():

    def __init__(self, message, op1=None, op2=None, op3=None, op4=None, op5=None , op6=None):
        self.m = message
        self.op1 = op1
        self.op2 = op2
        self.op3 = op3
        self.op4 = op4
        self.op5 = op5
        self.op6 = op6

    def opt_check(self):

        print(f"running opt_check of Q:{self.m}")
        if last_message() == "1" and self.op1:
            print(f"last_message():{last_message()} is equal to '1'")
            for q in self.op1:
                q.send()

        elif last_message() == "2" and self.op2:
            print(f"last_message():{last_message()} is equal to '2'")
            for q in self.op2:
                q.send()

        elif last_message() == "3" and self.op3 :
            print(f"last_message():{last_message()} is equal to '3'")
            for q in self.op3:
                q.send()
        elif last_message() == "4" and self.op4:
            print(f"last_message():{last_message()} is equal to '4'")
            for q in self.op4:
                q.send()
        elif last_message() == "5" and self.op5:
            print(f"last_message():{last_message()} is equal to '5'")
            for q in self.op5:
                q.send()
        elif last_message() == "6" and self.op6:
            print(f"last_message():{last_message()} is equal to '5'")
            for q in self.op6:
                q.send()
        else:
            if is_new_message() and last_message() in intro:
                question_1.send()
                presentation_video.send()
                question_2.send()
            else :
                if is_new_message():
                    self.send()


    def send(self):
        for x in self.m:
            xpath_input = '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]'
            input_box = driver.find_elements(By.XPATH, xpath_input)
            driver.execute_script(
                f'''
                          const text = `{x}`;
                          const dataTransfer = new DataTransfer();
                          dataTransfer.setData('text', text);
                          const event = new ClipboardEvent('paste', {{
                            clipboardData: dataTransfer,
                            bubbles: true
                          }});
                          arguments[0].dispatchEvent(event)
                          ''',
                input_box[0])
            input_box[0].send_keys(Keys.ENTER)

        sleep(1)


presentation_video = Questions(message=[

'''
How to earn upto 30000/-  to 40000/- per month from Social media
😇 Work From Home 😇
👇🏻👇🏻👇🏻
PRESENTATION VIDEO
https://youtu.be/PfJuuQJvGjM
Watch the full presentation without any distractions and get back to me by typing "INTERESTED" or "NOT INTERESTED"
😇
My Instagram Handle 👇🏻
https://instagram.com/deepsuccessss?igshid=YmMyMTA2M2Y=
*I've earned more than 12 LAKH+ in 12 months by just using social media for 2-3 
hours everyday.*
So watch it till the very end and after you have watched the full video
Message me I'd be happy to help you out! 😇
Note: Message me within 24 hours otherwise I won't be able to help you out. 
I hope you value the given time. 🥰
'''

])

presentation_link = Questions(message=[
    '''
PRESENTATION VIDEO
https://youtu.be/PfJuuQJvGjM
    '''

])

question_1 = Questions(message=[
    "Hey I'm SUGAR (Virtual Assistant) "
])
question_2 = Questions(message=[
    'To choose an Option TYPE 1 or 2',
    '''
1. INTERESTED
2. NOT INTERESTED
'''

])
question_3 = Questions(message=[
    'HAVE YOU WATCHED THE VIDEO ?',
    '''
1. YES
2. NOT YET
'''

])
question_4 = Questions(message=[
    'WHICH PACKAGE WOULD YOU LIKE TO CHOOSE ? ',
    'To choose an Option TYPE 1 , 2 , 3 or 4 ',
    '''
1. PLATINUM PACKAGE 
2. GOLD PACKAGE 
3. I HAVE MONEY PROBLEM
4. I HAVE A QUERY
'''

])

question_5 = Questions(message=[
    'To choose an Option TYPE 1 , 2 , 3 , 4 or 5',

    '1. I HAVE MONEY PROBLEM',
    '2. SELF DOUBT',
    '3. HOW TO EARN THROUGH LEADSGURU?',
    '4. TRUST ISSUE',
    '5. I HAVE ANOTHER QUERY',
    '6. WHAT TO DO AFTER BUYING THE PACKAGE'
])
question_6 = Questions(message=[
    'To choose an Option TYPE 1 or 2 ',
    '''
1. TRUST ISSUE WITH ME ?
2. TRUST ISSUE WITH COMPANY?
    '''

])
insta_profile = Questions(message=[
    '''
    My Instagram Handle 👇🏻
    https://instagram.com/deepsuccessss?igshid=YmMyMTA2M2Y=
    '''
])
question_7 = Questions(message=[
    """
I've limited slots in my group
I get hundreds of interested people daily on my WhatsApp about this business but I take only limited people and provide  them my personal mentorship so that they can start earning as soon as possible. 
So, kindly confirm me by Tomorrow if you're starting. 😊👍🏻
""",
    'To choose an Option TYPE 1 , 2 , 3 or 4 ',
    '''
1. PLATINUM PACKAGE 
2. GOLD PACKAGE 
3. I HAVE DOUBTS
4. I WILL CONFIRM TOMORROW
'''
])
question_1b = Questions(message=[
    'To choose an Option TYPE 1 or 2 '
    '1. PLATINUM PACKAGE ',
    '2. GOLD PACKAGE '

])
question_2b = Questions(message=[
    'HOW WOULD YOU LIKE TO PAY?',
    '1. PAY ME DIRECTLY',
    '2. PAY USING AFFILIATE LINK'

])
money_problem = Questions(message=[
    '3. I HAVE MONEY PROBLEM'
])
question_3b = Questions(message=[
    'To choose an Option TYPE 1 or 2 ',
    '''
1. I WILL ARRANGE MONEY
2. I WANT TO START WITH SILVER
'''
])
question_4b = Questions(message=[
    'To choose an Option TYPE 1 , 2 or 3 ',
    '1. GOLD PACKAGE ',
    '2. SILVER PACKAGE ',
    '3. I NEED MORE TIME'

])
question_5b = Questions(message=[
    'To choose an Option TYPE 1 , 2 or 3 ',
    '1. PLATINUM PACKAGE ',
    '2. GOLD ',
    '3. SILVER ',
])
question_6b = Questions(message=[

    '''
https://leadsguru.in/?ref=Deepanshu29"
1. Open the above link in your browser. 
2. Click on "Get Started Now"
3. Choose the course (Silver/Gold/Platinum)"
4. Click on "Buy Now"
5. Fill all your details and take screenshot of username and password"
6. Click on "Instamojo" for UPI or card payment
7. Send me screenshot after doing payment successfully 😊👍🏻
'''

])
question_7b = Questions(message=[

    '''
Phonpe Gpay Paytm
Same number (8619202808)
Send me screenshot after payment 😊
'''

])
continue_with_gs = Questions(message=[
    '''
DO YOU STILL WANT TO CONTINUE WITH GOLD OR SILVER?
1. YES
2. NO    
'''


])

silver_disadvantage = Questions(message=[
    '''
Silver lite course hai
Jada kuch seekhne ko bhi nahi milega
Commission bhi kam hai
And you won't be able to attend my mentorship sessions in silver
'''
])

call = Questions(message=[
    '1. SCHEDULE A CALL "it might take a while"'

])

Schedule_call = Questions(message=[
    'Your call has been Scheduled'
    'You will be contacted Soon !!!'
])

unrecognised = Questions(message=[
    "PLEASE TYPE TYPE A CORRECT OPTION OR TYPE 'HEY' TO START AGAIN",
])
stop_bot = Questions(message=[
    'Bot is stopped'
])
start_bot = Questions(message=[
    'bot-started'
])
validity = Questions(message=[
    'your validity is over please re subscribe'
])
admin_commands = Questions(message=[
    'you are admin'
])
end = Questions(message=[
    'thanks for giving your time :)'
])

current_question = question_1


def is_matched(a, b):
    r = SequenceMatcher(a=a.lower(), b=b.lower()).ratio()
    print(r)
    print(a,b)

    if r >= 0.9:

        return True

    return False


def is_new_message():
    return not last_message() == bot_last_message().lower()


class send_file():
    def __init__(self, filepath=None):
        self.filepath = filepath

    def send(self):
        print(self.filepath)
        image_url = '/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div/span[2]/div/div[1]/div[2]/div/span/div/div/ul/li[1]/button/input'
        attach_url = '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[1]/div[2]/div/div'
        send_button_url = '/html/body/div[1]/div/div/div[2]/div[2]/span/div/span/div/div/div[2]/div/div[2]/div[2]/div/div'
        attach_box = driver.find_element(By.XPATH, attach_url)
        attach_box.click()
        image_box = driver.find_element(By.XPATH, image_url)
        image_box.send_keys(self.filepath)
        sleep(1)
        send_button = driver.find_element(By.XPATH, send_button_url)
        send_button.click()
        sleep(2)

    # question_15.send()


def bot_last_message():

    lastmessage = driver.find_elements(By.CLASS_NAME, 'message-out')

    if lastmessage:
        lastmessage = lastmessage[-1].find_element(By.CLASS_NAME, '_1Gy50')
        message = lastmessage.text
        print("inside bot last message " + message)

        return message
    else:
        return None
    # else:
    #     question_1.send()
    #     presentation_video.send()
    #     question_2.send()


def last_message():
    lastmessage = driver.find_elements(By.CLASS_NAME, '_1Gy50')

    message = lastmessage[-1].text
    message = str(message.lower())

    return message


question_2.op1 = [question_3]
question_2.op2 = [end , Schedulecall(m='is not intrested')]

question_3.op1 = [question_4]
question_3.op2 = [presentation_link, question_3]

question_4.op1 = [question_2b, money_problem]
question_4.op2 = [question_2b, money_problem]
question_4.op3 = [send_file(filepath= filepath + r'\voicemails\money_problem.ogg') ,question_3b]
question_4.op4 = [question_5]

money_problem.op1 = [send_file(filepath=filepath + r'\voicemails\after_sale.ogg'), question_7b,
                     Schedulecall(m='lead is ready to pay'), save_contact]
money_problem.op2 =[question_6b]
money_problem.op3 =[question_3b]

question_5.op1 = [send_file(filepath= filepath + r'\voicemails\money_problem.ogg') , question_4]
question_5.op2 = [send_file(filepath=filepath + r'\voicemails\self_dout.ogg') , question_4]
question_5.op3 = [send_file(filepath=filepath + r'\voicemails\way_to_earn.ogg') , question_4]
question_5.op4 = [question_6]
question_5.op5 = [call]
question_5.op6 = [send_file(filepath=filepath + r'\voicemails\after_sale.ogg') , question_4]

call.op1 = [Schedulecall(m='wants to talk to you '),save_contact]

question_6.op1 = [send_file(filepath=filepath + r'\voicemails\trust_issue.ogg') ,  insta_profile ,question_2 ]
question_6.op2 = [send_file(filepath=filepath + r'\voicemails\trust_issue.ogg')  , insta_profile , question_2]

question_7.op1 = [question_2b]
question_7.op2 = [send_file(filepath=filepath + r'\voicemails\plat_pitch.ogg') , question_1b]
question_7.op3 =[question_5]
question_7.op4 = [question_2 , question_7]

question_1b.op1=[question_2b]
question_1b.op2=[send_file(filepath=filepath+r'\voicemails\plat_pitch.ogg'),question_2b]

question_2b.op1 =[send_file(filepath=filepath + r'\voicemails\after_sale.ogg'), question_7b,
                     Schedulecall(m='lead is ready to pay'), save_contact]
question_2b.op2 = [question_6b]

question_3b.op1 = [question_4b]
question_3b.op2 = [send_file(filepath=filepath + "\screenshots\gold_ss.jpeg") , send_file(filepath=filepath + "\screenshots\plat_ss.jpeg") , send_file(filepath=filepath + r'\voicemails\plat_pitch.ogg') , continue_with_gs]

continue_with_gs.op1 = [question_4b]
continue_with_gs.op2 = [question_5b]

question_4b.op1 =[question_2b]
question_4b.op2 = [silver_disadvantage,question_5b]
question_4b.op3 = [question_7]

question_5b.op1  = [question_2b]
question_5b.op2  = [question_2b]
question_5b.op3  = [question_2b]




question_list = []

for obj in gc.get_objects():
    if isinstance(obj, Questions):
        question_list.append(obj)


def find_question():
    bot_message = bot_last_message()
    if bot_message:
        for q in question_list:
            if is_matched(q.m[-1], bot_message):

                q.opt_check()
                return True
        return False
    else:
        return False


def send_message():
    # get_contact()
    if bot_last_message() == None:
        question_1.send()
        presentation_video.send()
        question_2.send()
    elif not last_message() == bot_last_message():
        if not funcs.stop:
            if not contact_save.new_contact(get_contact()):
                # find_question()

                if not find_question() and is_new_message():
                    print("this")
                    question_1.send()
                    presentation_video.send()
                    question_2.send()

        else:
            if last_message() == "admin-start":
                start_bot.send()
                funcs.stop = False
                funcs.find = True
            funcs.find = True

    else:
        funcs.find = True


def find_date(parent):
    # for x in parent:
    #     try:
    #         if len(x) > 4 and bool(parse(x)):
    #             print("True")
    #             return True
    #
    #     except:
    #         continue
    # print("False")
    return False


def get_element():
    # finding green dot

    if funcs.validity > 0:
        try:
            sleep(1)
            greendot = driver.find_elements(By.CLASS_NAME, "_1pJ9J")

            # if not elements() in contacts:
            if (greendot):

                parent = greendot[0].find_element(By.XPATH, "..").find_element(By.XPATH, "..").find_element(By.XPATH,
                                                                                                            "..").find_element(
                    By.XPATH, "..")
                parent = parent.text.split()

                cont_check = contact_save.new_contact(parent[0].lower())

                find_date(parent)

                if not find_date(parent):

                    if not cont_check and not is_new_message():

                        greendot[-1].click()
                        # sleep(1)
                        send_message()
                    else:
                        # sleep(1)
                        send_message()
                else:
                    # sleep(1)
                    send_message()

            else:
                # sleep(1)
                send_message()

        except:
            # sleep(2)
            funcs.find = True
    else:
        print("out")
        greendot = driver.find_elements(By.CLASS_NAME, "_1pJ9J")
        greendot[-1].click()
        message = last_message().split('-')
        print(message)

        if message == code:
            funcs.validity = int(message[2])


code = funcs.genrate_code()

while funcs.find:

    get_element()

