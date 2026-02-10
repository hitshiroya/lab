# Python OOP Interview Questions


---

## 1. What is Object-Oriented Programming (OOP) in Python?

Object-Oriented Programming (OOP) in Python is a programming approach that models around objects, instances of classes which encapsulate both data and objects. While it shares core principles with general OOP, Python's OOP has some unique features:

- **Dynamic Typing:** Python classes and objects don't require explicit type declarations.
- **Everything is an object:** Even basic data types (like integers, functions) are objects with attributes and methods.
- **Multiple Inheritance:** Python supports inheriting from multiple classes, enabling complex class hierarchies.
- **Duck Typing:** Python emphasizes behavior over type, allowing polymorphism without strict type hierarchies.
- **Built-in Magic Methods:** Python uses special methods (like `__init__`, `__str__`, `__len__`) to customize object behavior, enabling operator overloading and integration with Python syntax.

---

## 2. What are the key features of OOP?

The key features of OOP are:

- **Encapsulation:** Bundles data and methods within a class, hiding internal details from outside access.
- **Abstraction:** Hides complex implementation details and exposes only necessary functionality.
- **Inheritance:** Allows a new class to inherit properties and methods from an existing class.
- **Polymorphism:** Enables a single interface to represent different behaviors.

---

## 3. What is a class and an object in Python?

- **Class:** A blueprint for creating objects, defining their properties and methods.
- **Object:** An instance of a class.

**Example:**

```python
class Dog:                                    # This is a class
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
    
    def speak(self):
        print(f"{self.name} says Woof!")

dog1 = Dog("Buddy", "Golden Retriever")       # This is an object of the class
dog1.speak()
```

**Output:**
```
Buddy says Woof!
```

---

## 4. What is the __init__ method in Python?

The `__init__` method in Python is a special constructor method that automatically runs when a new object of a class is created. It is used to initialize the object's attributes with default or user-provided values. It is similar to constructors in other OOP languages like Java or C++.

**Example:**

```python
class Person:
    def __init__(self, name):
        self.name = name
        
p = Person("Magnus")

print(p.name)
```

**Output:**
```
Magnus
```

---

## 5. What is self in Python classes?

`self` is a reference to the current instance of the class. It is used to access attributes and methods of the class. When you define a method inside a class, the first parameter of the method is always `self`, which allows the method to refer to the object (or instance) on which the method was called.

---

## 6. What is the difference between instance variables and class variables?

- **Instance variables** belong to a specific object of a class and are defined inside methods using `self` (e.g., `self.name`). Each object gets its own copy, so modifying one instance's variable does not affect others.
- **Class variables**, on the other hand, are defined directly inside the class but outside methods. They are shared across all objects of that class, so changing a class variable affects every instance (unless it is overridden at the instance level).

**Example:**

```python
class Demo:
    class_var = "shared" # class variable
    
    def __init__(self, val):
        self.instance_var = val # instance variable
```

---

## 7. What is inheritance in Python?

Inheritance allows a class to inherit attributes and methods from another class. Inheritance enables the child class to inherit the properties (attributes) and behaviors (methods) of the parent class, and it can also define its own additional attributes and methods or override existing ones.

**Example:**

```python
# Define the Parent class (base class)
class Parent:
    pass

# Define the Child class that inherits from Parent class
class Child(Parent):
    pass
```

---

## 8. What is method overloading in Python?

In languages like Java or C++, method overloading allows multiple methods with the same name but different parameters. Python does not support true method overloading. If you define two methods with the same name, the latest one will overwrite the previous definition.

However, Python provides similar flexibility using default arguments or variable-length arguments like `*args` and `**kwargs` to handle variable numbers of arguments in a single method.

**Example:**

```python
def add(*args):
    return sum(args)


print(add(2, 3))         # 5
print(add(2, 3, 4))      # 9
print(add(1, 2, 3, 4))   # 10
```

**Output:**
```
5
9
10
```

Here, instead of having multiple `add()` methods with different signatures, Python uses one method with `*args` to handle all cases — this is Python's way of mimicking method overloading.

---

## 9. What is method overriding in Python?

Method overriding allows a subclass to provide a specific implementation of a method that is already defined in its superclass. This means that the subclass can "override" the behavior of the method inherited from the parent class, providing a different version that is more suitable for the subclass.

**Example:**

