"""
Python Object-Oriented Programming (OOP)
=========================================
This file covers classes, objects, inheritance, polymorphism, and more
"""

# ============================================
# 1. CLASSES AND OBJECTS
# ============================================

print("="*50)
print("CLASSES AND OBJECTS")
print("="*50)

# Simple class
class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
    
    def bark(self):
        return f"{self.name} says Woof!"
    
    def info(self):
        return f"{self.name} is a {self.breed}"

# Creating objects (instances)
dog1 = Dog("Buddy", "Golden Retriever")
dog2 = Dog("Max", "German Shepherd")

print(f"\n{dog1.bark()}")
print(f"{dog1.info()}")
print(f"\n{dog2.bark()}")
print(f"{dog2.info()}")

# ============================================
# 2. INSTANCE VS CLASS VARIABLES
# ============================================

print("\n" + "="*50)
print("INSTANCE VS CLASS VARIABLES")
print("="*50)

class Employee:
    # Class variable (shared by all instances)
    company = "TechCorp"
    employee_count = 0
    
    def __init__(self, name, salary):
        # Instance variables (unique to each instance)
        self.name = name
        self.salary = salary
        Employee.employee_count += 1
    
    def display_info(self):
        return f"{self.name} works at {self.company} with salary ${self.salary}"

emp1 = Employee("Alice", 50000)
emp2 = Employee("Bob", 60000)

print(f"\n{emp1.display_info()}")
print(f"{emp2.display_info()}")
print(f"\nTotal employees: {Employee.employee_count}")

# Modifying class variable
Employee.company = "NewTech"
print(f"\nAfter changing company:")
print(f"{emp1.display_info()}")
print(f"{emp2.display_info()}")

# ============================================
# 3. ENCAPSULATION (Public, Protected, Private)
# ============================================

print("\n" + "="*50)
print("ENCAPSULATION")
print("="*50)

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner              # Public
        self._account_number = "12345"  # Protected (convention)
        self.__balance = balance        # Private (name mangling)
    
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            return f"Deposited ${amount}. New balance: ${self.__balance}"
        return "Invalid amount"
    
    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            return f"Withdrew ${amount}. Remaining: ${self.__balance}"
        return "Insufficient funds or invalid amount"
    
    def get_balance(self):
        return self.__balance

account = BankAccount("Alice", 1000)

print(f"\nOwner: {account.owner}")  # OK
print(f"Protected: {account._account_number}")  # Works but shouldn't be used
# print(account.__balance)  # Error! Can't access private
print(f"Balance: {account.get_balance()}")  # Use getter method

print(f"\n{account.deposit(500)}")
print(f"{account.withdraw(200)}")

# ============================================
# 4. PROPERTY DECORATORS (Getters and Setters)
# ============================================

print("\n" + "="*50)
print("PROPERTY DECORATORS")
print("="*50)

class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age
    
    @property
    def name(self):
        """Getter for name"""
        return self._name
    
    @name.setter
    def name(self, value):
        """Setter for name"""
        if isinstance(value, str) and value:
            self._name = value
        else:
            raise ValueError("Name must be a non-empty string")
    
    @property
    def age(self):
        """Getter for age"""
        return self._age
    
    @age.setter
    def age(self, value):
        """Setter for age with validation"""
        if isinstance(value, int) and 0 <= value <= 150:
            self._age = value
        else:
            raise ValueError("Age must be between 0 and 150")
    
    @property
    def info(self):
        """Read-only property"""
        return f"{self._name} is {self._age} years old"

person = Person("Alice", 25)

print(f"\n{person.info}")

# Using setters
person.name = "Bob"
person.age = 30
print(f"{person.info}")

# Validation works
try:
    person.age = 200
except ValueError as e:
    print(f"\nError: {e}")

# ============================================
# 5. INHERITANCE
# ============================================

print("\n" + "="*50)
print("INHERITANCE")
print("="*50)

# Parent class (Base class)
class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
    
    def make_sound(self):
        return "Some generic sound"
    
    def info(self):
        return f"{self.name} is a {self.species}"

# Child classes (Derived classes)
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name, "Dog")
        self.breed = breed
    
    def make_sound(self):
        return "Woof! Woof!"

class Cat(Animal):
    def __init__(self, name, color):
        super().__init__(name, "Cat")
        self.color = color
    
    def make_sound(self):
        return "Meow!"

dog = Dog("Buddy", "Golden Retriever")
cat = Cat("Whiskers", "Orange")

print(f"\n{dog.info()}")
print(f"{dog.make_sound()}")
print(f"Breed: {dog.breed}")

print(f"\n{cat.info()}")
print(f"{cat.make_sound()}")
print(f"Color: {cat.color}")

# ============================================
# 6. POLYMORPHISM
# ============================================

print("\n" + "="*50)
print("POLYMORPHISM")
print("="*50)

