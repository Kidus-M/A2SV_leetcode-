print("Paste battery banks, empty line when done:")
lines = []
while True:
    t = input()
    if t.strip() == "":
        break
    lines.append(t.strip())

print("Processing...")

total = 0
for bank in lines:
    n = len(bank)
    if n < 2:
        continue
    suf = [-1] * n
    current = -1
    for i in range(n-1, -1, -1):
        suf[i] = current
        d = ord(bank[i]) - 48
        if d > current:
            current = d
    best = -1
    for i in range(n-1):
        left = ord(bank[i]) - 48
        right = suf[i]
        if right >= 0:
            val = left * 10 + right
            if val > best:
                best = val
    if best >= 0:
        total += best

print("Total joltage:", total)
