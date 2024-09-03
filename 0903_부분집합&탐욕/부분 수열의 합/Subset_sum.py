import sys

sys.stdin = open("sample_input.txt", "r")


def subset(n, k):
    global result
    for i in range(0, 1 << n):
        sub = []
        for j in range(n):
            if i & (1 << j):
                sub.append(arr[j])

        if sum(sub) == k:
            result += 1


T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split())
    arr = list(map(int, input().split()))
    result = 0
    subset(N, K)
    print(f"#{tc} {result}")
