# ! /usr/bin/python3
from sys import exit as sysExit
import sys

from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QStackedWidget, QFileDialog

class MainScreen(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainScreen, self).__init__()
        loadUi("main.ui", self)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    app.setApplicationName("RSA Encrypt-Decrypt")

    main = MainScreen()
    
    widget = QStackedWidget()
    widget.addWidget(main)
    widget.setMinimumHeight(688)
    widget.setMinimumWidth(480)

    widget.show()
    
    sys.exit(app.exec_())