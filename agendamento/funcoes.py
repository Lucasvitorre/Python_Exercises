from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
from selenium.webdriver.firefox.options import Options

class BOTWPP:
#Função para realizar a abertura do firefox com o perfil e com selecionador de conversa 
    def abertura_firefox(self):
        profile_path = "C:/Users/Lucas/AppData/Roaming/Mozilla/Firefox/Profiles/rdxu4olf.default-release"
        profile = FirefoxProfile(profile_path)
        options = Options()
        options.profile = profile
        self.driver = webdriver.Firefox(options=options)
        self.driver.get("https://web.whatsapp.com/")
        sleep(5)
        
    def envio_msg(self):
        #Selecionando a conversa do WPP.
        elem = self.driver.find_elements (By.CSS_SELECTOR,"#pane-side > div:nth-child(3)")
        elem[0].click()
        text_bar = self.driver.find_elements (By.XPATH,"/html/body/div[1]/div/div/div[2]/div[4]/div/footer/div[1]/div/span[2]/div/div[2]/div[1]/div")
        sleep(1)
        text_bar[0].click()
        sleep(1)
        text_bar[0].send_keys("Agora estamos utilizando um novo sistema de agendamento!!! \n Para iniciar o agendamento basta digitar: Agendamento")

'''
def coleta_info(info):
    infos = {
        "nome": input("Insira o seu nome: "),
        "data": input("Insira a data: "),
        "horário": input("Insira o horário: ")
    }
    info.append(infos)
    return info

def calendar(calendario):
    calendario = """ Script de criacão de evento"""
    '''