from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.lang import Builder

class ZOVUI(FloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.bind(size=self.update_button_pos)

    def update_button_pos(self, *args):
        self.ids.my_button.size = (self.width * 0.2, self.height * 0.1)

class MyApp(App):
    def build(self):
        Builder.load_file('ZOVUI.kv')
        return ZOVUI()

if __name__ == '__main__':
    MyApp().run()
