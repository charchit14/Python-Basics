#A program to calculate factorial using function and recursion

#Firstly, factorial using a function

# def factorial(n):
#     f=1 
#     for i in range (1,n+1):
#         f = f * i
#     return f


# b=int(input("Enter a number: "))
# a= factorial(b)
# print("The factorial is: ", a)

#Now, factorial using reursion
#Recursion is used to directly call a mathematical formula using a function
#We know, n! = n * (n-1)!

def factorial(n):
    if n==0:
        return 1
    else:
        return n * factorial (n-1)

b=int(input("Enter a number: "))
a= factorial(b)
print("The factorial is: ", a)

'''This works as follows:
say, we input 4 then,
 4 * factorial (3)      --> since it does not know what factorial of 3 is so:
 4 * (3 * factorial(2))
 4 * 3 * (2 * factorial(1)) 
 4 * 3 * 2 * (1 * factorial (0))    --> now since it knows factorial(0) is 1 as definded by us in if statement. so,
 we get, 4 * 3 * 2 *1'''