def check_king(last_char):
    vowels = ['a', 'e', 'i', 'o', 'u']

    if last_char == 'y':
        print('Ruled by nobody')
    elif last_char in vowels:
        print('Ruled by Alice')
    else:
        print('Ruled by Bob')


name = input("Enter the name: ").lower()

last_char = name[-1]

check_king(last_char)