pos = 50
count_zero = 0

while True:
    try:
        line = input().strip()
    except EOFError:
        break

    if line == "":
        break

    direction = line[0]
    amount = int(line[1:])

    if direction == "R":
        k0 = (100 - pos) % 100
        if k0 == 0:
            k0 = 100
    else:
        k0 = pos % 100
        if k0 == 0:
            k0 = 100

    if amount >= k0:
        count_zero += 1 + (amount - k0) // 100

    if direction == "R":
        pos = (pos + amount) % 100
    else:
        pos = (pos - amount) % 100

print(count_zero)
