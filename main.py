import sys
import minecraft_launcher_lib
import subprocess


minecraft_directory = minecraft_launcher_lib.utils.get_minecraft_directory()

def run():
    version = input('vers')
    username = input('name')


    minecraft_launcher_lib.install.install_minecraft_version(versionid=version, minecraft_directory=minecraft_directory)
    options = {
        'username': username,
        'uuid': str(uuid1()),
        'token': ''
    }

    subprocess.call(minecraft_launcher_lib.command.get_minecraft_command(version=version, minecraft_directory=minecraft_directory, options=options))







if __name__ == "__main__":
 run()