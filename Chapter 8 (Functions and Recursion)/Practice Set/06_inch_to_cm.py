# WAP to convert inch to centi-meters

def length(a):
    n = 2.54 * a
    return n

b = int(input("Enter length in inch: "))
v=length(b)
print("The length in cm is: ",v)