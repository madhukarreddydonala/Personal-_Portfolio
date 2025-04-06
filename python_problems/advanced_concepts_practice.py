"""
Practice Problems for Advanced Python Concepts
Try to solve these problems to better understand the concepts.
"""

# 1. Closure Practice: Shopping Cart
def create_shopping_cart():
    items = {}
    
    def add_item(item, price):
        items[item] = price
        return f"Added {item} for ${price}"
    
    def remove_item(item):
        if item in items:
            del items[item]
            return f"Removed {item}"
        return f"{item} not found"
    
    def get_total():
        return sum(items.values())
    
    return add_item, remove_item, get_total

# TODO: Try using the shopping cart
# cart = create_shopping_cart()
# add, remove, total = cart
# print(add("Apple", 1.99))
# print(add("Banana", 0.99))
# print(total())
# print(remove("Apple"))
# print(total())

# 2. Iterator Practice: File Reader
class FileReader:
    def __init__(self, filename):
        self.filename = filename
        self.file = None
    
    def __iter__(self):
        self.file = open(self.filename, 'r')
        return self
    
    def __next__(self):
        line = self.file.readline()
        if line:
            return line.strip()
        self.file.close()
        raise StopIteration

# TODO: Create a test.txt file and try reading it
# reader = FileReader('test.txt')
# for line in reader:
#     print(line)

# 3. Generator Practice: Prime Numbers
def prime_numbers():
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    
    n = 2
    while True:
        if is_prime(n):
            yield n
        n += 1

# TODO: Try generating prime numbers
# primes = prime_numbers()
# for _ in range(5):
#     print(next(primes))

# 4. Decorator Practice: Timer
import time
from functools import wraps

def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end - start:.4f} seconds")
        return result
    return wrapper

# TODO: Try the timer decorator
# @timer
# def slow_function():
#     time.sleep(1)
#     return "Done!"
# 
# print(slow_function())

# 5. Class Methods Practice: Library
class Library:
    total_books = 0
    books = {}
    
    def __init__(self, name):
        self.name = name
    
    def add_book(self, title, author):
        Library.books[title] = author
        Library.total_books += 1
        return f"Added {title} by {author}"
    
    @classmethod
    def get_total_books(cls):
        return cls.total_books
    
    @staticmethod
    def format_book_info(title, author):
        return f"Title: {title}, Author: {author}"

# TODO: Try using the Library class
# lib = Library("My Library")
# print(lib.add_book("Python Basics", "John Doe"))
# print(Library.get_total_books())
# print(Library.format_book_info("Python Basics", "John Doe"))

# Practice Problems:

# 1. Create a closure that maintains a counter for different categories
def create_category_counter():
    counters = {}
    
    def count(category):
        counters[category] = counters.get(category, 0) + 1
        return counters[category]
    
    def get_counts():
        return counters
    
    return count, get_counts

# 2. Create an iterator that reads a CSV file
class CSVReader:
    def __init__(self, filename):
        self.filename = filename
        self.file = None
    
    def __iter__(self):
        self.file = open(self.filename, 'r')
        return self
    
    def __next__(self):
        line = self.file.readline()
        if line:
            return line.strip().split(',')
        self.file.close()
        raise StopIteration

# 3. Create a generator for Fibonacci numbers
def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

# 4. Create a decorator that caches function results
def cache_results(func):
    cache = {}
    
    @wraps(func)
    def wrapper(*args):
        if args in cache:
            return cache[args]
        result = func(*args)
        cache[args] = result
        return result
    
    return wrapper

# 5. Create a class to manage a todo list
class TodoList:
    todos = []
    
    def __init__(self, title):
        self.title = title
    
    def add_todo(self, task):
        TodoList.todos.append({"task": task, "completed": False})
        return f"Added task: {task}"
    
    @classmethod
    def get_all_todos(cls):
        return cls.todos
    
    @staticmethod
    def format_todo(task, completed):
        status = "✓" if completed else " "
        return f"[{status}] {task}"

# Try these practice problems:
if __name__ == "__main__":
    # 1. Category Counter
    count, get_counts = create_category_counter()
    print(count("books"))  # 1
    print(count("books"))  # 2
    print(count("movies"))  # 1
    print(get_counts())  # {'books': 2, 'movies': 1}
    
    # 2. Fibonacci Generator
    fib = fibonacci()
    for _ in range(5):
        print(next(fib))  # 0, 1, 1, 2, 3
    
    # 3. Todo List
    todo = TodoList("My Tasks")
    print(todo.add_todo("Learn Python"))
    print(todo.add_todo("Build a project"))
    for task in TodoList.get_all_todos():
        print(TodoList.format_todo(task["task"], task["completed"])) 