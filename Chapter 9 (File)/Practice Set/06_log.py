#WAP to mine a log file and find out whether it contains 'python'

f= open("C:\\Users\\charc\\Desktop\\Learning Python\\Chapter 9 (File)\\Practice Set\\log.txt","r")
c=f.read()
if 'python' in c.lower():
    print("Python is present")
else:
    print("Python is not present")
f.close()

#'python' is present in line-12 of 'log.txt'