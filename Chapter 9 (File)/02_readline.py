#Showing the use of readline

f = open("C:\\Users\\charc\\Desktop\\Learning Python\\Chapter 9 (File)\\sample.txt","r")

#This will read the first line
d = f.readline() 
print(d)

#This will read the second line line
d = f.readline()
print(d)

#This will read the third line line
d = f.readline()
print(d)

f.close()