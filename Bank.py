from BankAccount import BankAccount


class Bank:
    accounts: dict[str, BankAccount]
    
    def __init__(self):
        self.accounts = {}
        
    # Create a new account
    def create_account(self, name, initial_balance, interest_rate, pin_code) -> BankAccount:
        account = BankAccount(name, initial_balance, interest_rate, pin_code)
        self.accounts[name] = account
        return account
    
    # Access an existing account
    def access_account(self, name, pin_code) -> BankAccount | None:
        account = self.accounts.get(name)
        if account and account.pin_code == pin_code:
            return account
        return None