print("Paste battery banks, empty line when done:")
lines = []
while True:
    try:
        t = input()
    except EOFError:
        break
    if t.strip() == "":
        break
    lines.append(t.strip())

k = 12
total = 0
for s in lines:
    n = len(s)
    if n <= k:
        pick = s
    else:
        to_remove = n - k
        stack = []
        for ch in s:
            while stack and to_remove > 0 and stack[-1] < ch:
                stack.pop()
                to_remove -= 1
            stack.append(ch)
        pick = "".join(stack[:k])
    total += int(pick)
print("Total joltage:", total)
