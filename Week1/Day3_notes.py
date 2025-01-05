#Day 3 Notes: Conditionals, String Formatting, and Nested Logic

#1. Conditionals
'''Conditionals allow your program to make decisions based on specific conditions. The syntax includes if, elif, and else.
Syntax:'''

if condition:
    # Executes if the condition is True
elif another_condition:
    # Executes if the previous conditions are False, but this is True
else:
    # Executes if all conditions above are False

score = 85
if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
else:
    print("Grade: F")

"""Logical Operators:

and: All conditions must be True.
or: At least one condition must be True.
not: Reverses the truth value of a condition.

Example with Logical Operators: """

number = 12
if number % 2 == 0 and number % 3 == 0:
    print("Divisible by both 2 and 3")
elif number % 2 == 0 or number % 3 == 0:
    print("Divisible by either 2 or 3")
else:
    print("Not divisible by 2 or 3")

#2. String Formatting
#String formatting dynamically embeds variables or expressions into strings.

"""a) f-strings (formatted strings):

Introduced in Python 3.6, f-strings use {} to include variables or expressions.
Syntax: Prefix the string with f.
Examples: """

name = "Alice"
age = 25
print(f"Hello, {name}! You are {age} years old.")  # Output: Hello, Alice! You are 25 years old.

#Inline expressions:
print(f"Next year, you will be {age + 1}.")  # Output: Next year, you will be 26.

# b) .format() Method:

"""The .format() method replaces placeholders {} in strings with specified values.
Useful for older versions of Python.
Examples:"""

name = "Alice"
age = 25
print("Hello, {}! You are {} years old.".format(name, age))  # Output: Hello, Alice! You are 25 years old.

# Using positional arguments
print("{1} is {0} years old.".format(age, name))  # Output: Alice is 25 years old.

#3. Nested Logic
#Conditionals can be nested inside each other for more complex logic.

#Example: Checking if a year is a leap year:

year = 2000
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap year")
        else:
            print("Not a leap year")
    else:
        print("Leap year")
else:
    print("Not a leap year")

#Simplified using elif:
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Leap year")
else:
    print("Not a leap year")

"""Tips for Writing Clear Conditionals
- Avoid unnecessary nesting by using elif or logical operators.
- Use comments to explain complex logic.
- Validate user input to ensure conditions work as expected.
- Key Examples

Odd or Even with String Formatting:"""

number = 7
if number % 2 == 0:
    print(f"{number} is even.")
else:
    print(f"{number} is odd.")

#Validating Input:

try:
    age = int(input("Enter your age: ").strip())
    if age < 0 or age > 120:
        print("Please provide a valid age.")
    else:
        print(f"You are {age} years old.")
except ValueError:
    print("Please provide a valid number.")
