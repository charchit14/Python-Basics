#WAP to calculate factorial 

# Using 'for' loop
n = int(input("Enter a number: "))
fact=1
for i in range (1,n+1):
    fact = i*fact
print("The factorial of", n, "is: ", fact)


# Using 'while' loop
f=1
j=1
while j<=n:
    f = f*j
    j+=1
print(f)
