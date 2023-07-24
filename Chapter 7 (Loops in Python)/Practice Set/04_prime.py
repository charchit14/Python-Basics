#WAP to find whether a number is prime or not

a = int(input("Enter a number: "))
pr = True

for i in range (2,a):
    if (a%i==0):
        pr = False
        # break

if (pr):
    print ("It is prime")
else:
    print("Not prime")


# def pr(c):
#     for i in range (2,c):
#         if c%i==0:
#             return False
#         else:
#             return True

# a = int(input("Enter a number: "))
# v=pr(a)
# if v:
#     print("Prime")
# else:
#     print("Not Prime")