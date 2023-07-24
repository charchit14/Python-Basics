#WAP to detect the spam comments
'''A spam comment is a text containing following keywords
make a lot of money,
buy now,
subscribe this,
click this'''

a = input("Enter a text: ")

if("make a lot of money" in a):
    print("This is spam")
elif("buy now" in a):
    print("This is spam")
elif("subscribe this" in a):
    print("This is spam")
elif("click this" in a):
    print("This is spam")
else:
    print("Maybe this is not spam")

#another method using boolean

# if("make a lot of money" in a):
#     spam = True
# elif("buy now" in a):
#     spam = True
# elif("subscribe this" in a):
#     spam = True
# elif("click this" in a):
#     spam = True
# else:
#     spam = False

# if(spam):
#     print("This is spam")
# else:
#     print("Not spam")