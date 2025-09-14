def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def count_almost_prime(n):
    count = 0
    for num in range(1, n + 1):
        divisors = set()
        temp = num
        i = 2
        while i * i <= temp:
            while temp % i == 0:
                divisors.add(i)
                temp //= i
            i += 1
        if temp > 1:
            divisors.add(temp)
        if len(divisors) == 2 and all(is_prime(p) for p in divisors):
            count += 1
    return count

n = int(input())
print(count_almost_prime(n))