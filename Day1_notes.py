#VARIABLES

"""
- a variable is a container for storing data
- in Python, variables are created when you assign value to them
"""

# Assigning values to variables
name = "Alice"        # String
age = 25              # Integer
height = 5.4          # Float
is_happy = True       # Boolean

# Printing variable values
print(name)           # Output: Alice
print(age + 5)        # Output: 30

"""Rules for Variable Names:

- Must start with a letter or an underscore (_).
- Cannot start with a number.
- Can contain letters, numbers, and underscores.
- Case-sensitive (myVar and myvar are different). """

#DATA TYPES

"""Python has several built-in data types. Here are the most common ones:
Data Type	    Example
int	            5, -42, 100
float	        3.14, -0.1
str	            "Hello", 'World'
bool	        True, False
"""

# Checking data types
x = 10
y = 3.14
z = "Python"

print(type(x))  # Output: <class 'int'>
print(type(y))  # Output: <class 'float'>
print(type(z))  # Output: <class 'str'>

#OPERATORS

#Operators are used to perform operations on variables and values.
"""
Operator Type	Example	    Description
Arithmetic	    +, -	    Add, subtract, multiply, divide
Comparison	    ==, <	    Compare values (True/False) """

#arithmetic examples:
a = 10
b = 3

print(a + b)  # Addition: 13
print(a / b)  # Division: 3.3333
print(a % b)  # Modulus: 1 (remainder)

#comparison examples:
x = 5
y = 10

print(x > y)  # Output: False
print(x == 5) # Output: True

#GIT FUNDAMENTALS

#1. Key Git Commands

"""
git init       Initialize a new Git repository in your project folder.
git add        Stage files to be included in the next commit.
"""
#git add file_name.py   # Add a specific file
#git add .              # Add all files in the folder

"""git commit:  Save changes to the repository. """
#git commit -m "Your commit message"

"""
git status:     Check the current status of your repository.
git push:       Upload commits to a remote repository (e.g., GitHub)"""
#git push origin main
