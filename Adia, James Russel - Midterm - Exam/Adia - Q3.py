import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class App(QWidget):

    def __init__(self):
        super().__init__() 
        self.title = "Midterm in OOP"
        self.x = 200
        self.y = 200 
        self.width = 400
        self.height = 200
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.x, self.y, self.width, self.height)

        self.textboxlbl = QLabel('Enter your fullname:', self)
        self.textboxlbl.move(40, 70)
        self.textboxlbl.setStyleSheet("color: red")
        
        self.textbox = QLineEdit(self)
        self.textbox.move(230, 70)
        

        self.button = QPushButton('Click to display your Fullname', self)
        self.button.move(40, 100)
        self.button.setStyleSheet("color: red")
        self.button.clicked.connect(self.on_click)
    
        self.resultbox = QLineEdit(self)
        self.resultbox.setReadOnly(True)
        self.resultbox.move(230, 100)

        self.show()

    @pyqtSlot()
    def on_click(self):
        self.resultbox.setText(self.textbox.text())
       

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())