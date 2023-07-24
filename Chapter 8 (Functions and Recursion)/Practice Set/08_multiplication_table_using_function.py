# #Write a function to generate a multiplication table using a function

def mult(a):
     for i in range (1,11):
         print(f"{a} * {i} = {a*i}")

n=int(input("Enter a number: "))
print()
print("The multiplication table is:")
m=mult(n)


#To print in list

# def mult(a):
#     table = []
#     for i in range (1,11):
#         q = f"{a} * {i} = {a*i}"
#         table.append(q)
#     return table

# n=int(input("Enter a number: "))
# m=mult(n)
# print("The multiplication table is: \n", m)