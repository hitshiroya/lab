"""
Python Generators and Iterators
================================
This file covers generators, iterators, yield, and generator expressions
"""

import sys

# ============================================
# 1. UNDERSTANDING ITERATORS
# ============================================

print("="*50)
print("ITERATORS")
print("="*50)

print("""
An iterator is an object that can be iterated (looped) upon.
It implements two methods: __iter__() and __next__()
""")

# Everything that can be used in a for loop is an iterable
my_list = [1, 2, 3, 4, 5]
my_iter = iter(my_list)  # Get iterator from iterable

print("\nManual iteration:")
print(next(my_iter))  # 1
print(next(my_iter))  # 2
print(next(my_iter))  # 3

# What for loop does behind the scenes
print("\nWhat for loop does:")
my_list = [1, 2, 3]
iterator = iter(my_list)
while True:
    try:
        element = next(iterator)
        print(element)
    except StopIteration:
        break

# ============================================
# 2. CREATING CUSTOM ITERATOR
# ============================================

print("\n" + "="*50)
print("CUSTOM ITERATOR CLASS")
print("="*50)

class CountDown:
    def __init__(self, start):
        self.current = start
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current <= 0:
            raise StopIteration
        self.current -= 1
        return self.current + 1

print("\nCountdown from 5:")
for num in CountDown(5):
    print(num, end=" ")

# Range-like iterator
class MyRange:
    def __init__(self, start, end):
        self.current = start
        self.end = end
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current >= self.end:
            raise StopIteration
        self.current += 1
        return self.current - 1

print("\n\nMyRange(1, 6):")
for num in MyRange(1, 6):
    print(num, end=" ")

# ============================================
# 3. GENERATORS - THE EASY WAY
# ============================================

print("\n\n" + "="*50)
print("GENERATORS")
print("="*50)

print("""
Generators are a simple way to create iterators using functions.
They use the 'yield' keyword instead of 'return'.
""")

# Simple generator function
def countdown(n):
    print("\nStarting countdown")
    while n > 0:
        yield n
        n -= 1
    print("Countdown complete!")

print("\nUsing generator:")
for num in countdown(5):
    print(num, end=" ")

# Generator vs Regular function
def regular_function():
    return [1, 2, 3, 4, 5]

def generator_function():
    yield 1
    yield 2
    yield 3
    yield 4
    yield 5

print("\n\nRegular function:", regular_function())
print("Generator function:", generator_function())  # Returns generator object

gen = generator_function()
print("First value:", next(gen))
print("Second value:", next(gen))

# ============================================
# 4. YIELD KEYWORD
# ============================================

print("\n" + "="*50)
print("YIELD KEYWORD")
print("="*50)

# Generator pauses at yield and resumes from there
def simple_generator():
    print("First yield")
    yield 1
    print("Second yield")
    yield 2
    print("Third yield")
    yield 3
    print("No more yields")

print("\nStep-by-step execution:")
gen = simple_generator()
print(f"Value: {next(gen)}")
print(f"Value: {next(gen)}")
print(f"Value: {next(gen)}")

# Infinite generator
def infinite_sequence():
    num = 0
    while True:
        yield num
        num += 1

print("\nInfinite sequence (first 10):")
gen = infinite_sequence()
for _ in range(10):
    print(next(gen), end=" ")

# ============================================
# 5. PRACTICAL GENERATOR EXAMPLES
# ============================================

print("\n\n" + "="*50)
print("PRACTICAL GENERATORS")
print("="*50)

# Fibonacci generator
def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

print("\nFirst 10 Fibonacci numbers:")
fib = fibonacci()
for _ in range(10):
    print(next(fib), end=" ")

# Reading large files line by line (memory efficient)
def read_large_file(file_path):
    """Generator to read large files line by line"""
    with open(file_path, 'r') as file:
        for line in file:
            yield line.strip()

# Even numbers generator
def even_numbers(n):
    """Generate even numbers up to n"""
    for i in range(n):
        if i % 2 == 0:
            yield i

print("\n\nEven numbers up to 20:")
for num in even_numbers(20):
    print(num, end=" ")

# Range generator (like built-in range)
def my_range(start, end, step=1):
    current = start
    while current < end:
        yield current
        current += step

print("\n\nCustom range(0, 10, 2):")
for num in my_range(0, 10, 2):
    print(num, end=" ")

# ============================================
# 6. GENERATOR EXPRESSIONS
# ============================================

print("\n\n" + "="*50)
print("GENERATOR EXPRESSIONS")
print("="*50)

# List comprehension vs Generator expression
list_comp = [x**2 for x in range(10)]  # Creates list in memory
gen_exp = (x**2 for x in range(10))     # Creates generator object

print(f"\nList comprehension: {list_comp}")
print(f"Generator expression: {gen_exp}")

# Memory comparison
list_size = sys.getsizeof(list_comp)
gen_size = sys.getsizeof(gen_exp)
print(f"\nList size: {list_size} bytes")
print(f"Generator size: {gen_size} bytes")

# Using generator expression
print("\nValues from generator:")
for value in gen_exp:
    print(value, end=" ")

# Generator expression with filter
print("\n\nEven squares:")
even_squares = (x**2 for x in range(10) if x % 2 == 0)
for value in even_squares:
    print(value, end=" ")

# Sum with generator expression
total = sum(x**2 for x in range(10))
print(f"\n\nSum of squares: {total}")

# ============================================
# 7. GENERATOR METHODS
# ============================================

print("\n" + "="*50)
print("GENERATOR METHODS")
print("="*50)

