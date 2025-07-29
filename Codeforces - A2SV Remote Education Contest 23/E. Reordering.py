from collections import defaultdict, deque

n = int(input())
words = []
alpha = "abcdefghijklmnopqrstuvwxyz"

graph = defaultdict(set)
indegree = defaultdict(int)

for _ in range(n):
    words.append(input())

valid = True
for i in range(1, n):
    word1 = words[i - 1]
    word2 = words[i]
    j = 0
    while j < len(word1):
        if j >= len(word2):
            valid = False
            break

        if word1[j] != word2[j]:
            if word2[j] not in graph[word1[j]]:
                graph[word1[j]].add(word2[j])
                indegree[word2[j]] += 1
            break
        j += 1

if valid:
    src = deque()
    for ch in alpha:
        if indegree[ch] == 0:
            src.append(ch)

    order = ""
    while src:
        cur = src.popleft()
        order += cur

        for nbor in graph[cur]:
            indegree[nbor] -= 1
            if indegree[nbor] == 0:
                src.append(nbor)

    if len(order) == len(alpha):
        print(order)
    else:
        print("Impossible")
else:
    print("Impossible")