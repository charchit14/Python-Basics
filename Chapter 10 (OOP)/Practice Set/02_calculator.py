#Create a class calculator to calculate square, cube, and square root of a number

class Calculator:
  
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


#Solving without 'self'
# class Calculator:

#     @staticmethod
#     def sqr(num):
#         return num ** 2
    
#     @staticmethod
#     def cube(num):
#         return num ** 3
    
#     @staticmethod
#     def root(num):
#         return num ** (1/2)

# cal = Calculator()
# n = float(input("Enter a number: "))

# s = cal.sqr(n)
# c = cal.cube(n)
# sr = cal.root(n)

# print(f"Square is: {s}\nCube is: {c}\nSquare root is: {sr}")