from datetime import datetime, timedelta
# Date and time 
def date_and_time(): 
    current_datetime = datetime.now()
    return current_datetime


# updates atm_balance.txt
def balance_update(transaction):
    with open("atm_balance.txt", "r") as atm_balance:
        old_balance = atm_balance.read()
    updated_balance = float(transaction) + float(old_balance)
    if updated_balance < 0:
        print("Insufficient funds please try again:")
        print("Your availible balance: $",old_balance)
    else:
        updated_balance = str(float(transaction) + float(old_balance))
        with open("atm_balance.txt", "w") as atm_balance:
            atm_balance.write(updated_balance)
            return updated_balance


# updates atm_history.txt
def atm_history_update(transaction):
    new_balance = balance_update(transaction)
    with open("atm_history.txt", "a") as atm_history:
        transaction_entry = f"{date_and_time()} | {'Deposit' if transaction >= 0 else 'Withdrawal'}: {abs(transaction)} | Balance: {new_balance}\n"
        atm_history.writelines(str(transaction_entry))
        atm_history.writelines("\n")


# transaction updater
def atm_transaction(transaction):
    transaction = transaction
   
    atm_history_update(transaction)


# balance check
def current_balance(balance_check):
    balance_check = float(balance_check)
    if balance_check == 1:
        with open("atm_balance.txt", "r") as atm_balance:
            balance = atm_balance.read()
            return balance
            

# check atm.history
def check_atm_history(limit=10):
    with open("atm_history.txt", "r") as atm_history:
        transactions = atm_history.readlines()
    return transactions[-limit:]

def isfloat(value):
    try:
        float(value)
        return True
    except ValueError:
        return False

# menu loop 
while True:
    menu = int(input("Welcome to Nate's ATM!!!\n\
    Please select from the following options\n\
    1) View balance\n\
    2) Deposit money\n\
    3) Withdrawl money\n\
    4) Transaction history\n\
    5) Exit\n"))

    # View balance
    if menu == 1:
       print("Your availible balance: $",current_balance(1))

    # deposit
    elif menu == 2:
        deposit_amount_input = input("Please enter the amount you would like to deposit\n")
        if isfloat(deposit_amount_input):
            deposit_amount = float(deposit_amount_input)
            if deposit_amount < 0:
                print("Invalid entry, deposit amount cannot be negative.")
            else:
                atm_transaction(deposit_amount)
                print("Current balance: $",current_balance(1))
        else:
            print("Invalid entry, please try again")

    # withdrawl
    elif menu == 3:
        print("Your availible balance: $",current_balance(1))
        withdrawl_amount_input = input("Please enter the amount you would like to withdrawl\n")
        if isfloat(withdrawl_amount_input):
            withdrawl_amount = float(withdrawl_amount_input)
            if withdrawl_amount < 0:
                print("Invalid entry, deposit amount cannot be negative.")
            else:
                atm_transaction(-abs(withdrawl_amount))
                print("Current balance: $",current_balance(1))
        else:
            print("Invalid entry, please try again")
        
        
    # transaction history
    elif menu == 4:
        transactions = check_atm_history(limit=10)
        transaction_history = "\n".join(transactions)
        print("Transaction History\n", transaction_history)
    
    elif menu == 5:
        print("Thank you for using Nate's ATM! Goodbye!")
        break
    # invalid entry
    else:
        print("Invalid entry, please try again.")


