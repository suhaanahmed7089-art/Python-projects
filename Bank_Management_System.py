# Creating a bank management system in python
# Project details
# this project allows user to:
# 1. Create an account in details like name, account number, account pin, balance
# 2. View account details
# 3. Deposit money in the account
# 4. Withdraw money from the account
# 5. View all accounts created in the bank management system
# 6. Exit the program gracefully when the user chooses to do so.
class Bank:
    def __init__(self):
        self.accounts = []
    def create_account(self):
        self.name=input("Enter your name: ")
        self.account_number=int(input("Enter your account number: "))
        self.account_pin=int(input("Enter a pin for your account: "))
        self.balance=float(input("Enter the initial balance for your account: "))
        # For checking if the account already exists or not
        for account in self.accounts:
            if account.account_number==self.account_number:
                print("Account already exists")
                return
        account=BankAccount(self.name,self.account_number,self.account_pin,self.balance)
        self.accounts.append(account)
        print("Account created successfully")
    def find_account(self):
        account_number=int(input("Enter your account number: "))
        account_pin=int(input("Enter your account pin: "))
        for account in self.accounts:
            if account.account_number==account_number and account.account_pin==account_pin:
                return account
        return None
    def deposit(self):
        account=self.find_account()
        if account:
            amount=float(input("Enter the amount you want to deposit: "))
            if amount<=0:
                print("Invalid amount")
            else:
                account.balance+=amount
                print("Amount deposited successfully")
        else:
            print("Invalid account number or pin")

    def withdraw(self):
        account=self.find_account()
        if account:
            amount=float(input("Enter the amount you want to withdraw: "))
            if amount<=0:
                print("Invalid amount")
            elif amount>account.balance:
                print("Insufficient balance")
            else:
                account.balance-=amount
                print("Amount withdrawn successfully")
        else:
            print("Invalid account number or pin")
    def view_account(self):
        account=self.find_account()
        if account:
            account.display()
        else:
            print("Invalid account number or pin")
    def view_all_accounts(self):
        if len(self.accounts)==0:
            print("No accounts found")
        else:
            print("-"*6+"All Account Details"+"-"*6)
            for accounts in self.accounts:
                accounts.display()
class BankAccount:
    def __init__(self,name,account_number,account_pin,balance):
        self.name=name
        self.account_number=account_number
        self.account_pin=account_pin
        self.balance=balance
    def display(self):
        print("")
        print("Name: ",self.name)
        print("Account Number: ",self.account_number)
        print("Account Pin: ",self.account_pin)
        print("Balance: ",self.balance)
b=Bank()
while True:
    try:
        print("Welcome to Bank Management System")
        print("1. Create an account")
        print("2. View account details")
        print("3. Deposit money")
        print("4. Withdraw money")
        print("5. View all accounts")
        print("6. Exit the program")
        choice=int(input("Enter your choice: "))
        if choice==1:
            b.create_account()
        elif choice==2:
            print("-"*6+"Account Details"+"-"*6)
            b.view_account()
        elif choice==3:
            b.deposit()
        elif choice==4:
            b.withdraw()
        elif choice==5:
            b.view_all_accounts()
        elif choice==6:
            print("Exiting the program")
            break
        else:
            print("Exiting the program")
            break
    except ValueError:
        print("Invalid choice , please enter a choice from (1-6)")
