# Basics of File (opening, reading, and closing)

# Using open function to read a file

# f = open("C:\\Users\\charc\\Desktop\\Learning Python\\Chapter 9 (File)\\sample.txt", "r")

#If we don't specify the mode, by default it is read

f = open("C:\\Users\\charc\\Desktop\\Learning Python\\Chapter 9 (File)\\sample.txt")
# d = f.read()
d = f.read(21) #This will only read 21 characters from the file
print(d)
f.close()


'''Note : If we are opening a binary file we need to write mode as "rb" for read
For text we need to write "rt" or simply "r"
By default it will be "rt" '''