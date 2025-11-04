# week 2 Python Challenge

# The most awaited moment of your first day of study has arrived. You are going to create your first solo program, and you are going to do it applying everything you have learned throughout this day.

# Imagine the situation: Your best friend has started a brewery and has everything ready. His product is fantastic. It has body, good flavor, good color, and just the right level of foam. But it lacks an identity. He can’t think of a name for his beer that would give it a unique and original identity.

# So, you come to him and say: “Don’t worry. I’m going to create a program that will ask you two questions and then tell you what to name your beer. It’s as simple as that.”

# I know that in the real world, we wouldn’t need to develop a software just to ask it two questions. But until we learn a bit more functionality, well, our programs are going to have to stay in the realm of simplicity. Yet if you’re just starting out, this is going to be quite a challenge.

# You’re going to create Python code that asks your friend to answer two questions that require a single word each, and then displays those combined words on the screen to form a creative brand.

# You can use any questions you want. The idea is for the outcome to be original, creative, and even funny. And if you want to add some difficulty to your challenge, I suggest you try to have the name of the beer printed in quotation marks on the screen.

# Remember that there are different ways for the print function to show the quotes without interrupting the stream, and it’s also possible to print out text in at least two lines using line breaks within the code.

# Well, try to do it on your own, and if it gets complicated, don’t worry, we will solve it together in the next lecture.

# Cheers and good luck.

# Beer Name Generator 

print("Welcome to the Beer Name Generator!\n")

word1 = input("What's your favorite animal? ")
word2 = input("What's your favorite place? ")

beer_name = word1 + " " + word2

print("\nYour new beer brand could be called:")
print(f"\"{beer_name}\" 🍻")
