#Another example of operator overloading

'''Here we will overload two operators, one will be '-'
And another will be '*' '''

class Number():

    def __init__(self, n):
        self.n = n

    def __sub__(self, n1):
        return self.n - n1.n
    
    def __mul__(self, n2):
        return self.n * n2.n


number1 = Number(2)
number2 = Number(6)

subtraction = number1 - number2
print(subtraction)

multiplication = number1 * number2
print(multiplication)