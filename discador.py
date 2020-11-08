import traceback
import time
import datetime
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver import ActionChains
from funcs import wait_element, do_element


class Discador:

    
    def __init__(self) -> None:
        # # configura um variáveis compartilhadas da class
        self.driver = None
        self.conta_print = 1
        self.espera = 0.5
        self.espera_seletor = 10
        self.url = ""
        self.nome = ""
        self.email = ""
        self.payload = { "start_date": datetime.datetime.utcnow() }
        # #
        # # Aguardar um tempo
        sleep(self.espera)
        # #


    def openBrowser(self):
        #
        # Para rodar local, use esse abaixo:
        chrome_options = Options()
        #chrome_options.add_extension('duplicate_tab_shortcut.crx')
        self.driver = webdriver.Chrome(chrome_options=chrome_options, executable_path="./chromedriver")
        # #
        # # Para rodar no docker, descomente as linhas abaixo e comente a de cima
        # chrome_options = Options()
        # chrome_options.add_argument('--headless')
        # chrome_options.add_argument('--no-sandbox')
        # chrome_options.add_argument('--disable-dev-shm-usage')
        # #self.driver = webdriver.Chrome(chrome_options=chrome_options, executable_path="./chromedriver")
        # #
        # # Configurando tamanho da janela do browser
        self.driver.set_window_size(1400, 800)
        # #


    def closeBrowser(self):
        if self.driver:
            self.driver.close()


    def go_for_it(self):
        self.driver.get(self.url)
        #
        # Aguardar um tempo
        sleep(self.espera)
        #


    def wait_for_it(self, selector="", tempo=10):
        el = None
        while not el:
            try: 
                el = wait_element(self.driver, selector, By.CSS_SELECTOR, tempo)
                print("Selector [{}] OK!".format(selector))
            except Exception as e:
                print("Erro no Selector [{}]! Descricao: {}".format(selector, str(e)))
                break
        #
        # Aguardar um tempo
        sleep(self.espera)
        #
        return el


    def do_form(self):

        # Pega o XPath do iframe e atribui a uma variável
        iframe = self.driver.find_element_by_xpath('//*[@id="pbui_iframe"]')

        # Muda o foco para o iframe
        self.driver.switch_to.frame(iframe)

        # nome
        do_element(self.driver, '//*[@id="meetingSimpleContainer"]/div[2]/div[2]/input', By.XPATH, 'click')
        do_element(self.driver, '//*[@id="meetingSimpleContainer"]/div[2]/div[2]/input', By.XPATH, 'send_keys', self.nome) 

        sleep(self.espera)

        # email
        do_element(self.driver, "#meetingSimpleContainer > div.style-box-2gTpv > div.style-email-input-1yF5y > input", By.CSS_SELECTOR, 'click')
        do_element(self.driver, "#meetingSimpleContainer > div.style-box-2gTpv > div.style-email-input-1yF5y > input", By.CSS_SELECTOR, 'send_keys', self.email) 

        sleep(self.espera)

        # click login button
        do_element(self.driver, "#guest_next-btn", By.CSS_SELECTOR, 'click') 

        # Retorna para a janela principal (fora do iframe)
        self.driver.switch_to.default_content()

        # Aguardar um tempo
        sleep(self.espera)


    def deal_with_modal(self):
        # Pega o XPath do iframe e atribui a uma variável
        iframe = self.driver.find_element_by_xpath('//*[@id="pbui_iframe"]')

        # Muda o foco para o iframe
        self.driver.switch_to.frame(iframe)
        # /html/body/div[3]/div[2]/div/div/div/div/div[1]/button
        #  /html/body/div[4]/div[2]/div/div/div/div/div[1]/button
        # body > div.style-modalbox-3IBZd > div.style-mask-23bQN.dialog-mask > div > div > div > div > div.style-fte-texts-KTJf0 > button
        do_element(self.driver, "body > div.style-modalbox-3IBZd > div.style-mask-23bQN.dialog-mask > div > div > div > div > div.style-fte-texts-KTJf0 > button", By.CSS_SELECTOR, 'click')
        sleep(self.espera)

        # Retorna para a janela principal (fora do iframe)
        self.driver.switch_to.default_content()
    
    def select_audio(self):

        # Pega o XPath do iframe e atribui a uma variável
        iframe = self.driver.find_element_by_xpath('//*[@id="pbui_iframe"]')

        # Muda o foco para o iframe
        self.driver.switch_to.frame(iframe)

        #  //*[@id="meetingSimpleContainer"]/div[3]/div[1]/div[2]/div[2]/button/div/span[2]/span[2]/i
        do_element(self.driver, '//*[@id="meetingSimpleContainer"]/div[3]/div[1]/div[2]/div[2]/button/div/span[2]/span[2]/i', By.XPATH, 'click')
        sleep(self.espera)

        # //*[@id="meetingSimpleContainer"]/div[3]/div[1]/div[2]/div[4]/ul/li[2]/div/div/div/div[2]/div/div/div[1]/button
        do_element(self.driver, '//*[@id="meetingSimpleContainer"]/div[3]/div[1]/div[2]/div[4]/ul/li[2]/div/div/div/div[2]/div/div/div[1]/button', By.XPATH, 'click')
        sleep(self.espera)

        # Retorna para a janela principal (fora do iframe)
        self.driver.switch_to.default_content()

    def select_country(self, ddd):
        
        # Pega o XPath do iframe e atribui a uma variável
        iframe = self.driver.find_element_by_xpath('//*[@id="pbui_iframe"]')

        # Muda o foco para o iframe
        self.driver.switch_to.frame(iframe)

        # //*[@id="meetingSimpleContainer"]/div[3]/div[1]/div[2]/div[4]/ul/li[2]/div/div/div/div[2]/div/div[1]/div[1]/div/div[3]/input
        do_element(self.driver, '//*[@id="meetingSimpleContainer"]/div[3]/div[1]/div[2]/div[4]/ul/li[2]/div/div/div/div[2]/div/div[1]/div[1]/div/div[3]/input', By.XPATH, 'click')
        for i in range(4):
            do_element(self.driver, '//*[@id="meetingSimpleContainer"]/div[3]/div[1]/div[2]/div[4]/ul/li[2]/div/div/div/div[2]/div/div[1]/div[1]/div/div[3]/input', By.XPATH, 'send_keys', Keys.BACKSPACE)
        do_element(self.driver, '//*[@id="meetingSimpleContainer"]/div[3]/div[1]/div[2]/div[4]/ul/li[2]/div/div/div/div[2]/div/div[1]/div[1]/div/div[3]/input', By.XPATH, 'send_keys', ddd)
        #sleep(self.espera)
        #do_element(self.driver, '//*[@id="meetingSimpleContainer"]/div[3]/div[1]/div[2]/div[4]/ul/li[2]/div/div/div/div[2]/div/div[1]/div[1]/div/div[3]/input', By.XPATH, 'click')
        #sleep(self.espera)
        
        # while(1):
        #     # //*[@id="meetingSimpleContainer"]/div[3]/div[1]/div[2]/div[4]/ul/li[2]/div/div/div/div[2]/div/div[2]/section/div[1]/div/ul/li[2]
        #     ul = wait_element(self.driver, '//*[@id="meetingSimpleContainer"]/div[3]/div[1]/div[2]/div[4]/ul/li[2]/div/div/div/div[2]/div/div[2]/section/div[1]/div/ul', By.XPATH, 10)
        #     #ddd = 1
        #     for li in ul.find_elements_by_xpath(".//li"):
        #         val = li.get_attribute("title")
        #         num = val.split("+")[1]
        #         print(int(num))
        #         if ddd == int(num):
        #             li.click()
        #             break
            
        #     for i in range(8):
        #         do_element(self.driver, '//*[@id="meetingSimpleContainer"]/div[3]/div[1]/div[2]/div[4]/ul/li[2]/div/div/div/div[2]/div/div[1]/div[1]/div/div[3]/input', By.XPATH, 'send_keys', Keys.ARROW_DOWN)
        #         sleep(self.espera)

        sleep(self.espera)

        # Retorna para a janela principal (fora do iframe)
        self.driver.switch_to.default_content()


    def type_phone_number(self, phone):
        # //*[@id="meetingSimpleContainer"]/div[3]/div[1]/div[2]/div[4]/ul/li[2]/div/div/div/div[2]/div/div/div[2]/input

        # Pega o XPath do iframe e atribui a uma variável
        iframe = self.driver.find_element_by_xpath('//*[@id="pbui_iframe"]')

        # Muda o foco para o iframe
        self.driver.switch_to.frame(iframe)

        #phone = '2013815436'
        do_element(self.driver, '//*[@id="meetingSimpleContainer"]/div[3]/div[1]/div[2]/div[4]/ul/li[2]/div/div/div/div[2]/div/div/div[2]/input', By.XPATH, 'click')
        sleep(self.espera)

        do_element(self.driver, '//*[@id="meetingSimpleContainer"]/div[3]/div[1]/div[2]/div[4]/ul/li[2]/div/div/div/div[2]/div/div/div[2]/input', By.XPATH, 'send_keys', phone)
        sleep(self.espera)

        do_element(self.driver, '//*[@id="meetingSimpleContainer"]/div[3]/div[1]/div[2]/div[4]/ul/li[2]/div/div/div/div[2]/div/div/div[2]/input', By.XPATH, 'send_keys', Keys.RETURN)
        sleep(self.espera)

        # Retorna para a janela principal (fora do iframe)
        self.driver.switch_to.default_content()

    def join_meeting(self):
        # //*[@id="interstitial_join_btn"]

        # Pega o XPath do iframe e atribui a uma variável
        iframe = self.driver.find_element_by_xpath('//*[@id="pbui_iframe"]')

        # Muda o foco para o iframe
        self.driver.switch_to.frame(iframe)

        do_element(self.driver, '//*[@id="interstitial_join_btn"]', By.XPATH, 'click')
        sleep(self.espera)

        # Retorna para a janela principal (fora do iframe)
        self.driver.switch_to.default_content()


    def duplicar(self):

        # Pega o XPath do iframe e atribui a uma variável
        #iframe = self.driver.find_element_by_xpath('//*[@id="pbui_iframe"]')

        # Muda o foco para o iframe
        #self.driver.switch_to.frame(iframe)

        ActionChains(self.driver).key_down(Keys.ALT).perform()
        ActionChains(self.driver).key_down(Keys.SHIFT).send_keys('d').key_up(Keys.SHIFT).perform()
        ActionChains(self.driver).key_up(Keys.ALT).perform()
        #body = self.driver.find_element_by_tag_name('body')

        #body.send_keys(Keys.ALT, Keys.SHIFT, 'd')
        #action_chains = ActionChains(self.driver).move_to_element(body)
        #action_chains.key_down(Keys.SHIFT).key_down(Keys.ALT).send_keys('d').key_up(Keys.ALT).key_up(Keys.SHIFT).perform()
        #action_chains.key_down('d').key_up('d').perform()
        #action_chains.key_down(Keys.SHIFT).key_down(Keys.ALT).key_down('d').key_up('d').perform()
        #action_chains.key_up(Keys.ALT).key_up(Keys.SHIFT).perform()
        #action_chains.key_down(Keys.CONTROL).send_keys('d').key_up(Keys.CONTROL).perform()
        sleep(self.espera)

        # Retorna para a janela principal (fora do iframe)
        #self.driver.switch_to.default_content()
        
        sleep(self.espera)
