#Slicing of a string

#Concatenation of string
    #title = "Treble Winners : "
    #name = "Manchester City"
    #print(title + name)

name = "Cityzens"
    #indexing a string
    # print(name[2])
    # print(name[0:4])
    # print(name[2:5])
    #print(name[:5])   
    #print(name[0:])   
    #leaving blank means first/last index

#negative indexing
# print(name[-5:-2]) #same as name[3:6]

# slicing with skip values
print(name[1:6:2]) #1 to 6 with skip value of 2, this means print every 2nd charchter from 1 to 6 (skip 1 charcater)
print(name[1:6:1]) #1 to 6 with skip value of 1, does not skip any
print(name[0::2])