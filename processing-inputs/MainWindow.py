# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui2.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(674, 479)
        MainWindow.setAutoFillBackground(True)
        MainWindow.setStyleSheet("\n"
"\n"
"QPushButton {\n"
"    border-radius: 4px;\n"
"    background-color: #80cbc4;\n"
"    box-shadow: 4px, 4px;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.frame)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.tabWidget.setFont(font)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.tab)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.chartOutputLabel = QtWidgets.QLabel(self.tab)
        self.chartOutputLabel.setObjectName("chartOutputLabel")
        self.gridLayout_4.addWidget(self.chartOutputLabel, 11, 3, 1, 1)
        self.host = QtWidgets.QLineEdit(self.tab)
        self.host.setObjectName("host")
        self.gridLayout_4.addWidget(self.host, 4, 4, 1, 1)
        self.testingDataLabel = QtWidgets.QLabel(self.tab)
        self.testingDataLabel.setObjectName("testingDataLabel")
        self.gridLayout_4.addWidget(self.testingDataLabel, 5, 0, 1, 1)
        self.database = QtWidgets.QLineEdit(self.tab)
        self.database.setObjectName("database")
        self.gridLayout_4.addWidget(self.database, 3, 4, 1, 1)
        self.chartOutput = QtWidgets.QLineEdit(self.tab)
        self.chartOutput.setObjectName("chartOutput")
        self.gridLayout_4.addWidget(self.chartOutput, 11, 4, 1, 1)
        self.materialLabel = QtWidgets.QLabel(self.tab)
        self.materialLabel.setObjectName("materialLabel")
        self.gridLayout_4.addWidget(self.materialLabel, 3, 0, 1, 1)
        self.databaseLabel = QtWidgets.QLabel(self.tab)
        self.databaseLabel.setObjectName("databaseLabel")
        self.gridLayout_4.addWidget(self.databaseLabel, 3, 3, 1, 1)
        self.bondAreaLabel = QtWidgets.QLabel(self.tab)
        self.bondAreaLabel.setObjectName("bondAreaLabel")
        self.gridLayout_4.addWidget(self.bondAreaLabel, 4, 0, 1, 1)
        self.material = QtWidgets.QLineEdit(self.tab)
        self.material.setObjectName("material")
        self.gridLayout_4.addWidget(self.material, 3, 1, 1, 1)
        self.bondArea = QtWidgets.QSpinBox(self.tab)
        self.bondArea.setMaximum(1000)
        self.bondArea.setProperty("value", 180)
        self.bondArea.setObjectName("bondArea")
        self.gridLayout_4.addWidget(self.bondArea, 4, 1, 1, 1)
        self.testingData = QtWidgets.QLineEdit(self.tab)
        self.testingData.setObjectName("testingData")
        self.gridLayout_4.addWidget(self.testingData, 5, 1, 1, 1)
        self.userLabel = QtWidgets.QLabel(self.tab)
        self.userLabel.setObjectName("userLabel")
        self.gridLayout_4.addWidget(self.userLabel, 5, 3, 1, 1)
        self.passwordLabel = QtWidgets.QLabel(self.tab)
        self.passwordLabel.setObjectName("passwordLabel")
        self.gridLayout_4.addWidget(self.passwordLabel, 6, 3, 1, 1)
        self.user = QtWidgets.QLineEdit(self.tab)
        self.user.setObjectName("user")
        self.gridLayout_4.addWidget(self.user, 5, 4, 1, 1)
        self.hostLabel = QtWidgets.QLabel(self.tab)
        self.hostLabel.setObjectName("hostLabel")
        self.gridLayout_4.addWidget(self.hostLabel, 4, 3, 1, 1)
        self.processDataButton = QtWidgets.QPushButton(self.tab)
        self.processDataButton.setEnabled(True)
        self.processDataButton.setStyleSheet("")
        self.processDataButton.setObjectName("processDataButton")
        self.gridLayout_4.addWidget(self.processDataButton, 15, 4, 1, 1)
        self.password = QtWidgets.QLineEdit(self.tab)
        self.password.setInputMethodHints(QtCore.Qt.ImhHiddenText|QtCore.Qt.ImhNoAutoUppercase|QtCore.Qt.ImhNoPredictiveText|QtCore.Qt.ImhSensitiveData)
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password.setObjectName("password")
        self.gridLayout_4.addWidget(self.password, 6, 4, 1, 1)
        self.weldingDataLabel = QtWidgets.QLabel(self.tab)
        self.weldingDataLabel.setObjectName("weldingDataLabel")
        self.gridLayout_4.addWidget(self.weldingDataLabel, 6, 0, 1, 1)
        self.weldingData = QtWidgets.QLineEdit(self.tab)
        self.weldingData.setObjectName("weldingData")
        self.gridLayout_4.addWidget(self.weldingData, 6, 1, 1, 1)
        self.outputDetailsHeading = QtWidgets.QLabel(self.tab)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.outputDetailsHeading.setFont(font)
        self.outputDetailsHeading.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.outputDetailsHeading.setObjectName("outputDetailsHeading")
        self.gridLayout_4.addWidget(self.outputDetailsHeading, 2, 3, 1, 2)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_4.addItem(spacerItem, 1, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_4.addItem(spacerItem1, 13, 4, 1, 1)
        self.inputDetailsHeading = QtWidgets.QLabel(self.tab)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.inputDetailsHeading.setFont(font)
        self.inputDetailsHeading.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.inputDetailsHeading.setObjectName("inputDetailsHeading")
        self.gridLayout_4.addWidget(self.inputDetailsHeading, 2, 0, 1, 2)
        self.tab1Heading = QtWidgets.QLabel(self.tab)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.tab1Heading.setFont(font)
        self.tab1Heading.setAlignment(QtCore.Qt.AlignCenter)
        self.tab1Heading.setObjectName("tab1Heading")
        self.gridLayout_4.addWidget(self.tab1Heading, 0, 0, 1, 5)
        self.errorLabel = QtWidgets.QLabel(self.tab)
        self.errorLabel.setStyleSheet("\n"
"")
        self.errorLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.errorLabel.setObjectName("errorLabel")
        self.gridLayout_4.addWidget(self.errorLabel, 12, 0, 1, 5)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridLayout = QtWidgets.QGridLayout(self.tab_2)
        self.gridLayout.setObjectName("gridLayout")
        self.tab2Heading = QtWidgets.QLabel(self.tab_2)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.tab2Heading.setFont(font)
        self.tab2Heading.setAlignment(QtCore.Qt.AlignCenter)
        self.tab2Heading.setObjectName("tab2Heading")
        self.gridLayout.addWidget(self.tab2Heading, 0, 0, 1, 2)
        self.tabWidget.addTab(self.tab_2, "")
        self.verticalLayout.addWidget(self.tabWidget)
        self.verticalLayout_2.addWidget(self.frame)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 674, 24))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.chartOutputLabel.setBuddy(self.chartOutput)
        self.testingDataLabel.setBuddy(self.testingData)
        self.materialLabel.setBuddy(self.material)
        self.databaseLabel.setBuddy(self.database)
        self.bondAreaLabel.setBuddy(self.bondArea)
        self.userLabel.setBuddy(self.user)
        self.passwordLabel.setBuddy(self.password)
        self.hostLabel.setBuddy(self.host)
        self.weldingDataLabel.setBuddy(self.weldingData)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.tabWidget, self.material)
        MainWindow.setTabOrder(self.material, self.bondArea)
        MainWindow.setTabOrder(self.bondArea, self.testingData)
        MainWindow.setTabOrder(self.testingData, self.weldingData)
        MainWindow.setTabOrder(self.weldingData, self.database)
        MainWindow.setTabOrder(self.database, self.host)
        MainWindow.setTabOrder(self.host, self.user)
        MainWindow.setTabOrder(self.user, self.password)
        MainWindow.setTabOrder(self.password, self.chartOutput)
        MainWindow.setTabOrder(self.chartOutput, self.processDataButton)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.chartOutputLabel.setText(_translate("MainWindow", "Chart Output:"))
        self.host.setText(_translate("MainWindow", "localhost"))
        self.testingDataLabel.setText(_translate("MainWindow", "Testing Data:"))
        self.database.setText(_translate("MainWindow", "materialtestsDB"))
        self.chartOutput.setText(_translate("MainWindow", "outputs/plots"))
        self.materialLabel.setText(_translate("MainWindow", "Material:"))
        self.databaseLabel.setText(_translate("MainWindow", "Database:"))
        self.bondAreaLabel.setText(_translate("MainWindow", "Bond Area:"))
        self.material.setText(_translate("MainWindow", "Aluminium 5754-H111"))
        self.testingData.setText(_translate("MainWindow", "refData/Testing-Data.xlsx"))
        self.userLabel.setText(_translate("MainWindow", "User:"))
        self.passwordLabel.setText(_translate("MainWindow", "Password:"))
        self.user.setText(_translate("MainWindow", "khalid"))
        self.hostLabel.setText(_translate("MainWindow", "Host:"))
        self.processDataButton.setText(_translate("MainWindow", "Process Data"))
        self.password.setText(_translate("MainWindow", "fyp2020"))
        self.weldingDataLabel.setText(_translate("MainWindow", "Welding Data:"))
        self.weldingData.setText(_translate("MainWindow", "refData/Welding data.xlsx"))
        self.outputDetailsHeading.setText(_translate("MainWindow", "OUTPUT DETAILS"))
        self.inputDetailsHeading.setText(_translate("MainWindow", "INPUT DETAILS"))
        self.tab1Heading.setText(_translate("MainWindow", "USW DATA PROCESSING"))
        self.errorLabel.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#fc2b2d;\">Error Label</span></p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Data Processing"))
        self.tab2Heading.setText(_translate("MainWindow", "USW MACHNINE LEARNING"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Machine Learning"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
