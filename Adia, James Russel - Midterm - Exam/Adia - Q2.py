import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class App(QWidget):

    def __init__(self):
        super().__init__() 
        self.title = "Special Midterm Exam in OOP"
        self.x = 200 
        self.y = 200 
        self.width = 300
        self.height = 300
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.x, self.y, self.width, self.height)

        self.button = QPushButton('Click to Change Color', self)
        self.button.move(100, 125)
        self.button.clicked.connect(self.changeButtonColor)

        self.show()

    @pyqtSlot()
    def changeButtonColor(self):
        self.button.setStyleSheet("background-color: yellow")
        


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())