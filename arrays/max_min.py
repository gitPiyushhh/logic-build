def elem_select(arr, k):
    arr.sort()
    part = slice(k)
    return (arr[part])

def unfairness_calc(arr, k):

    if k > 2 and k < len(arr):   
        arr_sub = elem_select(arr, k)
        unfair = max(arr_sub) - min(arr_sub)
        print( unfair )
    
    else:
        print(0)

## TC0: 
# arr = [1, 4, 7, 5]
# k = 2


## TC1:
arr = [1, 2, 3, 4, 10, 20, 30, 40, 100, 200]
k = 11

## TC2:
arr = [10, 100, 200, 300, 1000, 20, 30 ]
k = 8

unfairness_calc(arr, k)