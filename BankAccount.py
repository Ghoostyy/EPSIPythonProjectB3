from datetime import datetime

class BankAccount:
    def __init__(self, name, initial_balance, interest_rate, pin_code):
        self.name = name
        self.balance = initial_balance
        self.interest_rate = interest_rate
        self.pin_code = pin_code
        self.transaction_history = []
        self.interest_applied_this_month = True
        self.last_interest_update = datetime.now()

    # Check the balance
    def check_balance(self):
        self.apply_interest_if_needed()
        return self.balance
    
    # Deposit money into the account
    def deposit(self, amount):
        self.apply_interest_if_needed()
        if amount > 0:
            self.balance += amount
            self.transaction_history.append(f"Deposit of {amount}€ on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
            return True
        else:
            return False
        
    # Withdraw money from the account
    def withdraw(self, amount):
        self.apply_interest_if_needed()
        if amount > 0 and self.balance >= amount:
            self.balance -= amount
            self.transaction_history.append(f"Withdrawal of {amount}€ on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
            return True
        else:
            return False
        
    # Show the transaction history
    def show_transaction_history(self):
        return "\n".join(self.transaction_history) if self.transaction_history else "No transactions have been made."

    # Apply interest to the account balance and update the interest rate by 1% each month
    def apply_interest_if_needed(self):
        today = datetime.now()
        # Update the interest rate by 1% each month and reset
        if today.month != self.last_interest_update.month or today.year != self.last_interest_update.year:
            self.interest_rate += 1.0
            self.last_interest_update = today
            self.interest_applied_this_month = False
            
        # Apply interest if it hasn't been applied yet this month   
        if not self.interest_applied_this_month:
            interest = self.balance * (self.interest_rate / 100)
            self.balance += interest
            self.transaction_history.append(f"Interest of {interest:.2f}€ applied on {today.strftime('%Y-%m-%d %H:%M:%S')}")
            self.interest_applied_this_month = True
