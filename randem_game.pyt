
import random

from unittest import result
print('**guess my number**:')
print('you need to guess the number')
print('number is a range 1-12')
MAGIC_NUMBER=random.randint(1,12)
count=0
user=0
while user!=MAGIC_NUMBER:
    user=int(input('enter your choice:'))
    count+=1
    if user<1 or user>12:
        print('number is greater than yours')
    elif MAGIC_NUMBER>user:
        print('number is greater than yours')
    elif MAGIC_NUMBER<user:
        print('number is less than yours')
    if MAGIC_NUMBER==user:
        print('victory!!!)))')
        user2=int(input('if you want play again write 1 ,if you dont want write 2:'))
        if user2==1:
            MAGIC_NUMBER=random.randint(1,12)
            continue
        else:
         print('GAME OVER!(((')
         break
        

    
    

# L2=list(range(1,10))
# print(L2)
# L3=list('Hello')
# print(L3)
# from tkinter import N


# L1=[2.1,1,'cool','hello']
# print("1 element:",L1[0])
# print("2 element:",L1[1])
# print("3 element:",L1[2])
# a=10
# b=a+L1[0]
# print(b)
# d=L1[3]+"world"
# print(d)
