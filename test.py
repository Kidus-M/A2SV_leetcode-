def backtrack(index, total, n, angles):
    if index == n:
        return total % 360 == 0
    if backtrack(index + 1, total + angles[index], n, angles):
        return True
    if backtrack(index + 1, total - angles[index], n, angles):
        return True
    return False

n = int(input())
angles = [int(input()) for _ in range(n)]
print("YES" if backtrack(0, 0, n, angles) else "NO")