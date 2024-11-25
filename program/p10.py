num=5
star=1
space=num//2
for line in range(num):
    for sp in range(space):
        print(' ',end='')
    for st in range(star):
        print('*',end='')
    print()
    if(line<num/2):
        space=space+1
        star=star+1
    else:
        space=space-1
        star=star-1
        
    
