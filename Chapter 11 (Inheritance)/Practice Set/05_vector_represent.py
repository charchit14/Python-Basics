#Create a class to represent a vector of 'n' dimension

class Vector:

    def __init__(self, v):
        self.vec = v

    def __str__(self):

        list = []
        for i, num in enumerate(self.vec):
            represent = f" {num}a{i} "
            list.append(represent)
        return "+".join(list)

v1 = Vector([2, 4, 5, 1, 7, 9])
print(v1)