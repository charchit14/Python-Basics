#WAP to check whether a string is palindrome or not
#Eg: racecar is palindrome, dad is palindrome

a = input("Enter a string: ")

if (a[:] == a[::-1]):
    print("It is a palindrome")
else:
    print("It is not a palindrome")