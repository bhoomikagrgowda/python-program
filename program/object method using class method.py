class Bank:
    bank_detailes='sbi'
    bank_branch='kizikistha'
    bank_ifsc=12345
    def __init__(self,na,age,bal):
         self.cname=na
         self.cage=age
         self.cbal=bal
    def customer_detailes(self):
        print(f'name of the customer is{self.cname}')
        print(f'AGE of the customer is{self.cage}')
        print(f'balance of the customer is{self.cbal}')
    def withdraw(self):
        amount=int(input('enter the amount'))
        if self.bal>=amount:
            self.bal-=amount
            print('amount withdraw is a sucessfull')
            print(f'balance is self{self.bal}')
        else:
            print('insufficent balanced')

    def deposite(self):
        amount=int(input('enter deposite amount'))
        if amount>0:
            self.bal+=amount
            print('deposite is sucessfull')
        else:
            print('please enter the amount')        
         
girish=Bank('girsh',12343,3566)
madesha=Bank('madana gowda',12343,3566)

girish.withdraw()
madesha.deposite()

