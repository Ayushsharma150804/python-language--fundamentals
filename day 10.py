#function with output
def format_name(f_name, l_name):
    f_name = f_name.title()
    l_name = l_name.title()   #title function convert value in 1st latter in upper case and others in small case
    print(f"{f_name} {l_name}")
format_name("ayush", "AYUSH")

def format_name(f_name, l_name):
    print(f"{f_name} {l_name}")
format_name("ayush".title(), "AYUSH".title())

#function contain body, input ,and output
def create(creation):
    return creation+creation

def model(number):
    return number.title()

output_function = create("watch")
print(output_function)

output = model(create("watch more"))
print(output)

def number(num):
    return num+num.title()
def mul():
    return 2*2
out=mul()
out=number("num")
print(out)

#multiple return values
def format_name(f_name, l_name):
    if f_name == "" or l_name == "":
        return "You did not enter your first and last name"
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"Result:{formated_f_name} {formated_l_name}"


#directly printing
print(format_name("AnGEla", "YU"))
print(format_name(input("enter your first name: "), input("enter your last name: ")))

#function output store in variable
output = format_name(input("enter your first name: "), input("enter your last name: "))
print(output)

length = len(output)
print(length)

##Return as an early exit
def format_name(f_name, l_name):
    if f_name == "" or l_name == "":
        return "You did not enter your first and last name"
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"result:{formated_f_name} {formated_l_name}"

#leap year
def is_leap_year(year):
    # Write your code here.
    if year%4==0 and year%100 !=0 or year%400==0:
        return True
    else:
        return False
    # Don't change the function name.
is_leap_year(2026)

#or another way leap year
def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

#Docstring  '''.........''' 
def format_name(f_name, l_name):
    '''this is Docstring use for
        multiline comment and also use for define a function'''
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"{formated_f_name} {formated_l_name}"


formatted_name = format_name("AnGeLa", "YU")

length = len(formatted_name)

#if we can store function in variable we can only function name nor paranthesis in value
formatting=format_name
print(formatting("ayush", "sharma"))


#calculator perform multiply,division,subtraction,adition

def add(n1, n2):
    return n1 + n2

#TODO 1: Write out the other 3 functions - subtract, multiply and divide.
def subtract(n1,n2):
    return n1-n2

def multiplication(n1, n2):
    return n1*n2

def division(n1, n2):
    return n1/n2

#TODO 2: Add these 4 functions into a dictionary as the values. Keys = "+", "-", "*", "/"

oprations  ={
    "+" : add,
    "-" : subtract,
    "*" : multiplication,
    "/" : division
}

#TODO 3: Use the dictionary operations to perform the calculations. Multiply 4 * 8 using the dictionary.

if '*' in oprations:
    operation = oprations["*"]
    print(operation(int(input('enter a first number: ')), int(input('enter a second number:'))))

print(oprations["*"](4, 8))
#*****frustated********
yes = True
perform = input("'+' , '-' , '*' , '/' ")
if perform in oprations:
   result = oprations[perform](int(input("enter th first number")), int(input("enter the second number")))
   print(result)
   conti = input("enter 'yes' if perform opration with previous output or 'no' for new input")
   while yes:
       if conti=='yes':
          result=(oprations[input("'+' , '-' , '*' , '/' ")](result, int(input("enter a second number: "))))
          print(result)
       elif conti=='no':
           print(oprations[input("'+' , '-' , '*' , '/' ")](int(input("enter the first number")), int(input("enter a second number: "))))



#******************fresh new calculator ********************
logo = r"""
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""

def add(n1, n2):
     return n1 + n2

def subtract(n1,n2):
    return n1-n2

def multiplication(n1, n2):
    return n1*n2

def division(n1, n2):
    return n1/n2

operations  ={
    "+" : add,
    "-" : subtract,
    "*" : multiplication,
    "/" : division
}
def calculator():
    print(logo)
    num1= float(input("Enter the first number: "))
    should_accumulate = True
    while should_accumulate:
        for symbol in operations:
            print(symbol)
        choice_symbol = input("choose an operation: ")
        num2 = float(input("Enter the second number: "))
        answer= operations[choice_symbol](num1, num2)
        print(f"{num1} {choice_symbol} {num2} = {answer}")
        conti = input(f"Type 'y' to continue with {answer} or Type 'n' to start new calculation: ").lower()

        if conti == "y":
            num1 = answer
        else:
            should_accumulate = False
            print("\n" * 20)
            calculator()

calculator()








