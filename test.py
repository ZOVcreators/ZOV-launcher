# main.py
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder

class MyWidget(BoxLayout):
    pass

class MyApp(App):
    def build(self):
        return MyWidget()
    Builder.load_file("test.kv")

if __name__ == "__main__":
    MyApp().run()
