'''Create a class'Employee' and add 'salary' and 'increment' properties  to it.
Write a method 'SalaryAfterIncrement' with a '@property decorator' with a 'setter'
that changes the value of increment based on salary'''

class Employee:
    salary = 500
    increment = 200

    @property
    def SalaryAfterIncrement(self):
        return self.salary + self.increment
    
    @SalaryAfterIncrement.setter
    def SalaryAfterIncrement(self, value):
        self.increment = value - self.salary

a = Employee()

print(f"The initial salary is: {a.salary}")
print(f"The initial increment is: {a.increment}")
print(f"The initial total is: {a.SalaryAfterIncrement}")

print()

a.SalaryAfterIncrement = 900

print(f"The salary after increment is: {a.SalaryAfterIncrement}")
print(f"The salary was: {a.salary}")
print(f"So, the increment was: {a.increment}")