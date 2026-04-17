# from turtle import Turtle, Screen
#
# timmy =Turtle()
# print(timmy)
# timmy.shape("turtle") # object with method
# timmy.color("coral")# object with method
# timmy.forward(100)# object with method
#
#
# my_screen = Screen()
# print(my_screen.canvheight)  #object with attribute
# my_screen.exitonclick()   #object with method
#
from prettytable import PrettyTable

table = PrettyTable()
table.add_column("Pokemon Names",['Pikachu','Squirtle','Charmander'])
table.add_column("Type",['Electric','water','Fire'])
# table.add_row(["pokemon Name",5,6,7,8])
table.align = ("l")  #aling is feild or attribute or variable
print(table )


