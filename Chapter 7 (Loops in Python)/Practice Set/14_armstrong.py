#WAP to detect an armstrong number
#Eg: 371 = 3^3 + 7^3 + 1^3 is an armstrong number, 1634 = 1^4 + 6^4 + 3^4 + 4^4 is an armstrong

a=input("Enter a number: ")
v=len(a)
sum=0

for i in a:
    sum = sum + int(i)**v

if (sum == int(a)):
    print("It is an armstrong number")
else:
    print("It is not an armstrong number")