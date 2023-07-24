#This is a type of multiple inheritance (Child class inherits from multiple (two or more) parent class)

#Parent class - 1
class Team:
    teamName = "City"
    trophies = "Treble"

#Parent class - 2
class Position:
    teamName = "Man City"
    fwd = "Erling"
    goals = 52
    def IncrGoals(self):
        self.goals += 1

#Child class inheriting from both the parent class
class Player (Team, Position):
    foot = "left"

p = Player()

print(p.goals)
print(p.trophies)

p.IncrGoals()
print(p.goals)

'''Although 'teamName' is defined in both the parent class, 
this will print 'City' since, the 'class Team' is passed ahead of 'class Position' in child class'''
print(p.teamName)