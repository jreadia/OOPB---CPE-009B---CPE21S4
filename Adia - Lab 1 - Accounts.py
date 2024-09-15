# Accounts.py

class Accounts():
    # Creating the Constructor for the Accounts class
    def __init__(self, account_number, account_firstname, account_lastname, current_balance, address, email):
        self.account_number = account_number
        self.account_firstname = account_firstname
        self.account_lastname = account_lastname
        self.current_balance = current_balance
        self.address = address
        self.email = email

    # Creating the Update Address method
    def update_address(self, new_address):
        self.address = new_address

    # Creating the Update Email method
    def update_email(self, new_email):
        self.email = new_email