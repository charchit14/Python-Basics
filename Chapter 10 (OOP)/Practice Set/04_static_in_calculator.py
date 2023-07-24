#Add static method in Problem-2 to greet user 'Hello'

class Calculator:
    
    @staticmethod
    def __init__():
        print("\t\t\t\tHello! Welcome to the calulator")
    
    def sqr(self, num):
        self.num = num
        return self.num ** 2
    
    def cube(self, num):
        self.num = num
        return self.num ** 3
    
    def root(self, num):
        self.num = num
        return self.num ** (1/2)

cal = Calculator()

n = float(input("Enter a number: "))

s = cal.sqr(n)
c = cal.cube(n)
sr = cal.root(n)

print(f"Square is: {s}\nCube is: {c}\nSquare root is: {sr}")