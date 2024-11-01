#--------------------------------------------------------------DAY 1----------------------------------------------------------------------------------
# Hello World in Python
print("Hello, World!")

# Simple Math Operations
a = 10
b = 5

# Addition
add = a + b
print("Addition:", add)

# Subtraction
subtract = a - b
print("Subtraction:", subtract)

# Multiplication
multiply = a * b
print("Multiplication:", multiply)

# Division
divide = a / b
print("Division:", divide)

# Taking user input and printing a greeting
name = input("Enter your name: ")
print("Hello,", name + "!")

# Adding two numbers entered by the user
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
sum = num1 + num2
print("The sum is:", sum)

#-------------------------------------------------------------------DAY 2-------------------------------------------------------------------------
# Assigning values to variables
x = 10        # Integer
y = 3.14      # Float
name = "Alice" # String
is_student = True # Boolean

print("Integer:", x)
print("Float:", y)
print("String:", name)
print("Boolean:", is_student)


# Arithmetic operations
a = 15
b = 4

# Addition
add = a + b
print("Addition:", add)

# Subtraction
subtract = a - b
print("Subtraction:", subtract)

# Multiplication
multiply = a * b
print("Multiplication:", multiply)

# Division
divide = a / b
print("Division:", divide)

# Modulus (remainder)
modulus = a % b
print("Modulus:", modulus)

# Exponentiation
power = a ** b
print("Exponentiation:", power)


# Type conversion examples
# Integer to float
num_int = 5
num_float = float(num_int)
print("Integer to Float:", num_float)

# Float to integer
num_float = 5.67
num_int = int(num_float)
print("Float to Integer:", num_int)

# Integer to string
num_str = str(num_int)
print("Integer to String:", num_str)

# String to integer
str_num = "100"
num = int(str_num)
print("String to Integer:", num)

# String to float
str_float = "123.45"
num = float(str_float)
print("String to Float:", num)



# Taking user input (strings by default) and converting to integers
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

# Adding the numbers
result = num1 + num2
print("The sum is:", result)


#---------------------------------------------------------------------------DAY 3------------------------------------------------------
# Sample string
text = "Hello, World!"

# Using string methods
print(text.lower())         # Converts to lowercase
print(text.upper())         # Converts to uppercase
print(text.strip())         # Removes leading/trailing whitespace
print(text.replace("Hello", "Hi"))  # Replaces "Hello" with "Hi"
print(text.find("World"))    # Finds the index of "World"

# Splitting the string
words = text.split(", ")
print("Splitting:", words)  # Splits into ['Hello', 'World!']


# Indexing
text = "Python"
print(text[0])  # First character 'P'
print(text[-1]) # Last character 'n'

# Slicing
print(text[1:4])     # Characters from index 1 to 3 ('yth')
print(text[:3])      # First three characters ('Pyt')
print(text[3:])      # From index 3 to the end ('hon')
print(text[-3:])     # Last three characters ('hon')



# Concatenating strings
greeting = "Hello"
name = "Alice"
message = greeting + ", " + name + "!"
print("Concatenation:", message)

# Using f-strings for formatting (Python 3.6+)
age = 25
intro = f"My name is {name} and I am {age} years old."
print("Formatted String:", intro)

# Using `format` method for older versions of Python
intro = "My name is {} and I am {} years old.".format(name, age)
print("Using format:", intro)



text = "Python"
reversed_text = text[::-1]  # Reverses the string
print("Reversed:", reversed_text)  # Output: 'nohtyP'



# Taking user input and manipulating strings
full_name = input("Enter your full name: ").strip()

# Capitalizing each word
formatted_name = full_name.title()  # Converts to Title Case
print("Title Case:", formatted_name)

# Counting occurrences of a character
character = 'o'
count = full_name.lower().count(character)
print(f"Occurrences of '{character}':", count)

# Checking if a string starts or ends with a substring
print("Starts with 'Mr.':", full_name.startswith("Mr."))
print("Ends with 'Smith':", full_name.endswith("Smith"))

#----------------------------------------------------------DAY 4----------------------------------------------------
# Greeting the user
name = input("Enter your name: ")
print("Hello,", name + "!")


# Taking user input for two numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Performing arithmetic operations
print("Addition:", num1 + num2)
print("Subtraction:", num1 - num2)
print("Multiplication:", num1 * num2)
print("Division:", num1 / num2 if num2 != 0 else "Cannot divide by zero")


# Taking user input for the radius
radius = float(input("Enter the radius of the circle: "))

# Calculating the area
area = 3.14159 * radius ** 2
print(f"The area of the circle with radius {radius} is {area:.2f}")


# Taking temperature in Celsius
celsius = float(input("Enter temperature in Celsius: "))

# Converting to Fahrenheit
fahrenheit = (celsius * 9/5) + 32
print(f"{celsius}°C is equal to {fahrenheit:.2f}°F")


# Taking user inputs for principal, rate, and time
principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the interest rate (in %): "))
time = float(input("Enter the time in years: "))

# Calculating compound interest
amount = principal * (1 + rate / 100) ** time
interest = amount - principal
print(f"The compound interest is: {interest:.2f}")
print(f"The total amount after {time} years is: {amount:.2f}")


# Taking user inputs for weight (kg) and height (m)
weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in meters: "))

# Calculating BMI
bmi = weight / (height ** 2)
print(f"Your BMI is: {bmi:.2f}")


#--------------------------------------------------------------DAY 5-------------------------------------------------------------
# Creating a list and a tuple
my_list = [1, 2, 3, "apple", "banana"]
my_tuple = (1, 2, 3, "apple", "banana")

# Accessing elements
print("List first element:", my_list[0])       # Output: 1
print("Tuple last element:", my_tuple[-1])     # Output: "banana"


