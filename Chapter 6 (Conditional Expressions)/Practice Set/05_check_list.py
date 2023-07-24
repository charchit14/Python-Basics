#WAP which finds out whether a given name is present in a list or not

l =["eddy", "kyle", "ruben", "ake"]

a=input("Enter the name you want to check: ")

if(a in l):
    print("The name is present in the list")
else:
    print("The name is not present in the list")