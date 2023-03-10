#!/usr/bin/python3
# -*- coding: utf-8 -*-


from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPainter, QColor, QBrush, QFont
from PyQt5 import QtWidgets, QtCore


class Example(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(660, 418)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Text = QtWidgets.QLabel(self.centralwidget)
        self.Text.setGeometry(QtCore.QRect(40, 100, 660, 31))
        self.Text.setObjectName("Text")
        self.Text.setFont(QFont('Dosis', 15))
        self.Yes = QtWidgets.QPushButton(self.centralwidget)
        self.Yes.setGeometry(QtCore.QRect(140, 230, 121, 70))
        self.Yes.setObjectName("Да")
        self.Yes.setFont(QFont('Dosis', 15))
        self.Yes.setStyleSheet("""
                    QPushButton { background-color: white}
                    QPushButton:!hover { background-color: #FF9218}
                """)
        self.No = QtWidgets.QPushButton(self.centralwidget)
        self.No.setGeometry(QtCore.QRect(400, 230, 121, 70))
        self.No.setObjectName("No")
        self.No.setFont(QFont('Dosis', 15))
        self.No.setStyleSheet('QPushButton {background-color: #FF9218}')
        self.No.setStyleSheet("""
                    QPushButton { background-color: white}
                    QPushButton:!hover { background-color: #FF9218}
                """)
        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.show()

        self.setStyleSheet("#MainWindow{border-image:url(fon_1.jpg)}")

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "Обучашка"))
        self.Text.setText(_translate("MainWindow", "Вы уже регистрировались в нашем приложении?"))
        self.Yes.setText(_translate("MainWindow", "Да"))
        self.No.setText(_translate("MainWindow", "Нет"))