# Adding and removing elements in a list
fruits = ["apple", "banana", "cherry"]

# Appending an element
fruits.append("orange")
print("After appending:", fruits)

# Inserting an element at a specific position
fruits.insert(1, "blueberry")
print("After inserting at index 1:", fruits)

# Removing an element
fruits.remove("banana")
print("After removing 'banana':", fruits)

# Removing the last element with pop
last_fruit = fruits.pop()
print("Popped element:", last_fruit)
print("List after pop:", fruits)



# Slicing a list
numbers = [1, 2, 3, 4, 5, 6]
print("Sliced list (2:5):", numbers[2:5])  # Elements from index 2 to 4
print("Sliced list (start to 3):", numbers[:3])  # Elements from start to index 2
print("Sliced list (3 to end):", numbers[3:])  # Elements from index 3 to end


# Using a for loop to iterate through a list
colors = ["red", "green", "blue"]
for color in colors:
    print(color)

# Using a for loop to iterate through a tuple
dimensions = (1920, 1080)
for dimension in dimensions:
    print(dimension)



# List with duplicate elements
numbers = [1, 2, 3, 2, 4, 2]

# Counting occurrences
count_of_twos = numbers.count(2)
print("Count of 2s:", count_of_twos)

# Sorting a list
numbers.sort()
print("Sorted list:", numbers)

# Reversing a list
numbers.reverse()
print("Reversed list:", numbers)



# Unpacking a tuple into variables
person = ("Alice", 25, "Engineer")
name, age, profession = person
print("Name:", name)
print("Age:", age)
print("Profession:", profession)


# List containing a tuple and another list
nested_list = [("apple", "banana"), ["carrot", "potato"]]

# Accessing elements in a nested structure
print("First element of the tuple:", nested_list[0][0])  # Output: "apple"
print("Second element of the list:", nested_list[1][1])  # Output: "potato"

#--------------------------------------------------------------------------------DAY 6---------------------------------------------------------------
# Grade calculator
score = float(input("Enter your score (0-100): "))

if score >= 90:
    grade = 'A'
elif score >= 80:
    grade = 'B'
elif score >= 70:
    grade = 'C'
elif score >= 60:
    grade = 'D'
else:
    grade = 'F'

print(f"Your grade is: {grade}")



# Number guessing game
import random

number_to_guess = random.randint(1, 10)
guess = int(input("Guess a number between 1 and 10: "))

if guess == number_to_guess:
    print("Congratulations! You guessed the correct number!")
elif guess > number_to_guess:
    print("Too high! Try again.")
else:
    print("Too low! Try again.")


# Even or odd checker
number = int(input("Enter a number: "))

if number % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")


# Voting eligibility checker
age = int(input("Enter your age: "))

if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")



# Simple calculator
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operation = input("Choose an operation (+, -, *, /): ")

if operation == '+':
    result = num1 + num2
elif operation == '-':
    result = num1 - num2
elif operation == '*':
    result = num1 * num2
elif operation == '/':
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Error: Cannot divide by zero"
else:
    result = "Invalid operation selected."

print("Result:", result)


# Temperature categorizer
temperature = float(input("Enter the temperature in Celsius: "))

if temperature >= 30:
    print("It's hot outside.")
elif temperature >= 20:
    print("It's warm.")
elif temperature >= 10:
    print("It's cool.")
else:
    print("It's cold.")

#-----------------------------------------------------------------------------DAY 7----------------------------------------------------------------------
for variable in sequence:
    # code to execute

for i in range(5):
    print(i)

while condition:
    # code to execute

count = 0
while count < 5:
    print(count)
    count += 1


for i in range(1, 11):
    print(i)


n = int(input("Enter a number: "))
sum_of_numbers = 0
counter = 1

while counter <= n:
    sum_of_numbers += counter
    counter += 1

print("Sum of numbers from 1 to", n, "is:", sum_of_numbers)


# Triangle pattern
rows = int(input("Enter the number of rows: "))

for i in range(1, rows + 1):
    print("*" * i)


num = int(input("Enter a number: "))
factorial = 1

for i in range(1, num + 1):
    factorial *= i

print("Factorial of", num, "is:", factorial)


num = int(input("Enter a number: "))
is_prime = True

if num > 1:
    i = 2
    while i <= num // 2:
        if num % i == 0:
            is_prime = False
            break
        i += 1

if is_prime and num > 1:
    print(num, "is a prime number.")
else:
    print(num, "is not a prime number.")


n = int(input("Enter a number: "))
sum_even = 0

for i in range(1, n + 1):
    if i % 2 != 0:
        continue
    sum_even += i

print("Sum of even numbers from 1 to", n, "is:", sum_even)


# Pattern of numbers
rows = int(input("Enter the number of rows: "))

for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()
#-----------------------------------------------------------------------------------DAY 8----------------------------------------------------------------------------------

def function_name(parameters):
    # Code to execute
    return value


def add(a, b):
    return a + b

# Calling the function
result = add(5, 3)
print("Sum:", result)


def find_max(x, y):
    if x > y:
        return x
    else:
        return y

# Calling the function
max_number = find_max(10, 20)
print("Maximum number is:", max_number)


def area_of_circle(radius):
    return 3.14159 * radius ** 2

# Calling the function
radius = 5
area = area_of_circle(radius)
print("Area of the circle:", area)


def greet(name="User"):
    return f"Hello, {name}!"

# Calling the function with and without an argument
print(greet("Alice"))
print(greet())



def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Cannot divide by zero"

# Using the functions
num1, num2 = 10, 5
print("Addition:", add(num1, num2))
print("Subtraction:", subtract(num1, num2))
print("Multiplication:", multiply(num1, num2))
print("Division:", divide(num1, num2))
