print("Hello, World!") # Outputs: Hello, World!

# Variables
x = 5 # Integer variable
name = "Alice" # String variable
a,b,c = 1, 2, 3 # Multiple assignments

# Data Types 
integer = 10 # int
floating = 2.56 # float
string = "Hello"# str
boolean = True #bool 
my_list = [1, 2, 3] # list
my_tuple = (1, 2, 3) # tuple
my_dict = {"name":"Alice","age":25} # dict
my_set = {1 ,2 , 3} # set

# Control Flow
if x>0:
    print("x is positive")
elif x == O:
    print("x is zero")
else:
    print("x is negative")

for i in range(5):
    print(i) # Loops through numbers 0 to 4
while x < 10:
    x += 1 # Increment x by 1

# Functions
def my_function():
    return "Hello from function!"

# String Operations
upper_text = "Hello".upper() # "HELLO"
lower_text = "Hello".lower() # "hello"
split_text = "Hello World".split() # ['Hello', 'World']
joined_text = ",".join(["a", "b", "c"]) # "a,b,c"
replaced_text = "Hello".replace("H", "J") # "Jello"
length = len("Hello") # 5

# List Operations
my_list.append(4) # Adds 4 to my_list
my_list.remove(2) # Removes the first occurrence of
last_item = my_list.pop() # Removes and returns the last item
my_list.sort()# Sorts the list in ascending orde
my_list.reverse() # Reverses the order of the list

# Dictionary Operations
age = my_dict["age"] # Accesses the value associated with the key "age"
my_dict["age"] = 26 # Sets the value for the key "age
keys = my_dict.keys() # Returns all keys in the dictionary
values = my_dict.values() # Returns all values in the dictionary
items = my_dict.items() # Returns all key-value pairs

# File Operations
file = open("file.txt","r") # Opens a file for reading
file_content = file.read() # Reads the entire file
file.close() # Closes the file

# Error Handling
try:
    risky_code()
except ValueError:
    print("Caught a ValueError")
finally:
    print("This runs no matter what")

#Importing Modules
import math # Imports the entire math module
from math import sqrt  # Imports only the sqrt function from math
import math as m # Imports math with an alias

# Commonly Used Functions
length = len(my_list) # Returns the number of items in my_list
data_type = type(x) # Returns the type x
num_range = range(5) # Generates numbers from 0 to 4
total = sum([1, 2, 3]) # Returns the sum of all items in the list
smallest = min([1, 2, 3]) # Returns the smallest item in the list
largest = max([1, 2, 3]) # Returns the largest item in the list
absolute_value = abs(-5) # Returns the absolute value of -5
rounded_value = round(3.14159, 2) # Rounds to 2 decimal places

# List Comprehensions
squares = [x**2 for x in range(10)] # Creates a list of squares from 0 to 9

# Lamba Functions
increment = lambda x: x + 1 # Lambda function to add 1 to x

# Classes
class MyClass:
    def __init__(self, name)
        self.name = name # Constructor method

    def greet(self):
        return f"Hello,{self.name}!"

my_object = MyClass("Alice") # Creates an instance of MyClass
print(my_object.greet()) # 0utputs:Hello, Alice