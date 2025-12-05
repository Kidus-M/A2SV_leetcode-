print("Processing...")

ranges = []
while True:
    line = input().strip()
    if line == "":
        break
    a, b = map(int, line.split("-"))
    ranges.append((a, b))

fresh = 0
ids = []

while True:
    try:
        ids.append(int(input().strip()))
    except EOFError:
        break

for x in ids:
    for a, b in ranges:
        if a <= x <= b:
            fresh += 1
            break

print(fresh)
