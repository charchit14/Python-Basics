#WAP to generate multiplication tables from 2 to 20 and write them to different files. Place the files in a folder.

for i in range (2,21):
    with open(f"C:\\Users\\charc\\Desktop\\Learning Python\\Chapter 9 (File)\\Practice Set\\03_table\\table of {i}.txt","w") as f:
        for j in range (1,11):
            f.write(f"{i} * {j} = {i*j}")
            if j != 10:     #This will prevent printing a extra line after 10th multiplication (not necessary though)
                f.write("\n")