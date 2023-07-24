#WAP to create the following star pattern
'''       *
         ***
        *****'''

for i in range (1,4):
    spaces = " " * (3-i)
    stars = "*" * (2*i-1)   # here, (2i-1) creates odd number of stars which is needed in these sort of patterns
    print(spaces + stars)