#A program to create a list, printing its items, and also changing its items

a = [1, 6, 88, 99, 2.3, 44] #creating a list
print(a)

# print(a[4])
# print(a[1:4])
# print(a[0:5:2])

a[2] = 89 #changing the value of list 
print(a)

#we can create a list with different data types
b=[4, "Shark", True, 7.14]
print(b)
print(b[1])
b[1] = "City"
print(b[1])