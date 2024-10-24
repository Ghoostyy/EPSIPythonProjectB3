import os
import json
from BankAccount import BankAccount

def save_data_to_json(bank, filename="data/bank_data.json"):
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    
    data = {
        "accounts": {
            name: {
                "name": account.name,
                "balance": account.balance,
                "interest_rate": account.interest_rate,
                "pin_code": account.pin_code,
                "transaction_history": account.transaction_history,
                "interest_applied_this_month": account.interest_applied_this_month
            }
            for name, account in bank.accounts.items()
        }
    }
    print("Saving data to JSON file...")
    
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)
        
        
def load_data_from_json(bank, filename="data/bank_data.json"):
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            data = json.load(file)
            for name, account_data in data["accounts"].items():
                account = BankAccount(
                    name=account_data["name"],
                    initial_balance=account_data["balance"],
                    interest_rate=account_data["interest_rate"],
                    pin_code=account_data["pin_code"]
                )
                account.transaction_history = account_data["transaction_history"]
                account.interest_applied_this_month = account_data["interest_applied_this_month"]
                bank.accounts[name] = account
        print("Data loaded successfully.")
    else:
        print("No previous data found, starting fresh.")