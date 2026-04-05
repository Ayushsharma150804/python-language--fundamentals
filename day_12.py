#namespace and scope
enemies = 1


def increase_enemies():
    enemies = 2
    print(f"enemies inside function: {enemies}")


increase_enemies()
print(f"enemies outside function: {enemies}")

#local scope
def drink_portion():
    drinking = 3
    print(drinking)

drink_portion()

#can't access this drinking outside the function
#print(deinking)

#globle scope
player_health =100

def drink_portion():
 print(player_health)

drink_portion()

#local function() scope

plater = 1
def play_game():      #global function
    def drink_portionn():   #local function
        player_strength =12
        print(plater)
    drink_portionn()

drink_portionn()  #give error because it is local function access only inside play_game()
play_game()

enemies = 0
def increase_enemies():
    enemies = 2  #when create same veriable name inside function same with globle variable  so,inside function veriable is difference with globle function

    print(f"enemies inside function: {enemies}")


increase_enemies()
print(f"enemies outside function: {enemies}")

#Block Scope :Python is a bit different from other programming languages
#Python have no block scope


# Accessible anywhere
my_global_var = 1


def my_function():
    # Only accessible within my_function()
    my_local_var = 2


for _ in range(10):
    # Accessible anywhere
    my_block_var = 3



enemies = ["skeleton", "zombie" , "alien"]
level=1

if level<5:
    kill: str = enemies[0]

print(kill)        #here it print the kill because it considered kill is global variable



def create_enemies():
    new_enemies = ""
    if level<5:
        new_enemies = enemies[1]

    print(new_enemies) #local scope declare inside self function
# print(new_enemies)  #it gave error b\c new_enemies i local scope


# #prime number
# def is_prime(num):
#     ran = int(num / 2 + 1)
#     print(ran)
#     for i in range(2, ran):
#         if num % i == 0:
#             return False
#     return True



# print(is_prime(2))


# Modifying Global Scope

enemies = 1


def increase_enemies():

    global enemies
    enemies += 1            #use global variable value same inside function which make changes in it same variable
    print(f"enemies inside function: {enemies}")


increase_enemies()
print(f"enemies outside function: {enemies}")

#one another way to use which not use global keyword
enemies =2
def increase_enemies(danger):
    danger += 1
    print(f"enemies inside function: {danger}")
    return danger


enemies= increase_enemies(enemies)  #update the enemies value  same as danger value
print(f"enemies outside function: {enemies}")


#GLOBAL CONSTANT
PI = 3.14159 # PI VALUE NEVER CHANGE SO IT DEFINE AS GLOBAL SCOPE
#Global constants are normally declared in ALL_CAPS with a underscore in between.

GOOGLE_URL = "https://www.google.com"
def math():
    r=4
    area = PI *r * r

#***********number gussing project************

logo = r"""
  / _ \_   _  ___  ___ ___  /__   \ |__   ___    /\ \ \_   _ _ __ ___ | |__   ___ _ __ 
 / /_\/ | | |/ _ \/ __/ __|   / /\/ '_ \ / _ \  /  \/ / | | | '_ ` _ \| '_ \ / _ \ '__|
/ /_\\| |_| |  __/\__ \__ \  / /  | | | |  __/ / /\  /| |_| | | | | | | |_) |  __/ |   
\____/ \__,_|\___||___/___/  \/   |_| |_|\___| \_\ \/  \__,_|_| |_| |_|_.__/ \___|_| 
"""

import random


#one way of this game
def game():
    print(logo)
    computer = random.randint(1, 100)
    print(computer)

    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100. ")


    level = input("Choose a difficulty. Type 'easy' or 'hard':")

    if level == "easy":
        attempt = 10

    else:
        attempt = 5

    print(f"You have {attempt} attempts remaining to guess the number. ")

    for i in range(1,attempt+1):
        guess = int(input("Make a guess:"))
        attempt_re = attempt-i
        if computer==guess:
            print( f"You got it! The answer was {computer}.")
            break

        elif guess<computer:
            print(f"You have {attempt_re}attempts remaining to guess the number.")
            print("Too low.")
            print("Guess again.")

        elif guess>computer:
            print(f"You have {attempt_re} attempts remaining to guess the number.")
            print( "too high")

    if attempt_re==0:
        print("You've run out of guesses. Refresh the page to run again.")


game()

#another way of this game
from random import randint


EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5


# Function to check users' guess against actual answer
def check_answer(user_guess, actual_answer, turns):
    """Checks answer against guess, returns the number of turns remaining."""
    if user_guess > actual_answer:
        print("Too high.")
        return turns - 1
    elif user_guess < actual_answer:
        print("Too low.")
        return turns - 1
    else:
        print(f"You got it! The answer was {actual_answer}")


# Function to set difficulty
def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS


def game():
    print(logo)
    # Choosing a random number between 1 and 100.
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    answer = randint(1, 100)
    print(f"Pssst, the correct answer is {answer}")

    turns = set_difficulty()

    # Repeat the guessing functionality if they get it wrong.
    guess = 0
    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number.")
        # Let the user guess a number
        guess = int(input("Make a guess: "))
        # Track the number of turns and reduce by 1 if they get it wrong
        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print("You've run out of guesses, you lose.")
            return
        elif guess != answer:
            print("Guess again.")




game()


