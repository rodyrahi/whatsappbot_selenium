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
print(filepath)

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

print(filepath)

intro = ['hey', 'hello', 'hi', 'hii', 'hola', 'heyy']


def Schedulecall(message):
    try:
        url = 'https://web.whatsapp.com/send?phone=+918109204371+&text=' + get_contact() + ' ' + message
        driver.get(url)
        sleep(3)
        click_btn = driver.find_element(By.XPATH,
                                        '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[2]/button').send_keys(
            Keys.ENTER)
        sleep(1)
        funcs.find = True
    except:
        sleep(1)
        funcs.find = True


def element(url):
    element = driver.find_element(By.XPATH, url)

    return element


def get_contact():
    contact = element('//*[@id="main"]/header/div[2]/div/div').text
    # contact = contact.split()
    # contact = contact[-2] + contact[-1]

    return contact


class questions():

    def __init__(self, message):
        self.message = message

    def send(self):
        for x in self.message:
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
        funcs.find = True

    def send_next(self):
        for x in self.message:
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
            print("xxx")


# def send_next(self):
#         xpath_input = '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]'
#         input_box = driver.find_elements(By.XPATH, xpath_input)
#         for x in self.message:
#             sleep(1)
#             input_box[0].send_keys(x + Keys.ENTER)


