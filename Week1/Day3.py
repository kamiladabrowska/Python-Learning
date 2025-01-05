"""Exercise 1: Simple If-Else:
Write a program that asks the user for their age and:
Prints "Child" if they are under 12.
Prints "Teenager" if they are between 12 and 17.
Prints "Adult" otherwise."""

try:
    age = int(input("Hi! How old are you? "))
    if age < 12:
        print("Child")
    elif age <= 17:
        print("Teenager")
    else:
        print("Adult")
except ValueError:
    print("Please give me your age.")

"""Exercise 2: Nested If-Else:
Ask the user for their exam score and:
Print "A" if the score is 90 or above.
Print "B" if the score is 80–89.
Print "C" if the score is 70–79.
Print "F" otherwise."""

try:
    score = int(input("What is your score? ").strip())
    if score < 0:
        print("Your score can't be negative.")
    elif score <= 100:
        if score < 70:
            print("F")
        elif score < 80:
            print("C")
        elif score < 90:
            print("B")
        else:
            print("A")
    else:
        print("Please provide a score between 0 and 100.")
except ValueError:
    print("Please provide a valid numeric score.")

"""Exercise 3: Logical Operators:
Write a program that:
Asks the user for a number.
Checks if the number is divisible by both 2 and 3.
Prints appropriate messages for each case. """

try:
    number = int(input("Please give me a number: ").strip())
    if (number % 2 == 0) and (number % 3 == 0):
        print("Your number is divisible by both 2 and 3.")
    elif (number % 2 == 0) or (number % 3 == 0):
        if number % 2 == 0:
            print("Your number is divisible by 2.")
        else:
            print("Your number is divisible by 3.")
    else:
        print("Your number is not divisible by 2 nor 3.")

except ValueError:
    print("Please provide a number.")

"""Mini Challenge 1:
Ask the user to input a string.
Check if the string:
Starts with a vowel.
Ends with a punctuation mark.
Print messages based on the conditions."""

try:
    string = input("Please provide a string ").strip().lower()

    if not string:
        print("You haven't provided any text!")
    else:
        starts_with_vowel = string[0] in "eyuioa"
        ends_with_punct = string[-1] in ".,!?"
        if starts_with_vowel and ends_with_punct:
            print("Your string starts with a vowel and ends with a punctuation mark.")
        elif ends_with_punct:
            print("Your string ends with a punctuation mark.")
        elif starts_with_vowel:
            print("Your string starts with a vowel.")
        else:
            print("Your string doesn't start with a vowel or end with a punctuation mark.")
except Exception as e:
    print(f"Unexpected error: {e}.")

"""Exercise 1: f-strings Practice
Ask the user for their name and age.
Print a sentence like:
"Hello, Alice! You are 25 years old."""

try:
    name = input("Hello. What's your name? ").strip()
    age = input("How old are you? ").strip()
    if not name or not age:
        print("Please answer my questions!")
    else:
        print(f"Hello, {name}! You are {age} years old.")
except ValueError:
    print("Hello")

"""Exercise 2: If-Else with String Formatting
Ask the user for their favorite number.
Use an if-else statement to print:
"Your favorite number is odd."
"Your favorite number is even."
Format the message using either f-strings or .format()."""

try:
    number = int(input("What's your favorite number? ").strip())
    if number % 2 == 0:
        print(f"Your favorite number: {number} is even")
    else:
        print("Your favorite number {} is odd".format(number))
except ValueError:
    print("Please provide a valid number.")

"""Exercise 3: Nested If with Logical Operators
Ask the user for a year and check if it’s:
A leap year (divisible by 4 but not by 100, unless divisible by 400).
Print the result using f-strings."""

try:
    year = int(input("Please give me a year: ").strip())
    if year < 1:
        print("Please give me a valid year.")
    else:
        if year % 4 == 0:
            if year % 100 == 0 and year % 400 != 0:
                print(f"Year {year} is not a leap year.")
            else:
                print(f"Year {year} is a leap year.")
        else:
            print(f"Year {year} is not a leap year.")
except ValueError:
    print("Please provide a valid year.")

"""Mini Challenge 2:
Build a program that:
Asks the user to input their name and birth year.
Calculates their age and checks if they’re eligible to vote (age >= 18).
Uses f-strings to print:
"Hi, Alice! You are 25 years old and eligible to vote."
Or "Hi, Alice! You are 15 years old and not eligible to vote."

"""
try:
    name = input("What's your name? ").strip()
    birth_year = int(input("What's your birth year? ").strip())
    current_year = 2025
    age = current_year - birth_year
    if age < 0 or age > 120:
        print("Please provide a valid year.")
    else:
        if age >= 18:
            print(f"Hi, {name}! You are {age} years old and eligible to vote.")
        else:
            print(f"Hi, {name}! You are {age} years old and not eligible to vote.")

except ValueError:
    print("Please provide a valid year.")