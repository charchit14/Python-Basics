#WAP to sum a list with four numbers

n1=int(input("Enter first number: "))
n2=int(input("Enter second number: "))
n3=int(input("Enter third number: "))
n4=int(input("Enter fourth number: "))

list = [n1, n2, n3, n4]
print("Your list is: ",list)

add = list[0] + list[1] + list[2] + list[3]
print("The sum of list is: ",add)

#short way to sum list is as shown below
print("The sum is: ",sum(list))