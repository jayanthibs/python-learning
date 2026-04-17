# Data structures

# Lists

age = 25
has_license = False
my_list = ["Alice", 25, age, True, has_license]

#get single items
name = my_list[0]
age = my_list[1]

#change lists
my_list[0] = "Jaya"
my_list.append("Alice")
my_list.remove("Alice")
my_list.insert(3, "Alice")

print(my_list[2:3])    # start and end index



##Dictionaries


person = {
    "name": "Alice",
    "age": 25,
    "city": "New York"
}
#pull single value
person["age"]
#change value
person["name"] = "Dave"
#add new key value pair or field
person["license"] = True
#delete single value
del person["license"]



# Get all keys, values, or items
print(person.keys())    # dict_keys(['name', 'age', 'city'])
print(person.values())  # dict_values(['Alice', 30, 'New York'])
print(person.items())   # dict_items([('name', 'Alice'), ...])


#Tuples

# Empty tuple
empty = ()

# Tuple with items
point = (3, 5)
colors = ("red", "green", "blue")
#eror unchangable
colors[0] = "blue"


#set

# Empty set (careful!)
empty_set = set()  # NOT {} - that's a dict!

# Set with values - both ways work
numbers = {1, 2, 3, 4, 5}
fruits = set(["apple", "banana", "orange"])

# From a list (removes duplicates)
scores = [85, 90, 85, 92, 90]
unique_scores = set(scores)  # {85, 90, 92}