presentation_video = questions(message=[

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
I've earned more than 12 LAKH+ in 12 months by just using social media for 2-3 
hours everyday.
So watch it till the very end and after you have watched the full video
Message me I'd be happy to help you out! 😇
Note: Message me within 24 hours otherwise I won't be able to help you out. 
I hope you value the given time. 🥰
'''

])

question_1 = questions(message=[
    "Hey I'm SUGAR (Virtual Assistant) "
])
question_2 = questions(message=[
    'To choose an Option TYPE 1 or 2',
    '1. INTERESTED',
    '2. NOT INTERESTED'

])
question_3 = questions(message=[
    'HAVE YOU WATCHED THE VIDEO ?',
    '1. YES',
    '2. NOT YET'

])
question_4 = questions(message=[
    'WHICH PACKAGE WOULD YOU LIKE TO CHOOSE ? ',
    'To choose an Option TYPE 1 , 2 , 3 or 4 ',
    '1. PLATINUM PACKAGE ',
    '2. GOLD PACKAGE ',
    '3. I HAVE MONEY PROBLEM',
    '4. I HAVE A QUERY'

])

question_5 = questions(message=[
    'To choose an Option TYPE 1 , 2 , 3 , 4 or 5',

    '1. I HAVE MONEY PROBLEM',
    '2. SELF DOUBT',
    '3. HOW TO EARN THROUGH LEADSGURU?',
    '4. TRUST ISSUE',
    '5. I HAVE ANOTHER QUERY'
])
question_6 = questions(message=[
    'To choose an Option TYPE 1 or 2 ',
    '1. TRUST ISSUE WITH ME ?',
    '2. TRUST ISSUE WITH COMPANY?'

])
insta_profile = questions(message=[
    '''
    My Instagram Handle 👇🏻
    https://instagram.com/deepsuccessss?igshid=YmMyMTA2M2Y=
    '''
])
question_7 = questions(message=[
    """
I've limited slots in my group
I get hundreds of interested people daily on my WhatsApp about this business but I take only limited people and provide  them my personal mentorship so that they can start earning as soon as possible. 
So, kindly confirm me by Tomorrow if you're starting. 😊👍🏻
""",
    'To choose an Option TYPE 1 , 2 , 3 or 4 ',
    '1. PLATINUM PACKAGE ',
    '2. GOLD PACKAGE ',
    '3. I HAVE DOUBTS',
    '4. I WILL CONFIRM TOMORROW'
])
question_1b = questions(message=[
    'To choose an Option TYPE 1 or 2 '
    '1. PLATINUM PACKAGE ',
    '2. GOLD PACKAGE '

])
question_2b = questions(message=[
    'HOW WOULD YOU LIKE TO PAY?',
    '1. PAY ME DIRECTLY',
    '2. PAY USING AFFILIATE LINK'

])
money_problem = questions(message=[
    '3. I HAVE MONEY PROBLEM'
])
question_3b = questions(message=[
    'To choose an Option TYPE 1 or 2 ',
    '1. I WILL ARRANGE MONEY',
    '2. I WANT TO START WITH SILVER'
])
question_4b = questions(message=[
    'To choose an Option TYPE 1 , 2 or 3 ',
    '1. GOLD PACKAGE ',
    '2. SILVER PACKAGE ',
    '3. I NEED MORE TIME'

])
question_5b = questions(message=[
    'To choose an Option TYPE 1 , 2 or 3 ',
    '1. PLATINUM PACKAGE ',
    '2. GOLD ',
    '3. SILVER ',
])
question_6b = questions(message=[

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
question_7b = questions(message=[

    '''
    Phonpe Gpay Paytm
    Same number (8619202808)
    Send me screenshot after payment 😊
    '''

])
continue_with_gs = questions(message=[

    "DO YOU STILL WANT TO CONTINUE WITH GOLD OR SILVER? ",
    "1. YES",
    "2. NO"

])

silver_disadvantage = questions(message=[
    '''
        Silver lite course hai
        Jada kuch seekhne ko bhi nahi milega
        Commission bhi kam hai
        And you won't be able to attend my mentorship sessions in silver
    
    '''
])

call = questions(message=[
    '1. SCHEDULE A CALL "it might take a while"'

])

Schedule_call = questions(message=[
    'Your call has been Scheduled'
    'You will be contacted Soon !!!'
])

unrecognised = questions(message=[
    "PLEASE TYPE TYPE A CORRECT OPTION OR TYPE 'HEY' TO START AGAIN",
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
admin_commands = questions(message=[
    'you are admin'
])

current_question = question_1


def send_file(filepath):
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

    # question_15.send()


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

    funcs.find = True


def send_message():
    # get_contact()
    if not last_message() == last2nd_message():
        if not funcs.stop:
            if not contact_save.new_contact(get_contact()):
                print(get_contact())
                if last_message() in intro:
                    if get_contact() == "Rajendra":
                        # bot stop for a single user-----------------------------------------------------------
                        admin_commands.send()
                        print(last_message())


                    else:
                        question_1.send_next()
                        presentation_video.send_next()
                        sleep(1)
                        question_2.send()
                elif last2nd_message() == admin_commands.message[-1].lower():

                    if "single-stop" in last_message():
                        message = str(last_message()).split()
                        message = message[0]
                        contact_save.insert_contact(message)
                        contact_save.contacts = get_contact()

                        sleep(1)
                        Schedulecall(' stoped for -' + message)

                        print(message)

                elif last2nd_message() == question_2.message[-1].lower():
                    funcs.current_question = question_2
                    if last_message() == "1":
                        question_3.send()
                    elif last_message() == "2":
                        end()
                    else:
                        unrecognised.send_next()
                        question_2.send()


                elif last2nd_message() == question_3.message[-1].lower():
                    funcs.current_question = question_3
                    if last_message() == "1":
                        question_4.send()

                    elif last_message() == "2":
                        presentation_video.send_next()
                        question_7.send()
                    else:
                        unrecognised.send_next()
                        question_3.send()
                elif last2nd_message() == question_4.message[-1].lower():
                    funcs.current_question = question_4
                    if last_message() == "1":
                        question_2b.send_next()
                        money_problem.send()
                    elif last_message() == "2":
                        question_2b.send_next()
                        money_problem.send()
                    elif last_message() == "3":
                        question_3b.send()
                    elif last_message() == "4":
                        question_5.send()
                    else:
                        unrecognised.send_next()
                        question_4.send()

                elif last2nd_message() == money_problem.message[-1].lower():
                    if last_message()=="1":
                        contact_save.insert_contact(get_contact())
                        contact_save.contacts = get_contact()
                        send_file(filepath + r'\voicemails\after_sale.ogg')
                        sleep(1)
                        question_7b.send_next()
                        sleep(1)
                        Schedulecall('lead is ready to pay ')
                    if last_message()=="2":
                        question_6b.send()
                    if last_message()=="3":
                        question_3b.send()
                    else:
                        question_4.send_next()
                        money_problem.send()


                elif last2nd_message() == question_5.message[-1].lower():
                    funcs.current_question = question_5
                    if last_message() == "1":
                        send_file(filepath + r'\voicemails\money_problem.ogg')
                        sleep(1)
                        question_4.send()
                    elif last_message() == "2":
                        send_file(filepath + r'\voicemails\self_dout.ogg')
                        sleep(1)
                        question_4.send()
                    elif last_message() == "3":
                        send_file(filepath + r'\voicemails\way_to_earn.ogg')
                        sleep(1)
                        question_4.send()
                    elif last_message() == "4":
                        question_6.send()
                    elif last_message() == "5":
                        call.send()
                    else:
                        unrecognised.send_next()
                        question_5.send()
                elif last2nd_message() == call.message[-1].lower():
                    if last_message() == "1":

                        funcs.current_question = call
                        contact_save.insert_contact(get_contact())
                        contact_save.contacts = get_contact()
                        Schedule_call.send_next()
                        sleep(1)
                        Schedulecall('wants to talk to you ')
                    else:
                        unrecognised.send_next()
                        call.send()

                elif last2nd_message() == question_6.message[-1].lower():
                    funcs.current_question = question_6
                    if last_message() == "1" or last_message() == "2":
                        print("queation 2")
                        # trust issue  --------------------------------------

                        send_file(filepath + r'\voicemails\trust_issue.ogg')
                        sleep(1)
                        question_2.send()
                    else:
                        unrecognised.send_next()
                        question_6.send()



                # section-2 -----------------------------------------------------------------
                elif last2nd_message() == question_7.message[-1].lower():
                    funcs.current_question = question_7
                    if last_message() == "1":
                        question_2b.send()
                    elif last_message() == "2":
                        send_file(filepath + r'\voicemails\plat_pitch.ogg')
                        sleep(1)
                        question_1b.send()
                    elif last_message() == "3":
                        question_5.send()
                    elif last_message() == "4":
                        question_2.send()
                        question_7.send()

                elif last2nd_message() == question_1b.message[-1].lower():
                    funcs.current_question = question_1b
                    if last_message() == "1":
                        question_2b.send()
                    elif last_message() == "2":
                        # send_file(filepath+r'\voicemails\plat_pitch.ogg')
                        question_2b.send()
                    else:
                        unrecognised.send_next()
                        question_1b.send()


                # payment------------------------------------------------------------
                elif last2nd_message() == question_2b.message[-1].lower():
                    funcs.current_question = question_2b
                    if last_message() == "1":
                        print("ready")
                        contact_save.insert_contact(get_contact())
                        contact_save.contacts = get_contact()
                        send_file(filepath + r'\voicemails\after_sale.ogg')
                        sleep(1)
                        question_7b.send_next()
                        sleep(1)
                        Schedulecall('lead is ready to pay ')
                    elif last_message() == "2":
                        question_6b.send()

                        # question_9.send()
                    else:
                        unrecognised.send_next()
                        question_2b.send()
                elif last2nd_message() == question_3b.message[-1].lower():
                    funcs.current_question = question_3b
                    if last_message() == "1":
                        question_4b.send()
                    elif last_message() == "2":
                        send_file(filepath + "\screenshots\gold_ss.jpeg")
                        send_file(filepath + "\screenshots\plat_ss.jpeg")
                        sleep(1)
                        send_file(filepath + r'\voicemails\plat_pitch.ogg')

                        sleep(2)
                        continue_with_gs.send()
                    else:
                        unrecognised.send_next()
                        question_3b.send()
                elif last2nd_message() == continue_with_gs.message[-1].lower():
                    funcs.current_question = continue_with_gs
                    if last_message() == "1":
                        question_4b.send()
                    elif last_message() == "2":
                        question_5b.send()
                    else:
                        unrecognised.send_next()
                        continue_with_gs.send()
                elif last2nd_message() == question_4b.message[-1].lower():
                    funcs.current_question = question_4
                    if last_message() == "1":
                        question_2b.send()
                    elif last_message() == "2":
                        silver_disadvantage.send_next()
                        question_5b.send()
                    elif last_message() == "3":
                        question_7.send()
                    else:
                        unrecognised.send_next()
                        question_4b.send()

                elif last2nd_message() == question_5b.message[-1].lower():
                    funcs.current_question = question_5b
                    if last_message() == "1" or last_message() == "2" or last_message() == "3":
                        question_2b.send()
                    else:
                        unrecognised.send_next()
                        question_5b.send()





                # bot stop ----------------------------------------------------------------------------------
                elif last_message() == "admin-stop":
                    stop_bot.send_next()
                    funcs.stop = True
                else:

                    question_1.send_next()
                    presentation_video.send_next()
                    sleep(1)
                    question_2.send()

                sleep(1)
                funcs.find = True
            else:
                sleep(1)
                funcs.find = True

        else:
            if last_message() == "admin-start":
                start_bot.send_next()
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

                    if not cont_check:

                        greendot[-1].click()
                        sleep(1)
                        send_message()
                    else:
                        sleep(1)
                        send_message()
                else:
                    sleep(1)
                    send_message()

            else:
                sleep(1)
                send_message()
            # else:
            #     sleep(1)
            #     func.find = True
        except:
            sleep(2)
            funcs.find = True
    else:
        print("out")
        greendot = driver.find_elements(By.CLASS_NAME, "_1pJ9J")
        greendot[-1].click()
        message = last_message().split('-')
        print(message)

        if message == code:
            funcs.validity = int(message[2])

        sleep(10)
        funcs.find = True


code = funcs.genrate_code()


while funcs.find:
    
    get_element()
# print(opt._option(last_message() , last2nd_message()))
    sleep(1)
