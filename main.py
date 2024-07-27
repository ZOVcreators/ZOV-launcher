from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.lang import Builder
from kivy.core.window import Window
from uuid import uuid1
import minecraft_launcher_lib
import subprocess


Window.size = (960, 540)


class ZOVUI(FloatLayout):
    def JavaStarting(self):
        minecraft_directory = minecraft_launcher_lib.utils.get_minecraft_directory()
        version = '1.16.5'
        username = 'kilka'

        minecraft_launcher_lib.install.install_minecraft_version(versionid=version, minecraft_directory=minecraft_directory)
        options = {
            'username': username,
            'uuid': str(uuid1()),
            'token': ''
        }

        subprocess.call(minecraft_launcher_lib.command.get_minecraft_command(version=version, minecraft_directory=minecraft_directory, options=options))
        print('feafea')


class MyApp(App):
    def build(self):
        Builder.load_file('ZOVUI.kv')
        return ZOVUI()

if __name__ == '__main__':
    MyApp().run()
