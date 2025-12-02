pos = 50
count_zero = 0

while True:
    try:
        line = input().strip()
    except EOFError:
        break

    # Stop when user enters an empty line at the end
    if line == "":
        break

    direction = line[0]
    amount = int(line[1:])

    if direction == "L":
        pos = (pos - amount) % 100
    else:  # R
        pos = (pos + amount) % 100

    if pos == 0:
        count_zero += 1

print(count_zero)