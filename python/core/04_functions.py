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
# 8. PASS BY REFERENCE VS VALUE
# ============================================

print("\n" + "="*50)
print("PASS BY REFERENCE VS VALUE")
print("="*50)

print("""
Python uses "pass by object reference" (or "pass by assignment"):
- Variables are references to objects
- When you pass an argument, you pass a reference to the object
- Whether the original changes depends on:
  1. If the object is MUTABLE or IMMUTABLE
  2. If you MODIFY the object or REASSIGN the variable

IMMUTABLE: int, float, str, tuple, frozenset, bool
MUTABLE: list, dict, set, custom objects
""")

# ============================================
# 8.1. IMMUTABLE OBJECTS (int, str, tuple)
# ============================================

print("\n--- Immutable Objects ---")

# Integers (immutable)
print("\nExample 1: Integer (immutable)")
def modify_number(x):
    print(f"  Inside function, before: x = {x}, id = {id(x)}")
    x = x + 10  # Creates a NEW object
    print(f"  Inside function, after: x = {x}, id = {id(x)}")
    return x

num = 5
print(f"Before function call: num = {num}, id = {id(num)}")
result = modify_number(num)
print(f"After function call: num = {num}, id = {id(num)}")
print(f"Returned value: result = {result}")

# Strings (immutable)
print("\nExample 2: String (immutable)")
def modify_string(s):
    print(f"  Inside function, before: s = '{s}', id = {id(s)}")
    s = s + " World"  # Creates a NEW string
    print(f"  Inside function, after: s = '{s}', id = {id(s)}")

text = "Hello"
print(f"Before function call: text = '{text}', id = {id(text)}")
modify_string(text)
print(f"After function call: text = '{text}', id = {id(text)}")

# ============================================
# 8.2. MUTABLE OBJECTS (list, dict, set)
# ============================================

print("\n--- Mutable Objects ---")

# Lists (mutable) - modifying in place
print("\nExample 3: List - Modifying in place")
def modify_list_inplace(lst):
    print(f"  Inside function, before: lst = {lst}, id = {id(lst)}")
    lst.append(4)  # Modifies the SAME object
    lst[0] = 999   # Modifies the SAME object
    print(f"  Inside function, after: lst = {lst}, id = {id(lst)}")

my_list = [1, 2, 3]
print(f"Before function call: my_list = {my_list}, id = {id(my_list)}")
modify_list_inplace(my_list)
print(f"After function call: my_list = {my_list}, id = {id(my_list)}")
print("⚠️ Original list WAS modified!")

# Lists (mutable) - reassignment
print("\nExample 4: List - Reassignment")
def reassign_list(lst):
    print(f"  Inside function, before: lst = {lst}, id = {id(lst)}")
    lst = [10, 20, 30]  # Creates a NEW list (reassignment)
    print(f"  Inside function, after: lst = {lst}, id = {id(lst)}")

my_list2 = [1, 2, 3]
print(f"Before function call: my_list2 = {my_list2}, id = {id(my_list2)}")
reassign_list(my_list2)
print(f"After function call: my_list2 = {my_list2}, id = {id(my_list2)}")
print("✓ Original list was NOT modified (reassignment creates new object)")

# Dictionaries (mutable)
print("\nExample 5: Dictionary - Modifying in place")
def modify_dict(d):
    d["new_key"] = "new_value"
    d["name"] = "Modified"

my_dict = {"name": "Alice", "age": 25}
print(f"Before: {my_dict}")
modify_dict(my_dict)
print(f"After: {my_dict}")
print("⚠️ Original dictionary WAS modified!")

# ============================================
# 8.3. PREVENTING MODIFICATIONS
# ============================================

print("\n--- Preventing Modifications ---")

# Using copy for shallow copy
print("\nExample 6: Using copy()")
def modify_list_copy(lst):
    lst = lst.copy()  # Create a copy
    lst.append(4)
    return lst

original = [1, 2, 3]
modified = modify_list_copy(original)
print(f"Original: {original}")
print(f"Modified: {modified}")

# Using slicing for copy
print("\nExample 7: Using slicing [:] to copy")
def modify_with_slice(lst):
    lst = lst[:]  # Create a copy using slicing
    lst.append(4)
    return lst

original2 = [1, 2, 3]
modified2 = modify_with_slice(original2)
print(f"Original: {original2}")
print(f"Modified: {modified2}")

# Deep copy for nested structures
print("\nExample 8: Deep copy for nested structures")
import copy

def modify_nested(nested_list):
    nested_list_copy = copy.deepcopy(nested_list)
    nested_list_copy[0][0] = 999
    return nested_list_copy

nested = [[1, 2], [3, 4]]
modified_nested = modify_nested(nested)
print(f"Original nested: {nested}")
print(f"Modified nested: {modified_nested}")

