#A program to replace the words in a template with user's input

letter = '''Dear <|NAME|>
you are selected!
<|DATE|>'''

name = input("Enter your name: ")
date = input("Enter the date: ")

letter = letter.replace("<|NAME|>" , name)
letter = letter.replace("<|DATE|>" , date)
print(letter)