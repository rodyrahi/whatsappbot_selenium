import fuctions as funcs
from selenium.webdriver import Keys
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument('--profile-directory=Profile 6')
options.add_argument(
    "user-data-dir=C:\\Users\\home\\AppData\\Local\\Google\\Chrome\\User Data\\")  # Path to your chrome profile
driver = webdriver.Chrome(executable_path="C:\dev\chromedriver\chromedriver.exe", options=options)

driver.get('https://web.whatsapp.com')

input("enter")

class questions():
    def __init__(self , message):
        self.message = message

    def send(self):
        xpath_input = '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]'
        input_box = driver.find_elements(By.XPATH, xpath_input)
        input_box[0].send_keys(self.message + Keys.ENTER)
        get_element()


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
                       Ok Great
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

def last2nd_message():
    sleep(1)
    lastmessage = driver.find_elements(By.CLASS_NAME, 'message-out')
    message = lastmessage[-1].text

    message = message.split()
    message = message[:-2]
    message = ' '.join(message)

    # message = message


    message = str(message.lower())
    print(message)

    return message


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
        if last_message() == "hey":
            question_1.send()
        elif last2nd_message() == "are you ready ?" and last_message() == "yes":
            question_2.send()
        elif last2nd_message() == "are you ready ?" and last_message() == "no":
            end()

        elif last2nd_message() == "are you already into affiliate marketing/web marketing?" and last_message() == "yes":
            question_3.send()
        elif last2nd_message() == "are you already into affiliate marketing/web marketing?" and last_message() == "no":
            question_5.send()


        elif last2nd_message() == "4. i am not in affiliate marketing business":
            if last_message() == "1" or last_message()== "2" or last_message() == "3":
                question_4.send()
            if last_message() == "4":
                question_5.send()



        else:
            xpath_input = '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]'
            input_box = driver.find_elements(By.XPATH, xpath_input)
            input_box[0].send_keys("please type hey" + Keys.ENTER)

            sleep(1)
            get_element()
    else:
        get_element()








def get_element():

    # finding green dot

    greendot = driver.find_elements(By.CLASS_NAME, "_1pJ9J")
    if (greendot):
        sleep(1)
        greendot[-1].click()
        send_message()
    else:
        sleep(1)
        send_message()




get_element()



