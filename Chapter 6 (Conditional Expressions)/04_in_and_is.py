#Program showing use of 'is' and 'in'

#Use of is
a=None
if(a is None):
   print("Yes")
else:
    print("No")

#Use of in
l = [22, 34, 56, 78]
print(22 in l) #returns true if value 22 is present in the list l else returns false
print(344 in l)