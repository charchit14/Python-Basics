# WAP to read a text from a file and find out whether it contains the word 'Twinkle'

f = open("C:\\Users\\charc\\Desktop\\Learning Python\\Chapter 9 (File)\\Practice Set\\poem.txt","r")
x = f.read()

if ("twinkle" in x.lower()):
    print("Yes, the word 'twinkle' is present")
else:
    print("No, the word 'twinkle' is not present")

f.close()