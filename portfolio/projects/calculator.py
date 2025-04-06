"""
Calculator Application
A simple calculator that can perform basic arithmetic operations.
"""

def add(x, y):
    """Add two numbers."""
    return x + y

def subtract(x, y):
    """Subtract y from x."""
    return x - y

def multiply(x, y):
    """Multiply two numbers."""
    return x * y

def divide(x, y):
    """Divide x by y."""
    if y == 0:
        return "Error: Division by zero"
    return x / y

def calculator():
    """Main calculator function."""
    print("Simple Calculator")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")
    
    while True:
        # Get operation choice from user
        choice = input("Enter choice (1/2/3/4/5): ")
        
        # Check if choice is valid
        if choice in ('1', '2', '3', '4'):
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
            except ValueError:
                print("Invalid input. Please enter numbers only.")
                continue
        
        if choice == '1':
            print(f"{num1} + {num2} = {add(num1, num2)}")
        
        elif choice == '2':
            print(f"{num1} - {num2} = {subtract(num1, num2)}")
        
        elif choice == '3':
            print(f"{num1} * {num2} = {multiply(num1, num2)}")
        
        elif choice == '4':
            result = divide(num1, num2)
            print(f"{num1} / {num2} = {result}")
        
        elif choice == '5':
            print("Exiting calculator. Goodbye!")
            break
        
        else:
            print("Invalid input. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    calculator() 