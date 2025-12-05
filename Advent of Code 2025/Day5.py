print("Enter the ingredient ID ranges, then a blank line, then the IDs to check.")
print("Waiting for input...")

ranges = []
while True:
    line = input().strip()
    if line == "":
        break
    a, b = map(int, line.split("-"))
    ranges.append((a, b))

print("Ranges loaded:", ranges)
print("Now enter ingredient IDs to test (end with CTRL+D / CTRL+Z):")

fresh_count = 0

while True:
    try:
        x = int(input().strip())
        print("Checking:", x)
        is_fresh = False
        for a, b in ranges:
            if a <= x <= b:
                is_fresh = True
                break
        if is_fresh:
            print(x, "is FRESH")
            fresh_count += 1
        else:
            print(x, "is SPOILED")
    except EOFError:
        break

print("Total fresh ingredients:", fresh_count)
