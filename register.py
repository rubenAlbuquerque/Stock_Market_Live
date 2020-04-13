from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class Ui_MainWindow():
    def __init__(self, OtherWindow):
        self.window_regi = OtherWindow

        # with open('style.css') as f:
        #     self.style = f.read()

        self.initUI()
        self.window_regi.setWindowTitle(" ")
        self.window_regi.setWindowIcon(QIcon('Capturar.PNG'))
        self.window_regi.setGeometry(100, 100, 1700, 850)
        self.window_regi.setFixedSize(1700, 850)

        # image backgroud
        oImage = QImage("paises.jpg")
        sImage = oImage.scaled(QSize(1700, 850))  # resize Image to widgets size
        palette = QPalette()
        palette.setBrush(10, QBrush(sImage))  # 10 = Windowrole
        self.window_regi.setPalette(palette)

        self.window_regi.show()
        # self.app.setStyleSheet(self.style)

    def initUI(self):
        # Frame
        self.frame = QFrame(self.window_regi)
        self.frame.setObjectName("Frame")
        self.frame.resize(500, 550)
        self.frame.move(600, 150)

        # Label
        self.title = QLabel(self.window_regi)
        self.title.setText("Authorization")
        self.title.setFont(QFont('Calibri (Corpo)', 20, QFont.Bold))
        self.title.setAlignment(Qt.AlignCenter)
        self.title.setStyleSheet('color: White')
        self.title.resize(350, 100)
        self.title.move(670, 160)


        # Textbox: Email
        self.userfild = QLineEdit(self.window_regi)
        self.userfild.setPlaceholderText("Email")
        self.userfild.setAlignment(Qt.AlignCenter)
        self.userfild.resize(400, 60)
        self.userfild.move(650, 300)

        # Textbox: Password
        self.password = QLineEdit(self.window_regi)
        self.password.setPlaceholderText("Password")
        self.password.setAlignment(Qt.AlignCenter)
        self.password.resize(400, 60)
        self.password.move(650, 380)

        # Textbox: Confirm Password
        self.conf_password = QLineEdit(self.window_regi)
        self.conf_password.setPlaceholderText("Confirm Password")
        self.conf_password.setAlignment(Qt.AlignCenter)
        self.conf_password.resize(400, 60)
        self.conf_password.move(650, 460)

        # Register
        self.next = QPushButton("Create new account", self.window_regi)
        self.next.setObjectName("new_account")
        self.next.clicked.connect(self.create_account)
        self.next.resize(300, 60)
        self.next.move(700, 620)

    def create_account(self):
        print("----")


"""
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    OtherWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(OtherWindow)
    OtherWindow.show()
    sys.exit(app.exec_())
"""
