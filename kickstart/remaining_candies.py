from array import *


test_cases = int(input('Enter the test cases: '))
m = int(input('Enter the no. of bags: '))
n = int(input('Enter the no. of students: '))

arr = array('i', [])

for i in range(m):
    x = int(input('Enter the candies for {} bag: '.format(i+1)))
    arr.append(x)


total_candy = 0
candy_left = 0

## 1. Total candies
for i in arr:
    total_candy += i

## 2. Remaining candies are answer
candy_left = total_candy % n
print('Case #{}: {}'.format(test_cases, candy_left))