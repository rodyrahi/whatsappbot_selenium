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


def last_message():
    lastmessage = driver.find_elements(By.CLASS_NAME, '_1Gy50')

    message = lastmessage[-1].text
    message = str(message.lower())

    return message

def question_2():
    xpath_input = '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]'
    input_box = driver.find_elements(By.XPATH, xpath_input)
    input_box[0].send_keys("do you know about dm"+funcs.name+"?" + Keys.ENTER)

    get_element()

def question_1():
    xpath_input = '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]'
    input_box = driver.find_elements(By.XPATH, xpath_input)
    input_box[0].send_keys("hey there whats is your name ?" + Keys.ENTER)
    funcs.got_name = True

    get_element()

def send_message():
    if last_message() == "hey":
        question_1()
    elif last_message() ==  "hey there whats is your name ?":
        sleep(2)
        get_element()
    elif last_message() ==  "please type hey":
        print("stop")
        sleep(2)
        get_element()
    elif last_message() == "hii " + str(funcs.name):
        print("match")
        question_2()
    else:
        if not funcs.got_name:
            xpath_input = '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]'
            input_box = driver.find_elements(By.XPATH, xpath_input)
            input_box[0].send_keys("please type hey" + Keys.ENTER)
            print(funcs.name)
            sleep(2)
            get_element()
        else:
            if not last_message() == "hey there whats is your name ?":
                funcs.name.append(last_message())
                xpath_input = '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]'
                input_box = driver.find_elements(By.XPATH, xpath_input)
                input_box[0].send_keys("hii "+ last_message() + Keys.ENTER)

                funcs.got_name = False
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



