def power_squared(n, k):
    if k == 1:
        return n
    return n * power_squared(n, k - 1)



for t in range(10):
    tc = int(input())
    N, K = map(int, input().split())
    result = power_squared(N, K)
    print(f"#{tc} {result}")
