#Showing the inheritance method (This is a type of single inheritance, child class inherits from a single parent class)

#This is a parent class
class Employee:
    company = "Netflix"
    def Details(self):
        print("Employee at Netflix")

#This is a child/inherited class (from parent class - Employee) 
class Programmer (Employee):
    company = "Google"
    role = "DevOps"
    def Role(self):
        print(f"A {self.role} Engineer")
    def Details(self):
        print("Child employee at Netflix")


#Of Parent class
p = Employee()
p.Details()
print(p.company)

#Of Child class
c = Programmer()
print(c.role)

print()

#Now, showing the use of inheritance, this will run from parent class
c.Details()
print(c.company)

#This will run from child class as it is already present in child class (This is overriding)
c.Details()
print(c.company)