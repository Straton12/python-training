count = 1
while count <= 5:
    if count == 3:
        count += 1
        continue
    print("Iteration", count)
    count += 1


count = 1
while True:
    if count > 5:
        break
    print("Iteration", count)
    count += 1
