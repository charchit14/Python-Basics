#A program showing different set methods

a=set()
print(type(a))
#adding values to set
a.add(3)
a.add(1)
a.add((1,2,3)) #can add a tuple to set but not a list and dictionary
print(a)

print("The lenght of the set is: ",len(a))
a.remove(1) #removes the item/value 1 from set
print(a)

print(a.pop()) #removes a random element and shows it if we write print as well
print(a)

b={1,2,3,4,5,6}
c={5,6,7,8,9}

# union
print("Union :", b | c)
  
# intersection
print("Intersection :", b & c)
  
# difference
print("Difference :", b - c)
  
# symmetric difference
print("Symmetric difference :", b ^ c)