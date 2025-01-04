#TRY EXCEPT block

"""A `try-except` block is used to handle exceptions (runtime errors) that might occur during program execution. It prevents the program from crashing by catching and handling errors.
basic syntax:"""

try:
    # Code that might raise an exception
except ExceptionType:
    # Code to handle the exception

#You can handle specific exceptions separately or include a generic exception handler:
try:
    # Code that might raise an exception
except ValueError:
    # Handle ValueError specifically
except ZeroDivisionError:
    # Handle ZeroDivisionError specifically
except Exception as e:
    # Handle any other exceptions
    print(f"An unexpected error occurred: {e}")
else:
    # Executes if no exception occurs
finally:
    # Executes no matter what (useful for cleanup)

#EX:
    try:
        # Take two numbers as input
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))

        # Try to perform division
        result = num1 / num2
    except ValueError:
        print("Please enter valid integers.")
    except ZeroDivisionError:
        print("You cannot divide by zero.")
    else:
        print(f"The result is {result}.")
    finally:
        print("Thank you for using the division program!")


#STRING METHODS
words = " Words, words, words"
len(words)          #gives the len of the string
words.find("W")     #gives the index of the first occ of the character
words.rfind("s")    #gives the index of the last occ of the character
words.capitalize()  #capitalizes the first character
words.upper()       #uppercase of the string
words.lower()       #all lowercase
words.strip()       #strips the string of spaces in the beginning and end
words.isdigit()     #bool, if the string is numeric
words.isalpha()     #bool, if the string is only alphabetical
words.count("w")    #counts how many w's are in the string
words.replace(", ", " ")    # replaces ", " with " "
words.endswith(('s', 'x'))  #checks if the string ends with 's' OR 'x' (tuple can be provided)
help(str)           #gives all the methods for string type


#FOR LOOPS

#A for loop iterates over a sequence (e.g., string, list, range).

#Syntax:
for item in sequence:
    # Code to execute for each item

#Examples:

#Iterating Over Strings:
for char in "Python":
    print(char)

#Iterating with range():
for i in range(5):  # Loops from 0 to 4
    print(i)
# Output: 0, 1, 2, 3, 4

#WHILE LOOPS

#A while loop repeats as long as a condition is True.

#Syntax:
while condition:
    #Code to execute while condition is True

#Example:
counter = 5
while counter > 0:
    print(counter)
    counter -= 1
# Output: 5, 4, 3, 2, 1

#Loop Control Statements

#break: Exit the loop immediately.
for num in range(10):
    if num == 5:
        break
    print(num)
# Output: 0, 1, 2, 3, 4

#continue: Skip to the next iteration.
for num in range(5):
    if num == 3:
        continue
    print(num)
# Output: 0, 1, 2, 4


#ADVANCED Loop Techniques

#1. Enumerate in Loops
#When iterating over a sequence, you can use enumerate() to keep track of both the index and
#the item.

#Example: Numbering each character in a string.
string = "Python"
for index, char in enumerate(string):
    print(f"Index: {index}, Character: {char}")
# Output:
# Index: 0, Character: P
# Index: 1, Character: y
# ...

#2. Looping Over Multiple Iterables with zip()
#You can iterate over multiple sequences in parallel using zip().

#Example: Pairing items from two lists.
names = ["Alice", "Bob", "Charlie"]
scores = [85, 90, 95]
for name, score in zip(names, scores):
    print(f"{name} scored {score}.")
# Output:
# Alice scored 85.
# Bob scored 90.
# Charlie scored 95.

#3. Using List Comprehensions with Loops
#A list comprehension is a compact way to create a new list based on an existing iterable.

#Example: Square every number in a list.
numbers = [1, 2, 3, 4, 5]
squares = [num ** 2 for num in numbers]
print(squares)
# Output: [1, 4, 9, 16, 25]

#4. Loop with Else
#A for or while loop can have an else clause, which runs if the loop completes without
# hitting a break.

#Example: Check if a number is prime.
number = 29
for i in range(2, number):
    if number % i == 0:
        print(f"{number} is not a prime number.")
        break
else:
    print(f"{number} is a prime number.")
# Output: 29 is a prime number.

#5. Iterating Over Dictionaries
#Use .items() to loop through keys and values in a dictionary.

#Example: Displaying dictionary contents.
student_scores = {"Alice": 85, "Bob": 90, "Charlie": 95}
for student, score in student_scores.items():
    print(f"{student} scored {score}.")
# Output:
# Alice scored 85.
# Bob scored 90.
# Charlie scored 95.

#6. Filtering with Loops
#You can dynamically filter out specific elements during iteration.

#Example: Filtering out even numbers.
numbers = [1, 2, 3, 4, 5, 6]
odds = [num for num in numbers if num % 2 != 0]
print(odds)
# Output: [1, 3, 5]

#7. Using itertools for Infinite or Specialized Iterations
#Python’s itertools library provides advanced looping tools.

#Example: Create an infinite counter.
from itertools import count

for i in count(start=1, step=2):  # Infinite odd numbers
    print(i)
    if i > 9:
        break
# Output: 1, 3, 5, 7, 9
