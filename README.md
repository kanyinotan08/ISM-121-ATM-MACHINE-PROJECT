# ISM-121-ATM-MACHINE-PROJECT
# ATM Machine Simulator

A simple command-line ATM machine simulator built with Python for basic banking operations.

## Features

- Account creation with custom account number and PIN
- Deposit and withdraw money
- Check account balance
- Update PIN
- PIN verification for all operations

## Usage

Run the program:

bash
python atm_machine.py


### Setup

1. Enter a new account number
2. Set your PIN
3. Account created with initial balance of 0

### Operations

*Deposit* - Add funds to your account

*Check Balance* - View current balance

*Withdraw* - Remove funds (with insufficient funds protection)

*Update PIN* - Change your security PIN

Each operation requires PIN verification. After each transaction, you'll be prompted to continue or exit.

## Example


Enter new account number: 123456
Set your PIN: 1234
Account created successfully!

Enter PIN to deposit: 1234
Enter amount to deposit: 1000
Deposit successful. Balance: 1000

Continue? (YES/NO): YES