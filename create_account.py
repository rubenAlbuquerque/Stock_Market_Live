import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

"""
class Window_new_account():

    def __init__(self, ):
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

    def initUI(self):
        # Frame
        self.frame = QFrame(self.window)
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setObjectName("Frame")
        self.frame.resize(500, 550)
        self.frame.move(600, 150)


"""


class Ui_NewUser(object):
    """
    NEW USERS
    """
    def setupUi(self, NewUser):
        NewUser.setObjectName("NewUser")
        NewUser.resize(555, 372)
        NewUser.setStyleSheet("background-color: rgb(14, 14, 14);")
        self.l_newuser = QLabel(NewUser)
        self.l_newuser.setGeometry(QRect(180, 10, 181, 31))
        self.l_newuser.setStyleSheet("font: 24pt \".SF NS Text\";\n"
                                     "color: rgb(234, 239, 238);\n"
                                     "")
        self.l_newuser.setAlignment(Qt.AlignCenter)
        self.l_newuser.setObjectName("l_newuser")
        self.line = QFrame(NewUser)
        self.line.setGeometry(QRect(10, 50, 591, 20))
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.line.setObjectName("line")
        self.txt_firstname = QLineEdit(NewUser)
        self.txt_firstname.setEnabled(True)
        self.txt_firstname.setGeometry(QRect(30, 80, 230, 41))
        self.txt_firstname.setStyleSheet("background-color: rgb(207, 211, 211);\n"
                                         "border-style:outset;\n"
                                         "border-radius:10px;\n"
                                         "font: 14pt \"Arial\";")
        self.txt_firstname.setText("")
        self.txt_firstname.setObjectName("txt_firstname")
        self.txt_lastname = QLineEdit(NewUser)
        self.txt_lastname.setGeometry(QRect(290, 80, 229, 41))
        self.txt_lastname.setStyleSheet("background-color: rgb(207, 211, 211);\n"
                                        "border-style:outset;\n"
                                        "border-radius:10px;\n"
                                        "font: 14pt \"Arial\";")
        self.txt_lastname.setObjectName("txt_lastname")
        self.txt_phone = QLineEdit(NewUser)
        self.txt_phone.setGeometry(QRect(30, 140, 230, 41))
        self.txt_phone.setStyleSheet("background-color: rgb(207, 211, 211);\n"
                                     "border-style:outset;\n"
                                     "border-radius:10px;\n"
                                     "font: 14pt \"Arial\";")
        self.txt_phone.setObjectName("txt_phone")
        self.txt_email = QLineEdit(NewUser)
        self.txt_email.setGeometry(QRect(290, 140, 229, 41))
        self.txt_email.setStyleSheet("background-color: rgb(207, 211, 211);\n"
                                     "border-style:outset;\n"
                                     "border-radius:10px;\n"
                                     "font: 14pt \"Arial\";")
        self.txt_email.setObjectName("txt_email")
        self.txt_username = QLineEdit(NewUser)
        self.txt_username.setGeometry(QRect(30, 200, 230, 41))
        self.txt_username.setStyleSheet("background-color: rgb(207, 211, 211);\n"
                                        "border-style:outset;\n"
                                        "border-radius:10px;\n"
                                        "font: 14pt \"Arial\";")
        self.txt_username.setObjectName("txt_username")
        self.lineEdit = QLineEdit(NewUser)
        self.lineEdit.setGeometry(QRect(290, 200, 231, 41))
        self.lineEdit.setStyleSheet("background-color: rgb(207, 211, 211);\n"
                                    "border-style:outset;\n"
                                    "border-radius:10px;\n"
                                    "font: 14pt \"Arial\";")
        self.lineEdit.setObjectName("lineEdit")
        self.btn_submit = QPushButton(NewUser)
        self.btn_submit.setGeometry(QRect(190, 270, 159, 31))
        self.btn_submit.setStyleSheet("color: rgb(250, 255, 255);\n"
                                      "background-color: rgb(73, 199, 41);\n"
                                      "border-style:outset;\n"
                                      "border-radius:10px;\n"
                                      "font: 14pt \"Arial\";")
        self.btn_submit.setObjectName("btn_submit")
        self.Back = QPushButton(NewUser)
        self.Back.setGeometry(QRect(190, 320, 159, 31))
        self.Back.setStyleSheet("color: rgb(250, 255, 255);\n"
                                "background-color: rgb(73, 199, 41);\n"
                                "border-style:outset;\n"
                                "border-radius:10px;\n"
                                "font: 14pt \"Arial\";")
        self.Back.setObjectName("Back")

        self.retranslateUi(NewUser)
        QMetaObject.connectSlotsByName(NewUser)

