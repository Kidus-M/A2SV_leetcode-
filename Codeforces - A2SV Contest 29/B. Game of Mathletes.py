t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    x = list(map(int, input().split()))
    freq = [0] * (n + 1)
    for num in x:
        freq[num] += 1
    score = 0
    for i in range(1, n + 1):
        if k - i >= 1 and k - i <= n:
            if i == k - i:
                score += freq[i] // 2
            else:
                pairs = min(freq[i], freq[k - i])
                score += pairs
                freq[i] -= pairs
                freq[k - i] -= pairs
    print(score)