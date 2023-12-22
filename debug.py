from kivy.lang import Builder
from kivymd.tools.hotreload.app import MDApp

class debug(MDApp):
    KV_FILES = ['style.kv']
    DEBUG = True
    
    def build_app(self):
        return Builder.load_file('style.kv')
    
debug().run()