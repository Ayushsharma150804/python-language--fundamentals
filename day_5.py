#for loop
#Loops allow us to tell the computer to repeat actions without having to write repeated code. 
#If we wanted the computer to print out 1 through to 100, it would very painful to type a print statement for every number,
#or even just typing out all the numbers 1 through to 100. 
#Loops allow us to create a rule and the computer can follow it to do a repeated action.

fruits = ["Apple", "Peach", "Pear"]
for fruit in fruits:
    print(fruit)
    print(fruit + ' pie')
    print(fruits)

fru = ["Apple", "Peach", "Pear"]
for fruit in fru:
    print(fruit)
    print(fruit + ' pie')
print(fruits)


#Highest Score
student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]
print(range(1, 10))
total = sum(student_scores)
print(total)

sum=0
for score in student_scores:
    sum += score
print(sum)

print(max(student_scores))

max_score=0
for score in student_scores:
    if score>max_score:
        max_score=score
        print(max_score)


#For loop with range
for number in range(1,10):
    print(number )

for number in range(1,11):
    print(number)
for i in range(1,11,3):
    print(i)

sum=0
for number in range(1,101):
    sum += number
print(sum)

sum = 0
for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 5 == 0:
        print("Buzz")
    elif i % 3 == 0:
        print("Fizz")
    else:
        print(i)

#Password Generator Project

import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#easy level
password = ""
for char in range(0, nr_letters):
    password += random.choice(letters)

for char in range(0, nr_symbols):
    password += random.choice(symbols)
for char in range(0, nr_numbers):
    password += random.choice(numbers)
pass_len=len(password)
passw=""
for char in range(0, pass_len):
     passw += random.choice(password)

print(passw)

#hard level

password_list = []
for char in range(0, nr_letters):
    password_list.append(random.choice(letters))
for char in range(0, nr_symbols):
    password_list.append(random.choice(symbols))
for char in range(0, nr_numbers):
    password_list.append(random.choice(numbers))

print(password_list)
random.shuffle(password_list)
print(password_list)

password = ""
for char in password_list:
    password += char

print(f"your password is: {password}")







