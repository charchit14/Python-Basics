#Create a class Programmer to store information of two programmers working at Microsoft

class Programmer:
    company = "Microsoft"
    role = "DevOps"

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    
    def PrintData(self):
        print(f"Information of {self.name}: Company = {self.company}, Salary = {self.salary}, and Role = {self.role} ")

p1 = Programmer("Phil", 400)
p2 = Programmer("Ronnie", 600)

p1.role = "S/W Eng."

p1.PrintData()
p2.PrintData()