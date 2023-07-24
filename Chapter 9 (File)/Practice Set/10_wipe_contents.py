#WAP to wipe out the contents of file. 'wipe.txt' in this case

with open("C:\\Users\\charc\\Desktop\\Learning Python\\Chapter 9 (File)\\Practice Set\\wipe.txt","r") as f:
    z = f.read()

if z=='':
    print("The file is already clean")
else:
    with open("C:\\Users\\charc\\Desktop\\Learning Python\\Chapter 9 (File)\\Practice Set\\wipe.txt","w") as f:
        f.write('')
    print("The file is now clean")