# '''Create a class representing a vector of 'n' dimension.
# Overload + and * to calculate sum and dot product'''

class Vector:

    def __init__(self, v):
        self.vec = v

    def __str__(self):

        list = []
        for i, num in enumerate(self.vec):
            represent = f" {num}a{i} "
            list.append(represent)
        return "+".join(list)
    
    def __add__(self, other):

        if len(self.vec) != len(other.vec):
            raise ValueError("Vectors are of different dimension")
        else:
            #This is called 'list comprehension'. This accumulates all the value and then returns
            result = [self.vec[i] + other.vec[i] for i in range(len(self.vec))]
        return Vector(result)
      
    def __mul__(self, other):

        if len(self.vec) != len(other.vec):
            raise ValueError("Vectors are of different dimension")
        else:
            dot_result = sum([self.vec[i] * other.vec[i] for i in range(len(self.vec))])
        return dot_result


v1 = Vector([1, 7, 9])
v2 = Vector([4, 5, 1])

try:
    print(f"First vector is: {v1}")
    print(f"Second vector is: {v2}")
    print(f"Sum is: {v1 + v2}")
    print(f"Product is: {v1 * v2}")

except ValueError as e:
    print(f"{e}")