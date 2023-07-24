'''WAP to find out whether a student is pass or fail,
if it requires total 40% and at least 33% in each subject to pass.
Assume 3 subject and take marks as an input from the user.'''

#assuming total marks is 100 so obtained marks is obtained percentage
s1=int(input("Enter marks of first subject: "))
s2=int(input("Enter marks of second subject: "))
s3=int(input("Enter marks of third subject: "))

total= ((s1 + s2 + s3)/3)

#method 1
if (s1>100 or s2>100 or s3>100):
    print("Invalid Input")
elif(total >=40 and s1>=33 and s2>=33 and s3>=33):
    print("The result is: Pass")
    print("Total percentage is: ",total)
else:
    print("The result is: Fail")

#method 2
# if(s1<33 or s2<33 or s3<33):
#     print("You failed becaues at least one of your subject has less than 33 marks")
# elif(total<40):
#     print("You failed because your total percentage is below 40")
# else:
#     print("You passed")