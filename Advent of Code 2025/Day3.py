print("Yo, paste your battery banks. Empty line = done.")

lines = []
while True:
    t = input()
    if t.strip() == "":
        break
    lines.append(t.strip())

print("Alright, crunching...")

total = 0
for bank in lines:
    digits = list(bank)
    d1 = max(digits)
    i1 = digits.index(d1)
    d2 = max(digits[:i1] + digits[i1+1:])
    total += int(d1 + d2)

print("Total joltage:", total)
