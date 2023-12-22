from kivy.lang import Builder
from kivymd.app import MDApp

class Gerar:
    def __init__(self):
        ...

class GeradorQR(MDApp):
    def build(self):
        return Builder.load_file('style.kv')

if __name__ == '__main__':
    GeradorQR().run()