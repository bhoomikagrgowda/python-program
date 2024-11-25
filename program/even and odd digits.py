#WAP FIND SUM OF EVEN IP OF EVEN DIGITS
num = input("Enter a number: ")
sum = 0
for i in range(len(num)):
    digit = int(num[i])
    if i % 2 == 0 :
        if digit % 2 == 0:
            sum += digit
print("Sum of even digits at even index positions:",sum)

