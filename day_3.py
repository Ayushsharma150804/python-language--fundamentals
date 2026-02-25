# if else if <this condition is true>:n<then execute this line of code>
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("you can ride the rollercoaster")
else:
    print("you can not ride in  the rollercoaster")

if height == 120:
    print("you can ride the rollercoaster")
else:
    print("you can not ride in  the rollercoaster")

#modulo
print(10%3)
print(6%2)
print(6%5)

#pause 2
number = int(input("enter the number"))
if number % 2 == 0:
    print(number,"is even number")
else:
    print(number,"is odd number")

#nesting and elif
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
age= int(input("what is your age?"))

if height >= 120:
    print("You can ride the rollercoaster")
    if age <= 12:
        print("you pay the 5 rupee")
    elif age <=18:
        print("you pay the 7 rupee")
    else:
        print("you pay the 10 rupee")

else:
    print("Sorry you have to grow taller before you can ride.")

#multiple ifs
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill=0


if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))
    if age <= 12:
        print("Please pay $5.")
        bill = 5
    elif age <= 18:
        print("Please pay $7.")
        bill =7
    else:
        print("Please pay $12.")
        bill = 12
    photo = input("if you want to click photo press y for yes and n for no")
    if photo == "y":
        bill += 3

    print(f"you bill is{bill} ")

else:
    print("Sorry you have to grow taller before you can ride.")

#python pizza
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")

bill=0

if size =="S":
    bill += 15
elif size =="M":
    bill +=20
elif size =="L":
    bill +=25

if pepperoni == "Y":
    if size =="S":
        bill += 2
    else:
        bill += 3
if extra_cheese == "Y":
    bill += 1
print(f"Your final bill is: ${bill}.")

#logical operators
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))
    if age < 12:
        bill = 5
        print("Child tickets are $5.")
    elif age <= 18:
        bill = 7
        print("Youth tickets are $7.")
    elif age>=45 and age<=55:
        bill=0
        print("free to enjoy rollercoaster!")
    else:
        bill = 12
        print("Adult tickets are $12.")

    wants_photo = input("Do you want a photo taken? Y or N. ")
    if wants_photo == "Y":
        if age>=45 and age<=55:
            bill = 0
        else:
            bill += 3

    print(f"Your final bill is ${bill}")

else:
    print("Sorry, you have to grow taller before you can ride.")

#Treasure island project
print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
choice1=input("enter the what turn you have choose for continue your path left or right ? choose 1 ").lower()

if choice1=="left":
    choice2=input('you\'ve come to a lake. '
                  'There is an island in the middle of the lake.'
                  'Type "wait" to wait for a boat. '
                  'Type "swim" to swim across.')
    if choice2 == "wait":
        choose3=input("you arrived at the island unharmed."
              " There is house with 3 doors."
              "one red,one yellow and one blue . "
              "choose one of them")
        if choose3 == "red":
            print("you burnes by fire. game over.")
        elif choose3 == "yellow":
            print("you win!")
        elif choose3 == "blue":
            print("you eaten by beast. Game over .")
        else:
            print("Game over.you press invalid colour gate")

    else:
        print("you get attacked by an angry tout ,game over")

else:
    print("you fall into the hole.Game over")


