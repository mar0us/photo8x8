# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'data_create.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(998, 739)
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonFollowStyle)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.image_label = QtWidgets.QLabel(self.centralwidget)
        self.image_label.setEnabled(True)
        self.image_label.setGeometry(QtCore.QRect(40, 30, 400, 400))
        self.image_label.setMaximumSize(QtCore.QSize(401, 401))
        self.image_label.setText("")
        self.image_label.setObjectName("image_label")
        self.line1_button = QtWidgets.QPushButton(self.centralwidget)
        self.line1_button.setGeometry(QtCore.QRect(510, 295, 128, 128))
        self.line1_button.setStyleSheet("QPushButton\n"
"{ \n"
"    background-color: white\n"
"}")
        self.line1_button.setText("")
        self.line1_button.setObjectName("line1_button")
        self.line2_button = QtWidgets.QPushButton(self.centralwidget)
        self.line2_button.setGeometry(QtCore.QRect(650, 295, 128, 128))
        self.line2_button.setStyleSheet("QPushButton\n"
"{ \n"
"    background-color: white\n"
"}")
        self.line2_button.setText("")
        self.line2_button.setObjectName("line2_button")
        self.line3_button = QtWidgets.QPushButton(self.centralwidget)
        self.line3_button.setGeometry(QtCore.QRect(790, 295, 128, 128))
        self.line3_button.setStyleSheet("QPushButton\n"
"{ \n"
"    background-color: white\n"
"}")
        self.line3_button.setText("")
        self.line3_button.setObjectName("line3_button")
        self.line4_button = QtWidgets.QPushButton(self.centralwidget)
        self.line4_button.setGeometry(QtCore.QRect(510, 435, 128, 128))
        self.line4_button.setStyleSheet("QPushButton\n"
"{ \n"
"    background-color: white\n"
"}")
        self.line4_button.setText("")
        self.line4_button.setObjectName("line4_button")
        self.line5_button = QtWidgets.QPushButton(self.centralwidget)
        self.line5_button.setGeometry(QtCore.QRect(650, 435, 128, 128))
        self.line5_button.setStyleSheet("QPushButton\n"
"{ \n"
"    background-color: white\n"
"}")
        self.line5_button.setText("")
        self.line5_button.setObjectName("line5_button")
        self.line6_button = QtWidgets.QPushButton(self.centralwidget)
        self.line6_button.setGeometry(QtCore.QRect(790, 435, 128, 128))
        self.line6_button.setStyleSheet("QPushButton\n"
"{ \n"
"    background-color: white\n"
"}")
        self.line6_button.setText("")
        self.line6_button.setObjectName("line6_button")
        self.line9_button = QtWidgets.QPushButton(self.centralwidget)
        self.line9_button.setGeometry(QtCore.QRect(790, 570, 128, 128))
        self.line9_button.setStyleSheet("QPushButton\n"
"{ \n"
"    background-color: white\n"
"}")
        self.line9_button.setText("")
        self.line9_button.setObjectName("line9_button")
        self.line8_button = QtWidgets.QPushButton(self.centralwidget)
        self.line8_button.setGeometry(QtCore.QRect(650, 570, 128, 128))
        self.line8_button.setStyleSheet("QPushButton\n"
"{ \n"
"    background-color: white\n"
"}")
        self.line8_button.setText("")
        self.line8_button.setObjectName("line8_button")
        self.line7_button = QtWidgets.QPushButton(self.centralwidget)
        self.line7_button.setGeometry(QtCore.QRect(510, 570, 128, 128))
        self.line7_button.setStyleSheet("QPushButton\n"
"{ \n"
"    background-color: white\n"
"}")
        self.line7_button.setText("")
        self.line7_button.setObjectName("line7_button")
        self.down_button = QtWidgets.QPushButton(self.centralwidget)
        self.down_button.setGeometry(QtCore.QRect(170, 575, 128, 128))
        self.down_button.setStyleSheet("QPushButton\n"
"{ \n"
"    background-color: white\n"
"}")
        self.down_button.setText("")
        self.down_button.setObjectName("down_button")
        self.up_button = QtWidgets.QPushButton(self.centralwidget)
        self.up_button.setGeometry(QtCore.QRect(170, 440, 128, 128))
        self.up_button.setStyleSheet("QPushButton\n"
"{ \n"
"    background-color: white\n"
"}")
        self.up_button.setText("")
        self.up_button.setObjectName("up_button")
        self.left_button = QtWidgets.QPushButton(self.centralwidget)
        self.left_button.setGeometry(QtCore.QRect(30, 510, 128, 128))
        self.left_button.setStyleSheet("QPushButton\n"
"{ \n"
"    background-color: white\n"
"}")
        self.left_button.setText("")
        self.left_button.setObjectName("left_button")
        self.right_button = QtWidgets.QPushButton(self.centralwidget)
        self.right_button.setGeometry(QtCore.QRect(310, 510, 128, 128))
        self.right_button.setStyleSheet("QPushButton\n"
"{ \n"
"    background-color: white\n"
"}")
        self.right_button.setText("")
        self.right_button.setObjectName("right_button")
        self.map_label = QtWidgets.QLabel(self.centralwidget)
        self.map_label.setEnabled(True)
        self.map_label.setGeometry(QtCore.QRect(590, 20, 256, 256))
        self.map_label.setMaximumSize(QtCore.QSize(256, 256))
        self.map_label.setText("")
        self.map_label.setObjectName("map_label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
