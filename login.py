
from PyQt5 import QtWidgets
import sys
from PyQt5 import QtGui, QtCore

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.init_window()
    
    def init_window(self):
        
        self.title = QtWidgets.QLabel(self)
        self.title.setText("Login")
        #self.title.setFont()

        self.Line_Email = QtWidgets.QLineEdit(self)
        #self.Line_Email.setFixedWidth(470)

        self.Line_Pass = QtWidgets.QLineEdit(self)
        #self.Line_Pass.setFixedWidth(470)

        # Quit button
        self.qbtn = QtWidgets.QPushButton("Login", self)
        self.qbtn.setToolTip('Click to exit the program...')
        #self.qbtn.clicked.connect(QtCore.QCoreApplication.instance().quit)
        # self.qbtn.resize(self.qbtn.sizeHint())



        # Container widget
        self.main_widget = QtWidgets.QWidget(self)

        ## Set layout
        # Containers
        self.main_layout = QtWidgets.QVBoxLayout(self.main_widget)
        #self.main_layout.sizeConstraint = QtWidgets.QLayout.SetDefaultConstraint

        self.main_widget.setLayout(self.main_layout)
        self.setCentralWidget(self.main_widget)
        
        
        self.Box1 = QtWidgets.QHBoxLayout()
        self.Box1.addWidget(self.title)

        self.Box2 = QtWidgets.QHBoxLayout()
        self.Box2.addWidget(self.Line_Email)

        self.Box3 = QtWidgets.QHBoxLayout()
        self.Box3.addWidget(self.Line_Pass)

        self.Box4 = QtWidgets.QHBoxLayout()
        self.Box4.addWidget(self.qbtn)
        
        self.main_layout.addLayout(self.Box1)
        self.main_layout.addStretch(1)
        self.main_layout.addLayout(self.Box1)
        self.main_layout.addLayout(self.Box1)
        self.main_layout.addStretch(1)
        self.main_layout.addLayout(self.Box1)







        """
        layout = QtWidgets.QGridLayout()


        # Label
        label = QtWidgets.QLabel("label")
        #label.setAlignment(QtCore.Qt.AlignHCenter)

        button_login = QtWidgets.QPushButton("Login")


        V_box1 = QtWidgets.QVBoxLayout()
        V_box1.addWidget(label)
        V_box1.addWidget(button_login)

        self.setLayout(V_box1)
        """



        # MainWindow proprieties
        self.setGeometry(100, 100, 1700, 850)
        self.setWindowTitle(" ")
        self.setStyleSheet("QMainWindow {background-color:rgb(40, 56, 94)}")
        self.setWindowIcon(QtGui.QIcon('Capturar.PNG'))
        self.show()
        


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())















