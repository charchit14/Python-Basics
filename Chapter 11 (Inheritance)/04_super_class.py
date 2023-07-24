#Demonstration of super class (line-18 and line-27)

#This is a parent class
class Team:
    name = "City"

    def wage(self):
        print("City gives wage")

#This is first child class
class Players(Team):
    position = "mid"

    def other(self):
        print("We need defenders")
    def wage(self):
        print("Players need wage")
        super().wage()  #This will help us access wage() of it's parent class

#This is second child class
class Formation(Players):
    form = "3-2-4-1"

    def other(self):
        print("We need midfielders")
    def wage(self):
        super().wage()  #This will help us access wage() of it's parent class
        print("Give me wage")

p = Team()
c1 = Players()
c2 = Formation()

#Printing data
# p.wage()
c1.wage()
print()
c2.wage()