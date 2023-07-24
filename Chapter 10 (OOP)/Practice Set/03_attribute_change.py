'''Create a class attribute 'ca' and create a object from it.
Now, set 'ca' directly using 'object.ca = 0'
Check whether the class attribute is changed or not'''

class check:
    ca = 22

myObj = check()
myObj.ca = 0

print(f"Value of Object: {myObj.ca}")
print(f"Value of Class: {check.ca}")

#Hence it does not change the class attribure

print()

#To change the class attribute
# check.ca = 0
# print(f"Value of Object: {myObj.ca}")
# print(f"Value of Class: {check.ca}")