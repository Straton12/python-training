my_list = [1, 2, 3, 4, 5]
print(my_list)

# Accessing elements
print(my_list[0])  # Access the first element
print(my_list[-1])  # Access the last element

# Modifying elements
my_list.append(6)  # Add an element
my_list[2] = 10


my_tuple = (1, 2, 3)
print(my_tuple)

# Accessing elements
print(my_tuple[0])

# Unpackingdef get_info(name, age):
#     return name, age
#
# name, age = get_info("Alice", 30)
# print("Name:", name)
# print("Age:", age)
#
# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n * factorial(n - 1)
#
# result = factorial(5)
# print("Factorial:", result)
x, y, z = my_tuple

my_dict = {"name": "Alice", "age": 30, "city": "New York"}
print(my_dict)

# Accessing values
print(my_dict["name"])

# Modifying values
my_dict["age"] = 31
my_dict["job"] = "Engineer"