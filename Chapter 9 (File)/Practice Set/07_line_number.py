# #WAP to find out the line number in which 'python' is present in log file

i = 0
with open ("C:\\Users\\charc\\Desktop\\Learning Python\\Chapter 9 (File)\\Practice Set\\log.txt","r") as f:
    while True:
        i += 1
        x=f.readline()
        if 'python' in x.lower():
            print(f"Python is present in line {i}")
        #else:
        #   print("Python is not present")

#Here, 'i' is used as a counter to count the lines