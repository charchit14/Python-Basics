#Showing how a default arguement can be passed into a fucntion and using it

def greet(name="Ghost"):
    print("Hello!", name)

greet("Bhoot")

#greet() #throws error when no arguement is passed to function greet(name)
greet() #does not throw error when default arg. i.e. name=Ghost is passed to function

# n=input("Enter a name: ")
# greet(n)