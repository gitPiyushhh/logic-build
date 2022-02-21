def check_reverse_sorted(arr, s, e):
    for i in range(e, s, -1):
        if arr[i-1] > arr[i]:
            flag = True
        else:
            flag = False
    return flag

arr = [1,5,4,3,2,6]
rev_sorted = []
start_index = len(arr) - 1
end_index = 0

## Creating the rev sorted array
for i in range(1,len(arr)):
    rev_sorted.append(check_reverse_sorted(arr, i-1, i))

## 2. Loop over the rev sorted array {get the swap or reverse}
for i in range(1, len(rev_sorted)):
    if rev_sorted[i-1] == True and rev_sorted[i] == True:
        start_index = min(start_index, i-1)


print(start_index)