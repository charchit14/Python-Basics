# WAP to print sum of first n natural numbers using recursion

# Using recursion
# def s(n):
#         if n==0:
#             return 0
#         else:
#             return n + s(n-1)
    
# a = int(input("Enter a number: "))
# b=s(a)
# print("The sum is: ", b)

# Using function
def s(n):
    if n==0:
        return 0
    else:    
        total = 0
        for i in range (1, n+1):
            total = total + i
    return total

    
a = int(input("Enter a number: "))
b=s(a)
print("The sum is: ", b)
