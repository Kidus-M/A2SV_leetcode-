print("Yo! Paste your ID ranges in ONE line:")
line = input("Ranges: ").strip()

print("Got it! Crunching numbers... This might take a moment 👀")

parts = [p.strip() for p in line.split(",") if p.strip()]
ranges = []
for p in parts:
    a, b = p.split("-")
    ranges.append((int(a), int(b)))

min_lo = min(a for a,_ in ranges)
max_hi = max(b for _,b in ranges)

total = 0
seen = set()
max_digits = len(str(max_hi))

print("Generating repeated-digit patterns...")

for k in range(1, max_digits):
    start = 10**(k-1) if k > 1 else 1
    end = 10**k - 1
    for base in range(start, end+1):
        s = str(base)
        rep = s+s
        while len(rep) <= max_digits:
            num = int(rep)
            if num > max_hi:
                break
            if num >= min_lo and num not in seen:
                for a,b in ranges:
                    if a <= num <= b:
                        total += num
                        seen.add(num)
                        break
            rep += s

print("All done! 🎉")
print("Sum of invalid IDs:", total)
