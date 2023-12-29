from kivymd.app import MDApp
from kivymd.uix.screenmanager import ScreenManager
from kivymd.uix.screen import MDScreen
from kivy.lang import Builder

class LoginWin(MDScreen):
    ...
    
class MainWin(MDScreen):
    ...
    
class App(MDApp):
    def build(self):
        # ['Red', 'Pink', 'Purple', 'DeepPurple', 'Indigo', 'Blue', 'LightBlue', 'Cyan', 'Teal', 
        # 'Green', 'LightGreen', 'Lime', 'Yellow', 'Amber', 'Orange', 'DeepOrange', 'Brown', 'Gray', 'BlueGray']
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "BlueGray"
        return Builder.load_file('style.kv')
    
    def login(self):
        self.server = self.root.ids.entryServer.text
        self.user = self.root.ids.entryUser.text
        self.pwd = self.root.ids.entryPwd.text
        
if __name__ == '__main__':
    App().run()