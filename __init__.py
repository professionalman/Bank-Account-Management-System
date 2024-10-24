import create_account as account

def run_Program():
    Condition = True
    while Condition:
        menu = int(input("""
            MENU:
            1. Add Account
            2. Search Balance
            3. Transaction 
            4. Print Transaction
            5. Exit    
    
        """))
        if menu == 1:
            account.account_info()
        elif menu == 2:
            account.balance()
        elif menu == 3:
            account.transaction()
        elif menu == 4:
            account.PrintTran()
        elif menu == 5:
            exit()
        else:
            print('Please Enter valid Option ')

        while True:
            Continue = input("""
                Do you want to Continue Yes ot Not           
                """)
            if Continue.upper() == "YES":
                Condition = True
                break
            elif Continue.upper() == "NOT":
                Condition = False
                break
            else:
                print("Pls enter valid key")

if __name__ == "__main__":
    run_Program()