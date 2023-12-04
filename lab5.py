class BankAccount:
    def __init__(self , id_name , owner_name , balance):
        self.__id = id_name
        self.__owner_name = owner_name
        self.__balance = balance

    def get_id(self):
        return self.__id
    
    def get_owner_name(self):
        return self.__owner_name

    def get_balance(self):
        return self.__balance

    def deposite(self, amount):
        self.__balance += amount
        print("Ви поповнили рахунок на", amount)
    
    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print("Ви успішно зняли", amount)

        else:
            print("Недостатньо коштів")

    def show_account(self):
        print(f"Account ID:{self.__id_name}, Owner:{self.__owner_name}, Balance: ${self.__balance}")

class Bank:
    def __init__(self):
        self.accounts = []

    def get_accounts(self):
        return self.accounts
    
    def add_account(self, account):
        self.accounts.append(account)

    def remove_account(self, account_id):
        for account in self.accounts:
            if account.get_id()==account_id:
                self.accounts.remove(account)
                print(f"Account with ID {account_id}removed.")
                return
            
        print(f"Account with ID {account_id}not found.")
   
    def sort_accounts_by_balance(self):
        self.accounts.sort(key=lambda x: x.get_balance())
    
    def show_all_accounts(self):
        for account in self.accounts: 
            account.show_account()

def main():
    account1 = account_John_Doe(1, "John Doe", 1000.0)
    account2 = account_Jane_Doe(2, "Jane Doe", 2000.0)
    account3 = account_Bob_Smith(3, "Bob Smith", 1500.0)

    bank = Bank()
    bank.add_account(account_John_Doe)
    bank.add_account(account_Jane_Doe)
    bank.add_account(account_Bob_Smith)

    print()
    print()
    print("Accounts before sorting:")
    bank.show_all_accounts()

    print()
    account1.deposite(500.0)
    account2.withdraw(1000.0)

    bank.sort_accounts_by_balance()

    print("\nAccounts after sorting:")
    bank.show_all_accounts()

    bank.remove_account(2)
    
    print("\nAccounts after removing account with ID 2:")
    bank.show_all_accounts()

if __name__=='__main__':
    main()

    
