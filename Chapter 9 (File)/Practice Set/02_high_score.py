#WAP to read score from a file and print the high score whenever the high score is beaten in a game

#This function gives the current score of the game
def game():
    return 100
new = game()

#Reading the previous score from file which is pre-written in file
with open ("C:\\Users\\charc\\Desktop\\Learning Python\\Chapter 9 (File)\\Practice Set\\score.txt", "r") as f:
    v = f.read()

#Comparing the scores:

#This checks if the file is empty and if found empty, puts the current score as high score
if v=='':
    with open ("C:\\Users\\charc\\Desktop\\Learning Python\\Chapter 9 (File)\\Practice Set\\score.txt", "w") as f:
        f.write(str(new))
    print("High score is: ",new)

#If current score is greater than pre-written score in file, current score will over-write the old score
elif new>int(v):
    with open ("C:\\Users\\charc\\Desktop\\Learning Python\\Chapter 9 (File)\\Practice Set\\score.txt", "w") as f:
        f.write(str(new))
    print("High score is: ",new)

#If old score is still greater, it will remain in file
else:
    print("The high score is: ",v)