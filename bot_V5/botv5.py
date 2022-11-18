import csv
from difflib import SequenceMatcher
import pandas as pd
from defs import *
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





options = Options()
options.add_argument('--profile-directory=Person 1')
options.add_argument(
    "user-data-dir=C:\\Users\\" + user + "\\AppData\\Local\\Google\\Chrome\\User Data\\")
driver = webdriver.Chrome("C:\dev\chromedriver\chromedriver.exe", options=options)
driver.get('https://web.whatsapp.com')



input("enter")
print(filepath)

intro = ['hey', 'hello', 'hi', 'hii', 'hola', 'heyy', 'hy', 'hlo', 'hallo']


class Schedulecall():
    def __init__(self, m=None):
        self.message = m

    def send(self):
        try:
            url = 'https://web.whatsapp.com/send?phone=+918109204371+&text=' + get_contact() + ' ' + self.message
            driver.get(url)
            sleep(10)
            click_btn = driver.find_element(By.XPATH,
                                            '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[2]/button')
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



    def insert_contact(self, cont):
        filename = 'contacts.csv'
        # rows = [cont +'-'+ date.today() , cont]
        rows = [str(cont).lower()]

        # writing to csv file
        with open(filename, 'a', newline='') as csvfile:
            # creating a csv writer object
            csvwriter = csv.writer(csvfile)

            # writing the data rows
            csvwriter.writerow(rows)

    def new_contact(self ,cont):
        filename = 'contacts.csv'
        with open(filename, 'r', newline='') as f:

            reader = csv.reader(f)
            for row in reader:

                if cont in row:
                    return True
                else:
                    continue

            return False

    def drop_col(self, cont):
        data = pd.read_csv('contacts.csv')
        data = data.drop(labels=cont, axis=1)
    def send(self):
        print("save number")
        self.insert_contact(get_contact())
        self.contacts = get_contact()

save_contact_ = save_contact()
class Questions():

    def __init__(self, message, op1=None, op2=None, op3=None, op4=None, op5=None, op6=None):
        self.m = message
        self.op1 = op1
        self.op2 = op2
        self.op3 = op3
        self.op4 = op4
        self.op5 = op5
        self.op6 = op6

    def opt_check(self):
        if not last_message() == bot_last_message():
            lm = last_message()



            if lm == "1" and self.op1:

                for q in self.op1:
                    q.send()

            elif lm == "2" and self.op2:

                for q in self.op2:
                    q.send()

            elif lm == "3" and self.op3:

                for q in self.op3:
                    q.send()
            elif lm == "4" and self.op4:

                for q in self.op4:
                    q.send()
            elif lm == "5" and self.op5:

                for q in self.op5:
                    q.send()
            elif lm == "6" and self.op6:

                for q in self.op6:
                    q.send()
            else:
                if last_message() == "1" or last_message()=="2" or last_message()=="3" or last_message() == "4" or last_message() == "5" or last_message()=="6":

                    return
                else:
                    print("not matched")

                    if is_new_message() and lm in intro:
                        send_file(filepath=filepath + r'\voicemails\intro_note.ogg').send()

                        presentation_video.send()
                        question_2.send()
                    else:
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

PRESENTATION VIDEO
https://youtu.be/PfJuuQJvGjM
Watch the full presentation without any distractions and get back to me by typing "INTERESTED" or "NOT INTERESTED"
😇
My Instagram Handle 👇🏻
https://instagram.com/deepsuccessss?igshid=YmMyMTA2M2Y=

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
Silver lite Course hai...
Jada kuch Seekhne ko bhi Nahi Milega
Commission bhi Kam hai..
And you Won't be able to Attend my Mentorship Sessions in Silver.
'''
])

call = Questions(message=[
    '''
SCHEDULE A CALL "it might take a while"
1. YES
2. NO
'''

])
call_scheduled = Questions(message=[
    '''
