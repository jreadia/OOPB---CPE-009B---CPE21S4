import tkinter as tk
from tkinter import messagebox

class RegistrationForm(tk.Tk):
    def __init__(self):
        super().__init__()
        # Defining the layout of the window
        self.title("Account Registration System")
        self.geometry("400x400")
        self.resizable(False, False)
        self.center_window()
        self.configure(bg = "light blue")

        self.create_widgets()

    # Makes it so that the window opens in the center of the user's screen
    def center_window(self):
        self.update_idletasks()
        width = self.winfo_width()
        height = self.winfo_height()
        x = (self.winfo_screenwidth() // 2) - (width // 2)
        y = (self.winfo_screenheight() // 2) - (height // 2)
        self.geometry(f'{width}x{height}+{x}+{y}')

    # Creating the label widgets with their corresponding text fields (Entry) along with button widgets
    def create_widgets(self):
        title_label = tk.Label(self, text="Account Registration", font=("Arial", 16))
        title_label.place(x=100, y=20)

        labels = ["First Name", "Last Name", "Username", "Password", "Email Address", "Contact Number"]
        self.entries = {}

        y_position = 60
        for label in labels:
            lbl = tk.Label(self, text=label)
            lbl.place(x=50, y=y_position)
            entry = tk.Entry(self)
            entry.place(x=200, y=y_position)
            self.entries[label] = entry
            y_position += 40

        submit_button = tk.Button(self, text="Submit", command=self.submit)
        submit_button.place(x=100, y=y_position)

        clear_button = tk.Button(self, text="Clear", command=self.clear)
        clear_button.place(x=200, y=y_position)

    # Output a message box for submit button that tells the user that their input was successfully registered
    def submit(self):
        data = {label: entry.get() for label, entry in self.entries.items()}
        messagebox.showinfo("Submitted Data", f"Data Submitted: {data}")

    # Allows the clear button to clear all the entries made by the user
    def clear(self):
        for entry in self.entries.values():
            entry.delete(0, tk.END)
