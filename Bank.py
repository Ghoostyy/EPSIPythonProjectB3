from BankAccount import BankAccount


class Bank:
    def __init__(self):
        self.accounts = {}
        
    # Create a new account
    def create_account(self, name, initial_balance, interest_rate, pin_code):
        account = BankAccount(name, initial_balance, interest_rate, pin_code)
        self.accounts[name] = account
        return account
    
    # Access an existing account
    def access_account(self, name, pin_code):
        account = self.accounts.get(name)
        if account and account.pin_code == pin_code:
            return account
        return None