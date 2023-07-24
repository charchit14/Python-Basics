#WAP to replace the word 'bat' in a file by '###' and update the same file

with open ("C:\\Users\\charc\\Desktop\\Learning Python\\Chapter 9 (File)\\Practice Set\\bat.txt", "r") as f:
    c=f.read()
    if "bat" in c:
        print("The word 'bat' is present.")
        c=c.replace("bat","###")
        with open ("C:\\Users\\charc\\Desktop\\Learning Python\\Chapter 9 (File)\\Practice Set\\bat.txt", "w") as f:
            f.write(c)
            print("The modified content is:\n",c)
    else:
        print("The word 'bat' is not present so, can't replace anything.")