"""
Python Error Handling (Exception Handling)
==========================================
This file covers exceptions, try-except, custom exceptions, and error handling best practices
"""

import sys
import traceback
import logging
from typing import Optional

# ============================================
# 1. UNDERSTANDING EXCEPTIONS
# ============================================

print("="*50)
print("WHAT ARE EXCEPTIONS?")
print("="*50)

print("""
Exceptions are errors that occur during program execution.
When an exception occurs, the program stops unless it's handled.

Common built-in exceptions:
- ValueError: Invalid value
- TypeError: Wrong type
- KeyError: Key not found in dictionary
- IndexError: Index out of range
- ZeroDivisionError: Division by zero
- FileNotFoundError: File doesn't exist
- AttributeError: Invalid attribute reference
""")

# ============================================
# 2. BASIC TRY-EXCEPT
# ============================================

print("\n" + "="*50)
print("BASIC TRY-EXCEPT")
print("="*50)

# Without exception handling - program would crash
print("\nExample 1: Basic division")
try:
    result = 10 / 0  # This will cause ZeroDivisionError
    print(f"Result: {result}")
except:
    print("An error occurred!")

# Catching specific exception
print("\nExample 2: Specific exception")
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")

# Multiple exceptions
print("\nExample 3: Multiple exceptions")
try:
    numbers = [1, 2, 3]
    print(numbers[10])  # IndexError
except ZeroDivisionError:
    print("Division by zero!")
except IndexError:
    print("Index out of range!")

# Handling multiple exceptions with same handler
print("\nExample 4: Same handler for multiple exceptions")
try:
    # num = int("abc")  # ValueError
    result = 10 / 0     # ZeroDivisionError
except (ValueError, ZeroDivisionError) as e:
    print(f"Error occurred: {e}")

# ============================================
# 3. TRY-EXCEPT-ELSE-FINALLY
# ============================================

print("\n" + "="*50)
print("TRY-EXCEPT-ELSE-FINALLY")
print("="*50)

# ELSE: Executes if no exception occurs
print("\nExample 1: Using ELSE")
try:
    result = 10 / 2
except ZeroDivisionError:
    print("Cannot divide by zero!")
else:
    print(f"Division successful! Result: {result}")

# FINALLY: Always executes (cleanup code)
print("\nExample 2: Using FINALLY")
try:
    file = open("dummy.txt", "r")
    content = file.read()
except FileNotFoundError:
    print("File not found!")
finally:
    print("Cleanup: This always runs")
    # file.close()  # Would close file if it was opened

