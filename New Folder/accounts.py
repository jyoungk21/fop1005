class BankAccount():
    """
       Class doc string
    """
    interest_rate = 0.3
    
    def __init__(self, name, number, balance):
        """
          Init function
        """
        self.name = name
        self.number = number
        self.balance = balance
    
    def withdraw(self, amount):
        """
          Withdraw string
        """
        self.balance = self.balance - amount
    
    def deposit(self, amount):
        """
         Deposit string
         """
        self.balance = self.balance + amount
    
    def add_interest(self):
        #just a command
        """
          Interest function
        """
        self.balance += self.balance * self.interest_rate 

