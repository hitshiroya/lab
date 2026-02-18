"""
Python Decorators
=================
This file covers function decorators, class decorators, and built-in decorators
"""

import time
import functools

# ============================================
# 1. UNDERSTANDING DECORATORS
# ============================================

print("="*50)
print("WHAT ARE DECORATORS?")
print("="*50)

print("""
Decorators are functions that modify the behavior of other functions.
They allow you to wrap another function to extend its behavior without
permanently modifying it.

Syntax:
    @decorator
    def function():
        pass

Is equivalent to:
    function = decorator(function)
""")

# ============================================
# 2. BASIC DECORATOR
# ============================================

print("\n" + "="*50)
print("BASIC DECORATOR")
print("="*50)

# Simple decorator
def my_decorator(func):
    def wrapper():
        print("Before function call")
        func()
        print("After function call")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

print("\nCalling decorated function:")
say_hello()

# Without decorator syntax (equivalent)
def say_goodbye():
    print("Goodbye!")

say_goodbye = my_decorator(say_goodbye)
print("\nWithout @ syntax:")
say_goodbye()

# ============================================
# 3. DECORATOR WITH ARGUMENTS
# ============================================

print("\n" + "="*50)
print("DECORATOR WITH ARGUMENTS")
print("="*50)

def decorator_with_args(func):
    def wrapper(*args, **kwargs):
        print(f"\nCalling {func.__name__} with args: {args}, kwargs: {kwargs}")
        result = func(*args, **kwargs)
        print(f"Result: {result}")
        return result
    return wrapper

@decorator_with_args
def add(a, b):
    return a + b

@decorator_with_args
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

add(5, 3)
greet("Alice")
greet("Bob", greeting="Hi")

# ============================================
# 4. PRACTICAL DECORATORS
# ============================================

print("\n" + "="*50)
print("PRACTICAL DECORATORS")
print("="*50)

# Timing decorator
def timer(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"\n{func.__name__} took {end - start:.4f} seconds")
        return result
    return wrapper

@timer
def slow_function():
    time.sleep(0.1)
    return "Done!"

result = slow_function()

# Logging decorator
def logger(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"\n[LOG] Calling {func.__name__}")
        result = func(*args, **kwargs)
        print(f"[LOG] {func.__name__} returned {result}")
        return result
    return wrapper

@logger
def calculate(a, b):
    return a * b

calculate(5, 3)

# Cache/Memoization decorator
def memoize(func):
    cache = {}
    @functools.wraps(func)
    def wrapper(*args):
        if args in cache:
            print(f"\nReturning cached result for {args}")
            return cache[args]
        print(f"\nCalculating result for {args}")
        result = func(*args)
        cache[args] = result
        return result
    return wrapper

@memoize
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

print("\nFibonacci(5):", fibonacci(5))
print("Fibonacci(5) again:", fibonacci(5))  # Will use cache

# Authentication decorator
def require_auth(func):
    @functools.wraps(func)
    def wrapper(user, *args, **kwargs):
        if user.get("authenticated"):
            return func(user, *args, **kwargs)
        else:
            return "Access denied! Please login."
    return wrapper

@require_auth
def view_profile(user):
    return f"Welcome, {user['name']}!"

user1 = {"name": "Alice", "authenticated": True}
user2 = {"name": "Bob", "authenticated": False}

print(f"\n{view_profile(user1)}")
print(f"{view_profile(user2)}")

# ============================================
# 5. DECORATORS WITH PARAMETERS
# ============================================

print("\n" + "="*50)
print("DECORATORS WITH PARAMETERS")
print("="*50)

def repeat(times):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat(times=3)
def greet(name):
    print(f"Hello, {name}!")

print("\nRepeating 3 times:")
greet("Alice")

