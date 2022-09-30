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



def last_message():
    lastmessage = driver.find_elements(By.CLASS_NAME, '_1Gy50')

    message = lastmessage[-1].text
    message = str(message.lower())

    return message




class reply():


    def __init__(self, question=None,
                 option_1=None, option_2=None, option_3=None, option_4=None,
                 reply_1=None, reply_2=None, reply_3=None, reply_4=None):
        self.question = str(question)
        self.option_1 = str(option_1)
        self.option_2 = str(option_2)
        self.option_3 = str(option_3)
        self.option_4 = str(option_4)
        self.reply_1 = reply_1
        self.reply_2 = reply_2
        self.reply_3 = reply_3
        self.reply_4 = reply_4
        print(reply_1)
        # self.command = str(command).lower()

    def give_reply(self):


        if last_message() == self.question:
            sleep(1)
            get_element()

        elif last_message() == self.option_1:

            reply().reply_1

        elif last_message() == self.option_2:
            reply().reply_2.give_reply()
            print("2")
        elif last_message() == self.option_3:
            reply().reply_3.give_reply()
            print("3")
        elif last_message() == self.option_4:
            reply().reply_4.give_reply()
            print("4")
        elif last_message() == "not recognised please type hi to start":
            sleep(2)
            get_element()
        else:
            xpath_input = '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]'
            input_box = driver.find_elements(By.XPATH, xpath_input)
            input_box[0].send_keys("Not recognised please type hi to start" + Keys.ENTER)
            get_element()
        if not last_message() == self.question:
            xpath_input = '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]'
            input_box = driver.find_elements(By.XPATH, xpath_input)
            input_box[0].send_keys(self.question + Keys.ENTER)
    def name_reply(self):
        return last_message()






question_3 = reply(question='hi'+"how you doin" )
question_2 = reply(question='whats your name ', reply_1=question_3)
quetion_1 = reply(question='heybro', option_1='hey', reply_1=question_2.give_reply())