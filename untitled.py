# ЭТО САМ UI

################################################################################
## ЭТО САМ UI ВСЕ ИЗМЕНЯЕТСЯ В ui_test
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QMainWindow, QPushButton,
    QSizePolicy, QWidget)
import resourse

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(813, 500)
        MainWindow.setStyleSheet(u"background-color: rgba(51, 51, 51, 1);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(-1, -1, 201, 501))
        palette = QPalette()
        brush = QBrush(QColor(33, 33, 33, 229))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush)
        palette.setBrush(QPalette.Active, QPalette.Window, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.frame.setPalette(palette)
        self.frame.setStyleSheet(u"background-color: rgba(33, 33, 33, 0.9);")
        self.pushButton = QPushButton(self.frame)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(50, 0, 151, 51))
        self.pushButton.setAutoFillBackground(False)
        self.pushButton.setStyleSheet(u"background-color: rgba(54, 54, 54, 1);\n"
"border: None;")
        self.pushButton_2 = QPushButton(self.frame)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(0, 0, 51, 51))
        self.pushButton_2.setAutoFillBackground(False)
        self.pushButton_2.setStyleSheet(u"background-color: rgba(54, 54, 54, 1);\n"
"border: None;")
        self.pushButton_3 = QPushButton(self.frame)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(0, 60, 201, 51))
        self.pushButton_3.setAutoFillBackground(False)
        self.pushButton_3.setStyleSheet(u"background-color: rgba(54, 54, 54, 1);\n"
"border: None;")
        self.pushButton_4 = QPushButton(self.frame)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(0, 120, 201, 51))
        self.pushButton_4.setAutoFillBackground(False)
        self.pushButton_4.setStyleSheet(u"background-color: rgba(54, 54, 54, 1);\n"
"border: None;")
        self.pushButton_5 = QPushButton(self.frame)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setGeometry(QRect(0, 180, 201, 51))
        font = QFont()
        font.setPointSize(28)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setAutoFillBackground(False)
        self.pushButton_5.setStyleSheet(u"background-color: rgba(54, 54, 54, 1);\n"
"border: None;")
        self.pushButton_5.setIconSize(QSize(16, 16))
        self.pushButton_5.setAutoDefault(False)
        self.pushButton_5.setFlat(False)
        self.pushButton_6 = QPushButton(self.frame)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setGeometry(QRect(0, 435, 66, 71))
        self.pushButton_6.setAutoFillBackground(False)
        self.pushButton_6.setStyleSheet(u"background-color: rgba(54, 54, 54, 1);\n"
"border: None;")
        self.pushButton_7 = QPushButton(self.frame)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setGeometry(QRect(67, 435, 67, 71))
        self.pushButton_7.setAutoFillBackground(False)
        self.pushButton_7.setStyleSheet(u"background-color: rgba(54, 54, 54, 1);\n"
"border: None;")
        self.pushButton_8 = QPushButton(self.frame)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setGeometry(QRect(135, 435, 66, 71))
        self.pushButton_8.setAutoFillBackground(False)
        self.pushButton_8.setStyleSheet(u"background-color: rgba(54, 54, 54, 1);\n"
"border: None;")
        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(200, 360, 621, 141))
        self.frame_2.setStyleSheet(u"background-color: rgba(33, 33, 33, 1);")
        self.frame_3 = QFrame(self.frame_2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(0, 0, 621, 41))
        self.frame_3.setStyleSheet(u"background-color: rgba(23, 23, 23, 1);")
        self.pushButton_10 = QPushButton(self.frame_3)
        self.pushButton_10.setObjectName(u"pushButton_10")
        self.pushButton_10.setGeometry(QRect(50, 10, 81, 21))
        self.pushButton_10.setFont(font)
        self.pushButton_10.setAutoFillBackground(False)
        self.pushButton_10.setStyleSheet(u"background-color: rgba(54, 54, 54, 1);\n"
"border: None;")
        self.pushButton_10.setIconSize(QSize(16, 16))
        self.pushButton_11 = QPushButton(self.frame_3)
        self.pushButton_11.setObjectName(u"pushButton_11")
        self.pushButton_11.setGeometry(QRect(31, 10, 20, 21))
        self.pushButton_11.setFont(font)
        self.pushButton_11.setAutoFillBackground(False)
        self.pushButton_11.setStyleSheet(u"background-color: rgba(54, 54, 54, 1);\n"
"border: None;")
        self.pushButton_11.setIconSize(QSize(16, 16))
        self.pushButton_9 = QPushButton(self.centralwidget)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setGeometry(QRect(410, 330, 201, 51))
        palette1 = QPalette()
        brush1 = QBrush(QColor(67, 67, 67, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.Button, brush1)
        brush2 = QBrush(QColor(54, 54, 54, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.Base, brush2)
        palette1.setBrush(QPalette.Active, QPalette.Window, brush2)
        palette1.setBrush(QPalette.Inactive, QPalette.Button, brush2)
        palette1.setBrush(QPalette.Inactive, QPalette.Base, brush2)
        palette1.setBrush(QPalette.Inactive, QPalette.Window, brush2)
        brush3 = QBrush(QColor(59, 59, 59, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Disabled, QPalette.Button, brush3)
        palette1.setBrush(QPalette.Disabled, QPalette.Base, brush2)
        palette1.setBrush(QPalette.Disabled, QPalette.Window, brush2)
        self.pushButton_9.setPalette(palette1)
        self.pushButton_9.setFont(font)
        self.pushButton_9.setMouseTracking(False)
        self.pushButton_9.setAutoFillBackground(False)
        self.pushButton_9.setStyleSheet(u"background-color: rgba(54, 54, 54, 1);\n"
"border: None;")
        self.pushButton_9.setIconSize(QSize(16, 16))
        self.pushButton_9.setAutoDefault(False)
        self.pushButton_9.setFlat(False)
        MainWindow.setCentralWidget(self.centralwidget)
        self.frame_2.raise_()
        self.frame.raise_()
        self.pushButton_9.raise_()

        self.retranslateUi(MainWindow)

        self.pushButton_9.setDefault(False)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"ZOV Launcher", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_10.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.pushButton_11.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.pushButton_9.setText(QCoreApplication.translate("MainWindow", u"+", None))
    # retranslateUi