```python
class Parent:
    def show(self):
        print("Parent")
        
class Child(Parent):
    def show(self):   # Method overriding
        print("Child")
```

---

## 10. What is polymorphism in Python?

Polymorphism allows objects to be treated as instances of their parent class, enabling different implementations for the same interface. It enables a single function, method, or operator to work with different types of objects in a way that is determined at runtime, allowing code to be more flexible and reusable.

**Example:**

```python
class Bird:
   # Method to make a sound for the Bird class
    def speak(self):
        print("Chirp")
        
class Dog:
  # Method to make a sound for the Dog class
    def speak(self):
        print("Bark")
```

---

## 11. What is encapsulation, and how does Python achieve it?

Encapsulation is an OOP principle that restricts direct access to an object's internal data and exposes it only through controlled interfaces. It helps protect the internal state of an object and ensures data integrity.

In Python, encapsulation is achieved using naming conventions:

- **Single underscore `_var`:** Indicates a protected attribute (by convention, should not be accessed outside the class).
- **Double underscore `__var`:** Makes an attribute private using name mangling, which makes it harder to access from outside the class.

**Example:**

```python
class Example:
    def __init__(self):
        self.__private_var = 42
```

---

## 12. What is the super() function in Python?

`super()` allows access to methods of the parent class and it's often used to call the parent class's constructor.

**Example:**

```python
class A:
    def method(self):
        print("Method in class A")

class B(A):
    def method(self):
        super().method()  # Call method from class A
        print("Method in class B")

class C(A):
    def method(self):
        super().method()  # Call method from class A
        print("Method in class C")
```

---

## 13. What are abstract classes in Python?

Abstract class is a class that serves as a blueprint for other classes. It defines a structure that derived classes must follow but does not provide full implementation, abstract classes cannot be instantiated directly which means they are meant to be subclassed.

**Example:**

```python
from abc import ABC, abstractmethod
class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass
```

---

## 14. What is multiple inheritance in Python?

Multiple inheritance allows a subclass to inherit features from multiple parent classes, making it more versatile and capable of combining behaviors from different sources.

```python
class ChildClass(ParentClass1, ParentClass2, ...):
    # Class body
```

---

## 15. What is the diamond problem in multiple inheritance? How does Python handle it?

The **Diamond Problem** in multiple inheritance is a classic issue that arises when a class inherits from two classes that both inherit from a common ancestor. The problem occurs because, in such scenario, it's unclear which version of the inherited method should be invoked when the method is called on the subclass.

---

## 16. What are class methods in Python?

Class methods are methods that are bound to the class rather than its instances. They take the class itself as the first parameter, conventionally named `cls`, instead of `self`. Class methods are defined using the `@classmethod` decorator and can access or modify class-level attributes.

```python
class Demo:
    @classmethod
    def info(cls):
        print("Class Method")
```

---

## 17. What is the difference between staticmethod and classmethod?

In Python, both `@staticmethod` and `@classmethod` are used to define methods that are not bound to the instance of the class (i.e., they can be called on the class itself).

| Aspect | staticmethod | classmethod |
|--------|-------------|-------------|
| Binding | Not bound to either the instance or the class. | Bound to the class, not the instance. |
| First Argument | Does not take `self` or `cls` as the first argument. | Takes `cls` as the first argument (refers to the class). |
| Access to Class/Instance Variables | Cannot access or modify instance or class variables. | Can access and modify class variables (but not instance variables). |

---

## 18. What are magic methods in Python?

Magic methods (also called dunder methods) are special methods in Python that start and end with double underscores.

They allow customization of object behavior, such as how objects are represented, compared, or used with operators.

**Examples:**

- **`__init__`:** Constructor method, called when an object is created.
- **`__str__`:** Defines the string representation of an object.
- **`__len__`:** Defines behavior for the `len()` function.
- **`__add__`:** Enables operator overloading for `+`.

---

## 19. How does Python handle garbage collection?

Python uses automatic garbage collection to manage memory by identifying and removing unused objects and It employs reference counting and a cyclic garbage collector.

---

## 20. What is metaclass in Python?

A metaclass is a class of a class that defines how classes behave and classes are instances of metaclasses. Essentially, metaclasses define the "rules" for building classes, much like a class defines the rules for creating objects.

**Example:**

