# abstraction is when i hide 
# the complex details for something 
# alot more simple. 

#personal information
# a function allows us to wrap data or 
#information into a special box or 
#encolsure for reuse
# define a function
def personInformation():
    question1 = input("how old are you?")
    question2 = input("where do you live?")
    question3 = input("what school do you go to?")
    print(question1 + question2 + question3)

# # call the function 
# personInformation()
# personInformation()
# personInformation()


# make a function that guesses how old you are?
def age():
    q1 = int(input("What year is it now?"))
    q2 = int(input("What year were you born?"))
    answer = q1 - q2
    result = print(f'you are {answer} years old')

# call the function 

age()
age()
age()