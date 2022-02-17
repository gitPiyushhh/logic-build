from itertools import count


arr = [1, 5, 3, 4, 2]

count = 0
k = 2
n = len(arr)

## Sort array
arr.sort()

## Double pointer approach
for i in range(0, n):
    for j in range(i+1, n):
        if arr[j] - arr[i] == k:
            count += 1 


print (count)