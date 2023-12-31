from kivymd.tools.hotreload.app import MDApp
from kivy.lang import Builder
from kivymd.uix.screenmanager import MDScreenManager
from kivymd.uix.screen import MDScreen

class LoginWin(MDScreen):
    ...

class Gerador(MDScreen):
    ...
        
class GeradorQR(MDApp):
    KV_FILES = ['style.kv']
    DEBUG = True
    
    def build_app(self):
        Builder.load_file('style.kv')
        self.theme_cls.theme_style = 'Dark'
        self.sm = MDScreenManager()
        self.sm.add_widget(LoginWin())
        self.sm.add_widget(Gerador())
        
        return self.sm

    def back(self):
        self.root.current = 'login'
        
    def login(self):
        self.root.current = 'gerador'
        ...
        
GeradorQR().run()