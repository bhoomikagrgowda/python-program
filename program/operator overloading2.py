class rectangle:
    def __init__(self,l,br):
        self.lenght=l
        self.breath=br
        self.area=l*br

    def __gt__(self,second):#speial method for greater than
        if self.area>second.area:#compare the both objects area
            return True
        else:
            return False
R1=rectangle(400,200)
R2=rectangle(200,300)
print(R1>R2)
