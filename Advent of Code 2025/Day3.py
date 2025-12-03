print("Yo, paste your battery banks. Hit ENTER on an empty line when you're done.")

lines = []
while True:
    t = input()
    if t.strip() == "":
        break
    lines.append(t.strip())

print("Alright, processing...")

total = 0
for bank in lines:
    first = max(bank)
    i = bank.index(first)
    second = max(bank[i+1:])
    total += int(first + second)

print("Total joltage:", total)
