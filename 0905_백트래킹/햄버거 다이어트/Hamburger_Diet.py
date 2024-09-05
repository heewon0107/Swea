import sys

sys.stdin = open("sample_input.txt", "r")


def subset(idx, calory, point):
    global result
    # 칼로리 초과 시 리턴
    if calory > allow_cal:
        return

    if idx == N:
        if point > result:
            result = point
        return

    subset(idx + 1, calory + arr[idx][1], point + arr[idx][0])
    subset(idx + 1, calory, point)

T = int(input())
for tc in range(1, T + 1):
    N, allow_cal = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    result = 0
    atn = [0] * N
    subset(0, 0, 0)
    print(f"#{tc} {result}")