# Complete structure
print("\nExample 3: Complete structure")
def divide_numbers(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Error: Cannot divide by zero")
        return None
    except TypeError:
        print("Error: Invalid types")
        return None
    else:
        print(f"Success: {a} / {b} = {result}")
        return result
    finally:
        print("Cleanup completed")

divide_numbers(10, 2)
print()
divide_numbers(10, 0)

# ============================================
# 4. ACCESSING EXCEPTION DETAILS
# ============================================

print("\n" + "="*50)
print("ACCESSING EXCEPTION DETAILS")
print("="*50)

# Exception object
print("\nExample 1: Exception message")
try:
    number = int("not a number")
except ValueError as e:
    print(f"Exception type: {type(e).__name__}")
    print(f"Exception message: {e}")
    print(f"Exception args: {e.args}")

# Multiple exception info
print("\nExample 2: Detailed exception info")
try:
    result = 10 / 0
except Exception as e:
    print(f"Type: {type(e)}")
    print(f"Message: {str(e)}")
    print(f"Args: {e.args}")

# Exception traceback
print("\nExample 3: Traceback information")
try:
    def level1():
        level2()
    
    def level2():
        level3()
    
    def level3():
        result = 1 / 0
    
    level1()
except ZeroDivisionError:
    print("Error caught! Traceback:")
    traceback.print_exc()

# ============================================
# 5. RAISING EXCEPTIONS
# ============================================

print("\n" + "="*50)
print("RAISING EXCEPTIONS")
print("="*50)

# Basic raise
print("\nExample 1: Raising basic exception")
def check_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative!")
    if age < 18:
        raise ValueError("Must be 18 or older")
    return "Access granted"

try:
    print(check_age(25))
    print(check_age(-5))
except ValueError as e:
    print(f"Error: {e}")

# Re-raising exceptions
print("\nExample 2: Re-raising exceptions")
def process_data(data):
    try:
        result = int(data)
        return result
    except ValueError:
        print("Logging error...")
        raise  # Re-raises the same exception

try:
    process_data("invalid")
except ValueError:
    print("Caught re-raised exception")

# Raising different exception
print("\nExample 3: Raising different exception")
def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        raise ValueError("Division by zero is not allowed") from None

try:
    divide(10, 0)
except ValueError as e:
    print(f"Caught: {e}")

# Exception chaining
print("\nExample 4: Exception chaining")
def read_config():
    try:
        file = open("config.txt", "r")
    except FileNotFoundError as e:
        raise RuntimeError("Failed to load configuration") from e

try:
    read_config()
except RuntimeError as e:
    print(f"Error: {e}")
    print(f"Original cause: {e.__cause__}")

# ============================================
# 6. CUSTOM EXCEPTIONS
# ============================================

print("\n" + "="*50)
print("CUSTOM EXCEPTIONS")
print("="*50)

# Basic custom exception
print("\nExample 1: Basic custom exception")
class InvalidAgeError(Exception):
    pass

def verify_age(age):
    if age < 0 or age > 150:
        raise InvalidAgeError("Age must be between 0 and 150")
    return True

try:
    verify_age(200)
except InvalidAgeError as e:
    print(f"Custom error caught: {e}")

# Custom exception with attributes
print("\nExample 2: Custom exception with attributes")
class InsufficientFundsError(Exception):
    def __init__(self, balance, amount):
        self.balance = balance
        self.amount = amount
        self.message = f"Insufficient funds: Balance={balance}, Required={amount}"
        super().__init__(self.message)

class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance
    
    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficientFundsError(self.balance, amount)
        self.balance -= amount
        return self.balance

try:
    account = BankAccount(100)
    account.withdraw(150)
except InsufficientFundsError as e:
    print(f"Error: {e.message}")
    print(f"Balance: ${e.balance}")
    print(f"Attempted withdrawal: ${e.amount}")

# Exception hierarchy
print("\nExample 3: Custom exception hierarchy")
class ApplicationError(Exception):
    """Base exception for application"""
    pass

class DatabaseError(ApplicationError):
    """Database related errors"""
    pass

class ValidationError(ApplicationError):
    """Validation errors"""
    pass

class ConnectionError(DatabaseError):
    """Connection errors"""
    pass

def perform_operation(operation_type):
    if operation_type == "db_connect":
        raise ConnectionError("Failed to connect to database")
    elif operation_type == "validate":
        raise ValidationError("Invalid input data")

try:
    perform_operation("db_connect")
except ConnectionError as e:
    print(f"Connection error: {e}")
except DatabaseError as e:
    print(f"Database error: {e}")
except ApplicationError as e:
    print(f"Application error: {e}")

# ============================================
# 7. CONTEXT MANAGERS (with statement)
# ============================================

print("\n" + "="*50)
print("CONTEXT MANAGERS")
print("="*50)

# File handling with context manager
print("\nExample 1: File handling")
# This automatically closes the file
try:
    with open("test_file.txt", "w") as file:
        file.write("Hello, World!")
    print("File written successfully")
    
    with open("test_file.txt", "r") as file:
        content = file.read()
        print(f"File content: {content}")
except IOError as e:
    print(f"File error: {e}")

# Custom context manager using class
print("\nExample 2: Custom context manager (class)")
class DatabaseConnection:
    def __init__(self, db_name):
        self.db_name = db_name
        self.connection = None
    
    def __enter__(self):
        print(f"Opening connection to {self.db_name}")
        self.connection = f"Connection to {self.db_name}"
        return self.connection
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"Closing connection to {self.db_name}")
        if exc_type is not None:
            print(f"Exception occurred: {exc_type.__name__}: {exc_val}")
        return False  # Propagate exception

