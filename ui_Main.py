# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Main.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(880, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.Drop_Shadow_layout = QVBoxLayout(self.centralwidget)
        self.Drop_Shadow_layout.setSpacing(0)
        self.Drop_Shadow_layout.setObjectName(u"Drop_Shadow_layout")
        self.Drop_Shadow_layout.setContentsMargins(10, 10, 10, 10)
        self.Drop_Shadow = QFrame(self.centralwidget)
        self.Drop_Shadow.setObjectName(u"Drop_Shadow")
        self.Drop_Shadow.setStyleSheet(u"border-radius: 10px;\n"
"background-color: qlineargradient(spread:pad, x1:0.94, y1:0.892, x2:0.034, y2:0.085, stop:0.0501949 rgba(0, 0, 56, 255), stop:0.275797 rgba(39, 0, 59, 255), stop:0.545966 rgba(39, 0, 59, 255), stop:0.793621 rgba(0, 0, 74, 255), stop:0.949805 rgba(36, 0, 54, 255));\n"
"")
        self.Drop_Shadow.setFrameShape(QFrame.StyledPanel)
        self.Drop_Shadow.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.Drop_Shadow)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.Title_bar = QFrame(self.Drop_Shadow)
        self.Title_bar.setObjectName(u"Title_bar")
        self.Title_bar.setMaximumSize(QSize(16777215, 50))
        self.Title_bar.setStyleSheet(u"background-color: none;;")
        self.Title_bar.setFrameShape(QFrame.NoFrame)
        self.Title_bar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.Title_bar)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_title = QFrame(self.Title_bar)
        self.frame_title.setObjectName(u"frame_title")
        self.frame_title.setFrameShape(QFrame.StyledPanel)
        self.frame_title.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_title)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(15, 0, 0, 0)
        self.label_title = QLabel(self.frame_title)
        self.label_title.setObjectName(u"label_title")
        font = QFont()
        font.setFamily(u"Sitka Display Semibold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_title.setFont(font)
        self.label_title.setStyleSheet(u"color: rgb(221, 221, 221);")

        self.verticalLayout_2.addWidget(self.label_title)


        self.horizontalLayout.addWidget(self.frame_title)

        self.frame_bts = QFrame(self.Title_bar)
        self.frame_bts.setObjectName(u"frame_bts")
        self.frame_bts.setMaximumSize(QSize(100, 16777215))
        self.frame_bts.setFrameShape(QFrame.StyledPanel)
        self.frame_bts.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_bts)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.btn_mini = QPushButton(self.frame_bts)
        self.btn_mini.setObjectName(u"btn_mini")
        self.btn_mini.setMinimumSize(QSize(16, 16))
        self.btn_mini.setMaximumSize(QSize(17, 17))
        self.btn_mini.setStyleSheet(u"QPushButton{\n"
"border-radius:8;\n"
"background-color: rgb(85,255,127);\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgba(85,255,127,150);\n"
"}")

        self.horizontalLayout_2.addWidget(self.btn_mini)

        self.btn_maxi = QPushButton(self.frame_bts)
        self.btn_maxi.setObjectName(u"btn_maxi")
        self.btn_maxi.setMinimumSize(QSize(16, 16))
        self.btn_maxi.setMaximumSize(QSize(17, 17))
        self.btn_maxi.setStyleSheet(u"QPushButton{\n"
"border-radius:8;\n"
"background-color: rgb(255, 170, 0);\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgba(255, 85, 0, 150);\n"
"}")

        self.horizontalLayout_2.addWidget(self.btn_maxi)

        self.btn_close = QPushButton(self.frame_bts)
        self.btn_close.setObjectName(u"btn_close")
        self.btn_close.setMinimumSize(QSize(16, 16))
        self.btn_close.setMaximumSize(QSize(17, 17))
        self.btn_close.setStyleSheet(u"QPushButton{\n"
"border-radius:8;\n"
"	background-color: rgb(255, 0, 0);\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgba(255, 0, 0, 150);\n"
"}")

        self.horizontalLayout_2.addWidget(self.btn_close)


        self.horizontalLayout.addWidget(self.frame_bts)


        self.verticalLayout.addWidget(self.Title_bar)

        self.content_bar = QFrame(self.Drop_Shadow)
        self.content_bar.setObjectName(u"content_bar")
        self.content_bar.setStyleSheet(u"background-color: none;;")
        self.content_bar.setFrameShape(QFrame.StyledPanel)
        self.content_bar.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.content_bar)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.stackedWidget = QStackedWidget(self.content_bar)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page_home = QWidget()
        self.page_home.setObjectName(u"page_home")
        self.stackedWidget.addWidget(self.page_home)
        self.page_credits = QWidget()
        self.page_credits.setObjectName(u"page_credits")
        self.credits_content = QFrame(self.page_credits)
        self.credits_content.setObjectName(u"credits_content")
        self.credits_content.setGeometry(QRect(240, 200, 120, 80))
        self.credits_content.setFrameShape(QFrame.StyledPanel)
        self.credits_content.setFrameShadow(QFrame.Raised)
        self.stackedWidget.addWidget(self.page_credits)

        self.verticalLayout_4.addWidget(self.stackedWidget)


        self.verticalLayout.addWidget(self.content_bar)

        self.credit_bar = QFrame(self.Drop_Shadow)
        self.credit_bar.setObjectName(u"credit_bar")
        self.credit_bar.setMaximumSize(QSize(16777215, 30))
        self.credit_bar.setStyleSheet(u"background-color: none;;")
        self.credit_bar.setFrameShape(QFrame.StyledPanel)
        self.credit_bar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.credit_bar)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.credit_bar)
        self.frame.setObjectName(u"frame")
        self.frame.setMaximumSize(QSize(16777215, 30))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(9, 0, 0, 9)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"color: rgba(221, 221, 221, 200);")

        self.verticalLayout_3.addWidget(self.label)


        self.horizontalLayout_3.addWidget(self.frame)

        self.frame_grip = QFrame(self.credit_bar)
        self.frame_grip.setObjectName(u"frame_grip")
        self.frame_grip.setMaximumSize(QSize(30, 30))
        self.frame_grip.setFrameShape(QFrame.StyledPanel)
        self.frame_grip.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_3.addWidget(self.frame_grip)


        self.verticalLayout.addWidget(self.credit_bar)


        self.Drop_Shadow_layout.addWidget(self.Drop_Shadow)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_title.setText(QCoreApplication.translate("MainWindow", u"VidPDFier", None))
        self.btn_mini.setText("")
        self.btn_maxi.setText("")
        self.btn_close.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"By Nakira @HWork", None))
    # retranslateUi

