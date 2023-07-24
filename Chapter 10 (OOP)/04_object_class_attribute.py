#Demonstraion of atrribute that is present in both class and object

class Employee:
    company = "Netflix"
    salary = 600

shark = Employee()
fakeshark = Employee()

print(shark.company)

shark.salary = 400  #This is the object's attribute

print(shark.salary) #This will print 400 because it checks object attribute first then class, if found none, throws error

print(fakeshark.salary) #This will print 600 because there is no attribute for fakeshark's salary