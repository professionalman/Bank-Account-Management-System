import os
import time


def folderPath(folder_path):
    return "./customer_data/" + folder_path


def account_info():
    print("---------------Customer Account Info---------------")
    name = input("Enter Customer Name: ")
    account_no = input("Enter Customer Account No: ")
    email = input("Enter Customer Email ID: ")
    contact = input("Enter Customer Contact No: ")
    address = input("Enter Customer Address: ")
    account_type = input("Enter Customer Account Type: ")
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
            tran_data = f"{current_time}, {transaction_}, {debit_amt[:6]}, {credit_amt[:6]}, {available_Balance[:6]}"
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
            else:
                print("Invalid option")

            with open(folderPath(f"{cpath}/{accountNo}_info"), 'w') as open_2:
                open_2.write(f"{name.upper()},{_},{_},{_},{accountNo},{_},{available_Balance}")

            tran_data = f"{current_time}, {transaction_}, {float(debit_amt):.2f},{float(credit_amt):.2f},{float(available_Balance):.2f}"
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
        with open(folderPath(f"{cpath}/{accountNo}_Tran"), 'r') as open_:
            data = open_.read()
            print(data)
    else:
        print("Account does not exist")