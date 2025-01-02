# 1. STRING METHODS

"""String methods are built-in functions you can call on strings to
manipulate or analyze them. Here's a quick overview of the most commonly
used methods:

Method	Description	Example
.lower()	    Converts all characters to lowercase	"HELLO".lower() → "hello"
.upper()	    Converts all characters to uppercase	"hello".upper() → "HELLO"
.strip()	    Removes leading/trailing whitespace	    " hello ".strip() → "hello"
.replace(a, b)	Replaces a with b	                    "apple".replace("p", "b") → "abble"
.split()	    Splits a string into a list (by default, at spaces)	    "hello world".split() → ["hello", "world"]
.join(iterable)	Joins elements of an iterable into a string	            ",".join(["a", "b", "c"]) → "a,b,c"
"""
# Examples:

# Converting case
print("Python".upper())      # Output: PYTHON
print("PYTHON".lower())      # Output: python

# Removing whitespace
print("   hello   ".strip()) # Output: hello

# Replacing and splitting
print("banana".replace("a", "o")) # Output: bonono
print("a,b,c".split(","))         # Output: ['a', 'b', 'c']

# Joining strings
words = ["Python", "is", "fun"]
print(" ".join(words))       # Output: Python is fun

# 2. Integer Operations

"""Python provides various functions to work with integers. 
These include mathematical operations and conversions.

Function/Operator	    Description	                Example
+, -, *, /	            Arithmetic operators	    5 + 3 → 8, 5 / 2 → 2.5
%	                    Modulus (remainder)	        10 % 3 → 1
//	                    Floor division      	    10 // 3 → 3
abs()	                Returns the absolute value	abs(-5) → 5
round()	                Rounds a number	            round(3.14159, 2) → 3.14
int(), float(), str()	Converts between types	    int("5") → 5
"""

#Examples:

# Arithmetic operations
print(5 + 3)          # Output: 8
print(10 % 3)         # Output: 1

# Floor division and absolute value
print(10 // 3)        # Output: 3
print(abs(-42))       # Output: 42

# Rounding and type conversion
print(round(3.14159, 2))  # Output: 3.14
print(int("42"))          # Output: 42


# 3. User Input

"""User input allows interaction with your program. You can collect data 
using the input() function and validate or transform it."""

#Input Basics:
name = input("Enter your name: ")  # Takes input as a string
age = int(input("Enter your age: "))  # Converts input to an integer
print(f"Hello {name}, you are {age} years old!")

"""Validating Input: Use try and except blocks to handle invalid input gracefully:
"""
try:
    age = int(input("Enter your age: "))
    print(f"In 5 years, you will be {age + 5} years old.")
except ValueError:
    print("Please enter a valid number.")

"""Key Practice Tips
Combine string methods and user input to build simple programs.
Experiment with type conversions and validations for interactive input."""
