import sys

sys.stdin = open("sample_input(1).txt", "r")


def bn(s, e, n):
    global result
    if s > e:
        return
    mid = s - (s - e) // 2

    if B[mid] == n:
        result += 1

    if B[mid] < n:
        bn(mid + 1, e, n)
    elif B[mid] > n:
        bn(s, mid-1, n)


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    r = len(B)
    # B의 정수가 A에 들어 있는가
    result = 0
    for i in A:
        bn(0, r-1, i)
    print(f"#{tc} {result}")