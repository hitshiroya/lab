"""
Python Control Flow
===================
This file covers if statements, loops, and control flow
"""

# ============================================
# 1. IF, ELIF, ELSE STATEMENTS
# ============================================

print("="*50)
print("IF STATEMENTS")
print("="*50)

# Simple if statement
age = 18
if age >= 18:
    print("\nYou are an adult")

# if-else statement
temperature = 25
if temperature > 30:
    print("\nIt's hot outside!")
else:
    print("\nIt's pleasant outside!")

# if-elif-else statement
score = 85

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print(f"\nScore: {score}, Grade: {grade}")

# Nested if statements
age = 25
has_license = True

if age >= 18:
    if has_license:
        print("\nYou can drive")
    else:
        print("\nYou need a license to drive")
else:
    print("\nYou are too young to drive")

# Multiple conditions
username = "admin"
password = "pass123"

if username == "admin" and password == "pass123":
    print("\nLogin successful!")
else:
    print("\nInvalid credentials")

# ============================================
# 2. FOR LOOPS
# ============================================

print("\n" + "="*50)
print("FOR LOOPS")
print("="*50)

# Loop through range
print("\nNumbers 1 to 5:")
for i in range(1, 6):
    print(i, end=" ")

print("\n\nEven numbers from 0 to 10:")
for i in range(0, 11, 2):
    print(i, end=" ")

# Loop through string
print("\n\nLooping through string:")
for char in "Python":
    print(char, end=" ")

# Loop through list
print("\n\nLooping through list:")
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# Loop with enumerate (index + value)
print("\nWith index:")
for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")

# Loop with range and len
print("\nUsing range and len:")
for i in range(len(fruits)):
    print(f"{i}: {fruits[i]}")

# ============================================
# 3. WHILE LOOPS
# ============================================

print("\n" + "="*50)
print("WHILE LOOPS")
print("="*50)

# Basic while loop
print("\nCountdown:")
count = 5
while count > 0:
    print(count, end=" ")
    count -= 1
print("Go!")

# While loop with condition
print("\n\nSum until threshold:")
total = 0
number = 1
while total < 50:
    total += number
    number += 1
print(f"Total: {total}, Numbers added: {number - 1}")

# ============================================
# 4. BREAK, CONTINUE, PASS
# ============================================

print("\n" + "="*50)
print("BREAK, CONTINUE, PASS")
print("="*50)

# Break - exit loop
print("\nBreak example (stop at 5):")
for i in range(1, 11):
    if i == 5:
        break
    print(i, end=" ")

# Continue - skip iteration
print("\n\nContinue example (skip 5):")
for i in range(1, 11):
    if i == 5:
        continue
    print(i, end=" ")

# Pass - placeholder (do nothing)
print("\n\nPass example:")
for i in range(1, 6):
    if i == 3:
        pass  # Will implement later
    print(i, end=" ")

# ============================================
# 5. NESTED LOOPS
# ============================================

print("\n\n" + "="*50)
print("NESTED LOOPS")
print("="*50)

# Multiplication table
print("\nMultiplication table (2x2):")
for i in range(1, 3):
    for j in range(1, 3):
        print(f"{i} x {j} = {i*j}")
    print()

# Pattern printing
print("Pattern:")
for i in range(1, 6):
    for j in range(i):
        print("*", end=" ")
    print()

# ============================================
# 6. LIST COMPREHENSION (BONUS)
# ============================================

print("\n" + "="*50)
print("LIST COMPREHENSION (Bonus)")
print("="*50)

# Create list of squares
squares = [x**2 for x in range(1, 6)]
print("\nSquares:", squares)

# Filter even numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = [x for x in numbers if x % 2 == 0]
print("Even numbers:", evens)

# With if-else
labels = ["Even" if x % 2 == 0 else "Odd" for x in range(1, 6)]
print("Labels:", labels)

#