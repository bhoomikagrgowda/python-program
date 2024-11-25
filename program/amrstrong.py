num=153
res=0
copy=num
pow=len(str(num))
while(num!=0):
    rem=num%10
    res=res+(rem)**pow
    num//=10
print(res,num,copy)
if copy==res:
    print("amrystrong")
else:
    print("not amrystrong")
    
    
    
