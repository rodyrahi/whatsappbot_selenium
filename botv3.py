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
from selenium.webdriver.chrome.options import Options
import os
import sys

sys.setrecursionlimit(10 ** 6)

funcs.validity = 30

contacts = []
filepath = r'C:\Users\trivendra\PycharmProjects\whatsappbot'

def dec():
    print("-ve")
    funcs.validity -= 1


options = Options()
options.add_argument('--profile-directory=Person 1')
options.add_argument(
    "user-data-dir=C:\\Users\\trivendra\\AppData\\Local\\Google\\Chrome\\User Data\\")  # Path to your chrome profile
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


intro = ['hey', 'hello' , 'hi' , 'hii' , 'hola' , 'heyy' ]


def Schedulecall():
    try:
        url = 'https://web.whatsapp.com/send?phone=+918109204371+&text='+get_contact()
        driver.get(url)
        sleep(3)
        click_btn = driver.find_element(By.XPATH,
                                        '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[2]/button')
        click_btn.click()
        get_element()
    except:
        sleep(1)
        get_element()


def element(url):
    element = driver.find_element(By.XPATH, url)

    return element



def get_contact():
    contact = element('//*[@id="main"]/header/div[2]/div/div').text
    # contact = contact.split()
    # contact = contact[-2] + contact[-1]

    return contact

    # if contact_save.new_contact():
    #     driver.execute_script('''window.open("https://www.google.com", "_blank")''')



    # print(name_box)


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
        get_element()
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


"How to earn upto 30000/-  to 40000/- per month from Social media"

"😇 Work From Home 😇"

"👇🏻👇🏻👇🏻"

"PRESENTATION VIDEO"

"https://youtu.be/PfJuuQJvGjM"

'Watch the full presentation without any distractions and get back to me by typing "INTERESTED" or "NOT INTERESTED"'
'😇'

'My Instagram Handle 👇🏻'
'https://instagram.com/deepsuccessss?igshid=YmMyMTA2M2Y='


"I've earned more than 12 LAKH+ in 12 months by just using social media for 2-3 hours everyday.",

'So watch it till the very end and after you have watched the full video'

"Message me I'd be happy to help you out! 😇"

"Note: Message me within 24 hours otherwise I won't be able to help you out. I hope you value the given time. 🥰"

])


question_1 = questions(message=[
    "Hey I'm Sugar "
])
question_2 = questions(message=[
    "1. Interested",
    "2. Not Interested"
])
question_3 = questions(message=[

    "1. Did watched the video",
    "2. Did not watched the video",


])
question_4 = questions(message=[
    'Which Package?',
    'To chose a Option use 1,2',
    '1. Start Directly',
    '2. I have a query'
])
question_5 = questions(message=[
    'To chose a Option use "1" or "2"',
    '1. I have Money Problem',
    '2. Self Doubt',
    '3. How to Earn Through Leads Guru?',
    '4. Trust Issue'
])
question_6 = questions(message=[
    "1. Trust Issue With Me?",
    '2. Trust Issue with Company',

])
question_7 = questions(message=[
    'I have limited slots',
    '1. Start Directly',
    '2. I have a query',
    '3. Ok will Confirm Tomorrow'
])
question_1b = questions(message=[
    '1. Platinum Package',
    '2. Gold Package'

])
question_2b = questions(message=[
    'How would you like to pay?',
    '1. pay me',
    '2. Affliate link',
    '3. Money Problem'
])
question_3b = questions(message=[
    '1. Will Arrange my money',
    '2. I want to Start with SILVER'
])
question_4b = questions(message=[
    '1. Give me more time ',
    '2. Gold ',
    '3. Silver'
])
question_5b = questions(message=[
    '1. Platinum',
    '2. Gold ',
    '3. Silver',
])
question_6b = questions(message=[


"https://leadsguru.in/?ref=Deepanshu29"
"1. Open the above link in your browser." 
'2. Click on "Get Started Now"'
"3. Choose the course (Silver/Gold/Platinum)"
'4. Click on "Buy Now"'
"5. Fill all your details and take screenshot of username and password"
'6. Click on "Instamojo" for UPI or card payment'
"7. Send me screenshot after doing payment successfully 😊👍🏻"

])
question_7b = questions(message=[


    "Phonpe Gpay Paytm"
    "Same number (8619202808)"
    "Send me screenshot after payment 😊"

])

silver_disadvantage = questions(message=[
'''
Silver lite course hai
Jada kuch seekhne ko bhi nahi milega
Commission bhi kam hai
And you won't be able to attend my mentorship sessions in silver'''
])

