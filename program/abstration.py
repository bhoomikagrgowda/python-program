from abc import ABC,abstractmethod
class malathi(ABC):
    
    @abstractmethod
    def breakfast(self):
        pass
    @abstractmethod
    def lunch(self):
        pass
    def dinner(self):
        pass

class bhoomi(malathi):
    
    def breakfast(self):
        print('dosa and one coffee')
    
    def lunch(self):
        print('chiken briyani')
        
    def dinner(self):
        print('curd rice')
m=bhoomi()
m.breakfast()
m.dinner()
class banu(malathi):
    
    def breakfast(self):
        print('rice bath and one coffee')
    
    def lunch(self):
        print('chiken briyani')
        
    def dinner(self):
        print('curd rice')

r=banu()
r.breakfast()
