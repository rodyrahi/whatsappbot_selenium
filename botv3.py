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
                       "Type YES"
                       """)
question_8 = questions(message=
                       """
                       Are you sure 10,000 is greater than 20,000?
                       """)
question_9 = questions(message=
                       """
                       Well, you know what? I can help you Earn that greater figure of 20,000 within a week? JOKES APART!
                       Are you ready for that cha-ching sound of money?
                       Say "yes"
                       
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
                       """)



def last2nd_message():

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

        # for answer to be yes----------------------------------------------------------
        elif last2nd_message() == "4. i am not in affiliate marketing business":
            if last_message() == "1" or last_message()== "2" or last_message() == "3":
                question_4.send()
            if last_message() == "4":
                question_5.send()

        elif last2nd_message() == "2. 75 % Plus":
            if last_message() == "1" or last_message()== "2":
                question_6.send()


        elif last2nd_message() == "yes or no":
            if last_message() == "yes" or last_message()== "no":
                question_7.send()

        elif last2nd_message() == "type yes" and last_message() == "yes":
            question_12.send()

        # for answer to be no------------------------------------------------------------
        elif last2nd_message() == "2. 20,000":
            if last_message() == "1":
                question_8.send()
            if last_message() == "2":
                question_9.send()
        elif last2nd_message() == "say yes" and last_message() == "yes":
            question_10.send()
        elif last2nd_message() == "however, if you work exactly according to our strategies you will make a very handsome amount. i promise. yes?" and last_message() == "yes":
            question_11.send()
            question_12.send()





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

        greendot[-1].click()
        sleep(1)
        send_message()
    else:
        sleep(1)
        send_message()




get_element()
sleep(2)



