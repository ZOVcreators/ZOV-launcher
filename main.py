# Здесь прописан пока только вызов ui

import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from untitled import Ui_MainWindow

class ExpenseTracker(QMainWindow):
    def __init__(self):
        super(ExpenseTracker, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pushButton_4.clicked.connect(self.close)
        self.setStyleSheet(f"QMainWindow {{ border-image: url('Image (1).png') 0 0 0 0 stretch stretch; }}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ExpenseTracker()
    window.show()

    sys.exit(app.exec())
