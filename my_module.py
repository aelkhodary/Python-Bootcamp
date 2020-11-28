def my_func():
    print("Hey I am in my_module.py")

#*********** Challenge Solution *************/
class Account():

    def __init__(self,owner,balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self,dep_amt):
        self.balance += dep_amt
        print(f"Added {dep_amt} to the balance")

    def withdrawal(self,wd_amt):
        if self.balance >= wd_amt:
            self.balance -= wd_amt
            print('withdrawal accepted')
        else:
            print('Sorry No balance in your account')

    def __str__(self):
       return f"Owner : {self.owner} \nBalance: {self.balance}"
