#WAP to find out whether a post is talking about 'Shark' or not

p = input("Write a post: ")
if("shark" in p.lower()):                       
    print("The post is talking about Shark")
elif("SHARK" in p.upper()):
    print("The post is talking about Shark")
else:
    print("The post is not talking about Shark")

#'.lower' and '.upper' checks for lower and upper case respectively