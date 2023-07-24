#Showing the use of 'property decorator'. This is also known as 'getter' method

class Game():
    score = 240
    bonus = 400
    # total = 240 + 200
    '''Assume, the bonus keeps changing so that means each time we need to change the 'total' manually,
    so to avoid this we use 'property' '''

    @property
    def totalScore(self):
        return self.score + self.bonus

a = Game()

print(a.totalScore) 

'''This way 'totalScore' will act as a proprty when we put 'property'
else if we remove '@property' we need to call the function as:
'a.totalScore()' '''