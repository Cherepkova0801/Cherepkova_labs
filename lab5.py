class BankAccount:
    def __init__(self, account_id, owner_name, balance=0.0):
        self.__account_id = account_id
        self.__owner_name = owner_name
        self.__balance = balance

    @property
    def account_id(self):
        return self.__account_id
    
    @account_id.setter
    def account_id(self, a):
        self.__account_id = a

   
    @property
    def owner_name(self):
        return self.__owner_name

    @owner_name.setter
    def owner_name(self, name):
        self.__owner_name = name
        
    @property
    def balance(self):
        return self.__balance
            
    @balance.setter
    def balance(self, b):
        self.__balance = b
    def deposit(self, amount):
        self.__balance += amount
        print(f"You have successfully topped up your balance by {ammount}")

    def withdraw(self, ammount):
        if amount <= self.__balance:
            self.__balance -= amount
            print(f"You have successfully withdrawn {ammount} \nYour balance: {self.__balance}")
        else:
            print("Insufficient funds.")
    def show_account(self):
        print(f"Account ID: {self.__account_id}, Owner: {self.__owner_name}, Balance: ${self.__balance}")
class Bank:
    def __init__(self):
        self.__accounts = []
    @property
    def accounts(self):
        return self.__accounts
    
    def add_account(self, account):
        self.__accounts.append(account)
   
    def remove_account(self, account_id):
        for account in self.__accounts:
            if account.getAccountId() == account_id:
                self.__accounts.remove(account)
                print(f"Account with ID {account_id} removed.")
                return
        print(f"Account with ID {account_id} not found.")
        return False

    def sort_accounts_by_balance(self):
        self.__accounts.sort(key=lambda x: x.getBalance())

    def show_all_accounts(self):
        for account in self.__accounts:
            account.show_account()

def main():
    account1 = BankAccount(1, "John Doe", 1000.0)
    account2 = BankAccount(2, "Jane Doe", 2000.0)
    account3 = BankAccount(3, "Bob Smith", 1500.0)

    bank = Bank()
    bank.add_account(account1)
    bank.add_account(account2)
    bank.add_account(account3)

    print()
    print()
    print("Accounts before sorting:")
    bank.show_all_accounts()

    print()
    account1.deposit(500.0)
    account2.deposit(1000.0)

    bank.sort_accounts_by_balance()

    print("\nAccounts after sorting:")
    bank.show_all_accounts()

    print()
    account1.deposit(500.0)
    account2.deposit(1000.0)

    bank.sort_accounts_by_balance()

    print("\nAccounts after sorting:")
    bank.show_all_accounts()

    bank.remove_account(2)

    print("\nAccounts after removing account with ID 2:")
    bank.show_all_accounts()

if__name__ == '__main__':
    main()
    

    


    
