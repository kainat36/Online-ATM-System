import json
import random


def read_data():
    # reading data from json
    try:
        with open("users.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}


def save_data(user):
    # writing data in json file
    with open("users.json", "w") as file:
        json.dump(user, file, indent=4)


def create_account():
    """ taking name, deposit amount and pincode from user and generate userid and username randomly that will be unique
    through dictionary getting data and writing in json file and once account created it displays user id and name
"""
    name = input("Enter your name: ")
    deposit_amount = float(input("Enter initial deposit amount (more than 50): "))
    while deposit_amount < 50:
        deposit_amount = float(input("Please enter an initial deposit greater than 50: "))
    pin_code = input("Enter a 4-digit PIN code: ")
    if int(len(pin_code)) != 4:
        print("invalid pincode!")
        return

    user_id = random.randint(1000000000, 9999999999)
    username = name.lower() + str(random.randint(100, 999))

    user_data = {
        "name": name,
        "deposit": deposit_amount,
        "pin_code": pin_code,
        "id": user_id,
        "username": username,
        "status": "ACTIVE",
        "currency": "PKR",
        "statement": [{"transaction": "Deposit", "amount": deposit_amount}]
    }

    user_db[username] = user_data
    save_data(user_db)
    print("Account created successfully!")
    print(f"Your user ID is: {user_id}")
    print(f"Your username is: {username}")



def login():
    """ taking username and pin if these things match with json file data then login successful otherwise user not found
     if wrong pin code is entered more than 3 times then status of user got blocked from json file
    """
    user_name = input("Enter your username: ")
    pin_attempt_count = 0

    if user_name in user_db:
        while pin_attempt_count < 3:
            pin = input("Enter your PIN code: ")
            if pin == user_db[user_name]["pin_code"]:
                print(f"Authentication successful! welcome {user_name}")
                sub_menu(user_name)
                break
            else:

                pin_attempt_count += 1
                if pin_attempt_count < 3:
                    print("Incorrect PIN code. Please try again.")
                else:
                    print("Incorrect PIN code. Account is now blocked.")
                    user_db[user_name]["status"] = "BLOCKED"
                    save_data(user_db)
    else:
        print("User not found.")


def account_detail(username):
    """read a users details from json file and print details"""
    user_data = user_db[username]
    print(f"Name: {user_data['name']}")
    print(f"Username: {user_data['username']}")
    print(f"Status: {user_data['status']}")
    print(f"Balance: {user_data['deposit']} {user_data['currency']}")


def deposit(username):
    """taking amount from user he wants to deposit and check whether amount must be greater than 50
    updating to deposit amount in json and appends the statement"""
    amount = float(input("Enter the deposit amount: "))
    if amount >= 50:
        user_data = user_db[username]
        user_data["deposit"] += amount
        user_data["statement"].append({"transaction": "Deposit", "amount": amount})
        save_data(user_db)
        print(f"Deposit successful! New balance: {user_data['deposit']} {user_data['currency']}")
    else:
        print("Deposit amount should be at least 50.")


def withdraw(username):
    """ firstly check the status of user if it is blocked then will return the function if status is active then ask
    for amount for withdrawal then apply tax on amount given by user and check if amount is less than amount in
    total amount then display insufficient amount if amount is equal or greater than subtract amount from account
     and append the statement and display withdrawal successful"""
    user_data = user_db[username]
    if user_data["status"] == "BLOCKED":
        print("Account is blocked. Cannot withdraw.")
        return

    amount = float(input("Enter the withdrawal amount: "))
    tax = amount * 0.01
    total_amount = amount + tax

    if total_amount <= user_data["deposit"]:
        user_data["deposit"] -= total_amount
        user_data["statement"].append({"transaction": "Withdrawal", "amount": -total_amount})
        save_data(user_db)
        print(f"Withdrawal successful! with tax amount of {tax} Rs. New balance: {user_data['deposit']} "
              f"{user_data['currency']}")
    else:
        print("Insufficient balance for withdrawal.")


def update_pin(username):
    """ take old/current pin and matches with pincode in users.json file  against username and if both are equal then
    ask for new pincode that must be of 4 digit and update it else print incorrect current pin"""
    current_pin = input("Enter your current PIN code: ")
    if current_pin == user_db[username]["pin_code"]:
        new_pin = input("Enter your new 4-digit PIN code: ")
        if len(new_pin) == 4 and new_pin.isdigit():
            user_db[username]["pin_code"] = new_pin
            save_data(user_db)
            print("PIN code updated successfully.")
        else:
            print("New PIN code must be 4 digits.")
    else:
        print("Incorrect current PIN code.")


def check_statement(username):
    """ create statement with username and save in variable then write the statement from users.json in to
    user_statement in text file then read the file and print then data inside user_statement file and also create
    that text file"""
    user_data = user_db[username]
    statement_filename = f"{username}_statement.txt"

    with open(statement_filename, "w") as file:
        for entry in user_data["statement"]:
            file.write(f"Transaction: {entry['transaction']}, Amount: {entry['amount']} {user_data['currency']}\n")
    with open(statement_filename, 'r') as file1:
        get_statement = file1.read()
    print(f"Here is your bank statement:\n {get_statement}")


def sub_menu(username):
    """ having different options and user select from this submenu"""
    while True:
        print("\nSUB MENU:")
        print("1. Account Detail")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Update PIN")
        print("5. Check Statement")
        print("6. Logout")
        user_choice = input("Enter your choice: ")

        if user_choice == "1":
            account_detail(username)
        elif user_choice == "2":
            deposit(username)
        elif user_choice == "3":
            withdraw(username)
        elif user_choice == "4":
            update_pin(username)
        elif user_choice == "5":
            check_statement(username)
        elif user_choice == "6":
            print("Logged out. Thankyou for using online banking system")
            return
        else:
            print("Invalid choice.")


user_db = read_data()
