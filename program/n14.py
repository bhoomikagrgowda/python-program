num=4
sp=0
for line in range((num*2),1,-2):
    for space in range(sp):
        print(' ',end='')
    for value in range(1,line):
        print(value,end='')
    print()
    sp=sp+1
