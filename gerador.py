from kivymd.app import MDApp
from kivy.lang import Builder

class Gerador(MDApp):
    def build(self):
        return Builder.load_file('style.kv')

if __name__ == '__main__':
    Gerador().run()