#With Statement opens and closes the file automatically

with open ("C:\\Users\\charc\\Desktop\\Learning Python\\Chapter 9 (File)\\sample3.txt", "r") as f:
    v = f.read()
print(v)

with open ("C:\\Users\\charc\\Desktop\\Learning Python\\Chapter 9 (File)\\sample3.txt", "w") as f:
    f.write("NEW MODE")