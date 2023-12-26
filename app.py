from kivy.lang import Builder
from kivymd.app import MDApp, ThemeManager

class Gerar:
    def __init__(self):
        ...

class GeradorQR(MDApp):
    def build(self):
        theme_cls = ThemeManager()
        theme_cls.primary_palette = "DeepPurple"
        return Builder.load_file('style.kv')
    
    def on_start(self):
        self.fps_monitor_start()

if __name__ == '__main__':
    GeradorQR().run()