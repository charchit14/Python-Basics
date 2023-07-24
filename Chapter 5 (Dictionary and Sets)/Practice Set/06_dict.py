#A program that lets user create their own dictionary

d={}
l1 = input("Enter your lagnuage Kun: ")
l2 = input("Enter your lagnuage Erl: ")
l3 = input("Enter your lagnuage Kev: ")
l4 = input("Enter your lagnuage Ruben: ")

d["Kun"] =l1
d["Erl"] =l2
d["Kev"] =l3
d["Ruben"] =l4
print(d)

#If two keys are same then the latest value will be used : to learn more, change Kev to Erl (key need to be unique)
#but two or more values can be same