Your Call has been scheduled! You will be contacted within 12 hours. 😇  
'''

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
    'Bot is started'
])
validity = Questions(message=[
    'your validity is over please re subscribe'
])
admin_commands = Questions(message=[
    'you are admin'
])
single_stop = Questions(message=[
    'bot is stopped for the client'
])
single_start = Questions(message=[
    'bot is started for the client'
])
end = Questions(message=[
    'thanks for giving your time :)'
])

current_question = question_1


def is_matched(a, b):
    r = SequenceMatcher(a=a.lower(), b=b.lower()).ratio()


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


        return message
    else:
        return None
    # else:
    #     question_1.send()
    #     presentation_video.send()
    #     question_2.send()


def last_message():
    lastmessage = driver.find_elements(By.CLASS_NAME, '_1Gy50')

    if lastmessage:

        message = lastmessage[-1].text
        message = str(message.lower())

        return message

    else:
        return False


question_2.op1 = [question_3]
question_2.op2 = [end, Schedulecall(m='is not intrested')]

question_3.op1 = [question_4]
question_3.op2 = [presentation_link, question_3]

question_4.op1 = [question_2b, money_problem]
question_4.op2 = [question_2b, money_problem]
question_4.op3 = [send_file(filepath=filepath + r'\voicemails\money_problem.ogg'), question_3b]
question_4.op4 = [question_5]

money_problem.op1 = [save_contact() ,send_file(filepath=filepath + r'\voicemails\after_sale.ogg'), question_7b , Schedulecall(m="lead is ready to pay")]
money_problem.op2 = [[save_contact() ,send_file(filepath=filepath + r'\voicemails\after_sale.ogg'), question_6b , Schedulecall(m="lead is ready to pay using link")]]
money_problem.op3 = [question_3b]

question_5.op1 = [send_file(filepath=filepath + r'\voicemails\money_problem.ogg'), question_4]
question_5.op2 = [send_file(filepath=filepath + r'\voicemails\self_dout.ogg'), question_4]
question_5.op3 = [send_file(filepath=filepath + r'\voicemails\way_to_earn.ogg'), question_4]
question_5.op4 = [send_file(filepath=filepath + r'\voicemails\trust_issue.ogg'), insta_profile, question_2]
question_5.op5 = [call]
question_5.op6 = [send_file(filepath=filepath + r'\voicemails\after_sale.ogg'), question_4]

call.op1 = [call_scheduled, Schedulecall(m='wants to talk to you '), save_contact()]
call.op2 = [question_4]
# question_6.op1 = [send_file(filepath=filepath + r'\voicemails\trust_issue.ogg') ,  insta_profile ,question_2 ]
# question_6.op2 = [send_file(filepath=filepath + r'\voicemails\trust_issue.ogg')  , insta_profile , question_2]

question_7.op1 = [question_2b]
question_7.op2 = [send_file(filepath=filepath + r'\voicemails\plat_pitch.ogg'), question_1b]
question_7.op3 = [question_5]
question_7.op4 = [question_2]

question_1b.op1 = [question_2b]
question_1b.op2 = [send_file(filepath=filepath + r'\voicemails\plat_pitch.ogg'), question_2b]

question_2b.op1 = [send_file(filepath=filepath + r'\voicemails\after_sale.ogg'), question_7b, save_contact(),
                   Schedulecall(m='lead is ready to pay')]
question_2b.op2 = [question_6b,save_contact(),
                   Schedulecall(m='lead is ready to pay')]

question_3b.op1 = [question_4b]
question_3b.op2 = [send_file(filepath=filepath + "\screenshots\gold_ss.jpeg"),
                   send_file(filepath=filepath + "\screenshots\plat_ss.jpeg"),
                   send_file(filepath=filepath + r'\voicemails\plat_pitch.ogg'), continue_with_gs]

continue_with_gs.op1 = [question_4b]
continue_with_gs.op2 = [question_5b]

question_4b.op1 = [question_2b]
question_4b.op2 = [silver_disadvantage, question_5b]
question_4b.op3 = [question_7]

question_5b.op1 = [question_2b]
question_5b.op2 = [question_2b]
question_5b.op3 = [question_2b]

question_list = []

for obj in gc.get_objects():
    if isinstance(obj, Questions):
        question_list.append(obj)


def find_question():
    bot_message = bot_last_message()
    if bot_message:
        for q in question_list:
            if is_matched(q.m[-1], bot_message):
                if last_message():
                    q.opt_check()
                    return True
        return False
    else:
        return False


def send_message():
    if last_message() == 'admin-stop':
        stop_bot.send()
        funcs.stop = True


    if "single-stop" in last_message():
        message = str(last_message()).split()
        message = message[0]
        contact_save.insert_contact(message)
        contact_save.contacts = get_contact()

        single_stop.send()

        print(message)

    if "single-start" in last_message():
        message = str(last_message()).split()
        message = message[0]
        save_contact().drop_col(message)


        single_start.send()

        print(message)

    else:
        if bot_last_message() == None:
            send_file(filepath=filepath + r'\voicemails\intro_note.ogg').send()
            presentation_video.send()
            question_2.send()
        elif not last_message() == bot_last_message():
            if not funcs.stop:
                if not contact_save.new_contact(get_contact()):
                    # find_question()

                    if not find_question() and is_new_message():

                        send_file(filepath=filepath + r'\voicemails\intro_note.ogg').send()
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


def find_parents(greendot):
    for dots in greendot:
        parent = dots.find_element(By.XPATH, "..").find_element(By.XPATH, "..").find_element(
            By.XPATH,
            "..").find_element(
            By.XPATH, "..")
        parent = parent.find_element(By.CLASS_NAME, "_3q9s6")
        print(parent.text)
        if find_no(str(parent.text.lower())) and not parent.text.lower() == "my personal":
            return dots

    return None






def get_element():
    # finding green dot
    if funcs.stop is True:
        if last_message() == 'admin-start':
            start_bot.send()
            funcs.stop = False

    # get_contact()
    if funcs.stop is False:

        try:

            sleep(1)
            greendot = driver.find_elements(By.CLASS_NAME, "_1pJ9J")

            # if not elements() in contacts:
            if (greendot):



                parent = greendot[0].find_element(By.XPATH, "..").find_element(By.XPATH, "..").find_element(By.XPATH,
                                                                                                            "..").find_element(
                    By.XPATH, "..")
                parent = parent.find_element(By.CLASS_NAME , "_3q9s6")
                parent = parent.text.split()
                print(parent)

                cont_check = contact_save.new_contact(parent[0].lower())



                dot = find_parents(greendot)
                if dot:

                    if not cont_check and not is_new_message():
                        dot.click()
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


code = funcs.genrate_code()

while funcs.find:
    sleep(1)
    get_element()
