import sys
from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow, QPushButton, QLineEdit, QLabel
from PyQt5.QtGui import QIcon

class App(QWidget):

    def __init__(self):
        super().__init__() # initializes the main window like in the previous one
        # window = QMainWindow()
        self.title = "PyQt Labels"
        self.x = 200 # or left
        self.y = 200 # or top
        self.width = 300
        self.height = 300
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.x, self.y, self.width, self.height)
        self.setWindowIcon(QIcon("Chat_Bubble.ico"))

        # First label
        self.textboxlbl1 = QLabel("Hello World! ", self)
        self.textboxlbl1.move(20, 20)

        # Second label
        self.textboxlbl2 = QLabel("This program is written in Pycharm ", self)
        self.textboxlbl2.move(20, 50)

        self.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())