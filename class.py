class Bank:
    def __init__(self):
        self.balance = 0
        print("Account is created.")

    def option(self):
        print("You are Welcome")
        opt = input("""What do you like to do?
                   1. Check Balance
                   2. Deposit
                   3. Withdraw\n""")
        match opt:
            case "1":
                self.enquiry()
            case "2":
                self.deposit()
            case "3":
                self.withdraw()
            case _:
                print("Enter an option 1,2 or 3")

    def deposit(self):
        amount = float(input("Enter the amount you want to deposit: "))
        self.balance = self.balance + amount
        print(f"Deposit is successful and Your balance is new balance is {self.balance:.2f} ")

    def withdraw(self):
        amount = float(input("Enter the amount you want to withdraw: "))
        if amount > self.balance:
            print("Insufficient Balance")
        else:
            self.balance = self.balance - amount
            print("Withdraw is successful")

    def enquiry(self):
        print(f"Balance in the account is {self.balance:.2f}")





if __name__ == "__main__":
    b = Bank()
    b.option()
