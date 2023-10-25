temperature = 25
is_sunny = True

if temperature > 30 and is_sunny:
    print("It's a hot and sunny day.")
elif temperature > 30 and not is_sunny:
    print("It's hot but not sunny.")
else:
    print("It's not a hot day.")



fruits = ["apple", "banana", "cherry"]
desired_fruit = "banana"

if desired_fruit in fruits:
    print(f"{desired_fruit} is in the list of fruits.")
else:
    print(f"{desired_fruit} is not in the list of fruits.")