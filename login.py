
import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


from register import Ui_MainWindow

class MainWindow():

    def __init__(self):
        super().__init__()
        self.app = QApplication(sys.argv)
        self.window = QMainWindow()

        with open('style.css') as f:
            self.style = f.read()

        self.width = 1700
        self.height = 850
        self.initUI()
        self.window.setWindowTitle(" ")
        self.window.setWindowIcon(QIcon('Capturar.PNG'))
        self.window.setGeometry(100, 100, self.width, self.height)
        self.window.setFixedSize(1700, 850)

        # image backgroud
        oImage = QImage("Login_image.jpg")
        sImage = oImage.scaled(QSize(1700, 850))  # resize Image to widgets size
        palette = QPalette()
        palette.setBrush(10, QBrush(sImage))  # 10 = Windowrole
        self.window.setPalette(palette)

        self.window.show()
        self.app.setStyleSheet(self.style)
        sys.exit(self.app.exec_())

    def create_account(self):
        self.OtherWindow = QMainWindow()
        ui = Ui_MainWindow(self.OtherWindow)
        # ui.setupUi(self.OtherWindow)
        self.window.hide()

    def initUI(self):
        # Frame
        self.frame = QFrame(self.window)
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setObjectName("Frame")
        self.frame.resize(500, 550)
        self.frame.move(600, 150)

        # Textbox: Email
        self.userfild = QLineEdit(self.window)
        self.userfild.setPlaceholderText("Email ")
        self.userfild.setAlignment(Qt.AlignCenter)
        self.userfild.resize(400, 60)
        self.userfild.move(650, 300)

        # Textbox: Password
        self.password = QLineEdit(self.window)
        self.password.setPlaceholderText("Password ")
        self.password.setAlignment(Qt.AlignCenter)
        self.password.resize(400, 60)
        self.password.move(650, 380)

        # New Password
        self.new_pass = QPushButton("Forgot your password ?", self.window)
        self.new_pass.setObjectName("newpass")
        # .clicked.connect()
        self.new_pass.resize(200, 30)
        self.new_pass.move(820, 450)

        # Log in
        self.okButton = QPushButton("LOGIN", self.window)
        self.okButton.setObjectName("btn_login")
        # .clicked.connect()
        self.okButton.resize(300, 60)
        self.okButton.move(700, 540)

        # Register
        self.new_account = QPushButton("Create new account", self.window)
        self.new_account.setObjectName("new_account")
        self.new_account.clicked.connect(self.create_account)
        self.new_account.resize(300, 60)
        self.new_account.move(700, 620)




if __name__ == '__main__':
    ex = MainWindow()

















