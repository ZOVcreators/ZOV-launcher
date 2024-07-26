# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ZOVUI.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import QCoreApplication, QMetaObject, QRect, QSize, Qt
from PySide6.QtGui import QFont, QIcon, QPalette, QColor, QBrush, QResizeEvent
from PySide6.QtWidgets import QApplication, QFrame, QHBoxLayout, QMainWindow, QPushButton, QScrollArea, QVBoxLayout, QWidget
import Icons

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(813, 508)
        MainWindow.setStyleSheet(u"background-color: rgba(51, 51, 51, 1);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(200, 0, 621, 61))
        self.frame_2.setStyleSheet(u"background-color: rgba(33, 33, 33, 1);")
        self.verticalLayoutWidget = QWidget(self.frame_2)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(0, 0, 611, 61))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_3 = QFrame(self.verticalLayoutWidget)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setStyleSheet(u"background-color: rgba(23, 23, 23, 1);")
        self.VersionButtonJAVA = QPushButton(self.frame_3)
        self.VersionButtonJAVA.setObjectName(u"VersionButtonJAVA")
        self.VersionButtonJAVA.setGeometry(QRect(50, 6, 91, 31))
        font = QFont()
        font.setPointSize(9)
        self.VersionButtonJAVA.setFont(font)
        self.VersionButtonJAVA.setAutoFillBackground(False)
        self.VersionButtonJAVA.setStyleSheet(u"background-color: rgba(54, 54, 54, 1);\n"
"border: None;")
        self.VersionButtonJAVA.setIconSize(QSize(16, 16))
        self.AllVersionsJAVA = QPushButton(self.frame_3)
        self.AllVersionsJAVA.setObjectName(u"AllVersionsJAVA")
        self.AllVersionsJAVA.setGeometry(QRect(30, 6, 20, 31))
        font1 = QFont()
        font1.setPointSize(28)
        self.AllVersionsJAVA.setFont(font1)
        self.AllVersionsJAVA.setAutoFillBackground(False)
        self.AllVersionsJAVA.setStyleSheet(u"background-color: rgba(54, 54, 54, 1);\n"
"border: None;")
        self.AllVersionsJAVA.setIconSize(QSize(16, 16))
        self.SkinButtonJAVA = QPushButton(self.frame_3)
        self.SkinButtonJAVA.setObjectName(u"SkinButtonJAVA")
        self.SkinButtonJAVA.setGeometry(QRect(560, 5, 51, 51))
        self.SkinButtonJAVA.setAutoFillBackground(False)
        self.SkinButtonJAVA.setStyleSheet(u"background-color: rgba(54, 54, 54, 1);\n"
"border: None;")

        self.verticalLayout.addWidget(self.frame_3)

        self.verticalLayoutWidget_2 = QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(400, 40, 201, 67))
        self.verticalLayout_2 = QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.PlayButtonJAVA = QPushButton(self.verticalLayoutWidget_2)
        self.PlayButtonJAVA.setObjectName(u"PlayButtonJAVA")
        palette = QPalette()
        brush = QBrush(QColor(54, 54, 54, 255))
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
        self.PlayButtonJAVA.setPalette(palette)
        self.PlayButtonJAVA.setFont(font1)
        self.PlayButtonJAVA.setMouseTracking(False)
        self.PlayButtonJAVA.setAutoFillBackground(False)
        self.PlayButtonJAVA.setStyleSheet(u"background-color: rgba(54, 54, 54, 1);\n"
"border: None;")
        self.PlayButtonJAVA.setIconSize(QSize(16, 16))
        self.PlayButtonJAVA.setAutoDefault(False)
        self.PlayButtonJAVA.setFlat(False)

        self.verticalLayout_2.addWidget(self.PlayButtonJAVA)

        self.horizontalLayoutWidget = QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(0, 0, 201, 441))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.scrollArea = QScrollArea(self.horizontalLayoutWidget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setStyleSheet(u"background-color: rgba(33, 33, 33, 0.9);")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 197, 437))
        self.akauntButton = QPushButton(self.scrollAreaWidgetContents)
        self.akauntButton.setObjectName(u"akauntButton")
        self.akauntButton.setGeometry(QRect(0, 5, 201, 51))
        self.akauntButton.setAutoFillBackground(False)
        self.akauntButton.setStyleSheet(u"background-color: rgba(54, 54, 54, 1);\n"
"border: None;")
        self.JAVAButton = QPushButton(self.scrollAreaWidgetContents)
        self.JAVAButton.setObjectName(u"JAVAButton")
        self.JAVAButton.setGeometry(QRect(0, 60, 201, 51))
        self.JAVAButton.setAutoFillBackground(False)
        self.JAVAButton.setStyleSheet(u"background-color: rgba(54, 54, 54, 1);\n"
"border: None;")

        self.BedrockButton = QPushButton(self.scrollAreaWidgetContents)
        self.BedrockButton.setObjectName(u"BedrockButton")
        self.BedrockButton.setGeometry(QRect(0, 115, 201, 51))
        self.BedrockButton.setAutoFillBackground(False)
        self.BedrockButton.setStyleSheet(u"background-color: rgba(54, 54, 54, 1);\n"
"border: None;")
        self.AddButton = QPushButton(self.scrollAreaWidgetContents)
        self.AddButton.setObjectName(u"AddButton")
        self.AddButton.setGeometry(QRect(0, 170, 201, 51))
        self.AddButton.setFont(font1)
        self.AddButton.setAutoFillBackground(False)
        self.AddButton.setStyleSheet(u"background-color: rgba(54, 54, 54, 1);\n"
"border: None;")
        self.AddButton.setIconSize(QSize(16, 16))
        self.AddButton.setAutoDefault(False)
        self.AddButton.setFlat(False)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.horizontalLayout.addWidget(self.scrollArea)

        self.horizontalLayoutWidget_2 = QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setObjectName(u"horizontalLayoutWidget_2")
        self.horizontalLayoutWidget_2.setGeometry(QRect(-10, 440, 211, 71))
        self.horizontalLayout_2 = QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.horizontalLayoutWidget_2)
        self.frame.setObjectName(u"frame")
        palette1 = QPalette()
        brush1 = QBrush(QColor(33, 33, 33, 229))
        brush1.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette1.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette1.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette1.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette1.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette1.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        self.frame.setPalette(palette1)
        self.frame.setStyleSheet(u"background-color: rgba(33, 33, 33, 0.9);")
        self.SettingsButton = QPushButton(self.frame)
        self.SettingsButton.setObjectName(u"SettingsButton")
        self.SettingsButton.setGeometry(QRect(0, 0, 67, 71))
        self.SettingsButton.setAutoFillBackground(False)
        self.SettingsButton.setStyleSheet(u"background-color: rgba(54, 54, 54, 1);\n"
"border: None;")
        icon = QIcon()
        icon.addFile(u":/Icons/Icons/icons8-settings-100.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.SettingsButton.setIcon(icon)
        self.SettingsButton.setIconSize(QSize(60, 60))
        self.FriendsButton = QPushButton(self.frame)
        self.FriendsButton.setObjectName(u"FriendsButton")
        self.FriendsButton.setGeometry(QRect(70, 0, 67, 71))
        self.FriendsButton.setAutoFillBackground(False)
        self.FriendsButton.setStyleSheet(u"background-color: rgba(54, 54, 54, 1);\n"
"border: None;")
        self.ServerButton = QPushButton(self.frame)
        self.ServerButton.setObjectName(u"ServerButton")
        self.ServerButton.setGeometry(QRect(140, 0, 66, 71))
        self.ServerButton.setAutoFillBackground(False)
        self.ServerButton.setStyleSheet(u"background-color: rgba(54, 54, 54, 1);\n"
"border: None;")
        icon1 = QIcon()
        icon1.addFile(u":/Icons/Icons/icons8-news-100.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.ServerButton.setIcon(icon1)
        self.ServerButton.setIconSize(QSize(50, 50))

        self.horizontalLayout_2.addWidget(self.frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.PlayButtonJAVA.setDefault(False)


        QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"ZOV Launcher", None))
        self.VersionButtonJAVA.setText(QCoreApplication.translate("MainWindow", u"\u0432\u0435\u0440\u0441\u0438\u0438", None))
        self.AllVersionsJAVA.setText("")
        self.SkinButtonJAVA.setText(QCoreApplication.translate("MainWindow", u"Skins", None))
        self.PlayButtonJAVA.setText(QCoreApplication.translate("MainWindow", u"Play", None))
        self.akauntButton.setText(QCoreApplication.translate("MainWindow", u"\u0410\u041a\u041a\u0410\u0423\u041d\u0422", None))
        self.JAVAButton.setText(QCoreApplication.translate("MainWindow", u"JAVA", None))
        self.BedrockButton.setText(QCoreApplication.translate("MainWindow", u"BEDROCK", None))
        self.AddButton.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.SettingsButton.setText("")
        self.FriendsButton.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.ServerButton.setText("")
    # retranslateUi

