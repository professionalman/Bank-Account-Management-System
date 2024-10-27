# Bank Account Management System

This project is a simple command-line based Bank Account Management System implemented in Python. It allows users to create and manage bank accounts, perform transactions, and view account details.

## Features

- **Create Account:** Allows users to add new bank account details, including name, account number, email, contact number, address, and account type.
- **Check Balance:** Users can check the available balance of a specific account.
- **Perform Transactions:** Users can perform credit and debit transactions on accounts.
- **View Transactions:** Users can print the transaction history for any account.
- **Exit:** Option to exit the program.

## File Structure

- `__init__.py`: Contains the main program that runs the Bank Account Management System's menu-driven interface.
- `create_account.py`: Handles all account-related functionalities like creating accounts, checking balance, performing transactions, and printing transaction history.

## How to Run the Project

1. Clone the repository:
   ```bash
   git clone https://github.com/professionalman/Bank-Account-Management-System.git
2. Navigate to the project directory:
   ```bash
   cd bank-account-management-system
3. Run the program:
   ```bash
   python __init__.py

## How It Works

- The user is presented with a menu that allows selecting various options like adding a new account, checking the balance, making transactions, and printing transaction history.
- The `create_account.py` module handles the core functionality of managing account data.
- All data, including account details and transaction history, is stored locally in directories named after the account holder.

## Authors
- This project was created by Kavya Arora and Akash Malik.
  
