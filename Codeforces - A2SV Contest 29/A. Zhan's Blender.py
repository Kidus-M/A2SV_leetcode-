t = int(input())
for _ in range(t):
    n = int(input())
    x, y = map(int, input().split())
    if n == 0:
        print(0)
        continue
    batches = (n + y - 1) // y
    fruits_per_batch = min(x, y)
    full_seconds = (n + fruits_per_batch - 1) // fruits_per_batch
    print(max(batches, full_seconds))