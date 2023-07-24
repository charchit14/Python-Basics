'''This is a multilevel inheritance (child 1 inherits from parent and child 2 inherits from child 1)
i.e. Parent --> Child 1 --> Child 2
child 1 is parent of child 2'''

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

#This is second child class
class Formation(Players):
    form = "3-2-4-1"
    def other(self):
        print("We need midfielders")

p = Team()
c1 = Players()
c2 = Formation()

#Printing for child 2
c2.other()   #Takes from own class
c2.wage() #Takes from its parent class (i.e. child 1)
print(c2.name)  #Takes from the top Parent class