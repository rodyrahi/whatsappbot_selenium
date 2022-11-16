import os
from difflib import SequenceMatcher
from time import sleep
import gc
from selenium.webdriver import Keys

import contactsave
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

user = os.getlogin()

options = Options()
options.add_argument('--profile-directory=Person 1')
options.add_argument(
    "user-data-dir=C:\\Users\\" + user + "\\AppData\\Local\\Google\\Chrome\\User Data\\")
driver = webdriver.Chrome("C:\dev\chromedriver\chromedriver.exe", options=options)
driver.get('https://web.whatsapp.com')

qls = []

input("start")


def is_matched(a, b):
    r = SequenceMatcher(a=a, b=b).ratio()
    if r >= 0.8:
        return True

    return False


def is_new_message():
    return not last_message() == bot_last_message()


def bot_last_message():
    sleep(0.5)
    lastmessage = driver.find_elements(By.CLASS_NAME, 'message-out')
    # lastmessage =lastmessage.find_element(By.CLASS_NAME,'_1Gy50')

    if lastmessage:
        lastmessage = lastmessage[-1].find_element(By.CLASS_NAME, '_1Gy50')
        message = lastmessage.text
        print("inside bot last message " + message)
        # message = message.split()
        #
        # message = message[:-2]
        # message = ' '.join(message)
        # message = str(message.lower())

        return message
    else:
        print("unrecoginised")


def last_message():
    lastmessage = driver.find_elements(By.CLASS_NAME, '_1Gy50')

    message = lastmessage[-1].text

    message = str(message.lower())

    return message


class Question():
    def __init__(self, message, op1=None, op2=None, op3=None):
        self.m = str(message.lower())
        self.op1 = op1
        self.op2 = op2
        self.op3 = op3
        self.visited = False

    def opt_check(self):

        print(f"running opt_check of Q:{self.m}")
        if last_message() == "1":
            print(f"last_message():{last_message()} is equal to '1'")
            self.op1.send()
            self.visited = False
        if last_message() == "2":
            print(f"last_message():{last_message()} is equal to '2'")
            self.op2.send()
            self.visited = False
        if last_message() == "3":
            print(f"last_message():{last_message()} is equal to '3'")
            self.op3.send()
            self.visited = False

    def find(self, x):
        x = str(x)
        m = str(self.m)

        print(f'We or on question : {self.m}', x)

        if is_matched(self.m, x):
            # print(f'self.m : {self.m} is equal to x={x}')
            self.opt_check()
            return True
        elif self.op1 and is_matched(self.op1.m, x):
            # print(f'self.m.op1 : {self.op1.m} is equal to x={x}')
            self.op1.opt_check()
            return True
        elif self.op2 and is_matched(self.op2.m, x):
            # print(f'self.m.op2 : {self.op2.m} is equal to x={x}')
            self.op2.opt_check()
            return True
        elif self.op3 and is_matched(self.op3.m, x):
            # print(f'self.m.op3 : {self.op3.m} is equal to x={x}')
            self.op3.opt_check()
            return True
        else:
            if not self.visited:
                # print(f'{x} is not equal to any option and itself')
                if self.op1:
                    # print('Going inside find of op1')
                    self.op1.find(x)
                if self.op2:
                    # print('Going inside find of op2')
                    self.op2.find(x)
                if self.op3:
                    # print('Going inside find of op3')
                    self.op3.find(x)
        return False

    def _find(self, x):
        x = str(x)
        m = str(self.m)
        if self.m == x:
            # print("yes")
            return True
        elif self.op1 and self.op1.m == x:

            return True
        elif self.op2 and self.op2.m == x:

            return True
        elif self.op3 and self.op3.m == x:

            return True
        else:
            if self.op1:
                self.op1.find(x)
            if self.op2:
                self.op2.find(x)
            if self.op3:
                self.op3.find(x)

        return False

    def traverse(self):
        print("traversing")
        print("new messge" + str(is_new_message()))
        print(self.find(bot_last_message()))
        if is_new_message() and not self.find(bot_last_message()):
            self.send()

        print(bot_last_message(), self.m)

        if bot_last_message() == self.m:
            if last_message() == "1":
                if self.op1:
                    self.op1.traverse()
            if last_message() == "2":
                if self.op2:
                    print("op2")
                    self.op2.traverse()
            if last_message() == "3":
                if self.op3:
                    self.op3.traverse()
        else:
            pass

        return False

    def send(self):

        print(f'Inside send function of Q:"{self.m}"')
        xpath_input = '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]'
        input_box = driver.find_elements(By.XPATH, xpath_input)
        driver.execute_script(
            f'''
                                              const text = `{self.m}`;
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


q4 = Question(message="ok")
q3 = Question(message="""no problem 
1. yes
2. no""")
q2 = Question(message="""you like python?
1. yes
2. NO""")
q1 = Question(message="""are you into computers?
1. yes 
2. No""")

q1.op1 = q2
q1.op2 = q3

q2.op1 = q4
q2.op2 = q3

q4.op1 = q1


question_list=[]

for obj in gc.get_objects():
    if isinstance(obj, Question):
        question_list.append(obj)









def send_message():
    # s = question.get_objects()
    # print(s)
    print(f'running q1 find with x as {bot_last_message()}')
    # print(f'q1 find is {q1.find(bot_last_message())}')
    if bot_last_message() is None or last_message() in ['hello', 'hii', 'hi', 'hey',]:
        if is_new_message():
            q1.send()

    # q1.find(bot_last_message())
    for q in question_list:
        if is_matched(q.m,bot_last_message()):
            q.opt_check()


def get_element():
    # finding green dot

    try:
        sleep(1)
        greendot = driver.find_elements(By.CLASS_NAME, "_1pJ9J")

        # if not elements() in contacts:
        if greendot:
            parent = greendot[0].find_element(By.XPATH, "..").find_element(By.XPATH, "..").find_element(By.XPATH,
                                                                                                        "..").find_element(
                By.XPATH, "..")
            parent = parent.text.split()

            cont_check = contact_save.new_contact(parent[0].lower())

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

    except:
        sleep(2)


while True:
    sleep(1)
    print('rescanning')
    get_element()
