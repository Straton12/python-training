user_input = input("Enter an integer: ")
try:
    num = int(user_input)
    print("You entered:", num)
except ValueError:
    print("Invalid input. Please enter an integer.")

name = input("Enter your name: ")
age = input("Enter your age: ")
print(f"Hello, {name}! You are {age} years old.")
