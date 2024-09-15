# main.py
import Accounts
import ATM

# Creating an instance of the 1st account
Account_1 = Accounts.Accounts(account_number = 123456, 
                              account_firstname = "Royce", 
                              account_lastname = "Chua", 
                              current_balance = 1000, 
                              address = "Silver Street Quezon City", 
                              email = "roycechua123@gmail.com")

print("Account 1")
print(f"Account Name: {Account_1.account_firstname} {Account_1.account_lastname}")
print(f"Current Balance: {Account_1.current_balance}")
print(f"Address: {Account_1.address}")
print(f"Email: {Account_1.email} \n")

# Creating an instance of the 2nd account
Account_2 = Accounts.Accounts(account_number = 654321,
                              account_firstname = "John",
                              account_lastname = "Doe",
                              current_balance = 2000,
                              address = "Gold Street Quezon City",
                              email = "johndoe@yahoo.com")

print("Account 2")
print(f"Account Name: {Account_2.account_firstname} {Account_2.account_lastname}")
print(f"Current Balance: {Account_2.current_balance}")
print(f"Address: {Account_2.address}")
print(f"Email: {Account_2.email} \n")

# Creating and Using the ATM for Account 1
ATM_1 = ATM.ATM(Account_1.account_number, "", Account_1.current_balance, "", "")
ATM_1.deposit(Account_1.account_number, 345, Account_1.current_balance)
ATM_1.check_currentbalance(Account_1.account_number, Account_1.current_balance)
print()

# Creating and Using the ATM for Account 2
ATM_2 = ATM.ATM(Account_2.account_number, "", Account_2.current_balance, "", "")
ATM_2.withdraw(Account_2.account_number, 123, Account_2.current_balance)
ATM_2.check_currentbalance(Account_2.account_number, Account_2.current_balance)
print()

# Viewing transaction summary for Account 1
ATM_1.view_transactionsummary()
print()

# Viewing transaction summary for Account 2
ATM_2.view_transactionsummary()
print()

# Initializing the ATM machine with a serial number
ATM_serial_number = 123456789
print(f"ATM Serial Number: {ATM_serial_number}")
