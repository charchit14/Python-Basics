# Showing the use of write and append in a file

# f = open("C:\\Users\\charc\\Desktop\\Learning Python\\Chapter 9 (File)\\sample2.txt", "w")
# f.write("Okay! Writing, huh?")  #If we change this text it will overwrite the whole file
# f.close()

# To add to the end of file use 'append'
f = open("C:\\Users\\charc\\Desktop\\Learning Python\\Chapter 9 (File)\\sample2.txt", "a")
f.write("This is appending")    #Each time you run the program this line will be added to the EOF
f.close()