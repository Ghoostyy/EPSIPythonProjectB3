'''
Projet Final: Gestionnaire de Banque Simplifié

Objectif : Créer une application Python qui simule un gestionnaire de comptes bancaires. L'utilisateur peut consulter le solde de son compte, déposer de l'argent, retirer de l'argent, et afficher l'historique des transactions.
Fonctionnalités du projet :

Création d'un compte :
Demander à l'utilisateur de saisir son nom et de créer un compte avec un solde initial. ✔️

Consultation du solde :
L'utilisateur peut consulter le solde de son compte à tout moment. ✔️

Dépôt d'argent :
L'utilisateur peut déposer de l'argent sur son compte. Le montant est ajouté au solde. ✔️

Retrait d'argent :
L'utilisateur peut retirer de l'argent, à condition que le montant soit disponible sur son compte (le solde ne peut pas devenir négatif). ✔️

Historique des transactions :
Chaque dépôt ou retrait doit être enregistré dans l'historique des transactions, et l'utilisateur peut afficher cet historique. ✔️

Menu d'options :
L'utilisateur peut naviguer dans un menu avec différentes options (Consulter le solde, Déposer de l'argent, Retirer de l'argent, Afficher l'historique, Quitter). ✔️

Ajout d’intérêts mensuels :
Chaque mois, un taux d’intérêt est appliqué au solde du compte. Par exemple, un taux d’intérêt de 1% est ajouté au solde chaque mois. ✔️

Le taux d’intérêt peut être défini lors de la création du compte. ✔️

Possibilité de créer plusieurs comptes :
L’utilisateur peut créer plusieurs comptes bancaires (par exemple, un compte épargne et un compte courant). ✔️

L’utilisateur peut consulter, déposer, retirer, ou transférer de l’argent entre les différents comptes. ✔️

Transfert d’argent entre comptes :

L’utilisateur peut transférer de l’argent entre ses différents comptes (par exemple, transférer de l'argent d'un compte courant vers un compte épargne). ✔️

Affichage des détails des comptes :

L’utilisateur peut afficher une liste de tous ses comptes avec les soldes actuels et les taux d’intérêt associés. ✔️

Ajout d’un code PIN pour chaque compte :
Lors de la création de chaque compte, un code PIN est défini. Ce code PIN doit être saisi pour accéder au compte. ✔️

Pseudo-code
Fonction de création du compte :
Demander le nom de l'utilisateur. ✔️
Initialiser un solde à 0. ✔️

Fonction pour consulter le solde :
Afficher le solde actuel du compte. ✔️

Fonction pour déposer de l'argent :
Demander à l'utilisateur combien il souhaite déposer. ✔️
Ajouter ce montant au solde. ✔️

Fonction pour retirer de l'argent :
Demander à l'utilisateur combien il souhaite retirer. ✔️
Vérifier que le solde est suffisant. ✔️
Retirer le montant du solde. ✔️
Fonction pour afficher l'historique des transactions : ✔️
Afficher la liste des dépôts et retraits effectués. ✔️

Boucle principale :
Afficher un menu d'options (1. Consulter le solde, 2. Déposer, 3. Retirer, 4. Historique, 5. Quitter). ✔️
Répéter l'action choisie jusqu'à ce que l'utilisateur décide de quitter. ✔️

Création de plusieurs comptes : 
Lors de la création, chaque compte a un nom unique, un solde initial, un taux d’intérêt et un code PIN. ✔️

Application des intérêts mensuels :
À chaque début de mois, un intérêt est calculé et ajouté au solde du compte. ✔️

Transfert d’argent entre comptes :
L’utilisateur peut sélectionner un compte source et un compte cible pour transférer de l’argent. ✔️
Vérifier que le compte source a un solde suffisant. ✔️

Affichage des détails de chaque compte :
Afficher le solde, le taux d’intérêt et la date de la dernière application des intérêts. ✔️
Sécurité avec code PIN : ✔️
Lors de l’accès à un compte, l’utilisateur doit entrer le code PIN correspondant pour effectuer des actions. ✔️
'''

