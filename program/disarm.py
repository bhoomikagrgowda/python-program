num=135
copy=num
res=0
power=len(str(num))
while(num!=0):
    dig=num%10
    res=res+(dig)**power
    power=power-1
    num//=10
if copy==res:
    print("disarm")
else:
    print("not disarm")

   
