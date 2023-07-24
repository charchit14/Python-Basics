#An example of operator overloading
'''Operator Overloading helps us make our object to behave like built-in operators.
To implement this we use 'dunder method' i.e. __ (using double underscore)
For eg: to overload '+' operator we use '__add__()' '''


class Number():

    def __init__(self, num):
        self.num = num

    def __add__(self, num2):
        print("Operator overloaded")
        return self.num + num2.num  #Because 'num' holds the actual integer as defined in __init__

'''Here, n1 and n2 call the __init__
n1 refers to self and 2 refers to num. Same applies for n2'''
n1 = Number(2)
n2 = Number(4)

#This is where operator overloading happens. The '+' here will search for '__add__()'
result = n1 + n2

print(result)