# Same interface, different implementation
class Shape:
    def area(self):
        pass
    
    def perimeter(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14159 * self.radius ** 2
    
    def perimeter(self):
        return 2 * 3.14159 * self.radius

# Polymorphism in action
shapes = [
    Rectangle(5, 10),
    Circle(7),
    Rectangle(3, 4)
]

print("\nCalculating areas and perimeters:")
for shape in shapes:
    print(f"{shape.__class__.__name__}: Area = {shape.area():.2f}, Perimeter = {shape.perimeter():.2f}")

# ============================================
# 7. MULTIPLE INHERITANCE
# ============================================

print("\n" + "="*50)
print("MULTIPLE INHERITANCE")
print("="*50)

class Flyer:
    def fly(self):
        return "Flying in the sky"

class Swimmer:
    def swim(self):
        return "Swimming in water"

class Duck(Flyer, Swimmer):
    def __init__(self, name):
        self.name = name
    
    def quack(self):
        return "Quack quack!"

duck = Duck("Donald")
print(f"\n{duck.name} can:")
print(f"- {duck.fly()}")
print(f"- {duck.swim()}")
print(f"- {duck.quack()}")

# Method Resolution Order (MRO)
print(f"\nMRO: {Duck.__mro__}")

# ============================================
# 8. ABSTRACT CLASSES
# ============================================

print("\n" + "="*50)
print("ABSTRACT CLASSES")
print("="*50)

from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self, brand):
        self.brand = brand
    
    @abstractmethod
    def start(self):
        """Must be implemented by subclasses"""
        pass
    
    @abstractmethod
    def stop(self):
        """Must be implemented by subclasses"""
        pass
    
    def info(self):
        """Concrete method"""
        return f"This is a {self.brand} vehicle"

class Car(Vehicle):
    def start(self):
        return f"{self.brand} car engine started"
    
    def stop(self):
        return f"{self.brand} car engine stopped"

class Motorcycle(Vehicle):
    def start(self):
        return f"{self.brand} motorcycle engine started"
    
    def stop(self):
        return f"{self.brand} motorcycle engine stopped"

# Cannot instantiate abstract class
# vehicle = Vehicle("Generic")  # TypeError!

car = Car("Toyota")
bike = Motorcycle("Harley")

print(f"\n{car.info()}")
print(f"{car.start()}")
print(f"{car.stop()}")

print(f"\n{bike.info()}")
print(f"{bike.start()}")
print(f"{bike.stop()}")

# ============================================
# 9. MAGIC METHODS (DUNDER METHODS)
# ============================================

print("\n" + "="*50)
print("MAGIC METHODS")
print("="*50)

class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
    
    def __str__(self):
        """String representation for users"""
        return f"'{self.title}' by {self.author}"
    
    def __repr__(self):
        """String representation for developers"""
        return f"Book('{self.title}', '{self.author}', {self.pages})"
    
    def __len__(self):
        """Length of the book"""
        return self.pages
    
    def __eq__(self, other):
        """Equality comparison"""
        return self.title == other.title and self.author == other.author
    
    def __lt__(self, other):
        """Less than comparison"""
        return self.pages < other.pages
    
    def __add__(self, other):
        """Addition operator"""
        return self.pages + other.pages

book1 = Book("Python Guide", "John Doe", 300)
book2 = Book("Python Advanced", "Jane Smith", 450)

print(f"\nstr(book1): {str(book1)}")
print(f"repr(book1): {repr(book1)}")
print(f"len(book1): {len(book1)} pages")
print(f"book1 < book2: {book1 < book2}")
print(f"book1 + book2: {book1 + book2} total pages")

# ============================================
# 10. CLASS METHODS AND STATIC METHODS
# ============================================

print("\n" + "="*50)
print("CLASS METHODS AND STATIC METHODS")
print("="*50)

class Date:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year
    
    @classmethod
    def from_string(cls, date_string):
        """Alternative constructor"""
        day, month, year = map(int, date_string.split('-'))
        return cls(day, month, year)
    
    @staticmethod
    def is_valid_date(day, month, year):
        """Utility function related to the class"""
        return 1 <= day <= 31 and 1 <= month <= 12 and year > 0
    
    def display(self):
        return f"{self.day:02d}/{self.month:02d}/{self.year}"

# Regular instantiation
date1 = Date(15, 6, 2024)
print(f"\nDate 1: {date1.display()}")

# Using class method
date2 = Date.from_string("25-12-2024")
print(f"Date 2: {date2.display()}")

# Using static method
print(f"\nIs 31-12-2024 valid? {Date.is_valid_date(31, 12, 2024)}")
print(f"Is 32-13-2024 valid? {Date.is_valid_date(32, 13, 2024)}")

# ============================================
# 11. COMPOSITION (HAS-A RELATIONSHIP)
# ============================================

print("\n" + "="*50)
print("COMPOSITION")
print("="*50)

class Engine:
    def __init__(self, horsepower):
        self.horsepower = horsepower
    
    def start(self):
        return f"Engine with {self.horsepower}hp started"

class Wheel:
    def __init__(self, size):
        self.size = size

class Car:
    def __init__(self, brand, engine, wheels):
        self.brand = brand
        self.engine = engine  # Car HAS-A Engine
        self.wheels = wheels  # Car HAS-A list of Wheels
    
    def start(self):
        return f"{self.brand}: {self.engine.start()}"
    
    def info(self):
        return f"{self.brand} with {len(self.wheels)} wheels of size {self.wheels[0].size}\""

