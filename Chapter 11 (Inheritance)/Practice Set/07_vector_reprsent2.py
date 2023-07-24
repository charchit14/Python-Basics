#Write a __str__() method to reprsent vector as: 7i + 8j + 10k

class Vector:

    def __init__(self, vec):
        self.vec = vec
    
    def __str__(self):
        
        dimension = ['i', 'j', 'k']
        result = []
       
        for i, num in enumerate(self.vec):
                z = f" {num}{dimension[i]} "
                result.append(z)
        
        return "+".join(result)


v = Vector([7 , 8 , 10])
print(v)