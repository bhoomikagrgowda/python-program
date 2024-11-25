'''# using the Nested for loop
mainstring=input()
vow='aAeEiIoOuU'
c=0
for ele in mainstring.upper():
    for val in vow:
        if val==ele:
           c=c+1
print('the vowel contain in string is',c)

'''
#using the for loop
c=0
ms=input()
vowel='AEIOUaeiou'
for ele in ms:
    if ele in vowel:
        c+=1
print('the vowel contain in string is',c)

ms=banu
c=0
vowel='AEIOUaeiou'
#1st iteration
ms=b
vowel='AEIOUaeiou'
now we have to compare 'b' with elements present in vowel
it is not true so no increment will happened then value of c=0
#2st iteration
ms=a
vowel='AEIOUaeiou'
now we have to compare 'a' with elements present in vowel
it is  true so  increment will happened then value of c=1

#3st iteration
ms=n
vowel='AEIOUaeiou'
now we have to compare 'n' with elements present in vowel
it is not true so no increment will happened then value of c=1
#4st iteration
ms=u
vowel='AEIOUaeiou'
now we have to compare 'u' with elements present in vowel
it is  true so  increment will happened then value of c=2


