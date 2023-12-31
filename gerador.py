from kivymd.app import MDApp
from kivymd.uix.screenmanager import MDScreenManager
from kivymd.uix.screen import MDScreen
from kivymd.uix.dialog import MDDialog
from kivymd.toast import toast
from kivy.lang import Builder
import requests as r

class LoginWin(MDScreen):
    ...
    
class Gerador(MDScreen):
    ...
    
class App(MDApp):
    def build(self):
        Builder.load_file('style.kv')

        # Seta Telas
        self.sm = MDScreenManager()
        self.sm.add_widget(LoginWin())
        self.sm.add_widget(Gerador())
        
        # Seta temas
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Gray"

        return self.sm
    
    def back(self):
        self.root.current = 'login'
        
    def gerar(self):
        self.msg('Gerando, Aguarde...!')
        
    def msg(self, msg):
        self.dialog = MDDialog(text=msg)
        self.dialog.open()
        
    def login(self):
        ids = self.root.get_screen('login').ids
        self.server = str(ids.entryServer.text)
        self.user = str(ids.entryUser.text)
        self.pwd = str(ids.entryPwd.text)
        toast('Logado com sucesso')
        self.root.current = 'gerador'
            
if __name__ == '__main__':
    App().run()