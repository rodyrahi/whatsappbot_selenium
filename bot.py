
from selenium.webdriver import Keys
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


validity_days = 30
name = None
options = Options()
options.add_argument('--profile-directory=Profile 6')
options.add_argument(
    "user-data-dir=C:\\Users\\home\\AppData\\Local\\Google\\Chrome\\User Data\\")  # Path to your chrome profile
driver = webdriver.Chrome(executable_path="C:\dev\chromedriver\chromedriver.exe", options=options)

driver.get('https://web.whatsapp.com')

input("enter")

def get_name(name):
    answer = ['Hey! ' , 'Are you already into Affiliate Marketing/Web marketing?']
    lastmessage = driver.find_elements(By.CLASS_NAME, "_1Gy50")
    message = lastmessage[-1].text
    message = message.lower()
    if str(message) == "what's your name ?":
        sleep(1)
        get_name(name)
        get_element(name)
    else:
        name = message
        xpath_input = '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]'
        input_box = driver.find_elements(By.XPATH, xpath_input)
        input_box[0].send_keys(answer[0] + name + Keys.ENTER)
        input_box[0].send_keys(answer[1] + name + Keys.ENTER)
        get_element(name)



def get_intro(name):
    answer = [
                """
                Hey! Welcome to LeadsGuru :)
                Get ready to learn how to make money online with a few quick steps..
                My Name is Gautam
                What's Your Name ?
                """
            ]

    xpath_input = '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]'
    input_box = driver.find_elements(By.XPATH, xpath_input)
    input_box[0].send_keys( answer[0] + Keys.ENTER)
    get_name(name)

def comission(name):
    answer = [
        '2. (75% Plus)',
        ", that's Very less..",
        """
        Do you get total commission, daily in your bank account ?
        1.yes
        2.no
        """,
        'Do you Know',
        'Your platform is taking advantage of your hard work.'
    ]
    commands = [
        '1',
        '2',
        'yes',
        'no'
    ]
    lastmessage = driver.find_elements(By.CLASS_NAME, "_1Gy50")
    message = lastmessage[-1].text
    message = message.lower()
    if str(message) == str(answer[0]):
        sleep(2)
        comission(name)
    elif str(message) == str(commands[0]) or str(message) == str(commands[1]) :
        xpath_input = '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]'
        input_box = driver.find_elements(By.XPATH, xpath_input)
        input_box[0].send_keys( name + answer[1] + Keys.ENTER)
    elif str(message) == str(commands[2]) or str(message) == str(commands[3]):
        xpath_input = '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]'
        input_box = driver.find_elements(By.XPATH, xpath_input)
        input_box[0].send_keys( answer[5]+name + answer[6] + Keys.ENTER)
    else:
        sleep(2)
        comission(name)




def platform_choice(name):
    answer = [
        'ok!',
        '4.i am not in affiliate marketing business',
        'please choose a correct answer please ',
        """
        How much Commission you are getting on your Platform ?
        1. (50% Plus)
        2. (75% Plus)
        """

    ]
    commands = [
        '1',
        '2',
        '3',
        '4'
    ]
    lastmessage = driver.find_elements(By.CLASS_NAME, "_1Gy50")
    message = lastmessage[-1].text
    message = message.lower()
    if str(message) == commands[0] or str(message) == commands[1] or str(message) == commands[2]:
        xpath_input = '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]'
        input_box = driver.find_elements(By.XPATH, xpath_input)
        input_box[0].send_keys(answer[0]+name + Keys.ENTER)
        sleep(1)
        input_box[0].send_keys(answer[3] + Keys.ENTER)
        comission(name)

    elif str(message) == str(answer[2]):
        sleep(1)
        platform_choice(name)
    elif str(message) == str(answer[1]):
        sleep(1)
        platform_choice(name)
    else:
        xpath_input = '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]'
        input_box = driver.find_elements(By.XPATH, xpath_input)
        input_box[0].send_keys(answer[2] + Keys.ENTER)
        sleep(1)
        platform_choice(name)








def conversation(name):
    answer = [
        'are you already into affiliate marketing/web marketing?',
        """
        That's Great! Which platform are you currently using?
        Type 1 , 2 ,3 or 4
        1.BizGurukul
        2.LeadsArk
        3.Other
        4.I am not in Affiliate Marketing Business
        """


              ]
    commands = [
        'yes',
        'no',
    ]
    lastmessage = driver.find_elements(By.CLASS_NAME, "_1Gy50")
    message = lastmessage[-1].text
    message = message.lower()
    if str(message) == answer[0]:
        sleep(1)
        conversation(name)

    elif str(message) == str(commands[0]):
        xpath_input = '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]'
        input_box = driver.find_elements(By.XPATH, xpath_input)
        input_box[0].send_keys(answer[1] + Keys.ENTER)
        sleep(1)
        platform_choice(name)
    conversation(name)







def get_message(name):
    answer = ['please type "hi" to get started' , "What's Your Name ?"]
    intro = [
            'hi',
            'hey',
            'hello',
            'hii',

        ]
    # message

    lastmessage = driver.find_elements(By.CLASS_NAME, "_1Gy50")
    message = lastmessage[-1].text
    message = message.lower()
    # answer = answer[0].lower()

    if name == None:
        if (message):
            print(message)
            if str(message) == str(answer[0]):
                sleep(2)
                get_element(name)
            elif str(message) in str(intro):

                get_intro(name)
            else:
                print( message + answer[0])
                xpath_input = '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]'
                input_box = driver.find_elements(By.XPATH, xpath_input)
                input_box[0].send_keys(answer[0] + Keys.ENTER)
                get_element(name)
    else:
        conversation(name)










