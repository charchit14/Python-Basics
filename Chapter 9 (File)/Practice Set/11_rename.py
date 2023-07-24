#WAP to rename a file (Example: 'rename.txt' to 'rename2.txt')

'''Here we will copy the content of previous file to new file
then delete the previous file and name the new file with the 
name of previous file'''

#This is not direct renaming but just the imitation that gives the exact effect of rename process

#This module will be used to remove the file
import os

f1 = "C:\\Users\\charc\\Desktop\\Learning Python\\Chapter 9 (File)\\Practice Set\\rename.txt"
f2 = "C:\\Users\\charc\\Desktop\\Learning Python\\Chapter 9 (File)\\Practice Set\\rename2.txt"

with open(f1,"r") as f:
    z = f.read()

with open(f2,"w") as f:
    f.write(z)

os.remove(f1) #This will remove the file