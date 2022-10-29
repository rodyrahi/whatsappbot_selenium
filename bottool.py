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