class Account:
    def __init__(self,amount,accno):
        self.amount = amount
        self.acc = accno

    def credit(self, amount):
            self.amount += self.acc
            print(amount,"was debited")
            print(self.currbal() )
    def currbal(self):
         return self.amount
         print(amount,"is now current bal")

    def debit(self, amount):
              self.amount -= self.acc
              print(amount, "was debited")
              print(self.currbal())


User1 = Account(10000,12345)
User1.credit(500)
User1.debit(100)
