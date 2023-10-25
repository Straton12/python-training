def get_info(name, age):
    return name, age

name, age = get_info("Alice", 30)
print("Name:", name)
print("Age:", age)

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

result = factorial(5)
print("Factorial:", result)
