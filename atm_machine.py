ccount_number = ""
pin = ""
balance = 0

    # Create account
account_number = input("Enter new account number: ")
pin = input("Set your PIN: ")
print("Account created successfully!\n")

    # If user wants to continue
continue_using = "YES"
while continue_using == "YES":
 
        # Deposit
    entered_pin = input("Enter PIN to deposit: ")
    if entered_pin == pin:
        amount = int(input("Enter amount to deposit: "))
        balance += amount
        print("Deposit successful. Balance:", balance)
    else:
        print("Wrong PIN.")

    continue_using = input("\nContinue? (YES/NO): ")
    if continue_using != "YES":
        break


        # Withdraw
    entered_pin = input("\nEnter PIN to withdraw: ")
    if entered_pin == pin:
        amount = int(input("Enter amount to withdraw: "))
        if amount <= balance:
            balance -= amount
            print("Withdrawal successful. Balance:", balance)
        else:
            print("Insufficient funds.")
    else:
        print("Wrong PIN.")

        continue_using = input("\nContinue? (YES/NO): ")
        if continue_using != "YES":
            break

        # Update PIN
    entered_pin = input("\nEnter old PIN to update: ")
    if entered_pin == pin:
        pin = input("Enter new PIN: ")
        print("PIN updated successfully!")
    else:
        print("Wrong PIN.")

        continue_using = input("\nContinue? (YES/NO): ")
        
        # Check balance
        entered_pin = input("\nEnter PIN to check balance: ")
        if entered_pin == pin:
            print("Your balance is:", balance)
        else:
            print("Wrong PIN.")

        continue_using = input ("\nContinue? (YES/NO): ")
        if continue_using != "YES":
            break