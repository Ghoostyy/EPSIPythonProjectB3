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
L’utilisateur peut créer plusieurs comptes bancaires (par exemple, un compte épargne et un compte courant).

L’utilisateur peut consulter, déposer, retirer, ou transférer de l’argent entre les différents comptes. ✔️

Transfert d’argent entre comptes :

L’utilisateur peut transférer de l’argent entre ses différents comptes (par exemple, transférer de l'argent d'un compte courant vers un compte épargne). 

Affichage des détails des comptes :

L’utilisateur peut afficher une liste de tous ses comptes avec les soldes actuels et les taux d’intérêt associés.

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

import tkinter as tk
from tkinter import messagebox, simpledialog
from save import save_data_to_json, load_data_from_json
from Bank import Bank

class BankApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.bank = Bank()
        load_data_from_json(self.bank)
        self.current_account = None

        self.title("Simple Bank Manager")
        self.geometry("400x400")

        # Create the main menu frame once
        self.frame_menu = tk.Frame(self)

        self.label_title = tk.Label(self.frame_menu, text="Simple Bank Manager", font=("Arial", 16))
        self.label_title.pack(pady=10)

        self.btn_create_account = tk.Button(self.frame_menu, text="Create Account", command=self.show_create_account_frame)
        self.btn_create_account.pack(pady=5)

        self.btn_access_account = tk.Button(self.frame_menu, text="Access Account", command=self.show_access_account_frame)
        self.btn_access_account.pack(pady=5)

        self.btn_quit = tk.Button(self.frame_menu, text="Quit", command=self.quit)
        self.btn_quit.pack(pady=5)

        # Display the main menu initially
        self.frame_menu.pack()

    def show_create_account_frame(self):
        self.hide_all_frames()
        self.create_account_frame = tk.Frame(self)
        self.create_account_frame.pack(pady=20)

        tk.Label(self.create_account_frame, text="Account Holder's Name:").grid(row=0, column=0)
        self.entry_name = tk.Entry(self.create_account_frame)
        self.entry_name.grid(row=0, column=1)

        tk.Label(self.create_account_frame, text="Initial Balance:").grid(row=1, column=0)
        self.entry_balance = tk.Entry(self.create_account_frame)
        self.entry_balance.grid(row=1, column=1)

        tk.Label(self.create_account_frame, text="Interest Rate (%):").grid(row=2, column=0)
        self.entry_interest_rate = tk.Entry(self.create_account_frame)
        self.entry_interest_rate.grid(row=2, column=1)

        tk.Label(self.create_account_frame, text="Set a PIN Code:").grid(row=3, column=0)
        self.entry_pin = tk.Entry(self.create_account_frame, show='*')
        self.entry_pin.grid(row=3, column=1)

        self.btn_create = tk.Button(self.create_account_frame, text="Create Account", command=self.create_account)
        self.btn_create.grid(row=4, columnspan=2)

        self.btn_back = tk.Button(self.create_account_frame, text="Back", command=self.show_main_menu)
        self.btn_back.grid(row=5, columnspan=2)

    def show_access_account_frame(self):
        self.hide_all_frames()
        self.access_account_frame = tk.Frame(self)
        self.access_account_frame.pack(pady=20)

        tk.Label(self.access_account_frame, text="Account Holder's Name:").grid(row=0, column=0)
        self.entry_access_name = tk.Entry(self.access_account_frame)
        self.entry_access_name.grid(row=0, column=1)

        tk.Label(self.access_account_frame, text="Enter PIN Code:").grid(row=1, column=0)
        self.entry_access_pin = tk.Entry(self.access_account_frame, show='*')
        self.entry_access_pin.grid(row=1, column=1)

        self.btn_access = tk.Button(self.access_account_frame, text="Access Account", command=self.access_account)
        self.btn_access.grid(row=2, columnspan=2)

        self.btn_back_access = tk.Button(self.access_account_frame, text="Back", command=self.show_main_menu)
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
            if name and initial_balance >= 0 and interest_rate >= 0 and pin_code:
                self.bank.create_account(name, initial_balance, interest_rate, pin_code)
                messagebox.showinfo("Success", f"Account '{name}' created successfully!")
                self.show_main_menu()
            else:
                messagebox.showerror("Error", "Please fill in all fields with valid data.")
        except ValueError:
            messagebox.showerror("Error", "Invalid input for balance or interest rate.")

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
        self.account_frame = tk.Frame(self)
        self.account_frame.pack(pady=20)

        tk.Label(self.account_frame, text=f"Welcome, {self.current_account.name}!").pack()

        tk.Button(self.account_frame, text="Check Balance", command=self.check_balance).pack(pady=5)
        tk.Button(self.account_frame, text="Deposit Money", command=self.deposit_money).pack(pady=5)
        tk.Button(self.account_frame, text="Withdraw Money", command=self.withdraw_money).pack(pady=5)
        tk.Button(self.account_frame, text="Transaction History", command=self.show_transaction_history).pack(pady=5)
        tk.Button(self.account_frame, text="Transfer Money", command=self.show_transfer_frame).pack(pady=5)
        tk.Button(self.account_frame, text="Account Details", command=self.show_account_details).pack(pady=5)
        tk.Button(self.account_frame, text="Logout", command=self.show_main_menu).pack(pady=5)

    def check_balance(self):
        balance = self.current_account.check_balance()
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
        self.transfer_frame = tk.Frame(self)
        self.transfer_frame.pack(pady=20)

        tk.Label(self.transfer_frame, text="Transfer Money").pack(pady=10)

        tk.Label(self.transfer_frame, text="Destination Account:").pack(pady=5)
        self.entry_transfer_destination = tk.Entry(self.transfer_frame)
        self.entry_transfer_destination.pack(pady=5)

        tk.Label(self.transfer_frame, text="Amount:").pack(pady=5)
        self.entry_transfer_amount = tk.Entry(self.transfer_frame)
        self.entry_transfer_amount.pack(pady=5)

        self.btn_transfer = tk.Button(self.transfer_frame, text="Transfer", command=self.transfer_money)
        self.btn_transfer.pack(pady=10)

        self.btn_back_transfer = tk.Button(self.transfer_frame, text="Back", command=self.show_account_menu)
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
