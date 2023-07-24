#Create a class 'Pets' from 'Animals', and 'Dog' from 'Pets'. Also add a method 'bark' in 'Dog'.

class Animals():
    name = "Shark-Animals"

    def Animal_Data(self):
        list = ['Cat', 'Dog', 'Tiger', 'Elephant']
        print(f"The animals in {Animals.name} are: {list}")

class Pets(Animals):
    
    def Pets_Data(self):
        super().Animal_Data()
        print(f"You have reached 'Pet'")
    
class Dog(Pets):

    def bark(self, noise):
        self.noise = noise
        print(f"So, the noise is: {self.noise}")

    def Dog_Data(self):
        super().Pets_Data()
        print(f"You have reached 'Dog'")

d = Dog()

d.Dog_Data()

d.bark("Bhau-Bhau")