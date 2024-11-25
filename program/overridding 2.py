class Bank_v1():
    bank_name='sbi'
    bank_ifsc=1123
    bank_branch='bangaole'
    def __init__(self,cn,ca,acc,cbal):
        self.cname=cn
        self.cage=ca
        self.caccount=acc
        self.cbalance=cbal
    @classmethod
    def display_bank_detailes(cls):
        print(f'name of the bank is{cls.bank_name}')
        print(f'ifsc of the bank is {cls.bank_ifsc}')
        print(f'branch of the bank is {cls.bank_branch}')
              

    def customer_details(self):
        print(f'name of the customer {self.cname}')
        print(f'age of the customer {self.cage}')
        print(f'account of the customer {self.caccount}')
        print(f'bal of the customer {self.cbalance}')

    @staticmethod
    def get_int_values():
        amt=int(input("enter the value"))
        return amt
    
    def withdraw(self):
        amt=self.get_int_values()
        if amt>self.cbalance:
            print('so sorry urs balance is low')
        else:
            self.cbalance-=amt
            print('withdraw is sucessfull balance is',self.cbal)
    def deposite(self):
        amt=self.get_int_value()
        self.cbal+=amt
        print('money deposited sucessfull')


class Bank_v2(Bank_v1):
    bank_branch='Hyderbada'

    @staticmethod
    def get_str_values():
        sv=input('enter the str value')
        return sv
    @classmethod
    def change_branch(cls):
        nb.get_str_values()
        cls.branch=nb
        print('brnach is changed sucessfull')
        
shiva=Bank_v1('shiva',22,1234323,9099)
shiva.withdraw()
shiva.display_bank_detailes()

    
