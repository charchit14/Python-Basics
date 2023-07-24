#WAP to print a multiplication table in reverse order using 'for' loop

n=int(input("Enter a number: "))

for i in range (10,0,-1):
    print(f"{n} * {i} = {n*i}")