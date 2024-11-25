#to print frequnency og each and every charter present in string(BY USING SET)
'''s=input()
c=0
for ele in set(s):
    print(ele,s.count(ele))

#to print frequnency og each and every charter present in string(BY USING DIC)
s=input()
d={}
for ele in s:
    d[ele]=s.count(ele)
print(d)
'''
#to print frequnency og each and every charter present in string(BY NOT USING BUILD IN METHOD)
s=input()
d={}
for ele in s:
    if ele in d:
        d[ele]=d[ele]+1
    else:
        d[ele]=d[ele]-1
        
     

