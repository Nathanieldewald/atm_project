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
    transaction = str(transaction)
    with open("atm_history.txt", "a") as atm_history:
        transaction = {transaction:"transaction", balance_update(transaction):"Balance", date_and_time():"datetime"}
        atm_history.writelines(str(transaction))
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
def check_atm_history():
    with open("atm_history.txt", "r") as atm_history:
        transactions = atm_history.readlines()
        for i in transactions:
            print("$",i)


# menu loop 
while True:
    menu = int(input(
    "Welcome to Nate's ATM!!!\n\
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
        deposit_amount = float(input("Please enter the amount you would like to deposit\n"))
        atm_transaction(deposit_amount)
        print("Current balance: $",current_balance(1))

    # withdrawl
    elif menu == 3:
        print("Your availible balance: $",current_balance(1))
        withdrawl_amount = -abs(float(input("Please enter the amount you would like to withdrawl\n")))
        atm_transaction(withdrawl_amount)
        print("Current balance: $",current_balance(1))
        
    # transaction history
    elif menu == 4:
        check_atm_history()
    # exit
    elif menu == 5:
        print("Thank you for using Nate's ATM! Goodbye!")
        break
    # invalid entry
    else:
        print("Invalid entry, please try again.")