import time

# ATM class to handle bank account operations
class ATM:
    def __init__(self):
        self.balance = 0  # Initial balance

    # Function to check the balance
    def check_balance(self):
        print("Loading",end="")
        for _ in range(4):
            print(".",end="")
            time.sleep(1)

        print("\n==========================")
        print(f"Balance: ₱{self.balance}")
        print("==========================")

    # Function to deposit money
    def deposit(self):
        amount = float(input("Enter the amount to deposit: ₱"))
        if amount > 0:
            self.balance += amount

            print("Loading", end="")
            for _ in range(4):
                print(".", end="")
                time.sleep(1)

            print("\n==========================")
            print(f"Success Deposited ₱{amount}")
            print("==========================")
        else:
            print("Loading", end="")
            for _ in range(4):
                print(".", end="")
                time.sleep(1)

            print("\n=======================")
            print("Amount must be positive.")
            print("=======================")

    # Function to withdraw money
    def withdraw(self):
        amount = float(input("Enter the amount to withdraw: ₱"))
        if amount <= self.balance:
            self.balance -= amount

            print("Loading", end="")
            for _ in range(4):
                print(".", end="")
                time.sleep(1)

            print("\n=============================")
            print(f"Success Withdrew ₱{amount}")
            print("=============================")
        else:
            print("Loading", end="")
            for _ in range(4):
                print(".", end="")
                time.sleep(1)

            print("\n======================")
            print("Insufficient balance.")
            print("======================")

    # Function to exit the ATM
    def exit_atm(self):
        print("Loading", end="")
        for _ in range(4):
            print(".", end="")
            time.sleep(1)

        print("\n=====================================")
        print("Thank you for using the ATM. Goodbye!")
        print("=====================================\n")
        exit()


# Main function to run the ATM machine
def atm_machine():
    atm = ATM()  # Create an ATM object

    while True:
        print("ATM Machine")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")
        choice = input("Please select an option (1/2/3/4): ")

        if choice == '1':
            atm.check_balance()
        elif choice == '2':
            atm.deposit()
        elif choice == '3':
            atm.withdraw()
        elif choice == '4':
            atm.exit_atm()  # Exit the ATM
        else:
            print("Invalid choice. Please try again.")

# Run the ATM machine
atm_machine()
