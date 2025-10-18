
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
        '''this method returns the name of the account holder.'''

        return f"The name of the account holder: {self.account_holder}"
    
    def deposit(self, amount:float):
        '''
        this method accepts an amount and adds it to the account balance, 
        and then returns the amount has been deposited & updated balance.
        '''
        self.__balance += amount
        return f"The amount has been deposited is {amount} and your current balance is {self.__balance}"
    
    def withdraw(self, amount:float):
        '''
        this method accepts an amount and subtracts it from the account balance, 
        returning an amountthe that subtracted & the updated balance, 
        but it this only happens when if there are sufficient funds in the account.
        If there are insufficient funds, it will raise an exception and leave the balance unchanged
        '''
        if self.__balance >= amount:
            self.__balance -= amount
            return f"An amount has been withdrawn is {amount} from your account and your current balance is {self.__balance}"
        else:
            raise InsufficientFundsError(f"Insufficient Funds: balance is {self.__balance}, tried to withdraw {amount}")

# This class inherits from the built-in Exception class        
class InsufficientFundsError(Exception):
    pass