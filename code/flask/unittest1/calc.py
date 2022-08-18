# add, subtract, multiply (x,y)

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y==0:
        raise ValueError("Divide by zero is not allowed")
    return x / y


if __name__ == "__main__":
    print(add(1,9))
    print(subtract(1,9))
    print(multiply(1,9))
    print(f"{divide(1,9):4.2}")