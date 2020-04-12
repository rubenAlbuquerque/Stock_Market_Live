
import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class MainWindow():

    def __init__(self):
        super().__init__()
        self.app = QApplication(sys.argv)
        self.window = QMainWindow()

        with open('style.qss') as f:
            self.style = f.read()

        self.initUI()
        self.window.setWindowTitle(" ")
        self.window.setWindowIcon(QIcon('Capturar.PNG'))
        self.window.setGeometry(100, 100, 1700, 850)

        self.window.show()
        self.app.setStyleSheet(self.style)
        sys.exit(self.app.exec_())




    def initUI(self):
        with open('style.qss') as f:
            stylesheet = f.read()

        # self.setFixedSize(240, 480)


        self.okButton = QPushButton("OK", self.window)
        self.okButton.move(10, 100)
        self.cancelButton = QPushButton("Cancel", self.window)


        """"
        hbox.addWidget(cancelButton)

        hbox.addWidget(cancelButton)

        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hbox)
        vbox.addStretch(1)
        vbox.addStretch(1)

        self.setLayout(vbox)
        """

if __name__ == '__main__':

    ex = MainWindow()















