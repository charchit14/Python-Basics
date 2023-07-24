#WAP to create a multiplication table of a given number using 'for'

a=int(input("Enter a number to generate multiplication table: "))

for i in range(1,11):
    # print(a, "*", i, "=", a*i)
    print(f"{a} * {i} = {a*i}")   #can be done usinf f-string where variables are put inside {}