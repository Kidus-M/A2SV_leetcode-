def is_repeated(s):
    return s in (s + s)[1:-1]

print("Alright drop the input:")
raw = input().strip()
print("Running...")

parts = [p.strip() for p in raw.split(",") if p.strip()]

total = 0
for p in parts:
    a, b = map(int, p.split("-"))
    for n in range(a, b + 1):
        if is_repeated(str(n)):
            total += n

print(total)