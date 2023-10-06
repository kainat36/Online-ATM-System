from logo import l1
from Atm_functions_file import create_account, login
while True:
    print(l1)
    print("_________________Welcome to Online Banking ATM System 🏧______________")
    print("\n \t \t  MAIN MENU:")
    print("\t \t \t 1. Create Account")
    print("\t \t \t 2. Checkin")
    print(" \t \t \t 3. Exit")
    choice = input("\n \t \t Enter your choice: ")

    if choice == "1":
        create_account()
    elif choice == "2":
        login()
    elif choice == "3":
        print("Exiting from online ATM System.")
        break
    else:
        print("Invalid choice.")
