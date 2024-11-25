def singleton(arg):
    L=[]
    def inner():
        if not L:
            MCO=arg()
            L.append(MCO)
        return L[0]
    return inner
@ singleton
class Multiplex:
    def __init__(self):
        self.ticket=300
    def booking(self,nt):
        if nt<=self.ticket:
            self.ticket-=nt
            print('booking is sucess')
            print('remaing tickets are',self.ticket)
        else:
            print('booking is not sucess')
            print('remaing tickets are',self.ticket)
            
M1=Multiplex()
M2=Multiplex()
M1.booking(40)
print(M1)
M2.booking(90)
print(M2)
