class Engine:
    def __init__(self,en,em):
        self.ename=en
        self.emodel=em
    def Engine_work(self):
        print("perfomance of engine is good")

class Car:
    def __init__(self,cn,cmn,cc):
        self.carname=cn
        self.carmodel=cmn
        self.colour=cc
        en=input("enter the engine name")
        em=int(input("enter the model of engine"))

        CEO=Engine(en,em)
        self.cEngine=CEO

    def Car_perfomance(self):
        print("check the engine")
        self.cEngine.Engine_work()
        print("car is started")

e1=Car('BMW',2024,'WHITE')
e1.Car()
                
