#Use of logical operators like 'and, or, not' with conditional operators

ag = int(input("Enter your age: "))

if(ag==0 or ag<=0):
    print("Invalid age")
elif (ag>=40 and ag<=70):
    print("You are eligible")
elif(ag<40):
    print("Come back when you are older")
else:
    print("Should have come when you were younger")