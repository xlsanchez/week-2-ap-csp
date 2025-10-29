
# ----------------------------------------
# . Working with Strings
# ----------------------------------------

# Strings are sequences of characters enclosed in quotes (' ' or " ")
# greeting = "Hello"
# name = "World"

# # ----------------------------------------
# # Basic String Operations
# # ----------------------------------------

# # 1. Concatenation: Combining strings using the + operator
# message = greeting + " " + name
# print("Concatenated String:", message)  # Output: Hello World

# ----------------------------------------
# 2. String Functions
# ----------------------------------------

phrase = "Python is FUN!"
name = "XAVIER"
# Convert all characters to lowercase
print("Lowercase:", phrase.lower())  # Output: python is fun!
print("Lowercase:" , name.lower())
# Convert all characters to uppercase
print("Uppercase:", phrase.upper())  # Output: PYTHON IS FUN!
print("Uppercase:", name.upper())
print("Uppercase:", name.capitalize())

# # Check if all characters are uppercase
print("Is Uppercase?", phrase.isupper())  # Output: False
print("Is Uppercase?", name. isupper() )
# # Find the length of the string
# print("Length of phrase:", len(phrase))  # Output: 14

# # ----------------------------------------
# # 3. Indexing and Slicing
# # ----------------------------------------

chicago_mayor = "Johnson" 

# print the first letter of the mayor's name
print("First character of mayor name:" , chicago_mayor[0])
print("First character of mayor name:" , chicago_mayor[-1])

#get John \

print("First character of mayor name:" , chicago_mayor[0:4])
#first numbner in slicing is inclusive,
#second is exclusive
print("Last three letters of mayor name:" , chicago_mayor[4:])
print("Last three letters of mayor name:" , chicago_mayor[-3:])
last_name = "Sandoval"
print("Last three characters of my last name." , last_name[-3:])
print("First three characters of my last name." , last_name[0:3])

poppins = "supercalifragilisticexpialidocious"
# print out docious 
print(poppins[-7:])
# uppercase the entire string 
print(poppins.upper())
#print out super 
print(poppins[0:5])
# length of the string method 
print(len(poppins)) # output : 34 
decleration_of_independence = "We hold these truths to be self-evident, that all men are created equal, that they are endowed by their Creator with certain unalienable Rights, that among these are Life, Liberty and the pursuit of Happiness"
print(len(decleration_of_independence))

# # Indexing: Access characters by position (0-based index)
# print("First character:", phrase[0])  # Output: P
# print("Last character:", phrase[-1])  # Output: !

# # Slicing: Get a range of characters (start inclusive, end exclusive)
# print("Characters 1 to 4:", phrase[1:4])  # Output: yth

# # Example combining everything:
# print("Formatted Example:", (greeting + " " + name + "!").upper())
# # Output: HELLO WORLD!


# # ----------------------------------------
# # 7. Strings: Advanced Concepts
# # ----------------------------------------

# # Creating Strings: use single or double quotes
# greeting1 = 'Hello'
# greeting2 = "Hi there"

# # Printing Strings
# print(greeting1)
# print(greeting2)

# # ----------------------------------------
# # String Methods
# # ----------------------------------------

# sentence = "Python is fun to learn"

# # .split(): Splits the string into a list of words
# words = sentence.split()
# print("Split result:", words)

# # .format(): Allows inserting values into strings using {}
# name = "Marvin"
# age = 35
# intro = "My name is {} and I am {} years old.".format(name, age)
# print(intro)

# # You can also use f-strings (Python 3.6+)
# intro_fstring = f"My name is {name} and I am {age} years old."
# print(intro_fstring)
