#Showing the use of static method

class Players:
    club = "City"
    def wage(self, quote):  #We can pass multiple arguments as well
        print(f"Wage is 450k and my quote is: {quote}")

    @staticmethod
    def greet():
        print("Hello Champion")    

    @staticmethod
    def place():
        print("This is a nice place")

Foden = Players()
Foden.wage("nothing") #This is the argument for quote along with wwage
Foden.greet()
Foden.place()

#With the use of static method we need not pass 'self' as an argument 
'''@static method does not convert
'Foden.greet()' into 'Players.greet(Foden)'
Hence, 'self' is not needed'''