# send() method
def echo_generator():
    while True:
        received = yield
        print(f"Received: {received}")

gen = echo_generator()
next(gen)  # Prime the generator
gen.send("Hello")
gen.send("World")

# throw() method
def error_handler():
    try:
        while True:
            value = yield
            print(f"Got value: {value}")
    except ValueError:
        print("Caught ValueError!")

gen = error_handler()
next(gen)
gen.send(10)
gen.throw(ValueError)

# close() method
def closeable_generator():
    try:
        while True:
            value = yield
            print(f"Processing: {value}")
    except GeneratorExit:
        print("Generator closed!")

gen = closeable_generator()
next(gen)
gen.send("data")
gen.close()

# ============================================
# 8. YIELD FROM (Python 3.3+)
# ============================================

print("\n" + "="*50)
print("YIELD FROM")
print("="*50)

# Delegating to another generator
def generator1():
    yield 1
    yield 2

def generator2():
    yield 3
    yield 4

def combined_generator():
    yield from generator1()
    yield from generator2()

print("\nCombined generator:")
for value in combined_generator():
    print(value, end=" ")

# Flattening nested lists
def flatten(nested_list):
    for item in nested_list:
        if isinstance(item, list):
            yield from flatten(item)
        else:
            yield item

nested = [1, [2, 3, [4, 5]], 6, [7, [8, 9]]]
print(f"\n\nNested: {nested}")
print(f"Flattened: {list(flatten(nested))}")

# ============================================
# 9. PIPELINE PATTERN
# ============================================

print("\n" + "="*50)
print("GENERATOR PIPELINE")
print("="*50)

# Chaining generators for data processing
def read_numbers(numbers):
    """Read numbers"""
    for num in numbers:
        yield num

def filter_even(numbers):
    """Filter even numbers"""
    for num in numbers:
        if num % 2 == 0:
            yield num

def square_numbers(numbers):
    """Square the numbers"""
    for num in numbers:
        yield num ** 2

# Create pipeline
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pipeline = square_numbers(filter_even(read_numbers(data)))

print("\nPipeline result:")
print(list(pipeline))

# ============================================
# 10. GENERATOR VS LIST - PERFORMANCE
# ============================================

print("\n" + "="*50)
print("GENERATOR VS LIST - PERFORMANCE")
print("="*50)

import time

# List approach (creates all items in memory)
def list_approach(n):
    result = []
    for i in range(n):
        result.append(i ** 2)
    return result

# Generator approach (lazy evaluation)
def generator_approach(n):
    for i in range(n):
        yield i ** 2

n = 1000000

# List timing
start = time.time()
list_result = list_approach(n)
_ = sum(list_result)
list_time = time.time() - start

# Generator timing
start = time.time()
gen_result = generator_approach(n)
_ = sum(gen_result)
gen_time = time.time() - start

print(f"\nList approach: {list_time:.4f} seconds")
print(f"Generator approach: {gen_time:.4f} seconds")
print(f"Generator is {list_time/gen_time:.2f}x faster!")

# ============================================
# PRACTICE EXERCISES
# ============================================

print("\n" + "="*50)
print("PRACTICE EXERCISES")
print("="*50)

# Exercise 1: Prime number generator
def prime_generator(limit):
    """Generate prime numbers up to limit"""
    for num in range(2, limit):
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            yield num

print("\n1. Prime numbers up to 30:")
print(list(prime_generator(30)))

# Exercise 2: Reverse string generator
def reverse_string(text):
    """Generate characters in reverse"""
    for i in range(len(text) - 1, -1, -1):
        yield text[i]

print("\n2. Reverse 'Python':")
print(''.join(reverse_string("Python")))

# Exercise 3: Batch generator
def batch_generator(data, batch_size):
    """Generate data in batches"""
    for i in range(0, len(data), batch_size):
        yield data[i:i + batch_size]

data = list(range(20))
print("\n3. Batches of 5:")
for batch in batch_generator(data, 5):
    print(batch)

# Exercise 4: Cycle generator
def cycle(iterable):
    """Cycle through iterable indefinitely"""
    while True:
        for item in iterable:
            yield item

colors = ['red', 'green', 'blue']
color_cycle = cycle(colors)
print("\n4. First 10 from cycle:")
for _ in range(10):
    print(next(color_cycle), end=" ")

# Exercise 5: Running average generator
def running_average():
    """Calculate running average"""
    total = 0
    count = 0
    while True:
        value = yield (total / count if count > 0 else 0)
        total += value
        count += 1

avg = running_average()
next(avg)  # Prime it
print("\n\n5. Running average:")
print(f"After 10: {avg.send(10)}")
print(f"After 20: {avg.send(20)}")
print(f"After 30: {avg.send(30)}")

# Exercise 6: Enumerate generator
def my_enumerate(iterable, start=0):
    """Custom enumerate generator"""
    index = start
    for item in iterable:
        yield index, item
        index += 1

fruits = ['apple', 'banana', 'cherry']
print("\n6. Custom enumerate:")
for index, fruit in my_enumerate(fruits):
    print(f"{index}: {fruit}")

# Exercise 7: Zip generator
def my_zip(*iterables):
    """Custom zip generator"""
    iterators = [iter(it) for it in iterables]
    while True:
        try:
            yield tuple(next(it) for it in iterators)
        except StopIteration:
            break

list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
print("\n7. Custom zip:")
for pair in my_zip(list1, list2):
    print(pair)

print("\n" + "="*50)
print("Amazing!")
print("="*50)
