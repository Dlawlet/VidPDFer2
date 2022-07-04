# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Main.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(995, 771)
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
        self.page0 = QWidget()
        self.page0.setObjectName(u"page0")
        self.stackedWidget.addWidget(self.page0)
        self.page1 = QWidget()
        self.page1.setObjectName(u"page1")
        self.horizontalLayout_4 = QHBoxLayout(self.page1)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.leftgrid = QFrame(self.page1)
        self.leftgrid.setObjectName(u"leftgrid")
        self.leftgrid.setEnabled(True)
        self.leftgrid.setMinimumSize(QSize(300, 0))
        self.leftgrid.setStyleSheet(u"background-color: rgba(221, 221, 221, 50);")
        self.leftgrid.setFrameShape(QFrame.StyledPanel)
        self.leftgrid.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.leftgrid)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.left_bottom = QFrame(self.leftgrid)
        self.left_bottom.setObjectName(u"left_bottom")
        self.left_bottom.setMaximumSize(QSize(16777215, 50))
        self.left_bottom.setFrameShape(QFrame.StyledPanel)
        self.left_bottom.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.left_bottom)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_7 = QLabel(self.left_bottom)
        self.label_7.setObjectName(u"label_7")
        font1 = QFont()
        font1.setFamily(u"Segoe UI Variable Display")
        font1.setPointSize(14)
        font1.setBold(True)
        font1.setWeight(75)
        self.label_7.setFont(font1)
        self.label_7.setStyleSheet(u"background:none")

        self.horizontalLayout_6.addWidget(self.label_7)

        self.left_select_btn = QPushButton(self.left_bottom)
        self.left_select_btn.setObjectName(u"left_select_btn")
        self.left_select_btn.setMaximumSize(QSize(16777215, 30))
        font2 = QFont()
        font2.setFamily(u"Segoe UI")
        font2.setPointSize(12)
        font2.setBold(False)
        font2.setWeight(50)
        self.left_select_btn.setFont(font2)
        self.left_select_btn.setStyleSheet(u"QPushButton{\n"
"border-radius:8;\n"
"background-color: rgb(221, 221, 221);\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgba(221, 221, 221, 150);\n"
"}")

        self.horizontalLayout_6.addWidget(self.left_select_btn)


        self.gridLayout_2.addWidget(self.left_bottom, 2, 0, 1, 1)

        self.listWidget = QListWidget(self.leftgrid)
        self.listWidget.setObjectName(u"listWidget")

        self.gridLayout_2.addWidget(self.listWidget, 1, 0, 1, 1)

        self.label_6 = QLabel(self.leftgrid)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMaximumSize(QSize(16777215, 40))
        self.label_6.setFont(font1)
        self.label_6.setStyleSheet(u"background:none")

        self.gridLayout_2.addWidget(self.label_6, 0, 0, 1, 1, Qt.AlignHCenter)


        self.horizontalLayout_4.addWidget(self.leftgrid)

        self.middle_panel = QFrame(self.page1)
        self.middle_panel.setObjectName(u"middle_panel")
        self.middle_panel.setMinimumSize(QSize(200, 0))
        self.middle_panel.setMaximumSize(QSize(400, 16777215))
        self.middle_panel.setStyleSheet(u"background-color: rgba(221, 221, 221, 50);")
        self.middle_panel.setFrameShape(QFrame.StyledPanel)
        self.middle_panel.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.middle_panel)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_8 = QLabel(self.middle_panel)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMaximumSize(QSize(16777215, 40))
        self.label_8.setFont(font1)
        self.label_8.setStyleSheet(u"background:none")

        self.verticalLayout_5.addWidget(self.label_8)

        self.time_int = QFrame(self.middle_panel)
        self.time_int.setObjectName(u"time_int")
        self.time_int.setMaximumSize(QSize(16777215, 60))
        self.time_int.setStyleSheet(u"background:none")
        self.time_int.setFrameShape(QFrame.StyledPanel)
        self.time_int.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.time_int)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.spinBox = QSpinBox(self.time_int)
        self.spinBox.setObjectName(u"spinBox")
        self.spinBox.setMaximumSize(QSize(16777215, 30))
        font3 = QFont()
        font3.setFamily(u"Segoe MDL2 Assets")
        font3.setPointSize(14)
        self.spinBox.setFont(font3)

        self.horizontalLayout_5.addWidget(self.spinBox)

        self.label_3 = QLabel(self.time_int)
        self.label_3.setObjectName(u"label_3")
        font4 = QFont()
        font4.setFamily(u"Segoe UI Symbol")
        font4.setPointSize(14)
        self.label_3.setFont(font4)
        self.label_3.setStyleSheet(u"background:none")

        self.horizontalLayout_5.addWidget(self.label_3)


        self.verticalLayout_5.addWidget(self.time_int)

        self.label_9 = QLabel(self.middle_panel)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMaximumSize(QSize(16777215, 40))
        self.label_9.setFont(font1)
        self.label_9.setStyleSheet(u"background:none")

        self.verticalLayout_5.addWidget(self.label_9)

        self.imgpp_spin = QSpinBox(self.middle_panel)
        self.imgpp_spin.setObjectName(u"imgpp_spin")
        self.imgpp_spin.setMaximumSize(QSize(16777215, 30))
        self.imgpp_spin.setFont(font3)
        self.imgpp_spin.setStyleSheet(u"background:none")
        self.imgpp_spin.setMinimum(1)
        self.imgpp_spin.setMaximum(4)

        self.verticalLayout_5.addWidget(self.imgpp_spin)

        self.frame_6 = QFrame(self.middle_panel)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setStyleSheet(u"background:none")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)

        self.verticalLayout_5.addWidget(self.frame_6)

        self.preview_btn = QPushButton(self.middle_panel)
        self.preview_btn.setObjectName(u"preview_btn")
        self.preview_btn.setMaximumSize(QSize(16777215, 30))
        self.preview_btn.setStyleSheet(u"QPushButton{\n"
"border-radius:8;\n"
"background-color: rgb(85,255,127);\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgba(85,255,127,150);\n"
"}")

        self.verticalLayout_5.addWidget(self.preview_btn)

        self.frame_7 = QFrame(self.middle_panel)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setMaximumSize(QSize(16777215, 30))
        self.frame_7.setStyleSheet(u"background:none")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)

        self.verticalLayout_5.addWidget(self.frame_7)

        self.convert_btn = QPushButton(self.middle_panel)
        self.convert_btn.setObjectName(u"convert_btn")
        self.convert_btn.setMaximumSize(QSize(16777215, 30))
        self.convert_btn.setStyleSheet(u"QPushButton{\n"
"border-radius:8;\n"
"background-color: rgb(85,255,127);\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgba(85,255,127,150);\n"
"}")

        self.verticalLayout_5.addWidget(self.convert_btn)


        self.horizontalLayout_4.addWidget(self.middle_panel)

        self.rightgrid = QFrame(self.page1)
        self.rightgrid.setObjectName(u"rightgrid")
        self.rightgrid.setMaximumSize(QSize(1000, 16777215))
        self.rightgrid.setStyleSheet(u"background-color: rgba(221, 221, 221, 50)")
        self.rightgrid.setFrameShape(QFrame.StyledPanel)
        self.rightgrid.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.rightgrid)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_5 = QLabel(self.rightgrid)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMaximumSize(QSize(16777215, 40))
        self.label_5.setFont(font1)
        self.label_5.setStyleSheet(u"background:none")

        self.gridLayout.addWidget(self.label_5, 0, 0, 1, 1, Qt.AlignHCenter)

        self.progressBar = QProgressBar(self.rightgrid)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setValue(24)

        self.gridLayout.addWidget(self.progressBar, 2, 0, 1, 1)

        self.right_content = QFrame(self.rightgrid)
        self.right_content.setObjectName(u"right_content")
        self.right_content.setStyleSheet(u"border-radius:8px;")
        self.right_content.setFrameShape(QFrame.StyledPanel)
        self.right_content.setFrameShadow(QFrame.Raised)

        self.gridLayout.addWidget(self.right_content, 1, 0, 1, 1)


        self.horizontalLayout_4.addWidget(self.rightgrid)

        self.stackedWidget.addWidget(self.page1)

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
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Drag & Drop or ", None))
        self.left_select_btn.setText(QCoreApplication.translate("MainWindow", u"Select file(s)", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"File(s) ", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Time stamp", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"ms", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Image(s) per page", None))
        self.preview_btn.setText(QCoreApplication.translate("MainWindow", u"Preview", None))
        self.convert_btn.setText(QCoreApplication.translate("MainWindow", u"Convert", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Preview", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"By Nakira @HWork", None))
    # retranslateUi

