from tkinter import *


class MyWindow:
    def __init__(self, win):
        # common widgets

        # All labels of the calculator
        self.Label1 = Label(win, fg="red", text="Calculator")
        self.Label1.place(x=150, y=50)

        self.Label2 = Label(win, fg="blue", text="Number 1:")
        self.Label2.place(x=50, y=80)

        self.Label3 = Label(win, fg="green", text="Number 2:")
        self.Label3.place(x=50, y=110)

        self.Label4 = Label(win, fg="black", text="Result:")
        self.Label4.place(x=50, y=140)

        # All Entries for each label in the calculator
        self.Entry1 = Entry(win, bd=2)  # Corresponds to "Number 1:"
        self.Entry1.place(x=120, y=80)

        self.Entry2 = Entry(win, bd=2)  # Corresponds to "Number 2:"
        self.Entry2.place(x=120, y=110)

        self.Entry3 = Entry(win, bd=2)  # Corresponds to "Result:"
        self.Entry3.place(x=120, y=140)

        # All buttons in the calculator
        self.Button1 = Button(win, bg="white", text="Add")  # Add Button
        self.Button1.bind('<Button-1>', self.add)
        self.Button1.place(x=50, y=190)

        self.Button2 = Button(win, bg="white", text="Sub")  # Subtract Button
        self.Button2.bind('<Button-1>', self.sub)
        self.Button2.place(x=100, y=190)

        self.Button3 = Button(win, bg="white", text="Multiply")  # Multiply Button
        self.Button3.bind('<Button-1>', self.multiply)
        self.Button3.place(x=150, y=190)

        self.Button4 = Button(win, bg="white", text="Divide")  # Divide Button
        self.Button4.bind('<Button-1>', self.divide)
        self.Button4.place(x=225, y=190)

    def add(self, win):
        self.Entry3.delete(0, 'end')
        num1 = int(self.Entry1.get())
        num2 = int(self.Entry2.get())
        result = num1 + num2
        self.Entry3.insert(END, str(result))

    def sub(self, win):
        self.Entry3.delete(0, 'end')
        num1 = int(self.Entry1.get())
        num2 = int(self.Entry2.get())
        result = num1 - num2
        self.Entry3.insert(END, str(result))

    def multiply(self, win):
        self.Entry3.delete(0, 'end')
        num1 = int(self.Entry1.get())
        num2 = int(self.Entry2.get())
        result = num1 * num2
        self.Entry3.insert(END, str(result))

    def divide(self, win):
        self.Entry3.delete(0, 'end')
        num1 = int(self.Entry1.get())
        num2 = int(self.Entry2.get())
        result = num1 / num2
        self.Entry3.insert(END, str(result))


# An instance of Tkinter TK class
window = Tk()
MyWin = MyWindow(window)
window.configure(bg="light blue")

# function to set the size of window when opened and name of the window
window.geometry("400x300+10+10")
window.title("Standard Calculator")

# Main function to showcase window
window.mainloop()