def get_element(name):
    # finding green dot
    greendot = driver.find_elements(By.CLASS_NAME, "_1pJ9J")
    if (greendot):
        greendot[-1].click()
        get_message(name)
    else:
        get_message(name)




get_element(name)

#
# def day_des(validity_days):
#     validity_days -= 1
#     if validity_days > 0:
#
#         get_element()
#     else:
#         url = 'https://web.whatsapp.com/send?phone=+918109204371&text= validity is over'
#         driver.get(url)
#         sleep(10)
#         dots_url = "/html/body/div[1]/div/div/div[4]/div/header/div[3]/div/div[2]"
#         info_url = "/html/body/div[1]/div/span[4]/div/ul/div/div/li[1]/div[1]"
#         contact_url = '//*[@id="app"]/div/div/div[5]/span/div/span/div/div/section/div[1]/div[2]'
#
#         dots = driver.find_element(By.XPATH, dots_url)
#         dots.click()
#         info = driver.find_element(By.XPATH, info_url)
#         info.click()
#         contact = driver.find_element(By.XPATH, contact_url)
#
#         print(contact.text)
#
#
# # schedule.every().day.do(day_des(validity_days))
#
#
# # send_mail.send_mail()
#
# input("enter")
#
#
# def bot_stop(message):
#     if str(message) in "admin-start":
#         get_element(name)
#     else:
#         sleep(3)
#         lastmessage = driver.find_elements(By.CLASS_NAME, "_1Gy50")
#         message = lastmessage[-1].text
#         message = message.lower()
#         bot_stop(message)
#
#
#
# def get_name(message):
#
#     name = message
#     xpath_input = '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]'
#     input_box = driver.find_elements(By.XPATH, xpath_input)
#     input_box[0].send_keys("hey" + message + Keys.ENTER)
#     get_element(name)
#
# def get_intro(message):
#     xpath_input = '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]'
#     input_box = driver.find_elements(By.XPATH, xpath_input)
#     answer = [
#         """
#         Hey! Welcome to LeadsGuru :)
#         Get ready to learn how to make money online with a few quick steps..
#         My Name is Gautam
#         What's Your Name ?
#         """,
#         'Please type "hi" to get started'
#     ]
#     intro = [
#         'hi',
#         'hey',
#         'hello',
#         'hii',
#
#     ]
#     if str(message) in str(intro):
#         input_box[0].send_keys(answer[0] + Keys.ENTER)
#
#         lastmessage = driver.find_elements(By.CLASS_NAME, "_1Gy50")
#         message = lastmessage[-1].text
#         message = message.lower()
#         if str(message) in str(intro) or str(message) in str(answer):
#             get_name(message)
#         else:
#             get_element(name)
#     elif str(message) in str(answer):
#         get_element(name)
#     else:
#         input_box[0].send_keys(answer[1] + Keys.ENTER)
#
#
#
# def send_message(message):
#     # geting input
#     answers = [
#         """
#         Hey! Welcome to LeadsGuru :)
#         Get ready to learn how to make money online with a few quick steps..
#         My Name is Gautam
#         What's Your Name ?
#         """,
#         'hey',
#         """ Not recognised !!
#         please type "hi" to get started """,
#         'please chose a way of placing order type "home" for home delivery ',
#         'thanks for placing order',
#         'bot started',
#     ]
#
#     commands = [
#
#         'place order',
#         'home',
#
#     ]
#
#     xpath_input = '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]'
#     input_box = driver.find_elements(By.XPATH, xpath_input)
#
#     if message in str(commands[0]):
#         input_box[0].send_keys(answers[2] + Keys.ENTER)
#         sent = True
#         get_element()
#
#     elif message in str(commands[1]):
#         input_box[0].send_keys(answers[3] + Keys.ENTER)
#         sent = True
#         get_element()
#
#     elif str(message) in str(answers):
#         print("msg" + answers[0])
#         print("match")
#         get_element()
#
#     elif str(message) in "admin-start":
#         input_box[0].send_keys(answers[4] + Keys.ENTER)
#         get_element()
#
#     elif str(message) in "admin-stop":
#         input_box[0].send_keys("bot stoped " + Keys.ENTER)
#         bot_stop(message)
#
#
#     else:
#         input_box[0].send_keys(answers[1] + Keys.ENTER)
#         sleep(1)
#
#
# def get_element(name):
#     # finding green dot
#     greendot = driver.find_elements(By.CLASS_NAME, "_1pJ9J")
#     if (greendot):
#         greendot[-1].click()
#         get_message(name)
#     else:
#         get_message(name)
#
#
# def get_message(name):
#     # message
#
#     lastmessage = driver.find_elements(By.CLASS_NAME, "_1Gy50")
#     message = lastmessage[-1].text
#     message = message.lower()
#
#     print(message)
#
#     if (message):
#
#
#         if name:
#             get_intro(message)
#         else:
#             send_message(message)
#         # send_message(message)
#         # get_element()
#
# name = None
# get_element(name)
