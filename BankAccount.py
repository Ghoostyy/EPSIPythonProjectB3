from datetime import datetime

class BankAccount:
    name: str
    balance: float
    interest_rate: float
    pin_code: int
    transaction_history: list[str]
    interest_applied_this_month: bool
    last_interest_update: datetime
    
    has_savings_account: bool = False
    savings_balance: float = 0.0
    
    def __init__(self, name: str, initial_balance: float, interest_rate: float, pin_code: int):
        self.name = name
        self.balance = initial_balance
        self.interest_rate = interest_rate
        self.pin_code = pin_code
        self.transaction_history = []
        self.interest_applied_this_month = True
        self.last_interest_update = datetime.now()

    # Check the balance
    def check_balance(self) -> float:
        self.apply_interest_if_needed()
        return self.balance
    
    # Deposit money into the account
    def deposit(self, amount: float) -> bool:
        self.apply_interest_if_needed()
        if amount > 0:
            self.balance += amount
            self.transaction_history.append(f"Deposit of {amount}€ on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
            return True
        else:
            return False
        
    # Withdraw money from the account
    def withdraw(self, amount: float) -> bool:
        self.apply_interest_if_needed()
        if amount > 0 and self.balance >= amount:
            self.balance -= amount
            self.transaction_history.append(f"Withdrawal of {amount}€ on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
            return True
        else:
            return False
        
    # Show the transaction history
    def show_transaction_history(self) -> str:
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
            rate = self.interest_rate
            
            interest = self.balance * (rate / 100)
            self.balance += interest
            self.transaction_history.append(f"Interest of {interest:.2f}€ applied on {today.strftime('%Y-%m-%d %H:%M:%S')}")

            if self.has_savings_account:
                rate = self.interest_rate * 2

                interest = self.savings_balance * (rate / 100)
                self.savings_balance += interest
                self.transaction_history.append(f"Interest of {interest:.2f}€ to the savings account applied on {today.strftime('%Y-%m-%d %H:%M:%S')}")

            self.interest_applied_this_month = True
        
    # Check the savings account balance
    def check_savings_balance(self) -> float:
        self.apply_interest_if_needed()
        return self.savings_balance
            
    # Create a savings account
    def create_savings_account(self, initial_balance: float) -> bool:
        if not self.has_savings_account and initial_balance >= 0 and self.balance >= initial_balance:
            self.has_savings_account = True
            self.savings_balance = initial_balance
            self.balance -= initial_balance
            self.transaction_history.append(f"Deposit of {initial_balance}€ on Savings on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
            return True
        return False
    
    # Deposit money into the savings account
    def deposit_savings(self, amount: float) -> bool:
        if self.has_savings_account and amount > 0 and self.balance >= amount:
            self.balance -= amount
            self.savings_balance += amount
            self.transaction_history.append(f"Deposit of {amount}€ on Savings on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
            return True
        return False
    
    # Withdraw money from the savings account
    def withdraw_savings(self, amount: float) -> bool:
        if self.has_savings_account and amount > 0 and self.savings_balance >= amount:
            self.balance += amount
            self.savings_balance -= amount
            self.transaction_history.append(f"Withdrawal of {amount}€ on Savings on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
            return True
        return False
