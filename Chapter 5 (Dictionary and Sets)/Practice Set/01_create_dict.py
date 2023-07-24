#A program to ask user to search their desired word from a dictionary

dict = {
    "khanu" : "eat",
    "hidnu" : "walk",
    "sutnu" : "sleep"
}
print("The available keys are: ", dict.keys())
a=input("Enter the word you want to search: ")
print("Meaning is: ", dict.get(a))