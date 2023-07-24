#A program showing different methods in a dictionary

dict = {
    "Run" : "Go fast",
    "Eat" : "Put food in your mouth",
    "City" : "Win",
    "Marks" : [56, 18, 54],
    2 : "Wow",
    "Number" : 99,
    "AnotherDict" : {"Shark" : "Preadtor", "Num" : 100}
}

# print(type(dict))
# print(dict.keys())
# print(dict.values())

# dict=list(dict) #converting the dict type to list; is also applicable for keys and values separately
# print(type(dict))

# print(dict.items())

print(dict)
#updating the dictionary
updict= {"Maya" : "Dhoka",
         2 : "Not Marks"} #updates the previous key as well if used again
dict.update(updict)
print(dict)

print(dict.get(22)) #.get does not throw error even when key is not present (return none)
# print(dict[22]) #this will throw error when key is not present

del dict[2] #deletes the key 2 and its value

print(dict)