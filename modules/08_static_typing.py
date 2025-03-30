# === STATIC TYPING IN PYTHON ===
# Python is dynamically typed by default, but you can use optional type hints.

# --- VARIABLES WITH TYPE HINTS ---
name: str = "Taylor"
age: int = 26
height: float = 1.75
is_student: bool = False

print(f"{name} is {age} years old, {height}m tall, student: {is_student}")

# --- LISTS WITH TYPE HINTS ---
# List of strings
fruits: list[str] = ["apple", "banana", "mango"]

# You can also import List for older Python versions (<3.9)
# from typing import List
# fruits: List[str] = ["apple", "banana"]

for fruit in fruits:
    print("Fruit:", fruit)

# --- DICTIONARIES WITH TYPE HINTS ---
from typing import Dict, Any

# Dict with string keys and any type values
person: Dict[str, Any] = {
    "name": "Jordan",
    "age": 29,
    "is_employed": True
}

print("Person name:", person["name"])

# --- FUNCTION TYPE HINTS ---

def greet(name: str) -> str:
    return f"Hello, {name}!"

def add(a: int, b: int) -> int:
    return a + b

def get_fruit(index: int) -> str:
    return fruits[index]

print(greet("Morgan"))
print("Add 5 + 6:", add(5, 6))
print("Fruit at index 1:", get_fruit(1))

# --- NESTED TYPES ---
# List of dictionaries, where each dictionary represents a student

from typing import List

students: List[Dict[str, Any]] = [
    {"name": "Alice", "grade": 90},
    {"name": "Bob", "grade": 85}
]

for student in students:
    print(f"{student['name']} scored {student['grade']}")

# --- Practice ---
# 1. Create a list of integers and annotate it
# 2. Create a dictionary representing a book: title (str), pages (int), available (bool)
# 3. Write a function that takes a list of numbers and returns their average as float
