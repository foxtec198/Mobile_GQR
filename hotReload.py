from kivymd.tools.hotreload.app import MDApp
from kivy.lang import Builder
from kivymd.uix.screenmanager import MDScreenManager
from kivymd.uix.screen import MDScreen

class LoginWin(MDScreen):
    ...
    
class Gerador(MDApp):
    KV_FILES = ['style.kv']
    DEBUG = True
    
    def build_app(self):
        Builder.load_file('style.kv')
        self.sm = MDScreenManager()
        self.sm.add_widget(LoginWin())
        return self.sm
    
    def login(self):
        ...
        
Gerador().run()