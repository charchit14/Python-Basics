#A program showing that the items in a tuple can't be changed

t=(12, "City", 56, True)
print(t)

#trying to change a tuple which should result in error
t[2] = 22 
print(t)