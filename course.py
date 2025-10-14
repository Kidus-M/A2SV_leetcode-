def find_first_not_less(arr, target):
    left, right = 0, len(arr) - 1
    result = len(arr)
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] >= target:
            result = mid
            right = mid - 1
        else:
            left = mid + 1
    return result

def find_first_greater(arr, target):
    left, right = 0, len(arr) - 1
    result = len(arr)
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] > target:
            result = mid
            right = mid - 1
        else:
            left = mid + 1
    return result

n = int(input())
arr = list(map(int, input().split()))
arr.sort()
k = int(input())
for _ in range(k):
    l, r = map(int, input().split())
    left_idx = find_first_not_less(arr, l)
    right_idx = find_first_greater(arr, r)
    print(right_idx - left_idx)


