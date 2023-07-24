#Showing the use of 'setter' method (line - 14)

class Game():
    score = 240
    bonus = 400
  
    @property
    def totalScore(self):
        return self.score + self.bonus
    
    '''To maintain the equation of 'total = score + bonus'
    we use the 'setter' method which will set the bonus score automatically'''

    @totalScore.setter
    def totalScore (self, value):
        self.bonus = value - self.score
        #Here, 'value' means the new total score


a = Game()
print(f"The initial score before setter is: {a.totalScore}")

print()

#Now let's set 'total score' to some value and retrive the 'bonus value'
a.totalScore = 500

print(f"The toal score is {a.totalScore}")
print(f"So, the bonus score is set to = {a.bonus}")
print(f"The score is {a.score}")