with DatabaseConnection("mydb") as conn:
    print(f"Using: {conn}")
    print("Performing operations...")

# Custom context manager using contextlib
print("\nExample 3: Context manager with contextlib")
from contextlib import contextmanager

@contextmanager
def managed_resource(name):
    print(f"Acquiring resource: {name}")
    resource = f"Resource: {name}"
    try:
        yield resource
    finally:
        print(f"Releasing resource: {name}")

with managed_resource("Database") as res:
    print(f"Using {res}")

# ============================================
# 8. ASSERTION
# ============================================

print("\n" + "="*50)
print("ASSERTIONS")
print("="*50)

# Basic assertion
print("\nExample 1: Basic assertion")
def calculate_percentage(score, total):
    assert total > 0, "Total must be positive"
    assert score >= 0, "Score cannot be negative"
    assert score <= total, "Score cannot exceed total"
    return (score / total) * 100

try:
    print(f"Percentage: {calculate_percentage(85, 100)}")
    print(f"Percentage: {calculate_percentage(110, 100)}")  # Will fail
except AssertionError as e:
    print(f"Assertion failed: {e}")

# Assertions for debugging
print("\nExample 2: Assertions for debugging")
def process_list(items):
    assert isinstance(items, list), "Input must be a list"
    assert len(items) > 0, "List cannot be empty"
    return sum(items)

try:
    print(f"Sum: {process_list([1, 2, 3, 4, 5])}")
    print(f"Sum: {process_list([])}")  # Will fail
except AssertionError as e:
    print(f"Assertion failed: {e}")

# ============================================
# 9. LOGGING ERRORS
# ============================================

print("\n" + "="*50)
print("LOGGING ERRORS")
print("="*50)

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

logger = logging.getLogger(__name__)

# Logging exceptions
print("\nExample 1: Logging with exception info")
def divide_with_logging(a, b):
    try:
        result = a / b
        logger.info(f"Division successful: {a} / {b} = {result}")
        return result
    except ZeroDivisionError:
        logger.error(f"Division by zero: {a} / {b}", exc_info=True)
        return None
    except Exception as e:
        logger.exception(f"Unexpected error: {e}")
        return None

divide_with_logging(10, 2)
divide_with_logging(10, 0)

# Different logging levels
print("\nExample 2: Different logging levels")
def process_user_input(data):
    logger.debug(f"Processing data: {data}")
    
    if not data:
        logger.warning("Empty data received")
        return None
    
    try:
        result = int(data)
        logger.info(f"Successfully processed: {result}")
        return result
    except ValueError:
        logger.error(f"Invalid data format: {data}")
        return None
    except Exception as e:
        logger.critical(f"Critical error: {e}")
        raise

process_user_input("123")
process_user_input("abc")
process_user_input("")

# ============================================
# 10. BEST PRACTICES
# ============================================

print("\n" + "="*50)
print("ERROR HANDLING BEST PRACTICES")
print("="*50)

# 1. Be specific with exceptions
print("\nPractice 1: Be specific")
def good_exception_handling(value):
    try:
        return int(value)
    except ValueError:  # Specific, not generic Exception
        print(f"Cannot convert '{value}' to integer")
        return None

good_exception_handling("abc")

# 2. Don't catch exceptions silently
print("\nPractice 2: Don't catch silently")
def bad_practice(value):
    try:
        return int(value)
    except:
        pass  # BAD: Silent failure

def good_practice(value):
    try:
        return int(value)
    except ValueError as e:
        logger.error(f"Conversion error: {e}")
        return None

# 3. Use finally for cleanup
print("\nPractice 3: Use finally for cleanup")
def process_file(filename):
    file = None
    try:
        file = open(filename, 'r')
        return file.read()
    except FileNotFoundError:
        print(f"File {filename} not found")
        return None
    finally:
        if file:
            file.close()
            print("File closed properly")

