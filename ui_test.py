
import sys
import minecraft_launcher_lib
from PySide6.QtWidgets import QApplication, QMainWindow
from ZOVUI import Ui_MainWindow
import subprocess

minecraft_directory = minecraft_launcher_lib.utils.get_minecraft_directory()


class ExpenseTracker(QMainWindow):
    def __init__(self):
        super(ExpenseTracker, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


        self.ui.PlayButtonJAVA.clicked.connect(self.run)


        self.setStyleSheet(f"QMainWindow {{ border-image: url('Image (1).png') 0 0 0 0 stretch stretch; }}")

    def run(self):

        version = '1.16.5'
        username = 'advitt'

        minecraft_launcher_lib.install.install_minecraft_version(version, minecraft_directory)


        options = {
            'username': username
        }


        minecraft_command = minecraft_launcher_lib.command.get_minecraft_command(version, minecraft_directory, options)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ExpenseTracker()
    window.show()

    sys.exit(app.exec())
