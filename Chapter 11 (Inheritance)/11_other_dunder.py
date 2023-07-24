#Showing some other dunder methods

class Number():

    def __init__(self, n):
        self.n = n

    def __sub__(self, n1):
        return self.n - n1.n
    
    def __str__(self):
        return (f"What is this {self.n}")

    def __len__(self):
        return len(str(self.n)) #Here it needs to be converted to string to find length

number1 = Number(222)
number2 = Number(6)

#When we try to print the object directly it calls '__str__'
print(number1)

print(len(number1))