# -*- coding: utf-8 -*-

################################################################################
# Form generated from reading UI file 'gui.ui'
##
# Created by: Qt User Interface Compiler version 5.15.2
##
# WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.materialLabel = QLabel(self.centralwidget)
        self.materialLabel.setObjectName(u"materialLabel")
        self.materialLabel.setGeometry(QRect(80, 30, 101, 16))
        self.testingDirectoryLabel = QLabel(self.centralwidget)
        self.testingDirectoryLabel.setObjectName(u"testingDirectoryLabel")
        self.testingDirectoryLabel.setGeometry(QRect(80, 90, 201, 16))
        self.weldingDirectoryLabel = QLabel(self.centralwidget)
        self.weldingDirectoryLabel.setObjectName(u"weldingDirectoryLabel")
        self.weldingDirectoryLabel.setGeometry(QRect(340, 90, 161, 16))
        self.bondAreaLabel = QLabel(self.centralwidget)
        self.bondAreaLabel.setObjectName(u"bondAreaLabel")
        self.bondAreaLabel.setGeometry(QRect(340, 30, 121, 16))
        self.databaseLabel = QLabel(self.centralwidget)
        self.databaseLabel.setObjectName(u"databaseLabel")
        self.databaseLabel.setGeometry(QRect(80, 220, 61, 16))
        self.userLabel = QLabel(self.centralwidget)
        self.userLabel.setObjectName(u"userLabel")
        self.userLabel.setGeometry(QRect(80, 270, 60, 16))
        self.passwordLabel = QLabel(self.centralwidget)
        self.passwordLabel.setObjectName(u"passwordLabel")
        self.passwordLabel.setGeometry(QRect(200, 270, 60, 16))
        self.hostLabel = QLabel(self.centralwidget)
        self.hostLabel.setObjectName(u"hostLabel")
        self.hostLabel.setGeometry(QRect(200, 220, 60, 16))
        self.chartOutputLabel = QLabel(self.centralwidget)
        self.chartOutputLabel.setObjectName(u"chartOutputLabel")
        self.chartOutputLabel.setGeometry(QRect(80, 330, 141, 16))
        self.processButton = QPushButton(self.centralwidget)
        self.processButton.setObjectName(u"processButton")
        self.processButton.setGeometry(QRect(290, 430, 171, 32))
        self.materialInput = QPlainTextEdit(self.centralwidget)
        self.materialInput.setObjectName(u"materialInput")
        self.materialInput.setGeometry(QRect(80, 50, 181, 21))
        self.bondAreaInput = QPlainTextEdit(self.centralwidget)
        self.bondAreaInput.setObjectName(u"bondAreaInput")
        self.bondAreaInput.setGeometry(QRect(340, 50, 161, 21))
        self.TestingDirectoryInput = QPlainTextEdit(self.centralwidget)
        self.TestingDirectoryInput.setObjectName(u"TestingDirectoryInput")
        self.TestingDirectoryInput.setGeometry(QRect(80, 110, 181, 21))
        self.WeldingDirectoryInput = QPlainTextEdit(self.centralwidget)
        self.WeldingDirectoryInput.setObjectName(u"WeldingDirectoryInput")
        self.WeldingDirectoryInput.setGeometry(QRect(340, 110, 181, 21))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 24))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(
            QCoreApplication.translate("MainWindow", u"MainWindow", None)
        )
        self.materialLabel.setText(
            QCoreApplication.translate("MainWindow", u"Material Name", None)
        )
        self.testingDirectoryLabel.setText(
            QCoreApplication.translate(
                "MainWindow", u"Testing Data Directory", None)
        )
        self.weldingDirectoryLabel.setText(
            QCoreApplication.translate(
                "MainWindow", u"Welding Data Directory", None)
        )
        self.bondAreaLabel.setText(
            QCoreApplication.translate("MainWindow", u"Bond area (mm^2)", None)
        )
        self.databaseLabel.setText(
            QCoreApplication.translate("MainWindow", u"Database", None)
        )
        self.userLabel.setText(
            QCoreApplication.translate("MainWindow", u"User", None))
        self.passwordLabel.setText(
            QCoreApplication.translate("MainWindow", u"Password", None)
        )
        self.hostLabel.setText(
            QCoreApplication.translate("MainWindow", u"Host", None))
        self.chartOutputLabel.setText(
            QCoreApplication.translate(
                "MainWindow", u"Chart Output Directory", None)
        )
        self.processButton.setText(
            QCoreApplication.translate(
                "MainWindow", u"Process Testing Data", None)
        )
        self.materialInput.setPlainText(
            QCoreApplication.translate(
                "MainWindow", u"Aluminium 5754-H111", None)
        )
        self.bondAreaInput.setPlainText(
            QCoreApplication.translate("MainWindow", u"180", None)
        )
        self.TestingDirectoryInput.setPlainText(
            QCoreApplication.translate(
                "MainWindow", u"refData/Testing-Data.xlsx", None)
        )
        self.WeldingDirectoryInput.setPlainText(
            QCoreApplication.translate(
                "MainWindow", u"refData/Welding data.xlsx", None)
        )

    # retranslateUi
