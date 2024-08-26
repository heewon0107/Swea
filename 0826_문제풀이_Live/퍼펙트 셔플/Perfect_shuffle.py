T = int(input())
for tc in range(1, T+1):
    N = int(input())    # N = 카드의 개수
    arr = list(map(str, input().split()))
    result = [0] * N

    # d = (N + 1) // 2
    # i1 = 0
    # i2 = d
    # i3 = 0
    # while i3 < N:
    #     if i1 < d:
    #         result[i3] = arr[i1]
    #         i1 += 1
    #         i3 += 1
    #     if i2 < N:
    #         result[i3] = arr[i2]
    #         i2 += 1
    #         i3 += 1

    for i in range(0, N, 2):
        result[i] = arr[i]
        if N % 2 == 0:  # 짝수면
            result[i+1] = arr[N//2 + i]
        elif N//2 + i < N:
            result[i+1] = arr[N//2 + i]
    print(f"#{tc}", *result)