#printing
#Use what you learnt to print out the words "Hello world!" with Python code.Then click the run button to execute your code.
print("hello world")

#string manuplation : Learn to use string concatenation and the new line escape sequence to format strings in Python.


print("Hello world!\nhello world!\nhelloworld!")

#inputs : Learn to use the Python input() function to collect user input and use it within your code.
print("My name is" + " " + "Angela")

#variable : Learn to store values in containers for later use. Variables is a concept in programming that allows us to give a label to a piece of data so that we can refer or reference that data using the chosen variable name. We will see in this lesson how to create variables and how to use the variables to access the contained value.
input("What is your name?")

name=input("What is your name?")
print(len(name))

username=input("enter the username")
length=len(username)
print(length)

#variable name : Learn the rules of variable naming in Python.

#Rules : 1. Make sure your variable names are descriptive 2. Don't have spaces between words 3. Don't start with numbers 4. Don't use special words like print or input 5. Choose simple words that are less likely to become typos 6. Check the company style guidelines if you start work at a company
name = "Angela"
length = len(name)
print(length)

name=input("Enter your name:")
lengt = len(name)
print(lengt)

#band name generator project : Create a greeting for your program.Ask the user for the city that they grew up in and store it in a variable.Ask the user for the name of a pet and store it in a variable.Combine the name of their city and pet and show them their band name.
print("welcome to the band name Generator")
city=input("enter the name of city")
pet=input("enter the name of pet")
print("your band name is " + city + pet)