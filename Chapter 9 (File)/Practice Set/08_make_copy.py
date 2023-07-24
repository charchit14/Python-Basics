#WAP to make a copy of a file 'original.txt'. 
'''This means that copy the contents of 'original.txt'
to any other file say 'duplicate.txt' '''

#Opening and reading the original file
with open("C:\\Users\\charc\\Desktop\\Learning Python\\Chapter 9 (File)\\Practice Set\\original.txt","r") as file:
    x = file.read()

#Writing the contents of 'original' file to the 'duplicate' file
with open("C:\\Users\\charc\\Desktop\\Learning Python\\Chapter 9 (File)\\Practice Set\\duplicate.txt","w") as file:
    file.write(x)