try:
    result = 10 / 0
except ZeroDivisionError:
    print("ZeroDivisionError: Division by zero")
except Exception as e:
    print(f"Exception: {e}")

try:
    file = open("example.txt", "r")
    data = file.read()
except FileNotFoundError:
    print("File not found")
finally:
    file.close()