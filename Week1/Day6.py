#1. Create and query a product dictionary
"""
products = {
    "apple":0.5,
    "mango":1.75,
    "banana":1,
    "bread":1,
    "cola":1.5
}

product_query = input("Enter product name: ").strip().lower()

if product_query in products:
    print(f"The price of {product_query} is: ${products[product_query]:.2f}.")
else:
    print(f"{product_query} is not on the list")

#2. Find the top student

students = {"Alice": 85, "Bob": 92, "Charlie": 78, "Winiary": 82, "Marie": 98}
top_student = max(students, key=students.get)

print(f"The top student is {top_student} with score {students[top_student]}.")

#3. Filter Products by Price

products = {
    "apple":0.5,
    "mango":1.75,
    "banana":1,
    "bread":1,
    "cola":1.5
}
price_threshold = 1

products_above_threshold = {product: price for product, price in products.items() if price > price_threshold}

print("Products above the price threshold:")
for product, price in products_above_threshold.items():
    print(f"- {product}: ${price:.2f}")

#4. Count Word Frequency

def count_word_frequency(sentence):
    word_counts = {}
    for word in sentence.split():
        word_counts[word] = word_counts.get(word, 0) + 1
    return word_counts

sentence = input("Please give me a sentence: ")

word_counts = count_word_frequency(sentence)

print("Word frequency:")
for word, count in word_counts.items():
    print(f"{word}: {count}")

#5. Mini Challenge: Nested Dictionary for Students

students = {
    "Alice": {"age": 20, "scores": [85, 90, 88]},
    "Bob": {"age": 22, "scores": [78, 81, 85]},
    "Charlie": {"age": 19, "scores": [92, 89, 95]},
    "Marie": {"age": 89, "scores": [98, 99, 98]}
}

def score_average(students):
    for key, value in students.items():
        average = sum(value["scores"]) / len(value["scores"])
        print(f"{key}: {average:.2f}")

score_average(students)

###########################"""
#1. Write a text file
sentence = input("Enter a sentence: ")

with open("output.txt", "w") as file:
    file.write(sentence + "\n")

print("Sentence saved successfully!")

#2. Read and count lines
with open("output.txt", "r") as file:
    line_count = len(file.readlines())
    print(f"Total lines in file: {line_count}")

#3. Append user input
with open("output.txt", "a") as file:
    while True:
        text = input("Enter a line (type 'STOP' to finish): ")
        if text == "STOP":
            break
    file.write(text + "\n")
print("Lines appended successfully!")

#4. Read and Display File Contents
with open("output.txt", "r") as file:
    for line in file:
        print(line.rstrip())

#5. Mini Challenge: Process a Number File
with open("numbers.txt", "r") as file:
    numbers = [int(line.strip()) for line in file]

sum_numbers= sum(numbers)

with open("result.txt", "w") as result_file:
    result_file.write(f"Sum: {sum_numbers}\n")

print(f"Sum: {sum_numbers} (saved in result.txt)")