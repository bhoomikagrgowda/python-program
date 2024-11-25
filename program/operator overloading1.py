class Book:
    def __init__(self,n,au,p):
        self.bname=n
        self.bauthor=au
        self.bprize=p
    def __str__(self):
        return self.bname
    def __add__(self,second):
        return self.bprize+second.bprize
    def __sub__(self,second):
        return self.bprize-second.bprize
    def __mul__(self,intvalue):
        return self.bprize*intvalue
    def __truediv__(self,intvalue):
        return self.bprize/intvalue

    
python=Book('python','van gudio',10000)
django=Book('django','hashad',20000)

print(python+django)
print(python-django)
print(python * 3)
print(python / 2)



