#Grid Layout

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QLabel, QLineEdit, QPushButton, QHBoxLayout, QVBoxLayout

class GridExample(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        grid = QGridLayout()
        self.setLayout(grid)

        names = [
            '7', '8', '9', '/', ''
            '4', '5', '6', '*', ''
            '1', '2', '3', '-', ''
            '0', '.', '=', '+', ''
             '', '', '', '', '']

        self.textline = QLineEdit(self)
        grid.addWidget(self.textline, 0, 1, 1, 5)

        # using a loop to generate positions
        positions = [(i, j) for i in range(1, 7) for j in range(1, 6)] 
        for position, name in zip(positions, names):
            if name == '':
                continue
            button = QPushButton(name)
            grid.addWidget(button, *position)

        self.setGeometry(300, 300, 300, 150)
        self.setWindowTitle('Grid Layout')
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = GridExample()
    sys.exit(app.exec_())                               