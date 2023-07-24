'''Create a class to reprsent complex numbers
along with overloaded operators + and * that add & multiplies them '''

# Complex multiplication : (a+ib)(c+id) = (ac-bd) + i(ad+bc)

class myComplex():
    
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        new_real = self.real + other.real
        new_imag = self.imag + other.imag
        return myComplex(new_real, new_imag)


    def __mul__(self, other):
        new_real = (self.real * other.real) - (self.imag * other.imag)
        new_imag = (self.real * other.imag) + (other.real * self.imag)
        return myComplex(new_real, new_imag)

    def __str__(self):
        return f"{self.real} + {self.imag}i"

c1 = myComplex(3,2)
c2 = myComplex(1,7)

print(f"Sum is: {c1 + c2}")
print(f"Product is: {c1 * c2}")