# Prefix decorator
def prefix(prefix_text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            return f"{prefix_text}: {result}"
        return wrapper
    return decorator

@prefix("IMPORTANT")
def get_message():
    return "This is a message"

print(f"\n{get_message()}")

# Debug decorator with level
def debug(level="INFO"):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            print(f"\n[{level}] Calling {func.__name__}")
            print(f"[{level}] Arguments: {args}, {kwargs}")
            result = func(*args, **kwargs)
            print(f"[{level}] Returned: {result}")
            return result
        return wrapper
    return decorator

@debug(level="DEBUG")
def divide(a, b):
    return a / b

divide(10, 2)

# ============================================
# 6. CHAINING DECORATORS
# ============================================

print("\n" + "="*50)
print("CHAINING DECORATORS")
print("="*50)

def bold(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return f"**{result}**"
    return wrapper

def italic(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return f"_{result}_"
    return wrapper

@bold
@italic
def get_text():
    return "Hello World"

print(f"\n{get_text()}")  # **_Hello World_**

# Order matters!
@italic
@bold
def get_text2():
    return "Hello World"

print(f"{get_text2()}")  # _**Hello World**_

# ============================================
# 7. CLASS DECORATORS
# ============================================

print("\n" + "="*50)
print("CLASS DECORATORS")
print("="*50)

# Decorator as a class
class CountCalls:
    def __init__(self, func):
        self.func = func
        self.count = 0
    
    def __call__(self, *args, **kwargs):
        self.count += 1
        print(f"\nCall {self.count} of {self.func.__name__}")
        return self.func(*args, **kwargs)

@CountCalls
def say_hello():
    print("Hello!")

say_hello()
say_hello()
say_hello()

# Decorator for classes (not class-based decorator)
def singleton(cls):
    instances = {}
    @functools.wraps(cls)
    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return get_instance

@singleton
class Database:
    def __init__(self):
        print("\nInitializing database...")

db1 = Database()
db2 = Database()
print(f"Same instance? {db1 is db2}")

# ============================================
# 8. BUILT-IN DECORATORS
# ============================================

print("\n" + "="*50)
print("BUILT-IN DECORATORS")
print("="*50)

class MyClass:
    class_variable = "I'm a class variable"
    
    def __init__(self, value):
        self.value = value
    
    # Instance method (default)
    def instance_method(self):
        return f"Instance method called with value: {self.value}"
    
    # Class method
    @classmethod
    def class_method(cls):
        return f"Class method called. Class variable: {cls.class_variable}"
    
    # Static method
    @staticmethod
    def static_method(x, y):
        return f"Static method called with {x} and {y}"
    
    # Property decorator (getter)
    @property
    def formatted_value(self):
        return f"Value: {self.value}"
    
    # Setter for property
    @formatted_value.setter
    def formatted_value(self, new_value):
        self.value = new_value

obj = MyClass(42)

print(f"\n{obj.instance_method()}")
print(f"{MyClass.class_method()}")
print(f"{MyClass.static_method(10, 20)}")
print(f"{obj.formatted_value}")  # No parentheses!

obj.formatted_value = 100
print(f"After setter: {obj.formatted_value}")

# ============================================
# 9. FUNCTOOLS.WRAPS
# ============================================

print("\n" + "="*50)
print("FUNCTOOLS.WRAPS - Why it's important")
print("="*50)

# Without functools.wraps
def decorator_without_wraps(func):
    def wrapper(*args, **kwargs):
        """This is the wrapper function"""
        return func(*args, **kwargs)
    return wrapper

# With functools.wraps
def decorator_with_wraps(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        """This is the wrapper function"""
        return func(*args, **kwargs)
    return wrapper

@decorator_without_wraps
def function1():
    """This is function1"""
    pass

@decorator_with_wraps
def function2():
    """This is function2"""
    pass

print(f"\nWithout wraps - Name: {function1.__name__}")
print(f"Without wraps - Doc: {function1.__doc__}")

print(f"\nWith wraps - Name: {function2.__name__}")
print(f"With wraps - Doc: {function2.__doc__}")

# ============================================
# PRACTICE EXERCISES
# ============================================

print("\n" + "="*50)
print("PRACTICE EXERCISES")
print("="*50)

# Exercise 1: Uppercase decorator
def uppercase(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result.upper()
    return wrapper

@uppercase
def get_greeting(name):
    return f"hello, {name}"

print(f"\n1. {get_greeting('alice')}")

# Exercise 2: Validate arguments decorator
def validate_positive(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        for arg in args:
            if isinstance(arg, (int, float)) and arg < 0:
                raise ValueError("All arguments must be positive")
        return func(*args, **kwargs)
    return wrapper

@validate_positive
def multiply(a, b):
    return a * b

print(f"\n2. Multiply(5, 3): {multiply(5, 3)}")
# multiply(-5, 3)  # Would raise ValueError

# Exercise 3: Exception handler decorator
def exception_handler(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            return f"Error: {e}"
    return wrapper

@exception_handler
def divide_numbers(a, b):
    return a / b

print(f"\n3. Divide 10/2: {divide_numbers(10, 2)}")
print(f"   Divide 10/0: {divide_numbers(10, 0)}")

# Exercise 4: Rate limiter (simplified)
def rate_limit(max_calls):
    def decorator(func):
        calls = []
        
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            calls.append(time.time())
            if len(calls) > max_calls:
                return f"Rate limit exceeded! Max {max_calls} calls."
            return func(*args, **kwargs)
        return wrapper
    return decorator

@rate_limit(max_calls=3)
def api_call():
    return "API response"

print(f"\n4. Call 1: {api_call()}")
print(f"   Call 2: {api_call()}")
print(f"   Call 3: {api_call()}")
print(f"   Call 4: {api_call()}")

# Exercise 5: Type checker decorator
def type_check(*types):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for arg, expected_type in zip(args, types):
                if not isinstance(arg, expected_type):
                    raise TypeError(f"Expected {expected_type}, got {type(arg)}")
            return func(*args, **kwargs)
        return wrapper
    return decorator

@type_check(int, int)
def add_integers(a, b):
    return a + b

print(f"\n5. Add integers(5, 3): {add_integers(5, 3)}")
# add_integers("5", 3)  # Would raise TypeError

print("\n" + "="*50)
print("Excellent!")
print("="*50)
