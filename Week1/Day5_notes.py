#1. Functions
#a) Basics: Defining Functions
#A function is a reusable block of code that performs a specific task.

#Syntax:

def function_name(parameters):
    # Code to execute
    return result

#Example:

def greet(name):
    return f"Hello, {name}!"

print(greet("Alice"))  # Output: Hello, Alice!

#b) Default and Keyword Arguments
#Functions can have default values for parameters, which are used if no value is provided.

#Example:
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

print(greet("Bob"))  # Output: Hello, Bob!
print(greet("Alice", "Hi"))  # Output: Hi, Alice!

#c) Variable-Length Arguments (*args and **kwargs)

#*args: Accepts any number of positional arguments as a tuple.
#**kwargs: Accepts any number of keyword arguments as a dictionary.

#Example:
def summarize(*args, **kwargs):
    print("Positional arguments:", args)
    print("Keyword arguments:", kwargs)

summarize(1, 2, 3, name="Alice", age=25)
# Output:
# Positional arguments: (1, 2, 3)
# Keyword arguments: {'name': 'Alice', 'age': 25}

#d) Lambda Functions
#A lambda function is a small anonymous function that can have any number of arguments but only one expression.

#Example:
square = lambda x: x ** 2
print(square(5))  # Output: 25
