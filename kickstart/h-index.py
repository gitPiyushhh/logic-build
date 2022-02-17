from array import *

def get_score(arr):
    h_arr = array('i', [])
    max_citi = 0
    count = 0
    for i in range(len(arr)):
        ## 1. Storing as max
        if arr[i] > max_citi:
            max_citi = arr[i]
        
        j = i - 1

        ## 2. CHeck for the number if ny previous element matched to it

        while j>=0:
    
            ## If any no. matches, count++
            
            if arr[j] == max_citi:
                count += 1
            j -= 1
        ## 3. Add count to the new array
        h_arr.append(count)
    return list(h_arr)

print(get_score([1, 3, 3, 2, 2, 15]))