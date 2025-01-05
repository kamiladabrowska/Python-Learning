"""Exercise 1: String Manipulation
Ask the user to enter their full name.
Convert the name to:
All lowercase.
All uppercase.
Replace all spaces with hyphens (-) and print the result."""

name = str(input("Hello! What's your full name? "))

print(name.lower())
print(name.upper())
print(name.replace(" ", "-"))

"""Exercise 2: Working with Numbers
Ask the user to input a number.
Calculate and print:
The square of the number.
The remainder when divided by 7.
The absolute value of the number.
"""
try:
    number = int(input("Hello! Please provide a number: "))
    print(f"Square of the number: {number ** 2}")
    print(f"Remainder when divided by 7: {number % 7}")
    print(f"Absolute value: {abs(number)}")
except ValueError:
    print("Please give me a number")

"""Exercise 3: String and Numbers
Ask the user to input a sentence.
Count and print:
The number of words in the sentence (using .split()).
The number of characters (excluding spaces)."""

try:
    sentence = input("Please, give me a sentence: ")
    num_words = len(sentence.split(" "))
    print(f"Your sentence is {num_words} words long.")
    num_chars = len(sentence.replace(" ", ""))
    print(f"Your sentence has {num_chars} characters without spaces. \n")
except ValueError:
    print("Please give me a sentence!")