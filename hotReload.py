from kivymd.tools.hotreload.app import MDApp
from kivy.lang import Builder

class Gerador(MDApp):
    KV_FILES = ['style.kv']
    DEBUG = True
    
    def build_app(self):
        return Builder.load_file('style.kv')
    
    def login(self):
        ...
        
Gerador().run()