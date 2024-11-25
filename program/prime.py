num=19
for dem in range(2,num//2+1):
    if num%dem==0:
        print('not prime')
        break
    else:
        print('prime')
        
