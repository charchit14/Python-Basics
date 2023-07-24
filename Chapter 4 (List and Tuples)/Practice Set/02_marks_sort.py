#Taking marks of six students as input and printing in sorted manner

s1=int(input("Enter first student's mark: "))
s2=int(input("Enter second student's mark: "))
s3=int(input("Enter third student's mark: "))
s4=int(input("Enter fourth student's mark: "))
s5=int(input("Enter fifth student's mark: "))
s6=int(input("Enter sixth student's mark: "))

l1 = [s1, s2, s3, s4, s5, s6]
print("The entered marks are: ", l1)

l1.sort()
print("The sorted marks are: ",l1)