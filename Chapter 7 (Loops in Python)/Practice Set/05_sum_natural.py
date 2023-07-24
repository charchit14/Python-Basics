#WAP to find sum of first n natural numbers using 'while' loop

n=int(input("Enter a number: "))
sum = 0
i=1
while i<=n:
    sum = sum + i
    i=i+1
print("The sum till", n, "is: ", sum)