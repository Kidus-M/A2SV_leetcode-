line = input().strip()

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

for k in range(1, (max_digits // 2) + 1):
    start = 10**(k-1) if k > 1 else 1
    end = 10**k - 1
    for base in range(start, end + 1):
        s = f"{base}{base}"
        num = int(s)
        if num > max_hi:
            break
        if num < min_lo:
            continue
        if num in seen:
            continue
        for a, b in ranges:
            if a <= num <= b:
                total += num
                seen.add(num)
                break

print(total)
