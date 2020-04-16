
import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sqlite3
"""
self.showMaximized()
self.setWindowFlag(Qt.FramelessWindowHint) 
self.setWindowOpacity(0.7) """

#from Database_SQLite import *
# from . import Database_SQLite



class Login(object):
	def __init__(self, parent):
		super(Login, self).__init__()
		self.parent = parent


	def setupUI(self, MainWindow):

		#self.initUI()
		MainWindow.setWindowTitle(" ")
		MainWindow.setWindowIcon(QIcon('Capturar.PNG'))
		MainWindow.setGeometry(100, 100, 1700, 850)
		#MainWindow.setFixedSize(1700, 850)
		self.centralwidget = QWidget(MainWindow)

		# image backgroud
		oImage = QImage("login_backgroundg.png")
		sImage = oImage.scaled(QSize(1700, 850))  # resize Image to widgets size
		palette = QPalette()
		palette.setBrush(10, QBrush(sImage))  # 10 = Windowrole
		MainWindow.setPalette(palette)
		
		
		# Minimize
		self.buttonMinimizar = QToolButton(self.centralwidget)
		self.buttonMinimizar.setToolTip("Minimizar")
		self.buttonMinimizar.setIconSize(QSize(38, 25))
		self.buttonMinimizar.setAutoRaise(True)
		self.buttonMinimizar.clicked.connect(self.hideWindow)
		self.buttonMinimizar.setIcon(QApplication.style().standardIcon(QStyle.SP_TitleBarMinButton))
		self.buttonMinimizar.resize(53, 40)
		self.buttonMinimizar.move(55, 0)

		# CLOSE WINDOW
		self.buttonClose = QToolButton(self.centralwidget)
		self.buttonClose.setToolTip("Close")
		self.buttonClose.setIconSize(QSize(38, 25))
		self.buttonClose.setAutoRaise(True)
		self.buttonClose.setStyleSheet("Background:red")
		self.buttonClose.setIcon(QApplication.style().standardIcon(QStyle.SP_TitleBarCloseButton))
		self.buttonClose.clicked.connect(QCoreApplication.instance().quit)
		self.buttonClose.resize(53, 40)


		# Frame
		self.frame = QFrame(self.centralwidget)
		self.frame.setFrameShape(QFrame.StyledPanel)
		self.frame.setObjectName("Frame")
		self.frame.resize(500, 550)
		self.frame.move(600, 150)

		# Label
		self.title = QLabel(self.centralwidget)
		self.title.setText("Sing in")
		self.title.setFont(QFont('Calibri (Corpo)', 30, QFont.Bold))
		self.title.setAlignment(Qt.AlignCenter)
		self.title.setStyleSheet('color: Black')
		self.title.resize(350, 100)
		self.title.move(670, 160)

		# Textbox: Email
		self.emailfild = QLineEdit(self.centralwidget)
		self.emailfild.setPlaceholderText("Email ")
		self.emailfild.setAlignment(Qt.AlignCenter)
		self.emailfild.resize(400, 60)
		self.emailfild.move(650, 300)

		# Textbox: Password
		self.password = QLineEdit(self.centralwidget)
		self.password.setPlaceholderText("Password")
		self.password.setAlignment(Qt.AlignCenter)
		self.password.setEchoMode(QLineEdit.Password)
		self.password.resize(400, 60)
		self.password.move(650, 380)

		# New Password
		self.new_pass = QPushButton("Forgot your password ?", self.centralwidget)
		self.new_pass.setObjectName("newpass")
		self.new_pass.resize(200, 30)
		self.new_pass.move(820, 450)

		# Log in
		self.loginButton = QPushButton("LOGIN", self.centralwidget)
		self.loginButton.setObjectName("btn_login")
		# .clicked.connect()
		self.loginButton.resize(300, 60)
		self.loginButton.move(700, 540)

		# Register
		self.new_account = QPushButton("Create new account", self.centralwidget)
		self.new_account.setObjectName("new_account")
		#self.new_account.clicked.connect(self.create_account)
		self.new_account.resize(300, 60)
		self.new_account.move(700, 620)

		MainWindow.setCentralWidget(self.centralwidget)


	def hideWindow(self):
		self.parent.showMinimized()
		

