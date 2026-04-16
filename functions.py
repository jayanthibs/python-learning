#Example1

def greet():
    print("Hello!")
    print("Hello Again!")
    pass  # doesnt return anything

greet()

#Example2

def check_weather():
    temperature = 16
    if temperature > 25:
        print("It's hot!")
    else:
        print("It's nice weather")

check_weather()

#Example3 - parameters

def greet(name):
    print(f"Hello, {name}")

greet("Alice")

#example4 
def greet(first_name, last_name):
    print(f"Hello, {first_name} {last_name}")

greet("Alice", "Henderson")

#example4 

def greet(first_name, last_name):
    print(f"Hello, {first_name} {last_name}")

greet(last_name = "Henderson", first_name = "Alice" )



#example5 - default parameter
def greet( last_name, first_name = "John"):
    print(f"Hello, {first_name} {last_name}")

greet(last_name = "Henderson" )


# eaxmple1
def calculate_total(price, tax_rate, discount):
    tax = price * tax_rate
    final_price = price + tax - discount
    print(f"Total: ${final_price}")

# Order matters!
calculate_total(100, 0.08, 10)  # $98


# eaxmple2
def calculate_total(price, tax_rate, discount):
    tax = price * tax_rate
    final_price = price + tax - discount
    print(f"Total: ${final_price}")

# Order dosent matter
calculate_total(price=100, tax_rate=0.08, discount= 10)  # $98

#return value

#1
def add_print(a, b):
    print(a+b)

add_print(a=5, b=10)


def add_print(a, b):
    return a+b

result = add_print(a=5, b=10)

#another examplefor return 

def calculate_area(width, height):
    area = width * height
    return area

# Store the returned value
room_area = calculate_area(10, 12)
print(f"Room size: {room_area} sq ft")  # Room size: 120 sq ft


#multiple return

def simple_function():
    numbers = [1, 2, 3, 4, 5]
    first_number = numbers[0]
    last_number = numbers[-1]
    return first_number, last_number

first_number, last_number = simple_function()
print(first_number, last_number)