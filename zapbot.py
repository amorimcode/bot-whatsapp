from selenium import webdriver
import time

class WhatsappBot:
    def __init__(self):
        self.message = str(input('Digite a mensagem: '))
        self.contact = str(input('Digite o contato: '))
        options = webdriver.ChromeOptions()
        options.add_argument('lang=pt-br')
        self.driver = webdriver.Chrome(executable_path=r'./chromedriver.exe')
    
    
    def SendMessage(self):
        #<span dir="auto" title="TIRAR MUSICA" class="_1hI5g _1XH7x _1VzZY">TIRAR MUSICA</span>
        #<div tabindex="-1" class="DuUXI"><div tabindex="-1" class="_2HE1Z _1hRBM">
        #<span data-testid="send" data-icon="send" class="">
        self.driver.get('https://web.whatsapp.com')
        # for group in self.groups:
        for group in self.contact:
            time.sleep(10)
            group = self.driver.find_element_by_xpath(f"//span[@title='{self.contact}']")
            time.sleep(3)
            group.click()
            chat_box = self.driver.find_element_by_class_name('DuUXI')
            time.sleep(2)
            chat_box.click()
            n = 0
            while n < 10:
                chat_box.send_keys(self.message)
                send_button = self.driver.find_element_by_xpath(
                    '//span[@data-icon="send"]')
                time.sleep(1)
                send_button.click()
                time.sleep(1)
                n += 1

bot = WhatsappBot()
bot.SendMessage()
