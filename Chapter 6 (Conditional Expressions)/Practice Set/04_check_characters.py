#WAP to find whether a given username contains less than 10 characters or not

a=input("Enter a username: ")
v = len(a)
if(v<10):
    print("It has less than ten characters")
else:
    print("It has more than ten characters")