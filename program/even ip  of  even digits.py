#WAP FIND SUM OF EVEN IP OF EVEN DIGITS
num = input("Enter a number: ")
sum = 0
for ip in range(len(num)):
    digit = int(num[ip])
    if ip % 2 == 0 :
        if digit % 2 == 0:
            sum += digit
print("Sum of even digits at even index positions:",sum)
#1st iteration
num=2314
sum=0
ip=0
digit=int(2)
0%2=0 becomes true then 0%2==0
so (sum=0+2)the value of sum=2
#2st iteration
num=2314
sum=2
ip=1
digit=int(3)
1%2=0 becomes false then 1%2==0 so again sum value not change
so (sum=0+2)the value of sum=2
#3st iteration
num=2314
sum=2
ip=2
digit=int(1)
2%2=0 becomes true then 2%2==0
so (sum=2+1)the value of sum=3
#2st iteration
num=2314
sum=3
ip=3
digit=int(4)
3%2=0 becomes true then 3%2==0
so (sum=3)the value of sum=3
