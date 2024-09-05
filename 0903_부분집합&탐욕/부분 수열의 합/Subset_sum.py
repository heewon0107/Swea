import sys

sys.stdin = open("sample_input.txt", "r")


def subset(idx, total):
    global result
    if total > K:
        return
    if idx == N:
        if total == K:
            result += 1
        return
    subset(idx + 1, total + arr[idx])
    subset(idx + 1, total)


T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split())
    arr = list(map(int, input().split()))
    result = 0
    subset(0, 0)
    print(f"#{tc} {result}")
