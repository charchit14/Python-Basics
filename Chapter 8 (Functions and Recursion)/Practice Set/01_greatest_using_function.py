#WAP to find the greatest among three numbers using a function

def great(a, b, c):
    if a>=b and a>=c:
        return a
    elif b>=a and b>=c:
        return b
    else:
        return c
    

n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))
n3 = int(input("Enter third number: "))
         
gr = great(n1, n2, n3)
print('The greatest number is: ',gr)