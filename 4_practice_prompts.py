
# ----------------------------------------
# Print Practice Exercises
# ----------------------------------------

# Print Practice #1
# Write Python code that prints the sentence: I love learning Python
print("I love learning Python")


# # Print Practice #2
# # Write Python code that prints the sentence: Learning with 'TOTAL Python' is super fun!
# print("Learning with 'TOTAL Python' is super fun!")


# # Print Practice #3
# # Write Python code that prints the number 555 to the screen as a result of a mathematical expression
print(500 + 55)

# ##############################################################################################################
# # Find 3 objects around the room and create variables from it,
# # Insert those variables into an f-string sentence(look at slide 22)in repl.it
# w = "window"
# m = "mouse"
# c = "chair"
# print(f"Leo loves the {c} , uses the {m} and sees the {w}")

# # Familiarize yourself with the syntax of the print() function.
# # Print your name.
print("Xavier")
# # Print today's date.
print(f"October 30th, 2025")
# # Print the name of your favorite movie.
print("Scream")

# # Print your name and age on separate lines using a single print() function.
print("Xavier and I am 16 years old")

# # Use f-strings to print a message like: "In 10 years, [Your Name] will be [Your Age + 10] years old."

# print(f"In 10 years, [Your Name] will be [Your Age + 10] years old.")

# ##############################################################################################################

# ###########################String Practice##################################
# #syntax is the way we write code
# print("Hello World")
# name = "John"     
# #in other languages, this is different
# # in javascript for example, you define
# #variables with let or const or var
# #in python, you just give your variables a
# #name and then define it with a value


# #challenge
# # find a summary of the movie blue beetle online and create a 
# # variable called blue_beetle_summary and print it it out to the screen

blue_beetle_summary = "The 2023 movie Blue Beetle follows Jaime Reyes, a recent college graduate who unexpectedly becomes the superhero Blue Beetle after an ancient alien scarab chooses him as its symbiotic host. The scarab grants him a powerful suit of armor, and Jaime must learn to control its unpredictable powers to protect his family and fight against Victoria Kord, the CEO of Kord Industries, who wants the scarab for her own evil purposes. The film centers on Jaime's relationship with his family, who ultimately help him become a hero."
print(blue_beetle_summary)

# # print the length of the summary
print(len(blue_beetle_summary))

# # upper case the entire summary
print(blue_beetle_summary.upper())

# # print the summary
print(blue_beetle_summary)

# # print the summary in lowercase
print(blue_beetle_summary.lower())

# # replace the word blue with red
modified_blue_beetle_summary = blue_beetle_summary.replace("Blue", "Red")

# # print the summary
print(modified_blue_beetle_summary)

# # string index the word beetle and print it out
print("word"[0])
print("word"[1])
print("word"[2])  
print("word"[3]) 
print("word"[4])  
print("word"[5])



# # print the last word of the summary
my_string = "The 2023 movie Blue Beetle follows Jaime Reyes, a recent college graduate who unexpectedly becomes the superhero Blue Beetle after an ancient alien scarab chooses him as its symbiotic host. The scarab grants him a powerful suit of armor, and Jaime must learn to control its unpredictable powers to protect his family and fight against Victoria Kord, the CEO of Kord Industries, who wants the scarab for her own evil purposes. The film centers on Jaime's relationship with his family, who ultimately help him become a hero."
last_word = my_string.split()[-1]
print(last_word)
# # print the summary in reverse
my_string = "The 2023 movie Blue Beetle follows Jaime Reyes, a recent college graduate who unexpectedly becomes the superhero Blue Beetle after an ancient alien scarab chooses him as its symbiotic host. The scarab grants him a powerful suit of armor, and Jaime must learn to control its unpredictable powers to protect his family and fight against Victoria Kord, the CEO of Kord Industries, who wants the scarab for her own evil purposes. The film centers on Jaime's relationship with his family, who ultimately help him become a hero."
reversed_string = my_string[::-1]
print(reversed_string)

##########################input practice#############################################
#input is when we ask the user for input/data
# Ask the user to enter their name.
q1 = input("What is your name?")
# Input Practice #1
# Write Python code that allows the user to enter their answer, by making them the following question:
# What are you learning today?
q2 = input("What are you learing today?")
# Your code must be able to print to the screen whatever is entered by the user (use the print function).
print(q2)

# Input Practice #2
# Write Python code that allows the user to enter their answer, by making them the following question:
# Where are you from?
q3 = input("where are you from?")
# Your code must be able to print to the screen whatever is entered by the user (use the print function).
print(q3)

# Input Practice #3
# Write Python code that displays the user's full name on the screen, by allowing them to enter their first and last name with the following instructions:
# What is your name?
first_name = input("What is your name?")
# What is your surname?
surname = input("What is your surname?")
# The code must be able to print the user's first and last name on the screen, separated by a space.
print(f"{first_name} {surname}")

# Exercise:
# Write a program that asks the user for their name and favorite color, then prints a message using both pieces of information.
first_name = input("What is your name?")
color = input("What is your favorite color?")
print(f"Your name is {first_name} amd your favorite color is {color}")








