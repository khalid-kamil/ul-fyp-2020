# -*- coding: utf-8 -*-

################################################################################
# Form generated from reading UI file 'gui2.ui'
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
        MainWindow.resize(674, 479)
        MainWindow.setAutoFillBackground(True)
        MainWindow.setStyleSheet(u"\n"
                                 "\n"
                                 "QPushButton {\n"
                                 "    border-radius: 4px;\n"
                                 "	background-color: #80cbc4;\n"
                                 "}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tabWidget = QTabWidget(self.frame)
        self.tabWidget.setObjectName(u"tabWidget")
        font = QFont()
        font.setBold(False)
        font.setWeight(50)
        self.tabWidget.setFont(font)
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.gridLayout_4 = QGridLayout(self.tab)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.chartOutputLabel = QLabel(self.tab)
        self.chartOutputLabel.setObjectName(u"chartOutputLabel")

        self.gridLayout_4.addWidget(self.chartOutputLabel, 11, 3, 1, 1)

        self.host = QLineEdit(self.tab)
        self.host.setObjectName(u"host")

        self.gridLayout_4.addWidget(self.host, 4, 4, 1, 1)

        self.testingDataLabel = QLabel(self.tab)
        self.testingDataLabel.setObjectName(u"testingDataLabel")

        self.gridLayout_4.addWidget(self.testingDataLabel, 5, 0, 1, 1)

        self.database = QLineEdit(self.tab)
        self.database.setObjectName(u"database")

        self.gridLayout_4.addWidget(self.database, 3, 4, 1, 1)

        self.chartOutput = QLineEdit(self.tab)
        self.chartOutput.setObjectName(u"chartOutput")

        self.gridLayout_4.addWidget(self.chartOutput, 11, 4, 1, 1)

        self.materialLabel = QLabel(self.tab)
        self.materialLabel.setObjectName(u"materialLabel")

        self.gridLayout_4.addWidget(self.materialLabel, 3, 0, 1, 1)

        self.databaseLabel = QLabel(self.tab)
        self.databaseLabel.setObjectName(u"databaseLabel")

        self.gridLayout_4.addWidget(self.databaseLabel, 3, 3, 1, 1)

        self.bondAreaLabel = QLabel(self.tab)
        self.bondAreaLabel.setObjectName(u"bondAreaLabel")

        self.gridLayout_4.addWidget(self.bondAreaLabel, 4, 0, 1, 1)

        self.material = QLineEdit(self.tab)
        self.material.setObjectName(u"material")

        self.gridLayout_4.addWidget(self.material, 3, 1, 1, 1)

        self.bondArea = QSpinBox(self.tab)
        self.bondArea.setObjectName(u"bondArea")
        self.bondArea.setMaximum(1000)
        self.bondArea.setValue(180)

        self.gridLayout_4.addWidget(self.bondArea, 4, 1, 1, 1)

        self.testingData = QLineEdit(self.tab)
        self.testingData.setObjectName(u"testingData")

        self.gridLayout_4.addWidget(self.testingData, 5, 1, 1, 1)

        self.userLabel = QLabel(self.tab)
        self.userLabel.setObjectName(u"userLabel")

        self.gridLayout_4.addWidget(self.userLabel, 5, 3, 1, 1)

        self.passwordLabel = QLabel(self.tab)
        self.passwordLabel.setObjectName(u"passwordLabel")

        self.gridLayout_4.addWidget(self.passwordLabel, 6, 3, 1, 1)

        self.user = QLineEdit(self.tab)
        self.user.setObjectName(u"user")

        self.gridLayout_4.addWidget(self.user, 5, 4, 1, 1)

        self.hostLabel = QLabel(self.tab)
        self.hostLabel.setObjectName(u"hostLabel")

        self.gridLayout_4.addWidget(self.hostLabel, 4, 3, 1, 1)

        self.processDataButton = QPushButton(self.tab)
        self.processDataButton.setObjectName(u"processDataButton")
        self.processDataButton.setEnabled(True)
        self.processDataButton.setStyleSheet(u"")

        self.gridLayout_4.addWidget(self.processDataButton, 15, 4, 1, 1)

        self.password = QLineEdit(self.tab)
        self.password.setObjectName(u"password")
        self.password.setInputMethodHints(
            Qt.ImhHiddenText | Qt.ImhNoAutoUppercase | Qt.ImhNoPredictiveText | Qt.ImhSensitiveData)
        self.password.setEchoMode(QLineEdit.Password)

        self.gridLayout_4.addWidget(self.password, 6, 4, 1, 1)

        self.weldingDataLabel = QLabel(self.tab)
        self.weldingDataLabel.setObjectName(u"weldingDataLabel")

        self.gridLayout_4.addWidget(self.weldingDataLabel, 6, 0, 1, 1)

        self.weldingData = QLineEdit(self.tab)
        self.weldingData.setObjectName(u"weldingData")

        self.gridLayout_4.addWidget(self.weldingData, 6, 1, 1, 1)

        self.outputDetailsHeading = QLabel(self.tab)
        self.outputDetailsHeading.setObjectName(u"outputDetailsHeading")
        font1 = QFont()
        font1.setBold(True)
        font1.setWeight(75)
        self.outputDetailsHeading.setFont(font1)
        self.outputDetailsHeading.setAlignment(
            Qt.AlignLeading | Qt.AlignLeft | Qt.AlignVCenter)

        self.gridLayout_4.addWidget(self.outputDetailsHeading, 2, 3, 1, 2)

        self.verticalSpacer_2 = QSpacerItem(
            20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_4.addItem(self.verticalSpacer_2, 1, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(
            20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_4.addItem(self.verticalSpacer, 13, 4, 1, 1)

        self.inputDetailsHeading = QLabel(self.tab)
        self.inputDetailsHeading.setObjectName(u"inputDetailsHeading")
        self.inputDetailsHeading.setFont(font1)
        self.inputDetailsHeading.setAlignment(
            Qt.AlignLeading | Qt.AlignLeft | Qt.AlignVCenter)

        self.gridLayout_4.addWidget(self.inputDetailsHeading, 2, 0, 1, 2)

        self.tab1Heading = QLabel(self.tab)
        self.tab1Heading.setObjectName(u"tab1Heading")
        font2 = QFont()
        font2.setPointSize(16)
        font2.setBold(True)
        font2.setWeight(75)
        self.tab1Heading.setFont(font2)
        self.tab1Heading.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.tab1Heading, 0, 0, 1, 5)

        self.errorLabel = QLabel(self.tab)
        self.errorLabel.setObjectName(u"errorLabel")
        self.errorLabel.setStyleSheet(u"")
        self.errorLabel.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.errorLabel, 12, 0, 1, 5)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.gridLayout = QGridLayout(self.tab_2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.tab2Heading = QLabel(self.tab_2)
        self.tab2Heading.setObjectName(u"tab2Heading")
        self.tab2Heading.setFont(font2)
        self.tab2Heading.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.tab2Heading, 0, 0, 1, 2)

        self.tabWidget.addTab(self.tab_2, "")

        self.verticalLayout.addWidget(self.tabWidget)

        self.verticalLayout_2.addWidget(self.frame)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 674, 24))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
