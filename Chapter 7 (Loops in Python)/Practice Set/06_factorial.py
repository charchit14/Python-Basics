#WAP to calculate factorial using 'for' loop

n = int(input("Enter a number: "))
fact=1

for i in range (1,n+1):
    fact = i*fact

print("The factorial of", n, "is: ", fact)