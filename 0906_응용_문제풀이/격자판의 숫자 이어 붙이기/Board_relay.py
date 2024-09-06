import sys

sys.stdin = open("sample_input.txt", "r")


def board(i, j, string):
    if len(string) == 7:
        result.add(string)
        return

    for di, dj in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
        ni = i + di
        nj = j + dj
        if 0 <= ni < 4 and 0 <= nj < 4:
            board(ni, nj, string + arr[ni][nj])


T = int(input())
for tc in range(1, T + 1):
    arr = [input().split() for _ in range(4)]
    result = set()
    for i in range(4):
        for j in range(4):
            board(i, j, arr[i][j])

    print(f"#{tc} {len(result)}")
