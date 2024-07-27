from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.lang import Builder

class ZOVUI(FloatLayout):
    pass

class MyApp(App):
    def build(self):
        Builder.load_file('ZOVUI.kv')
        return ZOVUI()

if __name__ == '__main__':
    MyApp().run()
