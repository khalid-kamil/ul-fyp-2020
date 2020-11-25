from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from TestingData import TestingData
from ui_processing import Ui_MainWindow
import sys
from TestingData import TestingData
import matplotlib
import matplotlib.pyplot as plt

matplotlib.use('AGG')


class ProcessingApp(Ui_MainWindow):
    def __init__(self, window):
        self.setupUi(window)
        self.processButton.clicked.connect(self.processData)

    def processData(self):
        test = TestingData(self.materialInput.toPlainText(
        ), self.TestingDirectoryInput.toPlainText(), self.WeldingDirectoryInput.toPlainText(), self.bondAreaInput.toPlainText())


app = QApplication(sys.argv)
MainWindow = QMainWindow()

ui = ProcessingApp(MainWindow)

MainWindow.show()

app.exec_()
