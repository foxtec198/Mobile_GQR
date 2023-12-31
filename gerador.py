from kivymd.app import MDApp
from kivymd.uix.screenmanager import MDScreenManager
from kivymd.uix.screen import MDScreen
from kivy.lang import Builder
import pyodbc as sql

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

    # def con(self):
    #     driver = '{SQL Server}'
    #     str_c = f"DRIVER={driver};SERVER={self.server};UID={self.user};PWD={self.pwd}"
    #     self.conn = connect(str_c)
        
    def login(self):
        ids = self.root.get_screen('login').ids
        self.server = str(ids.entryServer.text)
        self.user = str(ids.entryUser.text)
        self.pwd = str(ids.entryPwd.text)
        self.root.current = 'gerador'
            
if __name__ == '__main__':
    App().run()