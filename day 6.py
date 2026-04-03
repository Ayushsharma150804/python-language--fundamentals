#function : A function in its simplest form is just a wrapper name for a block of code. 
# You give it name and then when you call the function by that name, all the code within the function block will be executed. 
# It can help us save time and reduce repeated code.



print("Hello World")

#Defining a new Function
#def <function name>():
 #   print("Hello")
    # Do something else
    # Do something else ...

def my_function():
    print("Hello World")
    print("byee")

my_function()

def get_user_name():
    name = input("what is your name? ")
    print(f"Hello {name}")
print("Hello")
get_user_name()

# #more seen in reeborg,s world
# def turn_around():
#     turn_left()
#     turn_left()
#
#
# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()
#
#
# move()
# move()
# move()
# turn_left()
# turn_right()
# turn_around()
# move()
# move()
# move()

# #reeborg  hurdel 1
# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()
#
#
# def jump():
#     move()
#     turn_left()
#     move()
#     turn_right()
#     move()
#     turn_right()
#     move()
#     turn_left()
# )
#
# for i in range(6):
#     jump()
#
# number_of_jumps=6
# while number_of_jumps>0:
#     jump()
#     number_of_jumps -= 1
#     print(number_of_jumps)

#4 spaces for indentation



num=4
while num>0:
    print(num)
    num -= 1

#reeborg hurdel2

# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()
#
#
# def jump():
#     move()
#     turn_left()
#     move()
#     turn_right()
#     move()
#     turn_right()
#     move()
#     turn_left()
#
#
# # number_of_jumps=6
# # while at_goal()!= True:
# #    jump()
#
# while not at_goal():
#     jump()
#     print(at_goal())

while 5>3:
    print("infinite loo")

# #reeborg hurdel3
# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()
#
#
# def jump():
#     turn_left()
#     while wall_on_right():
#         move()
#     turn_right()
#     move()
#     turn_right()
#
#     while front_is_clear():
#         move()
#     turn_left()
#
# while not at_goal():
#     if wall_in_front():
#         jump()
#     else:
#         move()

# #reeborg maze world
# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()
#
#
# while front_is_clear():
#     move()
#turn_left()
# while not at_goal():
#     if right_is_clear():
#         turn_right()
#         move()
#     elif front_is_clear():
#         move()
#     else:
#         turn_left()











