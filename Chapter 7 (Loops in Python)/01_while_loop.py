#A program showing how 'while' loop can be used

i = 0
while (i<10):
    print("Yes", i)
    i=i+1
print ("Finish")


#This adds values to the list until it recieves stop as an input

x=[]
i = input("Enter value: ")

while i !="stop":
    x.append(i)
    i = input("Enter value: ")
print(x)