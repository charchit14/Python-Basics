#A program showing use of OOP for Bus Form Application

''' 
StudentName ---> Pascal case (The first letter of each word is capital)
studentName, studentAddressName ---> Camel case (The first letter of first word is small and first letter of other words is capital)
'''
#Memory is allocated only after object is created in class

class BusForm:
    #formType = "Bus Form"
    def PrintData(self):
        print(f"Name is: {self.name}")
        print(f"Bus is: {self.bus}")

sharkApplication = BusForm()

sharkApplication.name = "Shark"
sharkApplication.bus = "Deluxe"

sharkApplication.PrintData()