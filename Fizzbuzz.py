# -*- coding: utf-8 -*-
"""
Spyder Editor
This is a temporary script file."""

#import array as arr

import random

numbers = []

#print(random.randint(3, 9))
n = int(input("vvedite razmer massiva: "))
summ = 0
ssatr=0
satr=int(input("Input column number "))
for i in range(n):
    r = []
    for j in range(n):
        r.append(random.randint(1,9))
       
        if i == j: 
            summ += r[j]
        if j==satr:
           ssatr+=r[j]
           
        
    numbers.append(r)

for i in range(n):
    for j in range(n):
        print(numbers[i][j], end='\t')
    print('') 
    
print('-------------------')

print("summai diagonal: " + str(summ))
test1 = numbers[1][2]+numbers[2][0]

print("summai satri " + str(satr) + " barobar ast ba " + str(ssatr))


#print(test1)














