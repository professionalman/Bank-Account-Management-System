import os
import time

def generate_account_no():
    # Check if the account number file exists
    if os.path.exists("account_number.txt"):
        with open("account_number.txt", "r") as file:
            last_account_no = int(file.read())
    else:
        last_account_no = 1000000  # Starting account number (you can change this)

    # Increment the account number for the new account
    new_account_no = last_account_no + 1

    # Update the file with the new account number
    with open("account_number.txt", "w") as file:
        file.write(str(new_account_no))

    return str(new_account_no)


def folderPath(folder_path):
    return "./customer_data/" + folder_path


def account_info():
    print("---------------Customer Account Info---------------")
    name = input("Enter Customer Name: ")
    account_no = generate_account_no()  # Automatically generate account number
    print(f"Generated Account Number: {account_no}")
    email = input("Enter Customer Email ID: ")
    contact = input("Enter Customer Contact No: ")
    address = input("Enter Customer Address: ")

    # Valid account types
    valid_account_types = ["SAVING", "CURRENT", "FIXED"]

    # Loop to ensure valid account type is entered
    while True:
        account_type = input("Enter Customer Account Type (SAVING, CURRENT, FIXED): ").upper()
        if account_type in valid_account_types:
            break
        else:
            print("Invalid account type. Please enter either 'SAVING', 'CURRENT', or 'FIXED'.")

    available_balance = input("Enter Customer Balance: ")

    folder_name = name.upper() + "_" + account_no
    os.mkdir(folderPath(folder_name))

    accountinfo = f"{name.upper()},{email},{contact},{address},{account_no},{account_type},{available_balance}"
    with open(folderPath(f"{folder_name}/{account_no}_info"), 'w') as info:
        info.write(accountinfo)


def balance():
    ok = True
    while ok:
        print("---------------Customer Available Balance---------------")
        name = input("Enter Account Holder Name: ")
        accountNo = input("Enter Account No: ")
        cpath = name.upper() + "_" + accountNo
        if os.path.exists(folderPath(cpath)):
            with open(folderPath(f"{cpath}/{accountNo}_info"), 'r') as open_:
                data = open_.read()
                _, _, _, _, _, _, available_Balance = data.split(",")
                print("Available Balance: ", available_Balance)
        else:
            print("Please enter valid account no and name")
        Qus = input("Do you want to search again? (Y/N): ").upper()
        if Qus == "Y":
            ok = True
        elif Qus == "N":
            ok = False
        else:
            print("Please enter a valid option")


def transaction():
    kk = True
    while kk:
        print("---------------Customer Transaction---------------")
        name = input("Enter Account Holder Name: ")
        accountNo = input("Enter Account No: ")
        cpath = name.upper() + "_" + accountNo
        if os.path.exists(folderPath(cpath)):
            with open(folderPath(f"{cpath}/{accountNo}_info"), 'r') as open_:
                data = open_.read()
                _, _, _, _, _, _, available_Balance = data.split(",")

            credit_amt = "0.00"
            debit_amt = "0.00"
            transaction_ = "Balance"
            current_time = time.strftime("%d/%m/%Y")
            tran_data = f"{current_time:<12} {transaction_:<15} {debit_amt:<10} {credit_amt:<10} {float(available_Balance):.2f}"

            with open(folderPath(f"{cpath}/{accountNo}_Tran"), 'a') as tran_file:
                tran_file.write(tran_data + "\n")

            tran = input("Do you want to Credit or Debit amount? ").upper()
            if "CREDIT" in tran:
                credit_amt = input("Enter credit amount: ")
                available_Balance = float(credit_amt) + float(available_Balance)
                transaction_ = "Deposit by self"

            elif "DEBIT" in tran:
                debit_amt = input("Enter debit amount: ")
                if float(debit_amt) <= float(available_Balance):
                    available_Balance = float(available_Balance) - float(debit_amt)
                    transaction_ = "Withdraw"
                else:
                    print("Insufficient balance")
                    continue  # Skip the rest of the loop if the transaction is invalid
            else:
                print("Invalid option")
                continue  # Skip the rest of the loop if invalid option

            # Update account info with new balance
            with open(folderPath(f"{cpath}/{accountNo}_info"), 'w') as open_2:
                open_2.write(f"{name.upper()},{_},{_},{_},{accountNo},{_},{available_Balance:.2f}")

            # Format the transaction output neatly
            tran_data = f"{current_time:<12} {transaction_:<15} {float(debit_amt):<10.2f} {float(credit_amt):<10.2f} {float(available_Balance):<10.2f}"
            with open(folderPath(f"{cpath}/{accountNo}_Tran"), 'a') as tran_file:
                tran_file.write(tran_data + "\n")

        else:
            print("Account does not exist")

        Qus = input("Do you want to perform another transaction? (Y/N): ").upper()
        kk = Qus == "Y"


def PrintTran():
    print("---------------Customer Transaction---------------")
    name = input("Enter Account Holder Name: ")
    accountNo = input("Enter Account No: ")
    cpath = name.upper() + "_" + accountNo
    if os.path.exists(folderPath(cpath)):
        print(f"{'Date':<12} {'Transaction':<15} {'Debit':<10} {'Credit':<10} {'Balance':<10}")
        print("=" * 60)  # Divider for better readability

        with open(folderPath(f"{cpath}/{accountNo}_Tran"), 'r') as open_:
            data = open_.readlines()
            for line in data:
                print(line.strip())
    else:
        print("Account does not exist")