call = questions(message=[
    '5. Schedule a Call'

])

Schedule_call = questions(message=[
    'Your call has been Scheduled'
    'You will be contacted Soon !!!'
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

    get_element()


def send_message():
    # get_contact()
    if not last_message() == last2nd_message():
        if not funcs.stop:
            if not get_contact() in contacts:
                print(get_contact())
                if last_message() in intro:
                    question_1.send_next()
                    presentation_video.send_next()
                    question_2.send()
                elif last2nd_message() == question_2.message[-1].lower():
                    if last_message() ==  "1":
                        question_3.send()
                    if last_message() == "2":
                        end()


                elif last2nd_message() == question_3.message[-1].lower():
                    if last_message()=="1":
                        question_4.send()

                    if last_message() =="2":
                        presentation_video.send_next()
                        question_7.send()
                elif last2nd_message() == question_4.message[-1].lower():
                    if last_message() == "1":
                        question_1b.send()
                    if last_message() == "2":
                        question_5.send_next()
                        call.send()

                elif last2nd_message() == question_5.message[-1].lower():
                    if last_message() == "1":
                        send_file(filepath +r'\voicemails\money_problem.ogg')
                        question_4.send()
                    if last_message() == "2":
                        send_file( filepath+r'\voicemails\self_dout.ogg')
                        question_4.send()
                    if last_message() == "3":
                        print(filepath+r'\voicemails\way_to_earn.ogg')
                        send_file(filepath+r'\voicemails\way_to_earn.ogg')
                        question_4.send()
                    if last_message() == "4":
                        question_6.send()
                elif last2nd_message() == call.message[-1].lower():
                    if last_message() == "5":
                        Schedule_call.send_next()
                        sleep(1)
                        Schedulecall()


                elif last2nd_message() == question_6.message[-1].lower():
                    if last_message() == "1" or last_message() == "2":
                       # trust issue  --------------------------------------
                        send_file(filepath+r'\voicemails\trust_issue.ogg')

                        question_2.send()



                # section-2 -----------------------------------------------------------------
                elif last2nd_message() == question_7.message[-1].lower():
                    if last_message() == "1":
                        question_1b.send()
                    if  last_message() == "2":
                        question_5.send()
                    if last_message()=="3":
                        unrecognised.send()

                elif last2nd_message() == question_1b.message[-1].lower():
                    if last_message()=="1":
                        question_2b.send()
                    if last_message() == "2":
                        send_file(filepath+r'\voicemails\plat_pitch.ogg')
                        question_2b.send()


                # payment------------------------------------------------------------
                elif last2nd_message() == question_2b.message[-1].lower():
                    if last_message() == "1":
                        contact_save.insert_contact(get_contact())
                        contact_save.contacts = get_contact()
                        question_7b.send()
                    if last_message() == "2":
                        question_6b.send()
                    if last_message() == "3":
                        question_3b.send()
                        # question_9.send()
                elif last2nd_message() == question_3b.message[-1].lower():
                    if last_message() == "1":
                        question_4b.send()
                    if last_message() == "2":
                        send_file(filepath+"\screenshots\gold_ss.jpeg")
                        send_file(filepath+"\screenshots\plat_ss.jpeg")
                        sleep(1)
                        question_4b.send()
                elif last2nd_message() == question_4b.message[-1].lower() and last_message() == "yes":
                    if last_message() == "1":
                        question_7.send()
                    if last_message() == "2":
                        question_2b.send()
                    if last_message() =="3":
                        silver_disadvantage.send_next()
                        question_5b.send()
                elif last2nd_message() == question_5b.message[-1].lower():
                    if last_message() == "1" or last_message() == "2" or last_message() =="3":
                        question_2b.send()



                # bot stop ----------------------------------------------------------------------------------
                elif last_message() == "admin-stop":
                    stop_bot.send_next()
                    funcs.stop = True
                else:
                    unrecognised.send()
                    get_element()

                sleep(1)
                get_element()
            else:
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

            # if not elements() in contacts:
            if (greendot):
                parent = greendot[0].find_element(By.XPATH , "..").find_element(By.XPATH , "..").find_element(By.XPATH , "..").find_element(By.XPATH , "..")
                parent = parent.text.split()
                print(parent[0])
                cont_check = contact_save.new_contact(parent[0])

                if cont_check:

                    greendot[-1].click()
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
            #     get_element()
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
