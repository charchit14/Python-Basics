#A program to create and print a dictionary

#creating a dictionary

dict = {
    "Run" : "Go fast",
    "Eat" : "Put food in your mouth",
    "City" : "Win",
    "Marks" : [56, 18, 54],
    2 : "Wow",
    "Number" : 99,
    "AnotherDict" : {"Shark" : "Preadtor", "Num" : 100}     #Adding second dictionary inside first dictionary
}

# print(dict["City"])
# print(dict["Eat"])
# print(dict["Marks"])
# print(dict[2])
# print(dict["Number"])
print(dict["AnotherDict"]["Shark"])

dict["Eat"] = "Food" #can change the value of dictionary
print(dict["Eat"])