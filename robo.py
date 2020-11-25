from time import sleep
import os
from discador import Discador

class Robo:

    def __init__(self) -> None:
        # discador
        self.discador = Discador()
        self.discador.url = "" #os.environ.get("URL", "")
        self.discador.nome = "Renato" #os.environ.get("NOME", "")
        self.discador.email = "renato.jose@hotmail.com" #os.environ.get("EMAIL", "")
        
    
    # configura bandeiras de multi adiquirencia
    def run_task(self, url, ddd, phone):
        #phone_list = [{'ddd':'1', 'phone':'5515579130'}, {'ddd':'1', 'phone':'2013815436'}, {'ddd':'1', 'phone':'2013657086'}]
        self.discador.url = url
        #ddd = p['ddd']
        #phone = p['phone']
        try:        
            # liga o browser
            self.discador.openBrowser()

            # navigate to site
            self.discador.go_for_it()

            # ------------------------------

            # form
            self.discador.do_form()

            #modal
            self.discador.deal_with_modal()

            #audio
            self.discador.select_audio()

            #country
            self.discador.select_country(ddd)

            # type phone
            self.discador.type_phone_number(phone)

            # join meeting
            self.discador.join_meeting()

            #self.run_task()
            sleep(15)

            # ------------------------------

        except Exception as e:
            print("Deu pau: {}".format(str(e)))
        finally:
            # fecha o browser no final
            self.discador.closeBrowser()