# bank_management_system.py

ACCOUNTS = {}
NEXT_ACCOUNT_NUMBER = 1001


def main_menu():
    print("\n===== Bank Management System =====")
    print("1. Create Account")
    print("2. View Balance")
    print("3. Deposit")
    print("4. Withdraw")
    print("5. Exit")
    choice = input("Enter your choice: ")
    return choice


def create_account(accounts):
    global NEXT_ACCOUNT_NUMBER

    print("\n===== Create Account =====")
    name = input("Enter your name: ")

    try:
        initial_deposit = float(input("Enter initial deposit: "))
        if initial_deposit < 0:
            raise ValueError("Initial deposit cannot be negative.")
    except ValueError as ve:
        print(f"Error: {ve}")
        return

    account_number = str(NEXT_ACCOUNT_NUMBER)  # Automatically generate account number
    NEXT_ACCOUNT_NUMBER += 1  # Increment for the next account

    accounts[account_number] = {
        'name': name,
        'balance': initial_deposit
    }
    print(f"Account created successfully! Your account number is {account_number}")


def view_balance(accounts):
    print("\n===== View Balance =====")
    account_number = input("Enter your account number: ")

    if account_number in accounts:
        print(f"Account Holder: {accounts[account_number]['name']}")
        print(f"Balance: {accounts[account_number]['balance']}")
    else:
        print("Account not found!")


def deposit(accounts):
    print("\n===== Deposit Money =====")

    while True:
        account_number = input("Enter your account number (or type 'quit' to return): ")

        if account_number.lower() == 'quit':
            return

        if account_number not in accounts:
            print("Account not found! Please try again.")
        else:
            break

    try:
        amount = float(input("Enter amount to deposit: "))
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
    except ValueError as ve:
        print(f"Error: {ve}")
        return

    accounts[account_number]['balance'] += amount
    print("Amount deposited successfully!")
    print(f"New Balance: {accounts[account_number]['balance']}")


def withdraw(accounts):
    print("\n===== Withdraw Money =====")

    while True:
        account_number = input("Enter your account number (or type 'quit' to return): ")

        if account_number.lower() == 'quit':
            return

        if account_number not in accounts:
            print("Account not found! Please try again.")
        else:
            break

    try:
        amount = float(input("Enter amount to withdraw: "))
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
    except ValueError as ve:
        print(f"Error: {ve}")
        return

    if accounts[account_number]['balance'] >= amount:
        accounts[account_number]['balance'] -= amount
        print("Amount withdrawn successfully!")
        print(f"New Balance: {accounts[account_number]['balance']}")
    else:
        print("Insufficient balance!")


def main():

    while True:
        choice = main_menu()
        if choice == '1':
            create_account(ACCOUNTS)
        elif choice == '2':
            view_balance(ACCOUNTS)
        elif choice == '3':
            deposit(ACCOUNTS)
        elif choice == '4':
            withdraw(ACCOUNTS)
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice! Please try again.")


if __name__ == "__main__":
    main()
