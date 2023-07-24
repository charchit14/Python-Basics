#WAP to censor a list of words and rewrite the file

#This is the list of words that need to be censored
words = ['bat', 'rat', 'cat', 'ant']

with open ("C:\\Users\\charc\\Desktop\\Learning Python\\Chapter 9 (File)\\Practice Set\\censor.txt", "r") as f:
    c=f.read()
    cen = False #Assuming no words need to be censored
    for i in words:
        if i in c:
            cen = True
            c=c.replace(i,"###")
    if cen:
        with open ("C:\\Users\\charc\\Desktop\\Learning Python\\Chapter 9 (File)\\Practice Set\\censor.txt", "w") as f:
            f.write(c)
            print("Words need to be censored.")
            print("The censored text is:\n",c)
    else:
        print("No words need to be censored.")