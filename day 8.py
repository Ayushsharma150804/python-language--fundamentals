#user define function
def greet():
    print("hello world")
    print("hii")
    print("byee")

greet()

#function with input

def greet_with_name(name):
    print(f"hello {name}")
    print(f"how are you {name}")
    print(f"bye {name}")

greet_with_name("ayush")   #parameter-greet_with_name   argument-ayush
greet_with_name(123)

#I was reading this article by Tim Urban - Your Life in Weeks and realised just how little time we actually have.
#Create a function called life_in_weeks() using maths and f-Strings that tells us how many weeks we have left, if we live until 90 years old.

def life_in_weeks(age):
    years_remaining = 90 - age
    weeks_remaining = years_remaining * 52
    print(f"You have {weeks_remaining} weeks left.")


life_in_weeks(12)

# Functions with input

def greet_with_name(name):
    print(f"Hello {name}")
    print(f"How do you do {name}?")


greet_with_name("Jack Bauer")

def greet_with(name, location):
    print(f"hello {name} your location is {location}")
#positional arguments
greet_with("ayush", "india")
greet_with("india","ayush")

#keyword arguments
greet_with(location="india", name="Ayush")

#love calculator
# way 1
def calculate_love_score(name1, name2):
    T = ["t", "r", "u", "e"]
    L = ["l", "o", "v", "e"]

    i = ""
    len1 = 0
    for i in T:
        count = name1.count(i)  #count function use for count thr number of argument in vriable and outpot in intier form
        len1 += count
    i = ""
    len2 = 0
    for i in T:
        count1 = name2.count(i)
        len2 += count1

    add1 = len1 + len2

    i = ""
    len3 = 0
    for i in L:
        count2 = name1.count(i)
        len3 += count2

    i = ""
    len4 = 0
    for i in L:
        count3 = name2.count(i)
        len4 += count3

    add2 = len3 + len4

    print(f"{add1}{add2}")

#way 2
calculate_love_score(name1="Ayush".lower(), name2="deepti".lower())


def calculate_love_score(name1, name2):
    combined_names = name1 + name2
    lower_names = combined_names.lower()

    t = lower_names.count("t")
    r = lower_names.count("r")
    u = lower_names.count("u")
    e = lower_names.count("e")
    first_digit = t + r + u + e

    l = lower_names.count("l")
    o = lower_names.count("o")
    v = lower_names.count("v")
    e = lower_names.count("e")
    second_digit = l + o + v + e

    score = int(str(first_digit) + str(second_digit))
    print(score)


calculate_love_score("Kanye West", "Kim Kardashian")
name1=input("enter the name")
len1=0
L=["l","o","v","e"]
for i in L:
    count=name1.count(i)
    len1 += count
    print(f"{i} is {len1}")

#Caesar cipher 1 

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


# TODO-1: Create a function called 'encrypt()' that takes 'original_text' and 'shift_amount' as 2 inputs.

def encrypt(original_text, shift_amount):
# TODO-2: Inside the 'encrypt()' function, shift each letter of the 'original_text' forwards in the alphabet
    encrypted_text = ""
    for i in original_text:
        encrypted_text = alphabet.index(i) + shift_amount
        # TODO-4: What happens if you try to shift z forwards by 9? Can you fix the code?
        encrypted_text %= len(alphabet)
        cipher_text =alphabet[encrypted_text]


#  by the shift amount and print the encrypted text.
    print(f"here is the encoded result {cipher_text}")


# TODO-3: Call the 'encrypt()' function and pass in the user inputs. You should be able to test the code and encrypt a
#  message.
encrypt(text, shift)



#Caesar cipher 2.

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


# TODO-1: Create a function called 'decrypt()' that takes 'original_text' and 'shift_amount' as inputs.
def decrypt():
    decoder = ""
    for letter in text_input:
        apha = alphabet.index(letter) - shift_amount
        decoder += alphabet[apha]
    print(f"here is the decode result {decoder}")


# TODO-2: Inside the 'decrypt()' function, shift each letter of the 'original_text' *backwards* in the alphabet
#  by the shift amount and print the decrypted text.
# TODO-3: Combine the 'encrypt()' and 'decrypt()' functions into one function called 'caesar()'.
#  Use the value of the user chosen 'direction' variable to determine which functionality to use.

def encrypt(original_text, shift_amount):
    cipher_text = ""
    for letter in original_text:
        shifted_position = alphabet.index(letter) + shift_amount
        shifted_position %= len(alphabet)
        cipher_text += alphabet[shifted_position]
    print(f"Here is the encoded result: {cipher_text}")


encrypt(original_text=text, shift_amount=shift)
decrypt(original_text=text, shift_amount=shift)

def caesar(direct, original_text, shift_amount):
    if direct =="encode":
        cipher = ""
        for letter in original_text:
            shifted_position = alphabet.index(letter) + shift_amount
            shifted_position %= len(alphabet)
            cipher += alphabet[shifted_position]
        print(f"here is the encoded result: {cipher}")
    elif direct =="decode":
        cipher = ""
        for letter in original_text:
            shift_amount *= -1

            shifted_position = alphabet.index(letter) + shift_amount
            shifted_position %= len(alphabet)
            cipher += alphabet[shifted_position]
        print(f"Here is the {direct}d result: {cipher}")

def caesar(original_text, shift_amount, encode_or_decode):
    cipher = ""
    for letter in original_text:

         if encode_or_decode == 'decode':
             shift_amount *= -1

         shifted_position = alphabet.index(letter) + shift_amount
         shifted_position %= len(alphabet)
         cipher += alphabet[shifted_position]
    print(f"here is the {direction} result: {cipher}")



caesar(text, shift, direction)

#Caesar cipher 3 and finsl complete.

logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""

# TODO-1: Import and print the logo from art.py when the program starts.
print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# TODO-2: What happens if the user enters a number/symbol/space?


def caesar(original_text, shift_amount, encode_or_decode):
    output_text = ""
    if encode_or_decode == "decode":
        shift_amount *= -1

    for letter in original_text:

        if letter not in alphabet:
            output_text += letter
        else:
            shifted_position = alphabet.index(letter) + shift_amount
            shifted_position %= len(alphabet)
            output_text += alphabet[shifted_position]
    print(f"Here is the {encode_or_decode}d result: {output_text}")


# TODO-3: Can you figure out a way to restart the cipher program?

should_continue = True

while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)

    restart = input("Type 'yes' for continue or 'no' for quit.\n ").lower()
    if restart == "no":
        should_continue = False
        print("Goodbye")
