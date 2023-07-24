# super() can be used in constructor as well

#This is a parent class
class Team:
    def __init__(self):
        print("Constructor of Parent")

#This is first child class
class Players(Team):
    def __init__(self):
        super().__init__()
        print("Constructor of Child 1")

#This is second child class
class Formation(Players):
   def __init__(self):
       super().__init__()
       print("Constructor of Child 2")

c2 = Formation()