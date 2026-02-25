#data types :Learn about the primitive data types in Python.Strings,Integers,Floats,Booleans
len("Hello")
print("hello"[0])
print("hello"[1])
print("hello"[-1])

#type erroe checking and conversion : TypeError These errors occur when you are using the wrong data type. e.g. len(12345) Because you can only give the len() function Strings, it will refuse to work and give you a TypeError if you give it a number (Integer).
print(len("12345"))

print((type("1234")))
print(type(1234))
print(type(True))
print(type(12.3))

print("number of latter in your name" + str(len(input("enter your name"))))

#mathematical operations :Basic Operators Learn to use the basic mathematical operators, +, -, *, /, // and ** PEMDAS Parentheses, Exponents, Multiplication/Division, Addition/Subtraction
print("My age: " + str(12))
print(3*3+3/3-3)
print(3 * 3 + 3 / 3 - 3)

#number manuplation 
bmi = 84 / 1.65 ** 2
print(bmi)
print(type(bmi))
print(int(bmi))
print(round(bmi))
print(round(1.6))
print(round(bmi, 2))

age=5
name=5
age += name
print(age)
age -= name
print(age)
age *= name
print(age)
age /= name
print(age)

aage=12
print(f"I am {age} yers old")

#tip calculator project 
print("welcome to the tip calculator!")
bill = float(input("what was the total bill? in rupee"))
tip = int(input("what percentage would you like to give the tip?"))
people = int(input("how many people to split the bill?"))
calculate_total_bill =( bill*(tip/100) + bill)/people
print(f"each person should pay in rupee {calculate_total_bill} ")