```python
class Meta(type):
   # This is an empty metaclass that inherits from 'type'
    pass
  
class Demo(metaclass=Meta):
   # The 'metaclass=Meta' instructs Python to use the 'Meta' metaclass 
    pass
```

---

## 21. How is data hiding implemented in Python?

Data hiding is implemented using name mangling to make attributes less accessible from outside the class. Attributes prefixed with double underscores (`__`) are internally renamed to include the class name, which discourages direct access.

```python
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance   # private attribute

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance

acc = BankAccount(1000)
print(acc.get_balance())  # 1000
# print(acc.__balance)    # AttributeError
```

---

## 22. What is the purpose of __slots__ in Python classes?

`__slots__` attribute is used to explicitly declare the allowed instance attributes in a class, preventing the creation of a default `__dict__` for each instance. This has two main benefits:

- **Memory optimization:** Instances consume less memory because no per-object `__dict__` is created.
- **Attribute restriction:** Only the attributes listed in `__slots__` can be assigned to instances, helping prevent accidental creation of new attributes.

**Example:**

```python
class Person:
    __slots__ = ['name', 'age']  # Only these attributes are allowed
    
    def __init__(self, name, age):
        self.name = name
        self.age = age

p = Person("Alice", 25)
p.name = "Bob"    # Allowed
# p.address = "Street"  # AttributeError: 'Person' object has no attribute 'address'
```

---

## 23. What is the Global Interpreter Lock (GIL) and its impact on Python OOP?

The Global Interpreter Lock (GIL) is a mutex that allows only one thread to execute Python bytecode at a time, even on multi-core systems.

**It's impact:**

- For CPU-bound tasks, multithreading is limited by the GIL, so performance gains are minimal.
- For I/O-bound tasks (like file handling, networking, databases), threads still help because the GIL is released during I/O operations.

---

## 24. How do you achieve operator overloading in Python?

Operator overloading lets you redefine how operators (like `+`, `-`, `*`) behave for user-defined classes. This is done by defining special methods (also called magic/dunder methods) inside your class.

**Example:**

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f"({self.x}, {self.y})"

p1 = Point(2, 3)
p2 = Point(4, 5)
print(p1 + p2)  # Output: (6, 8)
```

**Output:**
```
(6, 8)
```

---

## 25. What is the difference between composition and inheritance?

Composition and inheritance are two fundamental object-oriented programming (OOP) techniques for creating relationships between classes. The main difference between inheritance and composition is that:

- **Inheritance** is when a class derives from another class and automatically gets its behavior. It represents an "is-a" relationship. For example, a Car class inheriting from a Vehicle class.
- **Composition** is when a class contains objects of other classes and uses them to achieve functionality. It represents a "has-a" relationship. For example, a Car class having an Engine object.

---

## 26. How do you implement design patterns like Singleton in Python?

A Singleton ensures that only one instance of a class exists throughout the program. Python doesn't have a built-in Singleton keyword, but it can be implemented in the following ways:

### 26.1 Using a Class Variable

```python
class Singleton:
    _instance = None
    
    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

# Test
s1 = Singleton()
s2 = Singleton()
print(s1 is s2)  # True
```

Here, `__new__` ensures only one object is ever created.

### 26.2 Using a Decorator

```python
def singleton(cls):
    instances = {}
    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return get_instance

@singleton
class Database:
    pass

d1 = Database()
d2 = Database()
print(d1 is d2)  # True
```

### 26.3 Using a Module

Since Python modules are loaded once and cached, simply defining variables and functions inside a module ensures singleton-like behavior.

```python
# singleton_module.py
class Config:
    pass

config = Config()
```

---

## 27. Explain Python's MRO with an example.

Python's Method Resolution Order (MRO) determines the order in which classes are searched when calling a method in the presence of multiple inheritance.

It follows the C3 linearization algorithm.

**Example:**

```python
class A: pass
class B(A): pass
class C(A): pass
class D(B, C): pass

print(D.mro())
```

**Output:**
```
[<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>]
```

---

## 28. How would you identify the MRO of a class programmatically?

We can identify the Method Resolution Order (MRO) of a class programmatically in Python using the `mro()` Method or by using the `__mro__` attribute.

- **Using the `mro()` method:** This method returns a list of classes in the order they are checked for method resolution.
- **Using the `__mro__` attribute:** This attribute directly provides the MRO as a tuple of classes.

---


