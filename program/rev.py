num = 1234
rev = 0
while num != 0:
    ld = num % 10  # Extract the last digit
    rev = rev * 10 + ld  # Append the last digit to the reversed number
    num //= 10  # Remove the last digit from num
print(rev)
