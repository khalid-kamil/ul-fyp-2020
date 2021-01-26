import sys
import matplotlib
# matplotlib.use('AGG')
import matplotlib.pyplot as plt

from MainWindow import Ui_MainWindow
from TestingData import TestingData
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *



class ProcessingApp(Ui_MainWindow):
    def __init__(self, window):
        self.setupUi(window)
        self.processDataButton.clicked.connect(self.processData)

    def processData(self):
        test = TestingData(self.material.text(), self.testingData.text(), self.weldingData.text(), self.bondArea.value(
        ), self.database.text(), self.user.text(), self.password.text(), self.host.text(), self.chartOutput.text())


app = QApplication(sys.argv)
MainWindow = QMainWindow()
# ProcessingApp(Ui_MainWindow)
ui = ProcessingApp(MainWindow)


MainWindow.show()
app.exec_()
