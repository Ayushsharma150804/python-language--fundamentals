# Random module
import random
import own_module
rand_num= random.randint(1,10)
print(rand_num)
print(own_module.my_secret_num)

ram_num_0_1 =random.random() *5
print(ram_num_0_1)

random_float= random.uniform(1,10)
print(random_float)

num=random.randint(0,1)

if num==0:
    print("number is even")
else:
    print("number is odd")

#list
list=[1,2,3,4,5,6]
print(list)

fruits = ["cherry","Apple","Pear"]
print(fruits)

fruits.append("banana")
print(fruits)

fruits.extend(["orange","jackfruit"])
print(fruits)

print(fruits[1])
print(fruits[-2])
fruits[1]="guava"
print(fruits)

#Banker roulette
import random
friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]
print("Alice")

#method 1
print(random.choice(friends))
#method 2
random_index=random.randint(0,4)
print(friends[random_index])

#indexError
states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland",
                     "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island",
                     "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois",
                     "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin",
                     "California", "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado",
                     "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma",
                     "New Mexico", "Arizona", "Alaska", "Hawaii"]

print(states_of_america)

length=len(states_of_america)
print(states_of_america[length -1])

print(states_of_america[len(states_of_america) - 1])

fruits = ["Cherry", "Apple", "Pear"]
veg = ["Cucumber", "Kale", "Spinnach"]

dirty_item=[fruits,veg]
print(dirty_item)
print(dirty_item[0])
print(dirty_item[1])
print(dirty_item[1][1])
print(dirty_item[1][2])
print(dirty_item[0][1])

#rock paper scissor
import random
print("welcome to rock paper scissors game")
rock = ''''''
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game=[rock,paper,scissors]
user_input=int(input("enter the 0 for rock, 1 for paper , 2 for scissors"))
print(game[user_input])
computer_choice=random.randint(0,2)
print(f"computer choice is {game[computer_choice]}")

if user_input>=3 and user_input<0:
    print("you enter the invalid option.you loose!")
elif user_input==computer_choice:
    print("draw match")
elif user_input==1 and computer_choice==2:
    print("you loose!")
elif user_input<computer_choice:
    print("you win!")
elif computer_choice==1 and user_input==2:
    print("you win!")
elif computer_choice<user_input:
    print("you loose!")



