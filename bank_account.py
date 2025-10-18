
class BankAccount:

    # constructor
    def __init__(self, account_holder:str, initial_balance = 0):
        self.account_holder = account_holder
        self.__balance = initial_balance  # privet 

    # Getter 
    def get_balance(self):
        return f"Your current balance is: {self.__balance}"
    
    # Setter 
    def set_balance(self, new_balance:float):
        if new_balance < 0:
            print("Deposit must be positive")

        else:
            self.__balance = new_balance

    
    def get_account_holder(self):
        return f"The name of the account holder: {self.account_holder}"
    
    def deposit(self, amount:float):
        self.__balance += amount
        return f"The amount has been deposited is {amount} and your current balance is {self.__balance}"
    
    def dragging(self, amount:float):
        if self.__balance >= amount:
            self.__balance -= amount
            return f"An amount has been withdrawn is {amount} from your account and your current balance is {self.__balance}"
        else:
            raise InsufficientFundsError(f"Insufficient Funds: balance is {self.__balance}, tried to withdraw {amount}")
        
class InsufficientFundsError(Exception):
    pass