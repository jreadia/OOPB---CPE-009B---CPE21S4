import sys
import math
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

# Creating a Calculator program using PyQt5

class Calculator(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle('Calculator')
        self.setGeometry(100, 100, 300, 400)
        self.setWindowIcon(QIcon('Adia - CPE 009B - Lab Act 6 - GUI Design\Lab 6 - Supp Act\calculator.png'))
        
        # Central widget
        self.centralWidget = QWidget(self)
        self.setCentralWidget(self.centralWidget)
        
        # Layouts
        self.mainLayout = QVBoxLayout()
        self.gridLayout = QGridLayout()
        
        # Display
        self.display = QLineEdit()
        self.display.setReadOnly(True)
        self.display.setAlignment(Qt.AlignRight)
        self.display.setFixedHeight(35)
        self.mainLayout.addWidget(self.display)
        
        # Buttons
        buttons = [
            '7', '8', '9', '/', 'sin',
            '4', '5', '6', '*', 'cos',
            '1', '2', '3', '-', 'exp',
            '0', 'C', '=', '+', 'Exit'
        ]
        
        # Adding buttons to the grid layout
        row, col = 0, 0
        for button in buttons:
            btn = QPushButton(button)
            btn.clicked.connect(self.onButtonClick)
            self.gridLayout.addWidget(btn, row, col)
            col += 1
            if col > 4:
                col = 0
                row += 1
        
        # Adding layouts to the central widget
        self.mainLayout.addLayout(self.gridLayout)
        self.centralWidget.setLayout(self.mainLayout)
        
        # Menu bar
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('File')
        
        # Exit action
        exitAction = QAction('Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.triggered.connect(self.close)
        fileMenu.addAction(exitAction)
        
        # Clear action
        clearAction = QAction('Clear', self)
        clearAction.setShortcut('Ctrl+M')
        clearAction.triggered.connect(self.clearDisplay)
        fileMenu.addAction(clearAction)
        
        # Save action
        saveAction = QAction('Save', self)
        saveAction.setShortcut('Ctrl+S')
        saveAction.triggered.connect(self.saveToFile)
        fileMenu.addAction(saveAction)
        
        # Load action
        loadAction = QAction('Load', self)
        loadAction.setShortcut('Ctrl+L')
        loadAction.triggered.connect(self.loadFromFile)
        fileMenu.addAction(loadAction)
        
    def onButtonClick(self):
        sender = self.sender().text()
        
        # Clear the display
        if sender == 'C':
            self.display.clear()

        # Displaying the trigonometric functions
        elif sender == 'sin':
            self.display.setText(self.display.text() + 'sin(')
        elif sender == 'cos':
            self.display.setText(self.display.text() + 'cos(')
        elif sender == 'exp':
            self.display.setText(self.display.text() + 'exp(')

        # Calculate the result of the expression
        elif sender == '=':
            try:
                expression = self.display.text()
                if 'sin' in expression:
                    value = float(expression.replace('sin(', ''))
                    result = str(math.sin(math.radians(value)))
                elif 'cos' in expression:
                    value = float(expression.replace('cos(', ''))
                    result = str(math.cos(math.radians(value)))
                elif 'exp' in expression:
                    value = float(expression.replace('exp(', ''))
                    result = str(math.exp(value))
                else:
                    result = str(eval(expression)) 
                self.display.setText(result)
            except Exception as e:
                self.display.setText('Error')

        # Exit the program
        elif sender == 'Exit':
            self.close()
        else:
            self.display.setText(self.display.text() + sender)
    
    def clearDisplay(self):
        self.display.clear()
    
    def saveToFile(self):
        options = QFileDialog.Options()
        fileName, _ = QFileDialog.getSaveFileName(self, "Save File", "", "Text Files (*.txt);;All Files (*)", options=options)
        if fileName:
            with open(fileName, 'w') as file:
                file.write(self.display.text())
    
    def loadFromFile(self):
        options = QFileDialog.Options()
        fileName, _ = QFileDialog.getOpenFileName(self, "Open File", "", "Text Files (*.txt);;All Files (*)", options=options)
        if fileName:
            with open(fileName, 'r') as file:
                self.display.setText(file.read())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    calculator = Calculator()
    calculator.show()
    sys.exit(app.exec_())