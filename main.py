from bank_account import BankAccount, InsufficientFundsError

def main():


        account1 = BankAccount("Maha Saud", 1000)
        account2 = BankAccount("Sara Saad")
        account3 = BankAccount("Yara")
        
        print(f"{account2.get_account_holder()}. {account2.get_balance()}")

        print(f"{account2.get_account_holder()}. {account2.deposit(100)}")

        print(account3.set_balance(-8))
        print(account3.set_balance(10))
        print(f"{account3.get_account_holder()}. {account3.get_balance()}")

        try:

            print(f"{account1.get_account_holder()}. {account1.dragging(100)}")

            print(f"{account2.get_account_holder()}. {account2.dragging(1000)}")

        except InsufficientFundsError as e:
            print(e)

if __name__ == "__main__":
    main()