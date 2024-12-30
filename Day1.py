"""Exercise 1: Variables
Write a Python program to:
Store your name, age, and favorite number in variables.
Print them all on separate lines.
"""
name = input("Please share your name with me: ")
age = int(input("How old are you? "))
favorite_number = int(input("What's your favorite number? "))

print(name)
print(age)
print(favorite_number)

"""
Exercise 2: Arithmetic Operators
Write a Python program that:
Asks the user to input two numbers.
Calculates and prints the sum, difference, product, and quotient of the numbers."""

num1 = int(input("Please give me a first number: "))
num2 = int(input("Please give me a second number: "))

print(num1 + num2, num1- num2, num1*num2, num1/num2, ", ")

"""Exercise 3: Comparison Operators
Write a Python program to:
Ask the user to input two numbers.
Use comparison operators to check and print whether the first number is:
Greater than the second.
Less than the second.
Equal to the second.
"""
num1 = int(input("Please provide the first number: "))
num2 = int(input("Please provide the second number: "))

if num1 > num2:
    print("The first number is greater than the second.")
elif num1 < num2:
    print("The first number is lesser than the second.")
elif num1 == num2:
    print("The numbers are equal.")

#Write a program that takes your age and calculates how old you’ll be in 10 years.
age = int(input("How old are you? "))
age = age + 10
print(f"You will be {age} in 10 years!")

#Create a program to check if two numbers are equal or one is greater.
num1 = int(input("Please provide the first number: "))
num2 = int(input("Please provide the second number: "))

if num1 == num2:
    print("Your numbers are equal.")
else:
    print("Your numbers are different.")