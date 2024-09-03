import sys

sys.stdin = open("sample_input.txt", "r")


def board(level, i, j):
    global result
    global cnt
    if i == (4 or -1) or j == (4 or -1):
        return

    result.append(arr[i][j])
    if level == 7:
        if result not in stack:
            stack.append(result)
            cnt += 1
        result.pop()
        return
    for di, dj in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
        board(level + 1, i+di, j+dj)


T = int(input())
for tc in range(1, T + 1):
    arr = [list(map(str, input().split())) for _ in range(4)]
    result = []
    cnt = 0
    stack = []
    for i in range(4):
        for j in range(4):
            board(0, i, j)

    print(f"#{tc} {cnt}")