# WAP to remove a given word from a string and strip it at the same time

# Showing the use of strip function
# a = "       Hey   Bro        "
# print(a)
# print(a.strip())

def str(string,rep):
    new = string.replace(rep, " ")
    return new.strip()

s = "      Hey Good Boy      "
print("Unstripped string: ",s)
b=str(s,"Hey")
print("Stripped and replaced string: ",b)