# if QT_CONFIG(shortcut)
        self.chartOutputLabel.setBuddy(self.chartOutput)
        self.testingDataLabel.setBuddy(self.testingData)
        self.materialLabel.setBuddy(self.material)
        self.databaseLabel.setBuddy(self.database)
        self.bondAreaLabel.setBuddy(self.bondArea)
        self.userLabel.setBuddy(self.user)
        self.passwordLabel.setBuddy(self.password)
        self.hostLabel.setBuddy(self.host)
        self.weldingDataLabel.setBuddy(self.weldingData)
#endif // QT_CONFIG(shortcut)
        QWidget.setTabOrder(self.tabWidget, self.material)
        QWidget.setTabOrder(self.material, self.bondArea)
        QWidget.setTabOrder(self.bondArea, self.testingData)
        QWidget.setTabOrder(self.testingData, self.weldingData)
        QWidget.setTabOrder(self.weldingData, self.database)
        QWidget.setTabOrder(self.database, self.host)
        QWidget.setTabOrder(self.host, self.user)
        QWidget.setTabOrder(self.user, self.password)
        QWidget.setTabOrder(self.password, self.chartOutput)
        QWidget.setTabOrder(self.chartOutput, self.processDataButton)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate(
            "MainWindow", u"MainWindow", None))
        self.chartOutputLabel.setText(QCoreApplication.translate(
            "MainWindow", u"Chart Output:", None))
        self.host.setText(QCoreApplication.translate(
            "MainWindow", u"localhost", None))
        self.testingDataLabel.setText(QCoreApplication.translate(
            "MainWindow", u"Testing Data:", None))
        self.database.setText(QCoreApplication.translate(
            "MainWindow", u"materialtestsDB", None))
        self.chartOutput.setText(QCoreApplication.translate(
            "MainWindow", u"outputs/plots", None))
        self.materialLabel.setText(QCoreApplication.translate(
            "MainWindow", u"Material:", None))
        self.databaseLabel.setText(QCoreApplication.translate(
            "MainWindow", u"Database:", None))
        self.bondAreaLabel.setText(QCoreApplication.translate(
            "MainWindow", u"Bond Area:", None))
        self.material.setText(QCoreApplication.translate(
            "MainWindow", u"Aluminium 5754-H111", None))
        self.testingData.setText(QCoreApplication.translate(
            "MainWindow", u"refData/Testing-Data.xlsx", None))
        self.userLabel.setText(QCoreApplication.translate(
            "MainWindow", u"User:", None))
        self.passwordLabel.setText(QCoreApplication.translate(
            "MainWindow", u"Password:", None))
        self.user.setText(QCoreApplication.translate(
            "MainWindow", u"khalid", None))
        self.hostLabel.setText(QCoreApplication.translate(
            "MainWindow", u"Host:", None))
        self.processDataButton.setText(
            QCoreApplication.translate("MainWindow", u"Process Data", None))
        self.password.setText(QCoreApplication.translate(
            "MainWindow", u"fyp2020", None))
        self.weldingDataLabel.setText(QCoreApplication.translate(
            "MainWindow", u"Welding Data:", None))
        self.weldingData.setText(QCoreApplication.translate(
            "MainWindow", u"refData/Welding data.xlsx", None))
        self.outputDetailsHeading.setText(
            QCoreApplication.translate("MainWindow", u"OUTPUT DETAILS", None))
        self.inputDetailsHeading.setText(
            QCoreApplication.translate("MainWindow", u"INPUT DETAILS", None))
        self.tab1Heading.setText(QCoreApplication.translate(
            "MainWindow", u"USW DATA PROCESSING", None))
        self.errorLabel.setText(QCoreApplication.translate(
            "MainWindow", u"<html><head/><body><p><span style=\" color:#fc2b2d;\">Error Label</span></p></body></html>", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(
            self.tab), QCoreApplication.translate("MainWindow", u"Data Processing", None))
        self.tab2Heading.setText(QCoreApplication.translate(
            "MainWindow", u"USW MACHNINE LEARNING", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(
            self.tab_2), QCoreApplication.translate("MainWindow", u"Machine Learning", None))
    # retranslateUi
