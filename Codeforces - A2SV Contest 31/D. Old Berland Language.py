n = int(input())
lengths = list(map(int, input().split()))
used = set()
words = []
for l in lengths:
    found = False
    for i in range(1 << l):
        s = bin(i)[2:].zfill(l)
        if all(not s.startswith(w) and not w.startswith(s) for w in used):
            used.add(s)
            words.append(s)
            found = True
            break
    if not found:
        print("NO")
        exit()
print("YES")
for w in words:
    print(w)