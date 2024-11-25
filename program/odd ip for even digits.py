#WAP FIND SUM OF ODD INDEX POSITION OF EVEN DIGITS                            
num = input()# Input number as a string
sum = 0# Initialize sum to 0
for ip in range(len(num)):# Loop through each index and digit
    digit = int(num[ip])
    if ip % 2 != 0:
        if digit % 2 == 0: # Check if the index is odd and the digit is even
          sum += digit
print("The sum of even digits at odd index positions is:", sum)
