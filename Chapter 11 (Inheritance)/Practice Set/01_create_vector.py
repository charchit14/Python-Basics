#Create a class '2D' vector and use it to create antother class '3D' vector

class twoD:
    def __init__(self, i, j):
        self.i = i
        self.j = j
    
    def __str__(self):
        return (f"2D vector is: {self.i}i + {self.j}j")


class threeD(twoD):
    def __init__(self, i, j, k):
        super().__init__(i, j)
        self.k = k
    
    def __str__(self):
        return (f"3D vector is: {self.i}i + {self.j}j + {self.k}k")

two = twoD(2,3)
three = threeD(3,4,5)

#Here, to print these objects we need to call __str__()
print(two)
print(three)