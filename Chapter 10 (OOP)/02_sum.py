#Adding two numbers using OOP

class Numbers:
    def sum(self):
        return self.n1 + self.n2

numbs = Numbers()
numbs.n1 = 2
numbs.n2 = 4
s = numbs.sum()
print('The Sum is: ',s)


#This can also be done as follows:

# class Numbers:
#     def sum(self):
#         print(f"The sum is: {add.n1 + add.n2}")

# add = Numbers()
# add.n1 = 2
# add.n2 = 4
# add.sum()