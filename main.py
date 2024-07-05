# bank_management_system.py

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
    print("\n===== Create Account =====")
    name = input("Enter your name: ")
    account_number = input("Enter your account number: ")

    try:
        initial_deposit = float(input("Enter initial deposit: "))
        if initial_deposit < 0:
            raise ValueError("Initial deposit cannot be negative.")
    except ValueError as ve:
        print(f"Error: {ve}")
        return

    if account_number in accounts:
        print("Account number already exists!")
    else:
        accounts[account_number] = {
            'name': name,
            'balance': initial_deposit
        }
        print("Account created successfully!")


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
    account_number = input("Enter your account number: ")

    if account_number not in accounts:
        print("Account not found!")
        return

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
    account_number = input("Enter your account number: ")

    if account_number not in accounts:
        print("Account not found!")
        return

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
    accounts = {}
    while True:
        choice = main_menu()
        if choice == '1':
            create_account(accounts)
        elif choice == '2':
            view_balance(accounts)
        elif choice == '3':
            deposit(accounts)
        elif choice == '4':
            withdraw(accounts)
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice! Please try again.")


if __name__ == "__main__":
    main()
