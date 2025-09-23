n, s = map(int, input().split())
a = list(map(int, input().split()))

left = 0
current_sum = 0
max_length = 0

for right in range(n):
    current_sum += a[right]

    while current_sum > s and left <= right:
        current_sum -= a[left]
        left += 1

    max_length = max(max_length, right - left + 1)

print(max_length)