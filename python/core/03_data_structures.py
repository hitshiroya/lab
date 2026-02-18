"""
Python Data Structures
======================
This file covers Lists, Tuples, Dictionaries, and Sets
"""

# ============================================
# 1. LISTS - Ordered, Mutable, Allows Duplicates
# ============================================

print("="*50)
print("LISTS")
print("="*50)

# Creating lists
fruits = ["apple", "banana", "cherry"]
numbers = [1, 2, 3, 4, 5]
mixed = [1, "hello", 3.14, True]
empty_list = []

print("\nFruits:", fruits)
print("Numbers:", numbers)
print("Mixed:", mixed)

# Accessing elements
print("\nFirst fruit:", fruits[0])
print("Last fruit:", fruits[-1])
print("Second to last:", fruits[-2])

# Slicing
print("\nFirst two fruits:", fruits[0:2])
print("Last two fruits:", fruits[-2:])
print("Every other fruit:", fruits[::2])

# List methods
fruits.append("orange")           # Add to end
print("\nAfter append:", fruits)

fruits.insert(1, "mango")         # Insert at position
print("After insert:", fruits)

fruits.remove("banana")           # Remove by value
print("After remove:", fruits)

popped = fruits.pop()             # Remove and return last
print("Popped:", popped)
print("After pop:", fruits)

# More list operations
numbers = [3, 1, 4, 1, 5, 9, 2, 6]
print("\nOriginal:", numbers)

numbers.sort()                    # Sort in place
print("Sorted:", numbers)

numbers.reverse()                 # Reverse in place
print("Reversed:", numbers)

print("Count of 1:", numbers.count(1))
print("Index of 5:", numbers.index(5))

# List comprehension
squares = [x**2 for x in range(1, 6)]
print("\nSquares:", squares)

# ============================================
# 2. TUPLES - Ordered, Immutable, Allows Duplicates
# ============================================

print("\n" + "="*50)
print("TUPLES")
print("="*50)

# Creating tuples
coordinates = (10, 20)
person = ("Alice", 25, "Engineer")
single_element = (1,)  # Note the comma
empty_tuple = ()

print("\nCoordinates:", coordinates)
print("Person:", person)

# Accessing elements (same as lists)
print("\nName:", person[0])
print("Age:", person[1])

# Tuple unpacking
x, y = coordinates
name, age, job = person
print(f"\nUnpacked: x={x}, y={y}")
print(f"Name: {name}, Age: {age}, Job: {job}")

# Tuples are immutable (can't be changed)
# coordinates[0] = 15  # This would cause an error!

# But you can create a new tuple
new_coordinates = (15, 25)
print("\nNew coordinates:", new_coordinates)

# Tuple methods (limited because immutable)
numbers = (1, 2, 3, 2, 4, 2, 5)
print("\nCount of 2:", numbers.count(2))
print("Index of 4:", numbers.index(4))

# ============================================
# 3. DICTIONARIES - Unordered, Mutable, Key-Value Pairs
# ============================================

print("\n" + "="*50)
print("DICTIONARIES")
print("="*50)

# Creating dictionaries
student = {
    "name": "John",
    "age": 20,
    "grade": "A",
    "courses": ["Math", "Science"]
}

print("\nStudent:", student)

# Accessing values
print("\nName:", student["name"])
print("Age:", student.get("age"))
print("Grade:", student.get("grade", "N/A"))  # Default value

# Modifying dictionary
student["age"] = 21                    # Update value
student["email"] = "john@email.com"    # Add new key-value
print("\nUpdated student:", student)

# Dictionary methods
print("\nKeys:", student.keys())
print("Values:", student.values())
print("Items:", student.items())

# Looping through dictionary
print("\nLooping through items:")
for key, value in student.items():
    print(f"{key}: {value}")

# Check if key exists
if "name" in student:
    print("\nName exists in student dictionary")

# Remove items
email = student.pop("email")          # Remove and return value
print("\nRemoved email:", email)
print("After removal:", student)

# Dictionary comprehension
numbers = {x: x**2 for x in range(1, 6)}
print("\nSquares dict:", numbers)

# ============================================
# 4. SETS - Unordered, Mutable, No Duplicates
# ============================================

print("\n" + "="*50)
print("SETS")
print("="*50)

# Creating sets
fruits = {"apple", "banana", "cherry"}
numbers = {1, 2, 3, 4, 5}
mixed = {1, "hello", 3.14, True}

print("\nFruits set:", fruits)
print("Numbers set:", numbers)

# Sets automatically remove duplicates
numbers_with_duplicates = {1, 2, 2, 3, 3, 3, 4, 5}
print("\nSet removes duplicates:", numbers_with_duplicates)

# Set operations
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

print("\nSet 1:", set1)
print("Set 2:", set2)

# Union - all elements from both sets
print("\nUnion:", set1 | set2)
print("Union (method):", set1.union(set2))

# Intersection - common elements
print("\nIntersection:", set1 & set2)
print("Intersection (method):", set1.intersection(set2))

# Difference - elements in set1 but not in set2
print("\nDifference:", set1 - set2)
print("Difference (method):", set1.difference(set2))

# Symmetric difference - elements in either set, but not both
print("\nSymmetric Difference:", set1 ^ set2)

# Set methods
fruits.add("orange")               # Add single element
print("\nAfter add:", fruits)

fruits.remove("banana")            # Remove element (error if not found)
print("After remove:", fruits)

fruits.discard("mango")            # Remove element (no error if not found)
print("After discard:", fruits)

# ============================================
# 5. CHOOSING THE RIGHT DATA STRUCTURE
# ============================================

print("\n" + "="*50)
print("WHEN TO USE EACH DATA STRUCTURE")
print("="*50)

print("""
LIST:
- When you need ordered collection
- When you need to modify elements
- When duplicates are allowed
- Example: shopping list, student grades

TUPLE:
- When you need ordered collection
- When data should not be modified
- When duplicates are allowed
- Example: coordinates, RGB colors, database records

DICTIONARY:
- When you need key-value pairs
- When you need fast lookups by key
- When order doesn't matter (or you use Python 3.7+)
- Example: student info, configuration settings

SET:
- When you need unique elements only
- When you need set operations (union, intersection)
- When order doesn't matter
- Example: unique tags, removing duplicates
""")

