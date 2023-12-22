from kivy.lang import Builder
from kivymd.app import MDApp

class App(MDApp):
    def build(self):
        return Builder.load_file('style.kv')

if __name__ == '__main__':
    App().run()