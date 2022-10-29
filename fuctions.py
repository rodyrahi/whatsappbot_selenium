import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import schedule
import time
validity = 30
find = True
stop = False
fill = False
valid_days = 1
current_question = []

def genrate_code():
    validity_code = int(random.randint(0,1000000000000))
    return validity_code











# options = Options()
# options.add_argument('--profile-directory=Profile 6')
# options.add_argument(
#     "user-data-dir=C:\\Users\\home\\AppData\\Local\\Google\\Chrome\\User Data\\")  # Path to your chrome profile
# driver = webdriver.Chrome(executable_path="C:\dev\chromedriver\chromedriver.exe", options=options)
#
#
