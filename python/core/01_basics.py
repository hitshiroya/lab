"""
Python Basics - Getting Started
================================
This file covers the fundamental concepts of Python
"""

# ============================================
# 1. VARIABLES AND DATA TYPES
# ============================================

# Numbers
age = 25                    # Integer
price = 19.99              # Float
complex_num = 3 + 4j       # Complex number

# Strings
name = "Python"
message = 'Hello, World!'
multiline = """This is a
multiline string"""

# Boolean
is_active = True
is_completed = False

# None type
empty_value = None

# Print variables
print("Age:", age)
print("Name:", name)
print("Is Active:", is_active)

# ============================================
# 2. TYPE CHECKING AND CONVERSION
# ============================================

# Check type
print("\nType of age:", type(age))
print("Type of price:", type(price))
print("Type of name:", type(name))

# Type conversion
num_string = "100"
num_int = int(num_string)          # String to integer
num_float = float(num_string)      # String to float
num_to_string = str(123)           # Number to string

print("\nConverted:", num_int, type(num_int))

# ============================================
# 3. BASIC OPERATORS
# ============================================

# Arithmetic operators
a = 10
b = 3

print("\n--- Arithmetic Operators ---")
print("Addition:", a + b)          # 13
print("Subtraction:", a - b)       # 7
print("Multiplication:", a * b)    # 30
print("Division:", a / b)          # 3.333...
print("Floor Division:", a // b)   # 3
print("Modulus:", a % b)           # 1
print("Exponent:", a ** b)         # 1000

# Comparison operators
print("\n--- Comparison Operators ---")
print("Equal:", a == b)            # False
print("Not equal:", a != b)        # True
print("Greater than:", a > b)      # True
print("Less than:", a < b)         # False
print("Greater or equal:", a >= b) # True
print("Less or equal:", a <= b)    # False

# Logical operators
x = True
y = False

print("\n--- Logical Operators ---")
print("AND:", x and y)             # False
print("OR:", x or y)               # True
print("NOT:", not x)               # False

# ============================================
# 4. STRING OPERATIONS
# ============================================

text = "Python Programming"

print("\n--- String Operations ---")
print("Length:", len(text))
print("Uppercase:", text.upper())
print("Lowercase:", text.lower())
print("Replace:", text.replace("Python", "Java"))
print("Split:", text.split())
print("First character:", text[0])
print("Last character:", text[-1])
print("Slice (0-6):", text[0:6])

# String formatting
name = "Alice"
age = 30
print(f"\nMy name is {name} and I am {age} years old")  # f-string (Python 3.6+)
print("My name is {} and I am {} years old".format(name, age))  # format method

# ============================================
# 5. USER INPUT
# ============================================

# Uncomment to try interactive input
# user_name = input("Enter your name: ")
# print(f"Hello, {user_name}!")

# user_age = int(input("Enter your age: "))
# print(f"You will be {user_age + 10} in 10 years")

# ============================================
# 6. MULTIPLE ASSIGNMENTS
# ============================================

# Multiple variables in one line
x, y, z = 1, 2, 3
print("\nMultiple assignment:", x, y, z)

# Same value to multiple variables
a = b = c = 100
print("Same value:", a, b, c)

# Swap variables
a, b = 10, 20
print(f"\nBefore swap: a={a}, b={b}")
a, b = b, a
print(f"After swap: a={a}, b={b}")

