# aoc_day1_part2.py
# Counts every time the dial points at 0 during any click (including the end of a rotation).
# Run and paste instructions, then press Enter on an empty line (or send EOF/Ctrl-D).

pos = 50
count_zero = 0

while True:
    try:
        line = input().strip()
    except EOFError:
        break

    if line == "":
        break

    direction = line[0]
    amount = int(line[1:])

    if direction == "R":
        # k such that (pos + k) % 100 == 0  => k ≡ (100 - pos) % 100
        k0 = (100 - pos) % 100
        if k0 == 0:
            k0 = 100
    else:  # L
        # k such that (pos - k) % 100 == 0  => k ≡ pos % 100
        k0 = pos % 100
        if k0 == 0:
            k0 = 100

    if amount >= k0:
        # number of k in {1..amount} that are ≡ k0 (mod 100)
        count_zero += 1 + (amount - k0) // 100

    # update position after the rotation
    if direction == "R":
        pos = (pos + amount) % 100
    else:
        pos = (pos - amount) % 100

print(count_zero)
