#This program demonstrates the 'attribute' of a class

class Employee:
# This (line 5) is the attribute of the class not the object so whenever this is called it means the employee are of Netflix
# And applies to all the objects of this class
    company = "Netflix" 

shark = Employee()
fakeshark = Employee()

print(shark.company)
print(fakeshark.company)

Employee.company = "Google" #Changing the attribute of the class

print(shark.company)