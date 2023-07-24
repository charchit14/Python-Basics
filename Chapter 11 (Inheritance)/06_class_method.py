# A program showing 'class method' to change or access class attribute (line - 9) and (line - 11)

class Perfume():
    name = "Cobra"
    price = 250
    place = "Janakpur"

    def changePrice(self, new):
        self.__class__.price = new  # .__class__. will change the class attribute
    
    @classmethod    #This is another method to change class attribute (also replace 'self' by 'cls')
    def changePlace(cls, new_place):
        cls.place = new_place

p = Perfume()

print(p.price)  #This will print the class attribute price i.e. 250 

p.changePrice(233)
print(p.price)  #This will print 233 because it calls the function and updates the value

print(Perfume.price)    #This will also print 233 because class attribute has been changed in line-9 else it prints 250

print()

p.changePlace("Mahottari")
print(p.place)  #This prints 'Mahottari' because class attribute has been changed in 'changePlace' function