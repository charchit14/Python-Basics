#Constructor in python

# class Players:
#     club = "City"

#     #Creating the constructor
#     def __init__(self):
#         print("What just happened")

# Fod = Players()


class Players:
    club = "City"
    def __init__(self, name, position, salary): #We can pass multiple arguements to the constructor
        print("What just happened")
        self.name = name
        self.position = position
        self.salary = salary

    def getDetails(self):
        print(f"The Player {self.name} plays in {self.position} and earns {self.salary}")

Fod = Players("Ronnie", "ST", 99)
#Fod = Players() --> This thorws an error
Fod.getDetails()