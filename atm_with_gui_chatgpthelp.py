import tkinter as tk
import tkinter.messagebox as messagebox
import tkinter.simpledialog as simpledialog
from datetime import datetime

class ATM:
    def __init__(self):
        self.balance_file = "atm_balance.txt"
        self.history_file = "atm_history.txt"

    def date_and_time(self):
        current_datetime = datetime.now()
        return current_datetime

    def balance_update(self, transaction):
        with open(self.balance_file, "r") as atm_balance:
            old_balance = atm_balance.read()
        updated_balance = float(transaction) + float(old_balance)
        if updated_balance < 0:
            return None
        else:
            updated_balance = str(round(float(transaction) + float(old_balance), 2))
            with open(self.balance_file, "w") as atm_balance:
                atm_balance.write(updated_balance)
            return updated_balance

    def atm_history_update(self, transaction):
        new_balance = self.balance_update(transaction)
        if new_balance is not None:
            transaction_entry = f"{self.date_and_time()} | {'Deposit' if transaction >= 0 else 'Withdrawal'}: {abs(transaction)} | Balance: {new_balance}\n"
            with open(self.history_file, "a") as atm_history:
                atm_history.writelines(transaction_entry)

    def current_balance(self):
        with open(self.balance_file, "r") as atm_balance:
            balance = atm_balance.read()
        return balance

    def check_atm_history(self, limit=10):
        with open(self.history_file, "r") as atm_history:
            transactions = atm_history.readlines()
        return transactions[-limit:]

class ATM_GUI:
    def __init__(self):
        self.atm = ATM()
        self.main_window()

    def main_window(self):
        self.window = tk.Tk()
        self.window.title("Nate's ATM services")
        greeting = tk.Label(
            text="Welcome to Nate's ATM!!!\n\
        Please select from the following options\n\
        1) View balance\n\
        2) Deposit money\n\
        3) Withdraw money\n\
        4) Transaction history\n\
        5) Exit\n",
            fg="black",
            bg="white",
        )

        entry = tk.Entry(fg="black", bg="white", width=25)
        submit_button = tk.Button(text="Submit", command=lambda: self.process_menu_choice(entry.get()))

        greeting.pack()
        entry.pack()
        submit_button.pack()

        self.window.mainloop()

    def process_menu_choice(self, menu_choice):
        try:
            menu_choice = int(menu_choice)
            if menu_choice == 1:
                self.view_balance()
            elif menu_choice == 2:
                self.deposit_money()
            elif menu_choice == 3:
                self.withdraw_money()
            elif menu_choice == 4:
                self.transaction_history()
            elif menu_choice == 5:
                self.window.quit()
            else:
                messagebox.showerror("Error", "Invalid entry, please try again.")
        except ValueError:
            messagebox.showerror("Error", "Invalid entry, please try again.")

    def view_balance(self):
        balance = self.atm.current_balance()
        messagebox.showinfo("Current Balance", f"Your available balance: $ {balance}")

    def deposit_money(self):
        deposit_amount = simpledialog.askfloat("Deposit Money", "Please enter the amount you would like to deposit:")
        if deposit_amount is not None:
            self.atm.atm_history_update(abs(deposit_amount))
            balance = self.atm.current_balance()
            messagebox.showinfo("Current Balance", f"Current balance: $ {balance}")

    def withdraw_money(self):
        withdraw_amount = simpledialog.askfloat("Withdraw Money", "Please enter the amount you would like to withdraw:")
        if withdraw_amount is not None:
            self.atm.atm_history_update(-abs(withdraw_amount))
            balance = self.atm.current_balance()
            messagebox.showinfo("Current Balance", f"Your available balance: $ {balance}")

    def transaction_history(self):
        transactions = self.atm.check_atm_history()
        transaction_history = "\n".join(transactions)
        messagebox.showinfo("Transaction History", transaction_history)

if __name__ == "__main__":
    ATM_GUI()