# 4. Fail fast with appropriate exceptions
print("\nPractice 4: Fail fast")
def create_user(name, age, email):
    if not name:
        raise ValueError("Name is required")
    if age < 0:
        raise ValueError("Age cannot be negative")
    if "@" not in email:
        raise ValueError("Invalid email format")
    
    return {"name": name, "age": age, "email": email}

try:
    user = create_user("Alice", 25, "alice@example.com")
    print(f"User created: {user}")
except ValueError as e:
    print(f"Validation error: {e}")

# 5. Clean up resources with context managers
print("\nPractice 5: Use context managers")
# Good: Automatic cleanup
try:
    with open("test_file.txt", "r") as f:
        content = f.read()
except FileNotFoundError:
    print("File not found")

# 6. Document exceptions in docstrings
print("\nPractice 6: Document exceptions")
def calculate_average(numbers):
    """
    Calculate the average of a list of numbers.
    
    Args:
        numbers (list): List of numeric values
    
    Returns:
        float: The average value
    
    Raises:
        ValueError: If the list is empty
        TypeError: If the input is not a list
    """
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list")
    if len(numbers) == 0:
        raise ValueError("Cannot calculate average of empty list")
    return sum(numbers) / len(numbers)

try:
    print(f"Average: {calculate_average([1, 2, 3, 4, 5])}")
except (ValueError, TypeError) as e:
    print(f"Error: {e}")

# ============================================
# 11. REAL-WORLD EXAMPLES
# ============================================

print("\n" + "="*50)
print("REAL-WORLD EXAMPLES")
print("="*50)

# Example 1: API Request Handler
print("\nExample 1: API Request Handler")
class APIError(Exception):
    pass

class RateLimitError(APIError):
    pass

class AuthenticationError(APIError):
    pass

def make_api_request(endpoint, authenticated=True):
    """Simulate API request"""
    if not authenticated:
        raise AuthenticationError("Authentication required")
    
    if endpoint == "/rate-limited":
        raise RateLimitError("Rate limit exceeded")
    
    return {"status": "success", "data": {"endpoint": endpoint}}

def handle_api_request(endpoint):
    try:
        response = make_api_request(endpoint)
        print(f"Success: {response}")
        return response
    except AuthenticationError as e:
        logger.error(f"Auth error: {e}")
        return {"error": "Please login"}
    except RateLimitError as e:
        logger.warning(f"Rate limit: {e}")
        return {"error": "Please try again later"}
    except APIError as e:
        logger.error(f"API error: {e}")
        return {"error": "Service unavailable"}
    except Exception as e:
        logger.critical(f"Unexpected error: {e}")
        return {"error": "Internal error"}

handle_api_request("/users")
handle_api_request("/rate-limited")

# Example 2: Data Validation
print("\nExample 2: Data Validator")
class ValidationError(Exception):
    def __init__(self, field, message):
        self.field = field
        self.message = message
        super().__init__(f"{field}: {message}")

def validate_user_data(data):
    errors = []
    
    try:
        # Validate name
        if not data.get("name"):
            raise ValidationError("name", "Name is required")
        if len(data["name"]) < 2:
            raise ValidationError("name", "Name too short")
        
        # Validate age
        age = data.get("age")
        if age is None:
            raise ValidationError("age", "Age is required")
        if not isinstance(age, int):
            raise ValidationError("age", "Age must be an integer")
        if age < 0 or age > 150:
            raise ValidationError("age", "Age must be between 0 and 150")
        
        # Validate email
        email = data.get("email", "")
        if "@" not in email:
            raise ValidationError("email", "Invalid email format")
        
        return True, None
    
    except ValidationError as e:
        return False, e

# Test validation
test_data = [
    {"name": "Alice", "age": 25, "email": "alice@example.com"},
    {"name": "B", "age": 25, "email": "bob@example.com"},
    {"name": "Charlie", "age": -5, "email": "charlie@example.com"},
]