class SingUp(object):
	def __init__(self, parent):
		super(SingUp, self).__init__()
		self.parent = parent

	def setupUI(self, MainWindow):
		#self.initUI()
		MainWindow.setWindowTitle(" ")
		MainWindow.setWindowIcon(QIcon('Capturar.PNG'))
		MainWindow.setGeometry(100, 100, 1700, 850)
		MainWindow.setFixedSize(1700, 850)
		self.centralwidget = QWidget(MainWindow)

		# image backgroud
		oImage = QImage("login_backgroundg.png")
		sImage = oImage.scaled(QSize(1700, 850))  # resize Image to widgets size
		palette = QPalette()
		palette.setBrush(10, QBrush(sImage))  # 10 = Windowrole
		MainWindow.setPalette(palette)
		self.centralwidget = QWidget(MainWindow)

		# Minimize
		self.buttonMinimizar = QToolButton(self.centralwidget)
		self.buttonMinimizar.setToolTip("Minimizar")
		self.buttonMinimizar.setIconSize(QSize(38, 25))
		self.buttonMinimizar.setAutoRaise(True)
		self.buttonMinimizar.clicked.connect(self.hideWindow)
		self.buttonMinimizar.setIcon(QApplication.style().standardIcon(QStyle.SP_TitleBarMinButton))
		self.buttonMinimizar.resize(53, 40)
		self.buttonMinimizar.move(55, 0)

		# CLOSE WINDOW
		self.buttonClose = QToolButton(self.centralwidget)
		self.buttonClose.setToolTip("Close")
		self.buttonClose.setIconSize(QSize(38, 25))
		self.buttonClose.setAutoRaise(True)
		self.buttonClose.setStyleSheet("Background:red")
		self.buttonClose.setIcon(QApplication.style().standardIcon(QStyle.SP_TitleBarCloseButton))
		self.buttonClose.clicked.connect(QCoreApplication.instance().quit)
		self.buttonClose.resize(53, 40)

		# Frame
		self.frame = QFrame(self.centralwidget)
		self.frame.setObjectName("Frame")
		self.frame.resize(500, 550)
		self.frame.move(600, 150)

		# Label
		self.title = QLabel(self.centralwidget)
		self.title.setText("Sing Up")
		self.title.setFont(QFont('Calibri (Corpo)', 30, QFont.Bold))
		self.title.setAlignment(Qt.AlignCenter)
		self.title.setStyleSheet('color: Black')
		self.title.resize(350, 100)
		self.title.move(670, 160)


		# Textbox: Email
		self.emailfild = QLineEdit(self.centralwidget)
		self.emailfild.setPlaceholderText("Email")
		self.emailfild.setAlignment(Qt.AlignCenter)
		self.emailfild.resize(400, 60)
		self.emailfild.move(650, 300)

		# Textbox: Password
		self.password = QLineEdit(self.centralwidget)
		self.password.setPlaceholderText("Password")
		self.password.setAlignment(Qt.AlignCenter)
		self.password.setEchoMode(QLineEdit.Password)
		self.password.resize(400, 60)
		self.password.move(650, 380)

		# Textbox: Confirm Password
		self.conf_password = QLineEdit(self.centralwidget)
		self.conf_password.setPlaceholderText("Confirm Password")
		self.conf_password.setAlignment(Qt.AlignCenter)
		self.conf_password.setEchoMode(QLineEdit.Password)
		self.conf_password.resize(400, 60)
		self.conf_password.move(650, 460)

		# Label
		self.title = QLabel(self.centralwidget)
		self.title.setText("Back")
		self.title.setFont(QFont('Arial', 10, QFont.Bold))
		self.title.setAlignment(Qt.AlignCenter)
		self.title.setStyleSheet('Background: red; color: Black; ')
		self.title.resize(250, 60)
		self.title.move(670, 550)

		# Register
		self.next = QPushButton("Create new account", self.centralwidget)
		self.next.setObjectName("new_account")
		#self.next.clicked.connect(self.create_account)
		self.next.resize(300, 60)
		self.next.move(700, 620)

		
		MainWindow.setCentralWidget(self.centralwidget)

	def hideWindow(self):
		self.parent.showMinimized()

