#WAP to calculate grade of a student from his marks and given scheme
# 90 to 100 = Ex
# 80 to 90 = A
# 70 to 80 = B
# 60 to 70 = C
# 50 t0 60 = D
# <50 = F

a = int(input("Enter your marks: "))

if(a<50):
    g= "F"
elif(50<=a<60):
    g= "D"
elif(60<=a<70):
    g= "C"
elif(70<=a<80):
    g= "B"
elif(80<=a<90):
    g= "A"
elif(90<=a<=100):
    g= "Ex"
else:
    print("Invalid Input")

print("The grade is: ", g)