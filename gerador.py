from kivymd.app import MDApp
from kivymd.uix.screenmanager import MDScreenManager
from kivymd.uix.screen import MDScreen
from kivymd.toast import toast
from kivy.lang import Builder

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
    
    def on_start(self):
        self.ids = self.root.get_screen('login').ids
        self.ids.entryServer.text = '10.56.6.56'
    
    def back(self):
        self.root.current = 'login'
        
    def gerar(self):
        toast('Gerando, Aguarde...!')
        
    def login(self):
        self.server = self.ids.entryServer.text
        self.user = self.ids.entryUser.text
        self.pwd = self.ids.entryPwd.text
        if self.server != '' and self.user != '' and self.pwd != '':
            toast('Logado com sucesso')
            self.root.current = 'gerador'
        else:
            toast('Credenciais invalidas')
            
if __name__ == '__main__':
    App().run()