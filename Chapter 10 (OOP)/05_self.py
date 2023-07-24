#Use of 'self'

#Demonstration 1
class Players:
    club = "City"
    def wage(self):
        print("Wage is 450k")

Foden = Players()
Foden.wage()

''' Here wage is getting one arguement i.e. 'Foden'. So, if we remove 'self' then it still will be getting one arguemet
But for that there will be no given arguement in function 'wage'
Because line-9 gets converted to this line-14. i.e. both are same '''  
Players.wage(Foden)

print()

#Demonstration - 2
class Employee:
    company = "YouTube"
    def getSalary(self):
        print(f"Salary of ID #{self.ID} working in {self.company} is {self.salary}")
shark = Employee()
shark.ID = 1
shark.salary = 900
shark.getSalary()