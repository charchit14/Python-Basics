#WAP to convert celsius to fahrenheit using function

def temp(c):
    f= (9*c + 160) / 5
    return f

a = float(input("Enter the temperature in celsius: "))
m=(temp(a))
print("The temperature in Fahrenheit is: ",m)