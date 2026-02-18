"""
Python Functions
================
This file covers functions, arguments, scope, and lambda functions
"""

# ============================================
# 1. BASIC FUNCTIONS
# ============================================

print("="*50)
print("BASIC FUNCTIONS")
print("="*50)

# Simple function
def greet():
    print("Hello, World!")

greet()

# Function with parameters
def greet_person(name):
    print(f"Hello, {name}!")

greet_person("Alice")
greet_person("Bob")

# Function with return value
def add(a, b):
    return a + b

result = add(5, 3)
print(f"\n5 + 3 = {result}")

# Function with multiple return values
def get_person_info():
    name = "John"
    age = 25
    city = "New York"
    return name, age, city

name, age, city = get_person_info()
print(f"\nName: {name}, Age: {age}, City: {city}")

# ============================================
# 2. FUNCTION ARGUMENTS
# ============================================

print("\n" + "="*50)
print("FUNCTION ARGUMENTS")
print("="*50)

# Default arguments
def greet_with_default(name="Guest"):
    print(f"\nHello, {name}!")

greet_with_default()           # Uses default
greet_with_default("Alice")    # Uses provided value

# Keyword arguments
def introduce(name, age, city):
    print(f"\nMy name is {name}, I'm {age} years old, from {city}")

introduce(name="Alice", age=25, city="New York")
introduce(city="Paris", name="Bob", age=30)  # Order doesn't matter

# Mix positional and keyword arguments
def book_info(title, author, year=2024, publisher="Unknown"):
    print(f"\n'{title}' by {author} ({year}), Publisher: {publisher}")

book_info("Python Guide", "John Doe")
book_info("Python Guide", "John Doe", 2023)
book_info("Python Guide", "John Doe", publisher="ABC Press")

# ============================================
# 3. *ARGS AND **KWARGS
# ============================================

print("\n" + "="*50)
print("*ARGS AND **KWARGS")
print("="*50)

# *args - Variable number of positional arguments
def sum_all(*args):
    print(f"\nargs: {args}")
    return sum(args)

print("Sum:", sum_all(1, 2, 3))
print("Sum:", sum_all(1, 2, 3, 4, 5))

# **kwargs - Variable number of keyword arguments
def print_info(**kwargs):
    print(f"\nkwargs: {kwargs}")
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="Alice", age=25, city="New York")
print_info(title="Developer", company="TechCorp", experience=5)

# Combining all types of arguments
def complex_function(required, *args, default="value", **kwargs):
    print(f"\nRequired: {required}")
    print(f"Args: {args}")
    print(f"Default: {default}")
    print(f"Kwargs: {kwargs}")

complex_function("must have", 1, 2, 3, default="custom", key1="value1", key2="value2")

# ============================================
# 4. LAMBDA FUNCTIONS (Anonymous Functions)
# ============================================

print("\n" + "="*50)
print("LAMBDA FUNCTIONS")
print("="*50)

# Basic lambda
square = lambda x: x**2
print(f"\nSquare of 5: {square(5)}")

# Lambda with multiple arguments
add = lambda a, b: a + b
print(f"Add 3 and 7: {add(3, 7)}")

# Lambda with conditional
max_value = lambda a, b: a if a > b else b
print(f"Max of 10 and 20: {max_value(10, 20)}")

# Using lambda with built-in functions
numbers = [1, 2, 3, 4, 5]

# map() - apply function to each element
squared = list(map(lambda x: x**2, numbers))
print(f"\nSquared: {squared}")

# filter() - filter elements based on condition
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(f"Evens: {evens}")

# sorted() with key
students = [
    {"name": "Alice", "grade": 85},
    {"name": "Bob", "grade": 92},
    {"name": "Charlie", "grade": 78}
]
sorted_students = sorted(students, key=lambda x: x["grade"], reverse=True)
print("\nSorted by grade:")
for student in sorted_students:
    print(f"{student['name']}: {student['grade']}")

# ============================================
# 5. SCOPE (Local, Global, Nonlocal)
# ============================================

print("\n" + "="*50)
print("SCOPE")
print("="*50)

# Global variable
global_var = "I'm global"

def scope_demo():
    # Local variable
    local_var = "I'm local"
    print(f"\nInside function - Local: {local_var}")
    print(f"Inside function - Global: {global_var}")

scope_demo()
print(f"Outside function - Global: {global_var}")
# print(local_var)  # This would cause an error!

# Modifying global variable
counter = 0

def increment():
    global counter
    counter += 1
    print(f"\nCounter: {counter}")

increment()
increment()
increment()

# Nonlocal keyword (for nested functions)
def outer():
    x = "outer"
    
    def inner():
        nonlocal x
        x = "modified by inner"
        print(f"\nInner x: {x}")
    
    print(f"Before inner: {x}")
    inner()
    print(f"After inner: {x}")

outer()

# ============================================
# 6. NESTED FUNCTIONS AND CLOSURES
# ============================================

print("\n" + "="*50)
print("NESTED FUNCTIONS AND CLOSURES")
print("="*50)

# Nested function
def outer_function(message):
    def inner_function():
        print(f"\n{message}")
    
    inner_function()

outer_function("Hello from nested function!")

# Closure - function that remembers values from enclosing scope
def multiplier(factor):
    def multiply(number):
        return number * factor
    return multiply

times_two = multiplier(2)
times_three = multiplier(3)

print(f"\n5 * 2 = {times_two(5)}")
print(f"5 * 3 = {times_three(5)}")

# Practical closure example - counter
def make_counter():
    count = 0
    
    def counter():
        nonlocal count
        count += 1
        return count
    
    return counter

counter1 = make_counter()
counter2 = make_counter()

print(f"\nCounter1: {counter1()}")  # 1
print(f"Counter1: {counter1()}")  # 2
print(f"Counter2: {counter2()}")  # 1
print(f"Counter1: {counter1()}")  # 3

# ============================================
# 7. RECURSION
# ============================================

print("\n" + "="*50)
print("RECURSION")
print("="*50)

# Factorial using recursion
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

print(f"\nFactorial of 5: {factorial(5)}")

# Fibonacci using recursion
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

print("\nFibonacci sequence:")
for i in range(10):
    print(fibonacci(i), end=" ")

# Sum of list using recursion
def sum_list(lst):
    if len(lst) == 0:
        return 0
    return lst[0] + sum_list(lst[1:])

print(f"\n\nSum of [1,2,3,4,5]: {sum_list([1,2,3,4,5])}")

# ============================================
# 8. DOCSTRINGS AND ANNOTATIONS
# ============================================

print("\n" + "="*50)
print("DOCSTRINGS AND ANNOTATIONS")
print("="*50)

def calculate_area(length: float, width: float) -> float:
    """
    Calculate the area of a rectangle.
    
    Args:
        length (float): The length of the rectangle
        width (float): The width of the rectangle
    
    Returns:
        float: The area of the rectangle
    
    Example:
        >>> calculate_area(5, 3)
        15.0
    """
    return length * width

print(f"\nArea: {calculate_area(5, 3)}")
print(f"\nDocstring:\n{calculate_area.__doc__}")

