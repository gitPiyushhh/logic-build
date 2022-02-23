## 1. New String creation

from itertools import count


def create_string(s, n):
    str = s
    l = len(s)
    times =int(n / l)
    times_rem =int(n % l)

    for i in range(0, times-1):
        str += s
        times += 1

    print(times_rem)
    

    while times_rem:
        str += s[0]
        times_rem -= 1
    
    return str

## 2. Counting the number of a's 
    
def count_a(s, n):
    str = create_string(s, n)
    print(str)
    count = 0
    for i in str:
        if i == 'a': count += 1
    return count

s = 'aba'
n = 10

print(count_a(s, n))