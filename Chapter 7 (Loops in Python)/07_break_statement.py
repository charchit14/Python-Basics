#Showing the use of 'break' statement

for a in range(10):
    print(a)
    if a==6:
        break
else:   #only executes when 'for' loop is sucessfully termintaed not when 'for' is forced to terminate
    print("Okay! Mate") #executes when for loop is exhausted 