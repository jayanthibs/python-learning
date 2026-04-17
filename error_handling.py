# Missing colon
# if x > 5  # SyntaxError
#     print("Big number")


# Division by zero
result = 10 / 0  # ZeroDivisionError

# Variable doesn't exist
# print(score)  # NameError

# Wrong type
"hello" + 5  # TypeError


#------------------------------------------

try:
    result = 10 / 0 
except:
    print("Hi there!")