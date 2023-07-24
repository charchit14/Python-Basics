'''Override the __len__() method on vector of problem-5
to display the dimension of the vector'''


class Vector:

    def __init__(self, v):
        self.vec = v

    # def __str__(self):

    #     list = []
    #     for i, num in enumerate(self.vec):
    #         represent = f" {num}a{i} "
    #         list.append(represent)
    #     return "+".join(list)
    
    def __len__(self):
        return len(self.vec)


v1 = Vector([2, 4, 7, 9])
# print(f"The vector is: {v1}")
print(f"The dimension of vector is: {len(v1)}")