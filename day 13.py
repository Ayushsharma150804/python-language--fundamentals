#debug
# Describe the Problem - Write your answers as comments:
def my_function():
    for i in range(1, 20):
        if i == 20:
            print("You got it")


my_function()

# Describe the Problem - Write your answers as comments:
# 1. What is the for loop doing? : for loop can check if statement 19 times
# 2. When is the function meant to print "You got it"? function never print "you got it
# 3. What are your assumptions about the value of i? value of i never became 20


#bug fix
def my_function():
    for i in range(1, 21):  #increse the range
        if i == 20:
            print("You got it")


my_function()

#reproduce the bug
from random import randint
dice_images = ["❶", "❷", "❸", "❹", "❺", "❻"]
dice_num = randint(1, 6)
print(dice_images[dice_num])



#fix bug

dice_images = ["❶", "❷", "❸", "❹", "❺", "❻"]
dice_num = randint(0, 5)  #change in randint ranges 1.last range change to 5 2.first range to 0
print(dice_images[dice_num])


#play computer
year = int(input("What's your year of birth?"))

if year > 1980 and year < 1994: #this statement turns to False input type 1994
    print("You are a millennial.")
elif year > 1994:   #this also turns to False input type 1994
    print("You are a Gen Z.")


#fix the bug
year = int(input("What's your year of birth?"))

if year > 1980 and year < 1994: #this statement turns to False input type 1994
    print("You are a millennial.")
elif year >= 1994:   #this also turns to False input type 1994
    print("You are a Gen Z.")

age = int(input("How old are you?"))  #value error happen when user give input in string format
if age > 18:
print("You can drive at age {age}.")#indentation error happen #bug in print statement


#fix the error use try/except block

try:
    age = int(input("How old are you?"))
except ValueError:
    print("you can enter the number in string like fiften ! enter number such as 15")
    age = int(input("How old are you?"))

if age>18:
    print(f"you can drive at age {age}")

#use print

word_per_page = 0
pages = int(input("Number of pages: "))
word_per_page == int(input("Number of words per page: ")) # "==" is comparison operator not assignment operator
total_words = pages * word_per_page   #muntiply with 0 because we take word_per_page not this word_per_pages

print(f"pages {pages}") # dubug the error using the print statement
print(f"word_per_page = {word_per_page}")
print(total_words)

#fix code

pages = int(input("Number of pages: "))
word_per_page = int(input("Number of words per page: ")) # "==" is comparison operator not assignment operator
total_words = pages * word_per_page   #muntiply with 0 because we take word_per_page not this word_per_pages
print(total_words)

#use a debugger 
import random
import maths


def mutate(a_list):
    b_list = []
    new_item = 0
    for item in a_list:
        new_item = item * 2
        new_item += random.randint(1, 3)
        new_item = maths.add(new_item, item)
    b_list.append(new_item)                 #just changing the indentation of this line
    print(b_list)


mutate([1, 2, 3, 5, 8, 13])

#debug to correct this
def mutate(a_list):
    b_list = []
    new_item = 0
    for item in a_list:
        new_item = item * 2
        new_item += random.randint(1, 3)
        new_item = maths.add(new_item, item)
        b_list.append(new_item)
    print(b_list)


mutate([1, 2, 3, 5, 8, 13])

# Debugging Odd or Even
# - Read the code in exercise.py - Spot the problems 🐞. - Modify the code to fix the program. Fix the code so that it works and passes the tests when you submit.
def odd_or_even(number):
    if number % 2 == 0: #use == insted of =
        return "This is an even number."
    else:
        return "This is an odd number."

#Debugging Leap Year
def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:  #change 4000 to 400
                return True
            else:
                return False
        else:
            return True
    else:
        return False

# Debugging FizzBuzz
# Target is the number up to which we count
def fizz_buzz(target):
    for number in range(1, target + 1):
        if number % 3 == 0 and number % 5 == 0:   #or to and
            print("FizzBuzz")
        elif number % 3 == 0:   #change if to elif
            print("Fizz")
        elif number % 5 == 0:
            print("Buzz")
        else:
            print(number)  #remove square braces for correct result
