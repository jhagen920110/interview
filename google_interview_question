#Prompt: compare the adjacent integer, find the average (round up), and replace. Do it for each adjacent integer to find which pair would result in largest
#For ex) 1234, (1+2)/2 = 2 (round up from 1.5), resulting 234
#              (2+3)/2 = 3, resulting in 134
#              (3+4)/2 = 4, resulting in 124
#              Largest is 234

import math

num = 623315 # test case
num = [int(x) for x in str(num)] # convert int to list of single digits ([6,2,3,3,1,5])
largest = 0

def listToInt(numbers):
    return int(''.join([ "%d"%x for x in numbers])) # convert list of single digits to one integer (from [6,2,3,3,1,5] to 623315)

def compareNums(prev, next): # compare which number is the largest number
    if(prev > next):
        return prev
    else:
        return next

for x in range(len(num)-1):
    temp = list(num) # clone original number (in list form)
    y = math.ceil((num[x] + num[x+1])/2) # find the average and round up
    temp[x] = y # replace the number using index
    temp.pop(x+1) # pop the digit next to index
    current = listToInt(temp) 
    largest = compareNums(largest, current)

print(largest)
