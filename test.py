from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from kivy.graphics import Color, Rectangle

class CustomBoxLayout(BoxLayout):
    pass

class MainScreen(BoxLayout):
    pass

class ColorBox(Widget):
    def __init__(self, color=(1, 1, 1, 1), **kwargs):
        super(ColorBox, self).__init__(**kwargs)
        self.color = color
        with self.canvas.before:
            Color(*color)
            self.rect = Rectangle(size=self.size, pos=self.pos)
        self.bind(size=self.update_rect, pos=self.update_rect)

    def update_rect(self, *args):
        self.rect.size = self.size
        self.rect.pos = self.pos

    def change_color(self, new_color):
        self.color = new_color
        with self.canvas.before:
            Color(*new_color)
            self.rect = Rectangle(size=self.size, pos=self.pos)
        self.update_rect()

class TestApp(App):
    def build(self):
        return MainScreen()

    def change_box_color(self, box_id, new_color):
        box = self.root.ids.main_layout.ids[box_id]
        box.change_color(new_color)

if __name__ == '__main__':
    TestApp().run()