engine = Engine(300)
wheels = [Wheel(18) for _ in range(4)]
car = Car("BMW", engine, wheels)

print(f"\n{car.start()}")
print(f"{car.info()}")

# ============================================
# 12. OPERATOR OVERLOADING
# ============================================

print("\n" + "="*50)
print("OPERATOR OVERLOADING")
print("="*50)

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, other):
        """Vector addition"""
        return Vector(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other):
        """Vector subtraction"""
        return Vector(self.x - other.x, self.y - other.y)
    
    def __mul__(self, scalar):
        """Scalar multiplication"""
        return Vector(self.x * scalar, self.y * scalar)
    
    def __str__(self):
        return f"Vector({self.x}, {self.y})"
    
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

v1 = Vector(2, 3)
v2 = Vector(5, 7)

print(f"\nv1: {v1}")
print(f"v2: {v2}")
print(f"v1 + v2: {v1 + v2}")
print(f"v1 - v2: {v1 - v2}")
print(f"v1 * 3: {v1 * 3}")
print(f"v1 == v2: {v1 == v2}")

# ============================================
# PRACTICE EXERCISES
# ============================================

print("\n" + "="*50)
print("PRACTICE EXERCISES")
print("="*50)

# Exercise 1: Library System
class Library:
    def __init__(self, name):
        self.name = name
        self.books = []
    
    def add_book(self, book):
        self.books.append(book)
    
    def list_books(self):
        return [str(book) for book in self.books]

library = Library("City Library")
library.add_book(Book("Python 101", "John", 200))
library.add_book(Book("Java Guide", "Jane", 300))

print("\n1. Library books:")
for book in library.list_books():
    print(f"   - {book}")

# Exercise 2: Bank Account with Transaction History
class BankAccountAdvanced:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.__balance = balance
        self.__transactions = []
    
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            self.__transactions.append(f"Deposited ${amount}")
            return f"Deposited ${amount}"
        return "Invalid amount"
    
    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            self.__transactions.append(f"Withdrew ${amount}")
            return f"Withdrew ${amount}"
        return "Insufficient funds"
    
    def get_balance(self):
        return self.__balance
    
    def transaction_history(self):
        return self.__transactions

account = BankAccountAdvanced("Alice", 1000)
account.deposit(500)
account.withdraw(200)

print("\n2. Transaction history:")
for transaction in account.transaction_history():
    print(f"   - {transaction}")
print(f"   Final balance: ${account.get_balance()}")

# Exercise 3: Student Grade System
class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.grades = {}
    
    def add_grade(self, subject, grade):
        self.grades[subject] = grade
    
    def calculate_average(self):
        if not self.grades:
            return 0
        return sum(self.grades.values()) / len(self.grades)
    
    def get_letter_grade(self):
        avg = self.calculate_average()
        if avg >= 90: return 'A'
        elif avg >= 80: return 'B'
        elif avg >= 70: return 'C'
        elif avg >= 60: return 'D'
        else: return 'F'

student = Student("Bob", "S001")
student.add_grade("Math", 85)
student.add_grade("Science", 92)
student.add_grade("English", 88)

print(f"\n3. Student: {student.name}")
print(f"   Average: {student.calculate_average():.2f}")
print(f"   Grade: {student.get_letter_grade()}")

# Exercise 4: Stack Implementation
class Stack:
    def __init__(self):
        self.__items = []
    
    def push(self, item):
        self.__items.append(item)
    
    def pop(self):
        if not self.is_empty():
            return self.__items.pop()
        return None
    
    def peek(self):
        if not self.is_empty():
            return self.__items[-1]
        return None
    
    def is_empty(self):
        return len(self.__items) == 0
    
    def size(self):
        return len(self.__items)

stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)

print(f"\n4. Stack size: {stack.size()}")
print(f"   Top element: {stack.peek()}")
print(f"   Popped: {stack.pop()}")
print(f"   New size: {stack.size()}")

# Exercise 5: Temperature Converter
class Temperature:
    def __init__(self, celsius):
        self._celsius = celsius
    
    @property
    def celsius(self):
        return self._celsius
    
    @celsius.setter
    def celsius(self, value):
        if value < -273.15:
            raise ValueError("Temperature below absolute zero!")
        self._celsius = value
    
    @property
    def fahrenheit(self):
        return (self._celsius * 9/5) + 32
    
    @fahrenheit.setter
    def fahrenheit(self, value):
        self.celsius = (value - 32) * 5/9
    
    @property
    def kelvin(self):
        return self._celsius + 273.15

temp = Temperature(25)
print(f"\n5. {temp.celsius}°C = {temp.fahrenheit}°F = {temp.kelvin}K")

temp.fahrenheit = 100
print(f"   {temp.celsius:.2f}°C = {temp.fahrenheit}°F = {temp.kelvin:.2f}K")

print("\n" + "="*50)
print("Excellent!")
print("="*50)
