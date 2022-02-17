str = '3 9 4 3'

s = str.split(' ')

n = len(s)

k = 0

for i in range(0,n):
    if s[i] != s[n-(i+1)]:

        ## Max count increament

        k += 1

        ## Elem swap

        if s[i] > s[n-(i+1)]:
            s[n-(i+1)] = s[i]

        else:
            s[i] = s[n-(i+1)]


print(''.join(s))
    
