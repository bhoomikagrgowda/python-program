class Car:
    def __init__(self,cn,cm,cc):
        self.cname=cn
        self.cmodel=cm
        self.ccolour=cc
        
    def diplay_Car(self):
        print('car name is',self.cname)
        print('model name is',self.cmodel)
        print('colour name is',self.ccolour)
        
class Engine:
    def __init__(self,en,em):
        self.ename=en
        self.emodel=em
        cn=input('car name is')
        cm=input('model name is')
        cc=input('colour name is')
        
        abc=Car(cn,cm,cc)
        self.carengine=abc
    def diplay_Engine(self):
        print('engine name is',self.ename)
        print('engine model is',self.emodel)
        self.carengine.display_Car()


xyz=Engine('xyz',34)
xyz.display_Engine()
