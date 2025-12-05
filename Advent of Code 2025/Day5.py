print("Paste fresh ranges, then blank line, then ingredient IDs:")

import sys

section = 0
ranges = []
ids = []

for line in sys.stdin:
    line = line.strip()
    if line == "":
        section = 1
        continue
    if section == 0:
        a, b = map(int, line.split("-"))
        ranges.append((a, b))
    else:
        ids.append(int(line))
print("running")
fresh = 0
for x in ids:
    for a, b in ranges:
        if a <= x <= b:
            fresh += 1
            break

print(fresh)
