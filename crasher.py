from selenium.webdriver import Keys
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from selenium import webdriver
import pandas
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options




chrome_driver_path = "C:\dev\chromedriver"



# print(excel_data['Message'][0])
options = Options()
options.add_argument('--profile-directory=Profile 5')
options.add_argument(
    "user-data-dir=C:\\Users\\home\\AppData\\Local\\Google\\Chrome\\User Data\\")  # Path to your chrome profile
driver = webdriver.Chrome(executable_path="C:\dev\chromedriver\chromedriver.exe", options=options)


url = 'https://web.whatsapp.com/send?phone=+919589153292&text='
driver.get(url)
input("enter")





def crasher():
    template_parameters = [
        {'name': 'name', 'value': 'Ken'},
        {'name': 'place', 'value': 'Apollo Clinic'},
        {'name': 'date', 'value': '26th Nov 2020 at 10 AM'}
    ]

    # replace whatsapp_number with the whatsapp number you want to send to


    image = open("untitled.png")
    text_file = open("D:/data.txt", "r")

    # read whole file to a string
    data = text_file.read()

    # close file
    text_file.close()
    message = data

    xpath_input = '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]'
    input_box = driver.find_elements(By.XPATH, xpath_input)
    input_box[0].send_keys( template_parameters + Keys.ENTER)

    # driver.find_element(By.XPATH , '/*[@id="main"]/footer/div[1]/div/span[2]/div/div[1]/div[2]/div/div/span').click()
    #
    # driver.find_element(By.CSS_SELECTOR("input[type='file']")).sendKeys("untitled.png")
    #
    # driver.find_element(By.CSS_SELECTOR("span[data-icon='send-light']")).click()



crasher()


# for contact in excel_data['Contact'].tolist():
#     try:
#         url = 'https://web.whatsapp.com/send?phone=' + '+91' + str(contact) + '&text=' + \
#               excel_data['Message'][0]
#         print(url)
#         driver.get(url)
#         while driver.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[2]/button'):
#             click_btn = driver.find_element(By.XPATH,
#                                             '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[2]/button')
#             click_btn.click()
#             break
#
#     except Exception as e:
#         print("Sorry message could not sent to " + str(contact) + e)
#
# print("The script executed successfully.")


# def send_message(contact, message):
#
#
#     # url = 'https://web.whatsapp.com/send?phone=' + '+91' + str(int(contact)) + '&text=' + message
#
#     xpath_input = '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]'
#     input_box = WebDriverWait(driver,time).until(
#         EC.presence_of_element_located((By.XPATH, xpath_input)))
#     message = str(message)
#     encode = message.encode()
#     print(encode)
#     message = encode.decode()
#     print(message)
#     driver.execute_script(
#         f'''
#     const text = `{message}`;
#     const dataTransfer = new DataTransfer();
#     dataTransfer.setData('text', text);
#     const event = new ClipboardEvent('paste', {{
#       clipboardData: dataTransfer,
#       bubbles: true
#     }});
#     arguments[0].dispatchEvent(event)
#     ''',
#         input_box)
#
#     # input_box.send_keys(message+ Keys.ENTER)
#     b_xpath = '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[2]/button'
#     button = driver.find_element(By.XPATH,b_xpath)
#     button.click()
#     print(contact)
#
#
# for contact in contacts:
#     url = 'https://web.whatsapp.com/send?phone=' + '+91' + str(int(contact))
#     driver.get(url)
#     xpath_popup = '//*[@id="app"]/div/span[2]/div/span/div/div/div/div/div/div[2]/div/div'
#     try:
#         popup = WebDriverWait(driver, 10).until(
#             EC.presence_of_element_located((By.XPATH, xpath_popup)))
#     except:
#         popup=None
#     print(popup)
#     if popup is None:
#         print(url)
#         time = 15
#         for message in messages:
#
#             print()
#
#             send_message(contact, message)
#             time = 3
#     else:
#         print('found')
#         pass
#
#     sleep(5)
