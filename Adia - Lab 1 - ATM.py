# ATM.py
class ATM():
    # Creating the Constructor for the ATM class
    def __init__(self, account_number, amount, current_balance = 0, deposited = 0, withdrawn = 0):
        self.account_number = account_number
        self.amount = amount
        self.current_balance = current_balance
        self.deposit_amount = deposited
        self.withdraw_amount = withdrawn

    # Creating the Deposit method
    def deposit(self, account_number, amount, current_balance):
        current_balance += amount
        print(f"Successfully deposited {amount} PHP to Account Number: {account_number}. New balance is {current_balance} PHP")
        self.current_balance = current_balance
        self.deposit_amount = amount

    # Creating the Withdraw method
    def withdraw(self, account_number, amount, current_balance):
        current_balance -= amount
        print(f"Successfully withdrawn {amount} PHP from Account Number: {account_number}. New balance is {current_balance} PHP")
        self.current_balance = current_balance
        self.withdraw_amount = amount

    # Creating the Check Current Balance method
    def check_currentbalance(self, account_number, *args):
        print(f"Current balance of Account Number: {account_number} is {self.current_balance} PHP")
    
    # Creating the View Transaction Summary method
    def view_transactionsummary(self):
        print(f"Transaction Summary for Account Number: {self.account_number}")
        print(f"Current Balance: {self.current_balance} PHP")
        print(f"Amount deposited: {self.deposit_amount if self.deposit_amount else 0} PHP")
        print(f"Amount withdrawn: {self.withdraw_amount if self.withdraw_amount else 0} PHP")
        return self.account_number, self.current_balance, self.amount
