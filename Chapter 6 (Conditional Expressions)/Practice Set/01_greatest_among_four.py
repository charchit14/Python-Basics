#WAP to find the greatest of four numbers entered by user

a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
c=int(input("Enter third number: "))
d=int(input("Enter fourth number: "))

#method 1
if(a>b):
    g1=a
else:
    g1=b

if(c>d):
    g2=c
else:
    g2=d

if(g1>g2):
    print("The greatest is: ",g1)
else:
    print("The greatest is: ",g2)


#method 2
# if(a==b==c==d):
#     print("All the numbers are equal")
# elif(a>=b and a>=c and a>=d):
#     print("The greatest number is: ",a)
# elif(b>=a and b>=c and b>=d):
#     print("The greatest number is: ",b)
# elif(c>=a and c>=b and c>=d):
#     print("The greatest number is: ",c)
# elif(d>=a and d>=b and d>=c):
#     print("The greatest number is: ",d)
# else:
#     print("Try Again")