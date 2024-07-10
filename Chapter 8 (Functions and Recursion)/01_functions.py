# Creating a function and using it
# A function can take multiple values as well

# creating a function
def percent(mark):
    a = (sum(mark)/4)
    return a 

# using the function
mark1=[45, 56, 78, 89]
p1=percent(mark1)

mark2=[90, 98, 87, 76]
p2=percent(mark2)

print(p1,"and", p2)