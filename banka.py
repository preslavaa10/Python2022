class Account:
    def __init__(self,owner,balance=0):
        self.owner = owner
        self.balance = balance
        
    def __str__(self):
        return f'Account owner:   {self.owner}\nAccount balance: ${self.balance}'
        
    def deposit(self,dep_amt):
        self.balance += dep_amt
        print('Deposit Accepted')
        
    def withdraw(self,wd_amt):
        if self.balance >= wd_amt:
            self.balance -= wd_amt
            print('Withdrawal Accepted')
        else:
            print('Funds Unavailable!')

acct1 = Account('Preslava',100)
#Vsichko koeto moje da se testva po akaunta

#print(acct1)
#acct1.owner
#acct1.balance
#acct1.deposit(50)
#acct1.withdraw(75)
#acct1.withdraw(500)




