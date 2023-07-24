#Can you change the parameter 'self' to anything other say, 'shark'

#Using 'self'
class change():
    def __init__(self, name):
        self.name = name

x = change("This is the name")
print(x.name)

#Changing 'self'  to 'shark'
class change():
    def __init__(shark, name):
        shark.name = name

x = change("This is the name")
print(x.name)

#Hence, we change the parameter 'self' to any other thing