for data in test_data:
    valid, error = validate_user_data(data)
    if valid:
        print(f"✓ Valid data: {data['name']}")
    else:
        print(f"✗ Invalid: {error}")

# Example 3: Retry Logic
print("\nExample 3: Retry with exponential backoff")
import time

def retry_operation(max_attempts=3, delay=1):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for attempt in range(max_attempts):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    if attempt == max_attempts - 1:
                        logger.error(f"Failed after {max_attempts} attempts")
                        raise
                    wait_time = delay * (2 ** attempt)
                    logger.warning(f"Attempt {attempt + 1} failed: {e}. Retrying in {wait_time}s...")
                    time.sleep(wait_time)
        return wrapper
    return decorator

call_count = 0

@retry_operation(max_attempts=3, delay=0.1)
def unreliable_operation():
    global call_count
    call_count += 1
    if call_count < 3:
        raise ConnectionError("Service temporarily unavailable")
    return "Success!"

try:
    result = unreliable_operation()
    print(f"Result: {result}")
except ConnectionError as e:
    print(f"Operation failed: {e}")

# ============================================
# PRACTICE EXERCISES
# ============================================

print("\n" + "="*50)
print("PRACTICE EXERCISES")
print("="*50)

# Exercise 1: Safe division function
print("\nExercise 1: Safe division")
def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Error: Division by zero"
    except TypeError:
        return "Error: Invalid types"

print(f"10 / 2 = {safe_divide(10, 2)}")
print(f"10 / 0 = {safe_divide(10, 0)}")
print(f"'10' / 2 = {safe_divide('10', 2)}")

# Exercise 2: File reader with error handling
print("\nExercise 2: Safe file reader")
def read_file_safe(filename):
    try:
        with open(filename, 'r') as f:
            return f.read()
    except FileNotFoundError:
        return f"Error: File '{filename}' not found"
    except PermissionError:
        return f"Error: No permission to read '{filename}'"
    except Exception as e:
        return f"Error: {e}"

content = read_file_safe("test_file.txt")
print(f"Content: {content[:50]}..." if len(str(content)) > 50 else f"Content: {content}")

# Exercise 3: Input validator
print("\nExercise 3: Integer input validator")
def get_valid_integer(prompt, min_value=None, max_value=None):
    while True:
        try:
            value = int(input(prompt))
            if min_value is not None and value < min_value:
                raise ValueError(f"Value must be >= {min_value}")
            if max_value is not None and value > max_value:
                raise ValueError(f"Value must be <= {max_value}")
            return value
        except ValueError as e:
            print(f"Invalid input: {e}")
            return None

# Commented out for automated execution
# age = get_valid_integer("Enter age (0-150): ", 0, 150)

# Exercise 4: Custom exception for business logic
print("\nExercise 4: Shopping cart with custom exceptions")
class OutOfStockError(Exception):
    pass

class InvalidQuantityError(Exception):
    pass

class ShoppingCart:
    def __init__(self):
        self.items = {}
        self.inventory = {"apple": 10, "banana": 5, "orange": 8}
    
    def add_item(self, item, quantity):
        if quantity <= 0:
            raise InvalidQuantityError("Quantity must be positive")
        
        if item not in self.inventory:
            raise KeyError(f"Item '{item}' not available")
        
        if self.inventory[item] < quantity:
            raise OutOfStockError(f"Only {self.inventory[item]} {item}(s) available")
        
        self.items[item] = self.items.get(item, 0) + quantity
        print(f"Added {quantity} {item}(s) to cart")

cart = ShoppingCart()
try:
    cart.add_item("apple", 3)
    cart.add_item("banana", 10)  # Out of stock
except OutOfStockError as e:
    print(f"Error: {e}")
except InvalidQuantityError as e:
    print(f"Error: {e}")
except KeyError as e:
    print(f"Error: {e}")

print("\n" + "="*50)
print("Complete! You've mastered error handling!")
print("="*50)
