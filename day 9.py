#dictionary
programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again."}
#items from the dictionary
print(programming_dictionary["Bug"])

#empty dictionary
my_empty_dictionary = {}

#add new items in exiting dictionary
programming_dictionary["Loop"] = "The action of doing something over and over again."
print(programming_dictionary)

#edit exiting value in dictionary
programming_dictionary["Bug"] = "A moth in a computer"
print(programming_dictionary)

#empty existing dict
# programming_dictionary = {}
print(programming_dictionary)

#loop in a dictionary
for key in programming_dictionary:
    print(key)        #only return key not with value

#in loop want with value
for key in programming_dictionary:
    print(key)  # only return key not with value
    print(programming_dictionary[key])

# Grading Program
# You have access to a database of student_scores in the format of a dictionary. The keys in student_scores are the names of the students and the values are their exam scores.
# Write a program that converts their scores to grades.
student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

student_grades = {}
for grade in student_scores:
    if student_scores[grade] >= 91:
        student_grades[grade] = "Outstanding"
    elif student_scores[grade] >= 81:
        student_grades[grade] = "Exceeds Expectations"
    elif student_scores[grade] >= 71:
        student_grades[grade] = "Acceptable"
    else:
        student_grades[grade] = "Fail"

print(student_grades)

#nesting of dictionary
cpitals = {
    "india": "new delhi",
    "china": "hong kong",
    "nepal": "bhutan"
}

max()
travel ={
    "madhya pradesh": ["rewa" , "sidhi", "sigrauli", "mohonina"],   #neting of list on dictionary
    "assam": ["dajling", "dispur"]
}
print(travel["madhya pradesh"])
print(travel["madhya pradesh"][2])

#nesting of list into list that called 2D list
alphabet = ['a','b','c',['d','e']]
print(alphabet[3][0])

#nesting of dictionary in dictionary
watches = {
    "diollo": {
        "number of watches": 1,
        "wear times" : 50,
        "type": "automatic"
    },
    "fastrack" : "digital"
}

print(watches["diollo"])
print(watches["diollo"]["wear times"])

# Which line of code will change the starting_dictionary to the final_dictionary?

starting_dictionary = {
    "a": 9,
    "b": 8,
}


final_dictionary = {
    "a": 9,
    "b": 8,
    "c": 7,
}

starting_dictionary['c']=7
final_dictionary = starting_dictionary
print(final_dictionary)

#nested list and dictionary
travel_log = {
  "France": {
    "cities_visited": ["Paris", "Lille", "Dijon"],
    "total_visits": 12
   },
  "Germany": {
    "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
    "total_visits": 5
   },
}
print(travel_log["Germany"]["cities_visited"][2])

#Blind Auction Project
logo = r'''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''

print(logo)
# TODO-1: Ask the user for input


# TODO-2: Save data into dictionary {name: price}

# TODO-3: Whether if new bids need to be added

# TODO-4: Compare bids in dictionary

def find_highest_bidding(bidding_dictionary):
    highest_bid = 0
    winner =""
    for key in bidding_dictionary:
        current_bid = bidding_dictionary[key]
        if current_bid > highest_bid:
            highest_bid = current_bid
            winner = key
    print(f"The winner is {winner} with a bid of rupee{highest_bid}")


bids ={}
bid_continue=True

while bid_continue:
    name = input("Enter your name: ")
    bid_price = int(input("Enter your bid price: rupee"))

    bids[name] = bid_price

    conti = input("Do you want to continue (y/n)? ").lower()
    if conti == "n":
        bid_continue = False
        find_highest_bidding(bids)
    elif conti == "y":
        print("\n "*20)
