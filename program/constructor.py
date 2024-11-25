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
           
                 
