num=5
for line in range(num):
    for col in range(line):
        print(' ',end='')
    for int in range(num-line):
        print(line+1,end='')
    print()
