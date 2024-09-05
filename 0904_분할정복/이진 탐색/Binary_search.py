import sys

sys.stdin = open("sample_input(1).txt", "r")


def bn(s, e, n, direction):
    global result
    if s > e:
        return
    mid = s - (s - e) // 2

    if A[mid] == n:
        result += 1
        return
    elif A[mid] < n and (direction == "" or direction != "right"):
        bn(mid + 1, e, n, "right")
    elif A[mid] > n and (direction == "" or direction != "left"):
        bn(s, mid-1, n, "left")

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    # B의 정수가 A에 들어 있는가
    result = 0
    for i in B:
        bn(0, N-1, i , "")
    print(f"#{tc} {result}")