class DataVisualization(object):
	def __init__(self, parent):
		super(DataVisualization, self).__init__()
		self.parent = parent


	def setupUI(self, MainWindow):
		#self.initUI()
		MainWindow.setWindowTitle(" ")
		MainWindow.setWindowIcon(QIcon('Capturar.PNG'))
		MainWindow.setGeometry(100, 100, 1700, 850)
		MainWindow.setFixedSize(1700, 850)
		self.centralwidget = QWidget(MainWindow)

		# image backgroud
		oImage = QImage("cubos.jpg")
		sImage = oImage.scaled(QSize(1700, 850))  # resize Image to widgets size
		palette = QPalette()
		palette.setBrush(10, QBrush(sImage))  # 10 = Windowrole
		MainWindow.setPalette(palette)
		self.centralwidget = QWidget(MainWindow)

		# Minimize
		self.buttonMinimizar = QToolButton(self.centralwidget)
		self.buttonMinimizar.setToolTip("Minimizar")
		self.buttonMinimizar.setIconSize(QSize(38, 25))
		self.buttonMinimizar.setAutoRaise(True)
		self.buttonMinimizar.clicked.connect(self.hideWindow)
		self.buttonMinimizar.setIcon(QApplication.style().standardIcon(QStyle.SP_TitleBarMinButton))
		self.buttonMinimizar.resize(53, 40)
		self.buttonMinimizar.move(55, 0)

		# CLOSE WINDOW
		self.buttonClose = QToolButton(self.centralwidget)
		self.buttonClose.setToolTip("Close")
		self.buttonClose.setIconSize(QSize(38, 25))
		self.buttonClose.setAutoRaise(True)
		self.buttonClose.setStyleSheet("Background:red")
		self.buttonClose.setIcon(QApplication.style().standardIcon(QStyle.SP_TitleBarCloseButton))
		self.buttonClose.clicked.connect(QCoreApplication.instance().quit)
		self.buttonClose.resize(53, 40)


		# Label
		self.title = QLabel(self.centralwidget)
		self.title.setText("Sing Up")
		self.title.setFont(QFont('Calibri (Corpo)', 30, QFont.Bold))
		self.title.setAlignment(Qt.AlignCenter)
		self.title.setStyleSheet('color: Black')
		self.title.resize(350, 100)
		self.title.move(670, 160)




		# Register
		self.next = QPushButton("Create new account", self.centralwidget)
		self.next.setObjectName("new_account")
		#self.next.clicked.connect(self.create_account)
		self.next.resize(300, 60)
		self.next.move(700, 620)

		
		MainWindow.setCentralWidget(self.centralwidget)

	def hideWindow(self):
		self.parent.showMinimized()



class MainWindow(QMainWindow):
	def __init__(self, parent=None):
		super(MainWindow, self).__init__(parent)
		self.setWindowFlags(Qt.FramelessWindowHint)
		self.login = Login(self)
		self.singup = SingUp(self)
		self.datavisualization = DataVisualization(self)
		self.startUIWindow()

	
	def startDataVisualization(self):
		self.datavisualization.setupUI(self)
		#self.datavisualization.button.clicked.connect(funcao)
		#print("---")
		self.show()



	def new_user(self):
		email= self.singup.emailfild.text()
		password = self.singup.password.text()
		if password == self.singup.conf_password.text():
			if len(email) != 0:
				conn = sqlite3.connect('User_pass.db')
				c = conn.cursor()
				c.execute("""   CREATE TABLE 
								IF NOT EXISTS loginData(
								email TEXT,
								password TEXT) """)
	
				user_w_same_name = c.execute(f"""SELECT count(*) FROM loginData 
												WHERE email='{email}' """).fetchone()[0]

				if user_w_same_name == 0:
					c.execute("INSERT INTO loginData (email, password) VALUES(?, ?)", (email, password))
					conn.commit()
					c.close()
					conn.close()
					self.startUIWindow()


				else:
					self.singup.emailfild.setText("")
					self.singup.emailfild.setStyleSheet('border: 4px solid rgb(225, 0, 0);')
					self.singup.password.setText("")
					self.singup.conf_password.setText("")

		else:
			self.singup.conf_password.setText("")
			self.singup.conf_password.setStyleSheet('border: 4px solid rgb(225, 0, 0);')
	 
	def startSingUp(self):
		self.singup.setupUI(self)
		# Criar user...
		self.singup.next.clicked.connect(self.new_user)
		self.show()

	def user_login(self):
		# if len(self.login.emailfild.text()) != 0 and len(self.login.password.text()
		email = self.login.emailfild.text()
		password = self.login.password.text()
		if len(email) != 0 and len(password) != 0:
				
			conn = sqlite3.connect('User_pass.db')
			c = conn.cursor()
			data = c.execute(f"SELECT password FROM loginData WHERE email = '{email}' ").fetchall()[0][0]
			print(data)
			
			if  data == password:  # len(password) > 6 and
				self.startDataVisualization()
			else:
				self.login.password.setStyleSheet('border: 4px solid rgb(225, 0, 0);')
		elif len(email) != 0 or len(password) != 0:
			self.login.emailfild.setStyleSheet('border: 4px solid rgb(225, 0, 0);')
			self.login.password.setStyleSheet('border: 4px solid rgb(225, 0, 0);')


	def startUIWindow(self):
		self.login.setupUI(self)
		self.login.loginButton.clicked.connect(self.user_login)
		self.login.new_account.clicked.connect(self.startSingUp)
		#self.setLayout(self.login.vbox)
		self.show() #Maximized()
		


def main():
	# 
	with open('style.css') as f:
		style = f.read()

	#
	"""conn = sqlite3.connect('User_pass.db')
	c = conn.cursor()
	c.execute(CREATE TABLE 
				IF NOT EXISTS loginData(
				email TEXT,
				password TEXT))"""

	# 
	app = QApplication(sys.argv)
	w = MainWindow()
	app.setStyleSheet(style)
	sys.exit(app.exec_())




if __name__ == '__main__':
	main()
	















