class A:
    def __init__(self,a):
        print("__init__ of a")
    def __init__(self,a=10):
        self.a=a
ob=A(a=10)
print(ob.__dict__)
print(A.__dict__)
