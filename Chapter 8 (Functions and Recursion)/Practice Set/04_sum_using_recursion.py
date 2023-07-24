#WAP to print sum of first n natural numbers using recursion

def s(n):
        if n==0:
            return 0
        else:
            return n + s(n-1)
    
a = int(input("Enter a number: "))
b=s(a)
print("The sum is: ", b)