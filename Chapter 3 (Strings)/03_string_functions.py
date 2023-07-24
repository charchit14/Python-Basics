#Using different string functions

story = "in year 2023 Manchester City won the treble which includes the premier league, fa cup, and the champions league"

#string functions

# print(len(story))

# print(len("Count the total characters"))

# print(story.endswith("league"))

# print(story.count("c")) #counts the total number of c in the string story

# print(story.count("the")) #counts the total number of 'the' (which is word) in the string story
# print(story.count("th")) #counts total number of th in string story
# print(story.count("ball"))
# print(story.capitalize()) #capitalizes the first character of string i.e. "i" in this case
# print(story.find("City")) #will tell you the location of City in string if it is available else returns -1; if City is used multiple times it only returns the location of first City not for all or others

print(story.replace("the","win" )) #replaces "the" by "win"