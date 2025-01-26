"""1. Function with Default and Keyword Arguments
Write a function that calculates the total cost of an order:
It should take item_cost (mandatory), quantity (default 1), and discount (default 0).
Return the total cost after applying the discount."""

def total_cost(item_cost, discount=0, quantity=1):
    if discount == 0:
        return item_cost * quantity
    else:
        return (item_cost * quantity)*(100-discount)/100

"""2. Lambda with List Transformation
Given a list of numbers, use a lambda function inside map() to square each number. Return the new list."""

numbers = [1, 2, 3, 4, 5, 6]
squared_numbers = list(map(lambda x: x*x, numbers))

"""3. Nested Lists
Create a 3x3 matrix representing a tic-tac-toe board:
Use X, O, or - to represent empty spots.
Print the board row by row."""

tic_tac_toe = [
    ["X", "X", "O"],
    ["-", "X", "O"],
    ["O", "O", "X"]
]

for row in tic_tac_toe:
    print(row)

"""4. Combining Functions and Lists
Write a function that:
Accepts a list of numbers.
Returns the maximum number, minimum number, and their difference."""

def min_max_difference(*numbers):
    return min(numbers), max(numbers), max(numbers) - min(numbers)

"""5. Mini Challenge
Build a grade calculator:
Accept a dictionary where keys are student names, and values are lists of their scores (e.g., {"Alice": [80, 90], "Bob": [70, 85]}).
Write a function to calculate the average score for each student.
Write another function to find the student with the highest average."""

def average_score(**kwargs):
    averages = {}
    for student, scores in kwargs.items():
        averages[student] = sum(scores) / len(scores)
    return averages

student_scores = {
    "Alice": [80, 90, 100],
    "Bob": [70, 75, 80],
    "Charlie": [85, 90]
}

#Exercise: Practice Using Lambda Functions

"""1. Take a list of numbers and use map() with a lambda function to calculate the cube of each number.
Example input: [1, 2, 3] → Output: [1, 8, 27]"""

numbers = [1, 2, 3, 4]
numbers_cubed = list(map(lambda x: x*x*x, numbers))

print(numbers_cubed)

"""2. Take a list of numbers and use filter() with a lambda function to extract numbers greater than 10.
Example input: [5, 10, 15, 20] → Output: [15, 20]"""

numbers = [1, 4, 6, 11, 24, 56]

greater_than_10 = list(filter(lambda x: x > 10, numbers))
print(greater_than_10)

"""3. Sort a list of dictionaries by a specific key using sorted() and a lambda function.
Example input: [{'name': 'Alice', 'age': 25}, {'name': 'Bob', 'age': 20}]
Output: Sorted by age → "[{'name': 'Bob', 'age': 20}, {'name': 'Alice', 'age': 25}]"
"""
user_information = [{'name': 'Alice', 'age': 25}, {'name': 'Bob', 'age': 20}]
sorted_info = sorted(user_information, key=lambda person: person["age"])
print(sorted_info)