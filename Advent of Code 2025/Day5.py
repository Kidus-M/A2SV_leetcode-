print("Reading input...")
data = input()
lines = []
while data.strip():
    lines.append(data)
    data = input()
print("Fresh ranges read:", len(lines))

fresh_ranges = []
for line in lines:
    start, end = map(int, line.split('-'))
    fresh_ranges.append((start, end))
    print(f"Range: {start}-{end}")

print("\nReading blank line...")
blank = input()
print("Blank line passed")

print("\nReading available IDs...")
available = []
while True:
    try:
        data = input()
        if data.strip():
            id_val = int(data)
            available.append(id_val)
            print("Available ID:", id_val)
    except EOFError:
        break

print("\nProcessing...")

fresh_count = 0
for ingredient in available:
    is_fresh = False
    for start, end in fresh_ranges:
        if start <= ingredient <= end:
            is_fresh = True
            break
    if is_fresh:
        print(ingredient, "is fresh")
        fresh_count += 1
    else:
        print(ingredient, "is spoiled")

print("\nTotal fresh ingredients:", fresh_count)