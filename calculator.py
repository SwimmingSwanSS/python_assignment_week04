def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: Cannot divide by zero"
    
if __name__ == "__main__":
    x = 10
    y = 5

    print("Addition:", add(x, y))    
    print("Subtraction:", subtract(x, y))
    print("Multiplication:", multiply(x, y))
    print("Division", divide(x, y))