
#Abstraction
#Hiding the implementation details of class and only showing the essentials features to the user

#Encapsulation
#wrapping data and function into a single unit

class Account:

    def __init__(self,bal, accnt):
        self.bal = bal
        self.accnt= accnt

    def get_debit(self,debit):
        self.bal -= debit
        print("Money is debited",debit,"/-")
        print("Available balance after debit=",self.get_balnce(),"/-")

    def get_credit(self,credit):
        self.bal += credit
        print("Money is credited",credit,"/-")
        print("Available balance after credit= ",self.get_balnce(),"/-")

    def get_balnce(self):
        return self.bal
    
Ac = Account(25000,30004567) 
Ac.get_debit(5000)
Ac.get_credit(3000)
Ac.get_credit(5000)

#Ac.get_balnce()

