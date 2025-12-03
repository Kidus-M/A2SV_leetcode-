print("Alright, drop the battery banks:")
lines = []
while True:
    try:
        t = input().strip()
        if t:
            lines.append(t)
    except EOFError:
        break

print("Cooking...")

total = 0
for bank in lines:
    digits = list(bank)
    first = max(digits)
    i = digits.index(first)
    second = max(digits[i+1:])
    total += int(first + second)

print(total)
