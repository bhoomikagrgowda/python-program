num=6
fact=0
for dem in range(1,num+1):
    if num % dem ==0:
        fact = fact+dem
if fact == num:
     print("perfect number")
else:
     print("not perfect number")
          
