#WAP to check whether the contents of one file matches the contents of another file

'''Here we will check the contents of 
'original.txt' with 'duplicate.txt' '''

with open("C:\\Users\\charc\\Desktop\\Learning Python\\Chapter 9 (File)\\Practice Set\\original.txt","r") as file:
    x = file.read()

with open("C:\\Users\\charc\\Desktop\\Learning Python\\Chapter 9 (File)\\Practice Set\\duplicate.txt","r") as file:
    z = file.read()

if x==z:
    print("The contents match")
else:
    print("The contents do not match")