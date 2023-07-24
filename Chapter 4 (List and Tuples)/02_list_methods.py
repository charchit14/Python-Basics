#A program demonstrating different list methods

l1 = [2, 5 ,66, 23, 14, 999, 8, 999]

print(len(l1))

l1.sort()
print (l1)

l1.reverse()
print(l1)

l1.append(100)
print(l1)

l1.insert(0,9) #inserts 9 at 0th index position
print(l1)

l1.pop(0) #removes element at 0-index
print(l1)

l1.remove(999) #removes one 999 from list for multiple case
print(l1)

del l1[0] #deletes the item at 0-index from list
print(l1)

print(max(l1)) #Prints the maximum value of a list
print(min(l1)) #Prints the minimum value of a list

print(l1.index(66)) #Gives the location of number '66'