import customtkinter as ctk
from tkinter import messagebox, simpledialog
from save import save_data_to_json, load_data_from_json
from Bank import Bank
from BankAccount import BankAccount

# Initialize customtkinter settings
ctk.set_appearance_mode("dark")  # Modes: "System" (default), "Dark", "Light"
ctk.set_default_color_theme("blue")  # Themes: "blue" (default), "green", "dark-blue"

class BankApp(ctk.CTk):
    bank: Bank
    current_account: BankAccount | None

    def __init__(self):
        super().__init__()
        self.bank = Bank()
        load_data_from_json(self.bank)
        self.current_account = None

        self.title("Bank Manager")
        self.geometry("400x500")

        # Create the main menu frame
        self.frame_menu = ctk.CTkFrame(self)

        self.label_title = ctk.CTkLabel(self.frame_menu, text="Bank Manager", font=("Arial", 16))
        self.label_title.pack(pady=10)

        self.btn_create_account = ctk.CTkButton(self.frame_menu, text="Create Account", command=self.show_create_account_frame)
        self.btn_create_account.pack(pady=5)

        self.btn_access_account = ctk.CTkButton(self.frame_menu, text="Access Account", command=self.show_access_account_frame)
        self.btn_access_account.pack(pady=5)

        self.btn_quit = ctk.CTkButton(self.frame_menu, text="Quit", command=self.quit)
        self.btn_quit.pack(pady=5)

        # Display the main menu initially
        self.frame_menu.pack()

    def show_create_account_frame(self):
        self.hide_all_frames()
        self.create_account_frame = ctk.CTkFrame(self)
        self.create_account_frame.pack(pady=20)

        ctk.CTkLabel(self.create_account_frame, text="Account Holder's Name:").grid(row=0, column=0)
        self.entry_name = ctk.CTkEntry(self.create_account_frame)
        self.entry_name.grid(row=0, column=1)

        ctk.CTkLabel(self.create_account_frame, text="Interest Rate (%):").grid(row=1, column=0)
        self.entry_interest_rate = ctk.CTkEntry(self.create_account_frame)
        self.entry_interest_rate.grid(row=1, column=1)

        ctk.CTkLabel(self.create_account_frame, text="Set a PIN Code:").grid(row=2, column=0)
        self.entry_pin = ctk.CTkEntry(self.create_account_frame, show='*')
        self.entry_pin.grid(row=2, column=1)

        self.btn_create = ctk.CTkButton(self.create_account_frame, text="Create Account", command=self.create_account)
        self.btn_create.grid(row=3, columnspan=2, pady=10)

        self.btn_back = ctk.CTkButton(self.create_account_frame, text="Back", command=self.show_main_menu)
        self.btn_back.grid(row=4, columnspan=2)

    def show_access_account_frame(self):
        self.hide_all_frames()
        self.access_account_frame = ctk.CTkFrame(self)
        self.access_account_frame.pack(pady=20)

        ctk.CTkLabel(self.access_account_frame, text="Account Holder's Name:").grid(row=0, column=0)
        self.entry_access_name = ctk.CTkEntry(self.access_account_frame)
        self.entry_access_name.grid(row=0, column=1)

        ctk.CTkLabel(self.access_account_frame, text="Enter PIN Code:").grid(row=1, column=0)
        self.entry_access_pin = ctk.CTkEntry(self.access_account_frame, show='*')
        self.entry_access_pin.grid(row=1, column=1)

        self.btn_access = ctk.CTkButton(self.access_account_frame, text="Access Account", command=self.access_account)
        self.btn_access.grid(row=2, columnspan=2, pady=10)

        self.btn_back_access = ctk.CTkButton(self.access_account_frame, text="Back", command=self.show_main_menu)
        self.btn_back_access.grid(row=3, columnspan=2)

    def show_main_menu(self):
        self.hide_all_frames()
        self.frame_menu.pack()

    def hide_all_frames(self):
        for widget in self.winfo_children():
            widget.pack_forget()

    def create_account(self):
        name = self.entry_name.get()
        try:
            initial_balance = 0
            interest_rate = float(self.entry_interest_rate.get())
            pin_code = self.entry_pin.get()
            if name and interest_rate >= 0 and pin_code:
                self.bank.create_account(name, initial_balance, interest_rate, pin_code)
                messagebox.showinfo("Success", f"Account '{name}' created successfully!")
                self.show_main_menu()
            else:
                messagebox.showerror("Error", "Please fill in all fields with valid data.")
        except ValueError:
            messagebox.showerror("Error", "Invalid input for interest rate.")

    def access_account(self):
        name = self.entry_access_name.get()
        pin_code = self.entry_access_pin.get()
        self.current_account = self.bank.access_account(name, pin_code)

        if self.current_account:
            self.show_account_menu()
        else:
            messagebox.showerror("Error", "Invalid account name or PIN code.")

    def show_account_menu(self):
        self.hide_all_frames()
        self.account_frame = ctk.CTkFrame(self)
        self.account_frame.pack(pady=20)

        ctk.CTkLabel(self.account_frame, text=f"Welcome, {self.current_account.name}!").pack()

        ctk.CTkButton(self.account_frame, text="Check Balance", command=self.check_balance).pack(pady=5)
        ctk.CTkButton(self.account_frame, text="Deposit Money", command=self.deposit_money).pack(pady=5)
        ctk.CTkButton(self.account_frame, text="Withdraw Money", command=self.withdraw_money).pack(pady=5)
        ctk.CTkButton(self.account_frame, text="Transaction History", command=self.show_transaction_history).pack(pady=5)
        ctk.CTkButton(self.account_frame, text="Transfer Money", command=self.show_transfer_frame).pack(pady=5)
        ctk.CTkButton(self.account_frame, text="Account Details", command=self.show_account_details).pack(pady=5)
        
        if self.current_account.has_savings_account:
            ctk.CTkButton(self.account_frame, text="Deposit to Savings", command=self.transfer_to_savings_account).pack(pady=5)
            ctk.CTkButton(self.account_frame, text="Withdraw from Savings", command=self.withdraw_from_savings_account).pack(pady=5)
        else:
            ctk.CTkButton(self.account_frame, text="Create Savings Account", command=self.create_savings_account).pack(pady=5)

        ctk.CTkButton(self.account_frame, text="Logout", command=self.show_main_menu).pack(pady=5)

    def refresht_account_menu(self):
        self.hide_all_frames()
        self.show_account_menu()
             
    def create_savings_account(self):
        initial_balance = self.prompt_for_amount("Deposit")
        if initial_balance is not None:
            if self.current_account.create_savings_account(initial_balance):
                messagebox.showinfo("Success", "Savings account created successfully!")
                self.refresht_account_menu()
            else:
                messagebox.showerror("Error", "Savings account already exists, or invalid initial balance.")
    
    def transfer_to_savings_account(self):
        amount = self.prompt_for_amount("Transfer")
        if amount is not None:
            if self.current_account.deposit_savings(amount):
                messagebox.showinfo("Success", f"Transferred {amount:.2f}€ to savings account!")
            else:
                messagebox.showerror("Error", "Insufficient balance or invalid amount.")
    
    def withdraw_from_savings_account(self):
        amount = self.prompt_for_amount("Withdraw")
        if amount is not None:
            if self.current_account.withdraw_savings(amount):
                messagebox.showinfo("Success", f"Withdrew {amount:.2f}€ from savings account!")
            else:
                messagebox.showerror("Error", "Insufficient balance or invalid amount.")

    def check_balance(self):
        balance = self.current_account.check_balance()
        
        if self.current_account.has_savings_account:
            savings_balance = self.current_account.check_savings_balance()
            messagebox.showinfo("Savings Balance", f"Your balance is: {balance:.2f}€ \nYour savings balance is: {savings_balance:.2f}€")
        else: 
            messagebox.showinfo("Balance", f"Your balance is: {balance:.2f}€")
        

    def deposit_money(self):
        amount = self.prompt_for_amount("Deposit")
        if amount is not None:
            self.current_account.deposit(amount)
            messagebox.showinfo("Success", f"Deposited {amount:.2f}€ successfully!")

    def withdraw_money(self):
        if self.prompt_for_pin("withdraw money"):
            amount = self.prompt_for_amount("Withdraw")
            if amount is not None:
                if self.current_account.withdraw(amount):
                    messagebox.showinfo("Success", f"Withdrew {amount:.2f}€ successfully!")
                else:
                    messagebox.showerror("Error", "Insufficient balance or invalid amount.")
        else:
            messagebox.showerror("Error", "Invalid PIN.")

    def show_transaction_history(self):
        history = self.current_account.show_transaction_history()
        messagebox.showinfo("Transaction History", history)

    def show_transfer_frame(self):
        self.hide_all_frames()
        self.transfer_frame = ctk.CTkFrame(self)
        self.transfer_frame.pack(pady=20)

        ctk.CTkLabel(self.transfer_frame, text="Transfer Money").pack(pady=10)

        ctk.CTkLabel(self.transfer_frame, text="Destination Account:").pack(pady=5)
        self.entry_transfer_destination = ctk.CTkEntry(self.transfer_frame)
        self.entry_transfer_destination.pack(pady=5)

        ctk.CTkLabel(self.transfer_frame, text="Amount:").pack(pady=5)
        self.entry_transfer_amount = ctk.CTkEntry(self.transfer_frame)
        self.entry_transfer_amount.pack(pady=5)

        self.btn_transfer = ctk.CTkButton(self.transfer_frame, text="Transfer", command=self.transfer_money)
        self.btn_transfer.pack(pady=10)

        self.btn_back_transfer = ctk.CTkButton(self.transfer_frame, text="Back", command=self.show_account_menu)
        self.btn_back_transfer.pack(pady=5)

    def transfer_money(self):
        destination_account_name = self.entry_transfer_destination.get()
        try:
            amount = float(self.entry_transfer_amount.get())
            destination_account = self.bank.accounts.get(destination_account_name)
            if destination_account and amount > 0 and self.current_account.balance >= amount:
                # Perform the transfer
                self.current_account.withdraw(amount)
                destination_account.deposit(amount)
                messagebox.showinfo("Success", f"Transferred {amount:.2f}€ to {destination_account_name}!")
            else:
                messagebox.showerror("Error", "Invalid transfer details.")
        except ValueError:
            messagebox.showerror("Error", "Invalid amount.")

    def show_account_details(self):
        details = f"Account: {self.current_account.name}\n" \
                  f"Balance: {self.current_account.balance:.2f}€\n" \
                  f"Interest Rate: {self.current_account.interest_rate}%"
                  
        if self.current_account.has_savings_account:
            details += f"\nSavings Balance: {self.current_account.savings_balance:.2f}€" \
                       f"\nSavings Interest Rate: {self.current_account.interest_rate * 2}%"
            
        messagebox.showinfo("Account Details", details)

    def prompt_for_amount(self, action):
        amount_str = simpledialog.askstring("Amount", f"Enter amount to {action}:")
        try:
            return float(amount_str) if amount_str else None
        except ValueError:
            messagebox.showerror("Error", "Invalid amount.")
            return None

    def prompt_for_pin(self, action):
        entered_pin = simpledialog.askstring("PIN", f"Enter PIN to {action}:", show='*')
        return entered_pin == self.current_account.pin_code

    def quit(self):
        save_data_to_json(self.bank)
        self.destroy()

if __name__ == "__main__":
    app = BankApp()
    app.mainloop()
