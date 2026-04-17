name = "Alice"

age = 25

is_student = True


#numbers
# arithmatic operators
5 + 5
5 - 5
5 * 5
5 / 5



#string

string = "My name is Jayanthi"

my_long_string = """
My name is Jaya.
My last name is Bala.
"""

# string manipulation

first_name = "Jaya"
last_name = "Bala"

full_name = first_name + " " + last_name

long_dash = "-" * 30 

print(full_name)
print(long_dash)


# length of the string
len(full_name)
len(first_name)

# Booleans
is_Logged_in = True

age = 17
can_vote = age >= 18


age = 18
is_18 = age == 18




#Logical operators

age = 25
has_license = True
drunk = True


# AND - both must be true
can_drive = age >= 16 and has_license
print(can_drive)  # True

# OR - at least one must be true
day = "Saturday"
is_weekend = day == "Saturday" or day == "Sunday"
print(is_weekend)  # True

# NOT - reverses the value
is_adult = age >= 18
is_child = not is_adult
print(is_child)  # False


can_drive = age >= 16 and has_license and not drunk

# string manipulation

name = "Jaya"

string = "Hi there, my name is Jaya!"

#f strings
name = "Mithra"


string = f"Hi there, my name is {name}!"


#string methods

name = "Jaya"
name.lower()  # lowercase
name.upper() #uppercase

text = " I love the python programming"
text.title()   # first letter of all words to capital




# if-else

temperature = 25

if temperature > 25:
    print("It's hot!")
else:
    print("It's nice weather!")

#if-elif-else  -----1
temperature = 26

if temperature > 30:
    print("It's very hot!")
elif temperature > 25:
    print("It's hot!")
else:
    print("It's nice weather!")    


    #if-elif-else  -----2

score = 85

if score >= 90:
    print("A - Excellent!")
elif score >= 80:
    print("B - Good job!")
elif score >= 70:
    print("C - Keep it up!")
else:
    print("F - Need improvement")


# if-else and logical operators

age = 25
has_license = True

weekend = True
holiday = False
raining = True

# Both must be True
if age >= 18 and has_license:
    print("You can drive!")

# At least one must be True
if weekend or holiday:
    print("No work today!")

# Reverse the condition
if not raining:
    print("Let's go outside!")



#Nested if
has_ticket = True
age = 15

if has_ticket:
    if age >= 18:
        print("Enjoy the movie!")
    else:
        print("Need adult supervision")
else:
    print("Buy a ticket first")






#for loop starts from 0

for i in range(5):
    print(i)

#giving diff range to start
for i in range(1, 6):
    print(i)

#count by 2's
for i in range(0, 10, 2):
    print(i)