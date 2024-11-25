num=19
for dem in range(2,int(num**(0.5)+1)):
                 if num%dem==0:
                       print('not prime')
                       break
                 else:
                    print('prime')
