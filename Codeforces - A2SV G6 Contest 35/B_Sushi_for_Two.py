n = int(input())
t = list(map(int, input().split()))

groups = []
count = 1

for i in range(1, n):
    if t[i] == t[i - 1]:
        count += 1
    else:
        groups.append(count)
        count = 1
groups.append(count)

ans = 0
for i in range(len(groups) - 1):
    ans = max(ans, 2 * min(groups[i], groups[i + 1]))

print(ans)
