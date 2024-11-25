num=3
spa=num-1
for line in range(1,num*2,2):
    for sp in range(spa):
        print(' ',end=' ')
    for st in range(line):
        print('*',end=' ')
    print()
    spa=spa-1