# ============================================
# 8.4. DEFAULT MUTABLE ARGUMENTS (GOTCHA!)
# ============================================

print("\n--- Default Mutable Arguments (Common Gotcha!) ---")

# BAD: Mutable default argument
print("\nExample 9: BAD - Mutable default argument")
def bad_append(item, lst=[]):  # ⚠️ DON'T DO THIS!
    lst.append(item)
    return lst

print(f"Call 1: {bad_append(1)}")
print(f"Call 2: {bad_append(2)}")
print(f"Call 3: {bad_append(3)}")
print("⚠️ Same list is reused! Default is created only once!")

# GOOD: Using None as default
print("\nExample 10: GOOD - Using None as default")
def good_append(item, lst=None):
    if lst is None:
        lst = []  # Create new list each time
    lst.append(item)
    return lst

print(f"Call 1: {good_append(1)}")
print(f"Call 2: {good_append(2)}")
print(f"Call 3: {good_append(3)}")
print("✓ New list created each time!")

# Another example with dictionary
print("\nExample 11: Dictionary default argument")
def add_to_config(key, value, config=None):
    if config is None:
        config = {}
    config[key] = value
    return config

print(f"Config 1: {add_to_config('name', 'Alice')}")
print(f"Config 2: {add_to_config('age', 25)}")

# ============================================
# 8.5. PRACTICAL EXAMPLES
# ============================================

print("\n--- Practical Examples ---")

# Example 1: Swap without return (doesn't work as expected)
print("\nExample 12: Swap attempt (doesn't work)")
def swap_wrong(a, b):
    temp = a
    a = b
    b = temp
    print(f"  Inside function: a={a}, b={b}")

x, y = 10, 20
print(f"Before swap: x={x}, y={y}")
swap_wrong(x, y)
print(f"After swap: x={x}, y={y}")
print("✗ Didn't work! Use return or pass mutable container")

# Example 2: Swap using return
print("\nExample 13: Swap using return")
def swap_correct(a, b):
    return b, a

x, y = 10, 20
print(f"Before swap: x={x}, y={y}")
x, y = swap_correct(x, y)
print(f"After swap: x={x}, y={y}")
print("✓ Works!")

# Example 3: Modifying list elements
print("\nExample 14: Modifying list elements")
def double_values(numbers):
    for i in range(len(numbers)):
        numbers[i] *= 2

nums = [1, 2, 3, 4, 5]
print(f"Before: {nums}")
double_values(nums)
print(f"After: {nums}")
print("✓ List modified in place")

# Example 4: Returning new list instead of modifying
print("\nExample 15: Returning new list (functional approach)")
def double_values_functional(numbers):
    return [x * 2 for x in numbers]

nums2 = [1, 2, 3, 4, 5]
print(f"Original: {nums2}")
doubled = double_values_functional(nums2)
print(f"Doubled: {doubled}")
print(f"Original unchanged: {nums2}")

# ============================================
# 8.6. CUSTOM OBJECTS
# ============================================

print("\n--- Custom Objects ---")

print("\nExample 16: Custom class objects (mutable)")
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __repr__(self):
        return f"Person(name='{self.name}', age={self.age})"

def modify_person(person):
    person.age += 1  # Modifies the original object
    person.name = "Modified"

def reassign_person(person):
    person = Person("New Person", 100)  # Reassignment (doesn't affect original)

p1 = Person("Alice", 25)
print(f"Original: {p1}")

modify_person(p1)
print(f"After modify: {p1}")

p2 = Person("Bob", 30)
print(f"\nOriginal: {p2}")
reassign_person(p2)
print(f"After reassign: {p2}")

# ============================================
# 8.7. SUMMARY AND BEST PRACTICES
# ============================================

print("\n" + "="*50)
print("SUMMARY")
print("="*50)

print("""
KEY TAKEAWAYS:

1. IMMUTABLE objects (int, str, tuple):
   - Cannot be changed in place
   - Modifications create new objects
   - Original always remains unchanged

2. MUTABLE objects (list, dict, set):
   - CAN be changed in place
   - Modifications affect the original
   - Reassignment creates new object (doesn't affect original)

3. WHEN TO USE EACH APPROACH:
   - Modify in place: When you want to change the original
   - Return new object: When you want to preserve the original
   
4. AVOID MUTABLE DEFAULT ARGUMENTS:
   - Use None as default, then create new object inside function
   
5. USE COPY when needed:
   - Shallow copy: list.copy() or dict.copy() or lst[:]
   - Deep copy: copy.deepcopy() for nested structures

MEMORY TIP:
"If you can change it in place, it's mutable. 
 If reassignment is the only way to 'change' it, it's immutable."
""")

# ============================================
# 9. DOCSTRINGS AND ANNOTATIONS
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

