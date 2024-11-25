num=1000
num=222
space=num-1
for row in range((num*2)-1,0,-2):
    for sp in range(space):
        print('   ',end='')
    for col in range(row):
        print('*',end='')
    print()
    space=space+1
