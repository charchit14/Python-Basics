#WAP to create a multiplication table of a given number using 'while'

a=int(input("Enter a number to generate multiplication table: "))
i=1
while (i<=10):
    print(f"{a} * {i} = {a*i}")
    i=i+1