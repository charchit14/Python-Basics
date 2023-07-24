#WAP to print diamond star pattern

rows = 7

for i in range (1,rows+1):
    space = " " * (rows-i)
    star = "*" * ((2*i)-1)
    print (space, star)

for j in range (rows-1,0,-1):
    space2 = " " * (rows-j)
    star2  = "*" * ((2*j)-1)
    print (space2,star2)