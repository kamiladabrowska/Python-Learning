"""Day 4 Exercises
Exercise 1: For Loop with Strings
Write a program to print each character of a string on a new line."""

string = input("Please give me a string of text: ")
for char in string:
    print(char)

"""Exercise 2: Countdown Timer with While Loop
Create a program that counts down from 10 to 0 using a while loop."""

i = 10
while i >= 0:
    print(i)
    i -= 1

"""Exercise 3: Combining Loops and Conditionals
Write a program that asks the user for a sentence and:
Counts the number of vowels in the sentence using a for loop."""

sentence = input("Please give me a sentence: ").lower()
vowels = 'eyuioa'
count = 0
if not sentence:
    print("You gave me an empty input.")
else:
    for letter in sentence:
        if letter in vowels:
            count += 1
    print(f"Your sentence has {count} vowels.")

"""Mini Challenge:
Build a program that:
Asks the user to input a number.
Prints the multiplication table for that number (from 1 to 10) using a for loop."""

try:
    number = int(input("Please give me a number: "))
except ValueError:
    print("Please provide a valid integer")
else:
    for i in range(1,11):
        print(f"{number} * {i} = {number * i}")

#Exercises to Practice Advanced Looping

"""Exercise 1: Enumerate and List Comprehension
Take a sentence as input.
Create a list of tuples where each tuple contains the index of a word and the word itself.
Example Input: "Learning Python is fun" Expected Output: [(0, "Learning"), (1, "Python"), (2, "is"), (3, "fun")]
"""

sentence2 = input("Please give me a sentence: ").strip()
if not sentence2:
    print("You did not provide a sentence.")
else:
    a_list = [(index, word) for index, word in enumerate(sentence2.split())]
    print(a_list)

"""
Exercise 2: Filtering with Loops
Ask the user for a list of numbers (comma-separated).
Filter out all numbers divisible by 3 and return the new list.
Example Input: "3, 6, 7, 8, 9" Expected Output: [7, 8]"""

numbers_list = input("Please give me a list of numbers (comma-separated): ").split(", ")
if not numbers_list:
    print("Please give me a list of numbers.")
else:
    new_list = [number for number in list(numbers_list) if int(number) % 3 != 0]
    print(new_list)

"""Exercise 3: Prime Numbers with Else
Write a program that asks the user for a number and determines if it’s a prime number.
Use a for-else loop to implement the check."""

try:
    user_number = int(input("Please give a number: "))
except ValueError:
    print("Please provide a valid number: ")
else:
    for i in range(2, user_number):
        if user_number % i == 0:
            print(f"Number {user_number} is not a prime number.")
            break
    else:
        print(f"Number {user_number} is a prime number.")


"""Exercise 4: Using zip()
Ask the user for two lists of equal length (comma-separated).
Combine the two lists into a list of tuples.
Example Input:
First List: "apple, banana, cherry"
Second List: "red, yellow, purple"
Expected Output: [("apple", "red"), ("banana", "yellow"), ("cherry", "purple")]"""

print("You will be asked to provide two comma-separated lists of the same length.")
first_list = input("Please give me the first list: ").split(", ")
second_list = input("Please give me the second list: ").split(", ")
if len(first_list) != len(second_list):
    print("The length of the lists is not the same.")
else:
    for element1, element2 in list(zip(first_list, second_list)):
        print(element1, element2)
